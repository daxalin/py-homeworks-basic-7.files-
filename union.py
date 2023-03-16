def read_from_file():
    list_of_files = ['1.txt', '2.txt', '3.txt']
    union_files = []
    for file in list_of_files:
        with open(file, "r", encoding='utf-8') as f:
            temp = []
            for line in f:
                temp.append(line.strip())
            temp.insert(0, str(len(temp)))
            temp.insert(0, file)
            union_files.append(temp)
        union_files.sort(key=len)

    file = 'all_text'
    with open(file, 'w', encoding='utf-8') as f:
        for string in union_files:
            for _ in string:
                f.writelines(_ + '\n')
    return

read_from_file()