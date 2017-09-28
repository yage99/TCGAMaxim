# -*- coding: utf-8 -*-

import re
matcher = re.compile("(\{.*\})(.*)")

def clinical_parser(file):
    import xml.etree.ElementTree
    e = xml.etree.ElementTree.parse(file).getroot()

    print_node(e)

def print_node(node, level=0, lastElement=False):
    leng = "  " * level
    if lastElement:
        if node:
            line = leng + "└─┬─>"
        else:
            line = leng + "└─>"
    else:
        if node:
            line = leng + "├─┬─>"
        else:
            line = leng + "├─>"

    #print node.tag
    if node.text is not None and "\n" not in node.text:
        print(line + matcher.match(node.tag).group(2) + ": " + node.text)
    else:
        print(line + matcher.match(node.tag).group(2))

    for idx, child in enumerate(node):
        print_node(child, level+1, idx==len(node)-1)

