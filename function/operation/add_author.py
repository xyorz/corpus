import os
import re

index_dir = "C:/Users/Administrator/Desktop/corpus/doc/"


def read_file(index: str, list_name):
    l = os.listdir(index)
    for i in l:
        if os.path.isfile(index + i) and i.endswith(".utf8"):

            with open(index + i, 'r', encoding='utf-8') as file:
                text = ""
                first_line = True
                next_line = file.readline()
                # current_section = ""
                current_author = ""
                while next_line:
                    if first_line:
                        if no_dot(next_line):
                            next_line = "--d" + next_line
                        else:
                            next_line = "--d" + i.replace(".utf8", "") + "\n" + next_line
                        first_line = False
                        text += next_line
                        next_line = file.readline()
                        continue
                    if next_line.find("--a") != 0 and next_line.find("--d") != 0 and next_line.find("--s") != 0 and next_line.find("--p") != 0 and next_line != "\n":
                        if no_dot(next_line):
                            # 如果开头是姓
                            if 2 <= len(next_line) <= 4 and (next_line.replace("\n", "")[0] in name_list or next_line.replace("\n", "")[0:2] in name_list):
                                current_author = next_line
                                # next_line = "--a" + next_line
                                # text += next_line
                                next_line = file.readline()
                                continue
                            # 如果当前已经拥有姓名
                            if current_author:
                                next_line = "--a" + current_author + "--s" + next_line
                            # 如果没有拥有
                            else:
                                next_line = "--s" + next_line
                        else:
                            next_line = "--p" + next_line
                    text += next_line
                    next_line = file.readline()

            with open(index + i, 'w', encoding='utf-8') as file:
                file.write(text)

        elif os.path.isdir(index + i):
            read_file(index + i + '/', list_name)


def no_dot(line: str):
    a, b, c, d = line.find("。"), line.find("，"), line.find("！"), line.find("？")
    for i in [a, b, c, d]:
        if not i < 0:
            return False
    return True


name_list = []

with open("百家姓.txt", "r", encoding="utf-8") as file:
    line = file.readline()
    while(line):
        name_list.append(line.replace("\n", ""))
        line = file.readline()

read_file(index_dir, name_list)