# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
# платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
# час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
# скрипт с параметрами.


from sys import argv
from random import randint
def salary():
    try:
        time, rate, bonus = map(int, argv[1:4])
        print(f"зарплата = {time * rate + bonus}")
    except ValueError:
        print("Введите 3 численных значения в скрипте")


# def bigger(list):
#     new_list = []
#     for i in range(1, len(list)):
#         if list[i] > list[i-1]:
#             new_list.append(list[i])
#     return new_list


def bigger(list):
    my_list = [list[i] for i in range(1, len(list)) if list[i] > list[i-1]]
    return my_list


salary()
print(bigger([1, 3, 8, 4, 9, 45, 33, 33, 313]))


new_ = [num for num in range(20, 241) if (num % 20 == 0 or num % 21 == 0)]
print(new_)

new_list = [randint(-20, 20) for _ in range(20)]
gen_list = [num for num in new_list if new_list.count(num) == 1]
print(gen_list)


