with open('./data.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data.find('\r'))
