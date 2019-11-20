import sys
from xml.etree.ElementTree import XMLPullParser
from xml.etree.ElementTree import ElementTree


class IDSetter(object):
    def __init__(self, doc_id):
        self._count = 1
        self._id = str(doc_id)
        self._tree = ElementTree()

        self._Title = ''
        self._Author = ''
        self._Dynasty = ''
        self._Category = '原文'

    def set(self, doc):
        parser = XMLPullParser(['start', 'end'])
        parser.feed(doc)
        for event, elem in parser.read_events():
            if event == 'start':
                if elem.tag == '文档':
                    self._tree = ElementTree(elem)
                    elem.set('id', self._id)
                if elem.tag == '章节' or elem.tag == '段' or elem.tag == '句':
                    self._id += '.' + str(self._count)
                    elem.set('id', self._id)
                    self._count = 1
                    if elem.tag == '章节':
                        if '作者' in elem.attrib.keys():
                            self._Author = elem.attrib['作者']
                        if '时期' in elem.attrib.keys():
                            self._Dynasty = elem.attrib['时期']
                        if '类别' in elem.attrib.keys():
                            self._Category = elem.attrib['类别']
                    # 如果段和句没有作者/时期/类别标签，将章节的数据写入
                    if elem.tag == '段' or elem.tag == '句' or elem.tag == '章节':
                        if '作者' not in elem.attrib.keys():
                            elem.attrib['作者'] = self._Author
                        if '时期' not in elem.attrib.keys():
                            elem.attrib['时期'] = self._Dynasty
                        if '类别' not in elem.attrib.keys():
                            elem.attrib['类别'] = self._Category
            elif event == 'end':
                if elem.tag == '章节' or elem.tag == '段' or elem.tag == '句':
                    self._count = int(self._id.split('.')[-1])
                    self._id = self._id[0:self._id.rfind('.')]
                    self._count += 1
                    if elem.tag == '章节':
                        self._Author = ''
                        self._Dynasty = ''
                        self._Category = '原文'
        return self

    def write(self, fileName):
        self._tree.write(fileName, encoding='utf-8')


def reset():
    with open('./IDCounter.txt', 'w+', encoding='utf-8') as file:
        file.write('0')


if __name__ == '__main__':
    # if sys.argv[1] == 'reset':
    #     reset()
    # else:
    with open('./论语解集义疏.xml', 'r', encoding='utf-8') as file:
        exampleXML = file.read()
    with open('./index/IDCounter.txt', 'r', encoding='utf-8') as file:
        count = file.read()
        count = int(count)
        s = IDSetter(count)
        s.set(exampleXML).write('./document/doc_ancient/ttt.xml')
    with open('./index/IDCounter.txt', 'w+', encoding='utf-8') as file:
        file.write(str(count + 1))

