# -*- coding: utf-8 -*-

import re


class tcga_clinical:
    _matcher = re.compile("(\{.*\})(.*)")
    
    def __init__(self, file):
        import xml.etree.ElementTree
        self.root = xml.etree.ElementTree.parse(file).getroot()

        self.dict_clinical = self.__clinical_parse_to_dict(self.root)

    def print_nodes(self):
        self.__print_node(self.root)

    def __clinical_parse_to_dict(self, node):
        elements = {}
    
        for child in node:
            key = tcga_clinical._matcher.match(child.tag).group(2)
            if 'prefered_name' in child.attrib:
                key = child.attrb['prefered_name']
            
            elements[key] = self.__clinical_parse_to_dict(child)
        
        if node.text is not None and '\n' not in node.text:
            key = tcga_clinical._matcher.match(node.tag).group(2)
            if 'prefered_name' in node.attrib:
                key = node.attrb['prefered_name']

            elements[key] = node.text

        return elements


    def __print_node(self, node, level=0, lastElement=False):
        leng = "  " * level
        if lastElement:
            if len(node) > 0:
                line = leng + "└─┬─>"
            else:
                line = leng + "└─>"
        else:
            if len(node) > 0:
                line = leng + "├─┬─>"
            else:
                line = leng + "├─>"

        key = tcga_clinical._matcher.match(node.tag).group(2)
        if 'prefered_name' in node.attrib:
            key = node.attrib['prefered_name']
        if node.text is not None and "\n" not in node.text:
            print(line + key + ": " + node.text)
        else:
            print(line + key)

        for idx, child in enumerate(node):
            self.__print_node(child, level+1, idx==len(node)-1)

