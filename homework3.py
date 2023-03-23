def div(a, b):
    try:
        a, b = int(a), int(b)
        div_num = a / b
    except ValueError:
        return "Value Error"
    except ZeroDivisionError:
        return "деление на ноль"
    return round(div_num, 3)


def data(**kwargs):
    print(list(kwargs.values()))
    return " ".join(kwargs.values())

def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    num_sum = sum(my_list)
    return num_sum - min(num_1, num_2, num_3)


def my_pow(x, y):
    try:
        result = 1
        for p in range(abs(y)):
            result /= x
        return result
#       return 1/(x**abs(y))
    except TypeError:
        return "введите целое число и степень числа"

def sum_list():
    s = 0
    while True:
        el = input("введите значения, через пробел, для выхода введите  q  ")
        el = el.split()
        for num in el:
            if num == 'q':
                return s
            else:
                try:
                    s+=int(num)
                except(ValueError):
                    print("для выхода напишите 'q' ")
                    break


def big_first_letter(words):
    s = ""
    for word in words.split():
        chars = 0
        for char in word:
            if 97<=ord(char)<=122:
                chars+= 1
        if chars == len(word):
            s += word.title() + " "
        else:
            s = "можно использовать только маленькие латинские буквы"
            break
    return s


print(big_first_letter("hello 23ew friend"))
print(sum_list())
print(my_pow(-2, -3))
print(my_func(int(input("введите число 1")), int(input("введите число 2")), int(input("введите число 3"))))
print(data(name=input("введите имя: "), surname=input("введите фамилию: "), address=input("введите адрес: ")))
print(div(input("Введите делимое - "), input("введите делитель: ")))


