chars_to_skin = [' ', '+', '$', '#', '-', '~', '|', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def get_zh_to_hant_list(input: str, zh_to_hant_map):
    index = 0
    transform_list = []
    for char in input:
        transform_list.append([])
        if char in chars_to_skin:
            index += 1
            continue
        hits = zh_to_hant_map.filter(zh=char)
        for r in hits:
            transform_list[index].append(r.hant)
        index += 1
    return transform_list


def get_res(input, zh_to_hant_list, index):
    if index > len(input)-1:
        return ['']
    res_list = get_res(input, zh_to_hant_list, index+1)
    if len(zh_to_hant_list[index]) == 0:
        for i in range(len(res_list)):
            res_list[i] = input[index] + res_list[i]
    elif len(zh_to_hant_list[index]) == 1:
        for i in range(len(res_list)):
            res_list[i] = zh_to_hant_list[index][0] + res_list[i]
    else:
        delete_count = 0
        for i in range(len(res_list)):
            r = res_list[i]
            for j in range(len(zh_to_hant_list[index])):
                res_list.append(zh_to_hant_list[index][j] + r)
            delete_count += 1
        for _ in range(delete_count):
            del res_list[0]
    return res_list


def get_res_list(input, zh_to_hant_map):
    zh_to_hant_list = get_zh_to_hant_list(input, zh_to_hant_map)
    res_list = get_res(input, zh_to_hant_list, 0)
    if not (len(res_list) == 1 and res_list[0] == input):
        res_list.insert(0, input)
    return res_list
