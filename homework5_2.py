with open("text_1.txt", "r", encoding="utf-8") as f:
    t_list = f.readlines()
    lines_count = len(t_list)
    print(f"в файле {lines_count} строк")
    for i in range(len(t_list)):
        print(f'в строке {i+1} {len(t_list[i])} символов')
    for k, i in enumerate(t_list, 1):
        print(f"в строке {k} {len(i.split())} слов")

