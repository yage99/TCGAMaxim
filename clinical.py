# -*- coding: utf-8 -*-


class clinical:
    import re
    _matcher = re.compile("(\{.*\})(.*)")

    def __init__(self, file):

        import xml.etree.ElementTree
        self.file = file
        self.root = xml.etree.ElementTree.parse(file).getroot()

        self.dict_clinical = self.__clinical_parse_to_dict(self.root)

    def print_nodes(self):
        for idx, child in enumerate(self.root):
            self.__print_node(child, lastElement=(idx == (len(self.root) - 1)))

    def retrive_by_prefered_name_path(self, names):
        dic = {}
        for path in names:
            dic[path] = self.__get_node(self.dict_clinical, path.split('/'))

        return dic

    def __get_node(self, node, name):
        if isinstance(node, type([])):
            results = []
            for item in node:
                results.append(self.__get_node(item, name))
            return results

        if len(name) == 1:
            if name[0] in node:
                return node[name[0]]
            else:
                return None

        if name[0] in node:
            return self.__get_node(node[name[0]], name[1:])
        else:
            # print("no node named %s" % name[0])
            return None

    def retrive_days_to_death(self):
        results = {}
        v = self.retrive_by_prefered_name_path([
            'patient/days_to_death',
            'patient/days_to_last_followup',
            'patient/vital_status',
            'patient/follow_ups/follow_up/days_to_death',
            'patient/follow_ups/follow_up/days_to_last_followup',
            'patient/follow_ups/follow_up/vital_status'
        ])
        dump = v['patient/follow_ups/follow_up/days_to_death']
        days_to_death = []

        try:
            days_to_death.append(int(v['patient/days_to_death']))
        except Exception:
            pass

        if isinstance(dump, type([])):
            for num in dump:
                try:
                    days_to_death.append(int(num))
                except Exception:
                    pass
        else:
            try:
                days_to_death.append(int(dump))
            except Exception:
                pass

        results['days_to_death'] = days_to_death

        days_to_last_followup = []

        try:
            days_to_last_followup.append(int(
                v['patient/days_to_last_followup']))
        except Exception:
            pass

        dump = v['patient/follow_ups/follow_up/days_to_last_followup']

        if isinstance(dump, type([])):
            for num in dump:
                try:
                    days_to_last_followup.append(int(num))
                except Exception:
                    pass
        else:
            try:
                days_to_last_followup.append(int(dump))
            except Exception:
                pass

        results['days_to_last_followup'] = days_to_last_followup

        if v['patient/vital_status'] is not None:
            vital_status = [v['patient/vital_status']]
        else:
            vital_status = []

        if v['patient/follow_ups/follow_up/vital_status'] is not None:
            if isinstance(
                    v['patient/follow_ups/follow_up/vital_status'], type([])):
                vital_status.extend(
                        v['patient/follow_ups/follow_up/vital_status'])
            else:
                vital_status.append(
                        v['patient/follow_ups/follow_up/vital_status'])

        results['vital_status'] = vital_status

        return results

    def __clinical_parse_to_dict(self, node):
        elements = {}

        for child in node:
            key = clinical._matcher.match(child.tag).group(2)
            if 'prefered_name' in child.attrib:
                key = child.attrb['prefered_name']

            if key in elements and elements[key] is not None:
                v = elements[key]
                if isinstance(v, type([])):
                    v.append(self.__clinical_parse_to_dict(child))
                else:
                    elements[key] = [v, self.__clinical_parse_to_dict(child)]
            else:
                elements[key] = self.__clinical_parse_to_dict(child)

        if node.text is not None and '\n' not in node.text:
            # key = clinical._matcher.match(node.tag).group(2)
            # if 'prefered_name' in node.attrib:
            #     key = node.attrb['prefered_name']

            # elements[key] = node.text
            return node.text

        return elements

    def __print_node(self, node, level="", lastElement=False):
        if lastElement:
            if len(node) > 0:
                line = level + "└─┬> "
                level = level + "  "
            else:
                line = level + "└──> "
                level = level + "  "
        else:
            if len(node) > 0:
                line = level + "├─┬> "
                level = level + "│ "
            else:
                line = level + "├──> "
                level = level + "│ "

        key = clinical._matcher.match(node.tag).group(2)
        if 'prefered_name' in node.attrib:
            key = node.attrib['prefered_name']
        if node.text is not None and "\n" not in node.text:
            print(line + key + ": " + node.text)
        else:
            print(line + key)

        for idx, child in enumerate(node):
            self.__print_node(child, level, idx == len(node)-1)
