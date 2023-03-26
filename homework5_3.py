with open("text_3.txt", 'r', encoding="Utf-8") as f:
    num = 0
    result = 0
    for i in f:
        if float(i.split()[1]) < 20000:
            print(i.split()[0])
        result += float(i.split()[1])
        num += 1
    print(f'{"-"*58}\nсредняя величина доходов {round(result/num, 3)}')


    # empl_dict = {i.split()[0]: float(i.split()[1]) for i in f}
    # print(f'средняя зарплата = {sum(empl_dict.values())/len(empl_dict)}\n'
    #       f'сотрудники с низкой зарплатой:\n'
    #       f'{[el[0] for el in empl_dict.items() if el[1] < 20000 ]}')
