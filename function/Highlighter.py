import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from operation.corpus_search.CorpusCommandParser import CommandParser


class HighLighter(object):
    def __init__(self, string: str):
        self._s = string
        self._replaced = []

    def add(self, commandInfo: CommandParser):
        for i in commandInfo.getWordList():
            for j in i:
                for k in j:
                    if k not in self._replaced:
                        self._s = self._s.replace(k, '<span class=\'highlight\'>' + k + '</span>')

    def get(self):
        return self._s


# if __name__ == '__main__':
    # print(HighLighter(Token('北京 上海'), '北京在在在上海的').get())