def div(a, b):
    try:
        a, b = int(a), int(b)
        div_num = a / b
    except ValueError:
        return "Value Error"
    except ZeroDivisionError:
        return "деление на ноль"
    return round(div_num, 3)


print(div(input("Введите делимое - "), input("введите делитель: ")))
