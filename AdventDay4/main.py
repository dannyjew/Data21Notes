with open('PassportInfo.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    v = [x for x in data[::1]]
    print(len(v))