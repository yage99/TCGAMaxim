# -*- coding: utf-8 -*-

class clinical:
    import re
    _matcher = re.compile("(\{.*\})(.*)")
    
    def __init__(self, file):

        import xml.etree.ElementTree
        self.root = xml.etree.ElementTree.parse(file).getroot()

        self.dict_clinical = self.__clinical_parse_to_dict(self.root)

    def print_nodes(self):
        self.__print_node(self.root, lastElement = True)

    def __clinical_parse_to_dict(self, node):
        elements = {}
    
        for child in node:
            key = clinical._matcher.match(child.tag).group(2)
            if 'prefered_name' in child.attrib:
                key = child.attrb['prefered_name']
            
            elements[key] = self.__clinical_parse_to_dict(child)
        
        if node.text is not None and '\n' not in node.text:
            key = clinical._matcher.match(node.tag).group(2)
            if 'prefered_name' in node.attrib:
                key = node.attrb['prefered_name']

            elements[key] = node.text

        return elements


    def __print_node(self, node, level="", lastElement=False):
        if lastElement:
            if len(node) > 0:
                line = level + "└─┬─>"
                level = level + "  "
            else:
                line = level + "└───>"
                level = level + "  "
        else:
            if len(node) > 0:
                line = level + "├─┬─>"
                level = level + "│ "
            else:
                line = level + "├───>"
                level = level + "│ "

        key = clinical._matcher.match(node.tag).group(2)
        if 'prefered_name' in node.attrib:
            key = node.attrib['prefered_name']
        if node.text is not None and "\n" not in node.text:
            print(line + key + ": " + node.text)
        else:
            print(line + key)

        for idx, child in enumerate(node):
            self.__print_node(child, level, idx==len(node)-1)

