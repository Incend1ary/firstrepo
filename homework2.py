new_list = [4, 5.2, True, [1, 4], None, 'привет']
for i, item in enumerate(new_list, 1):
    print(f"{i} {item} {type(item)}")


inp_list = list(input("введите значения списка без запятых и пробелов "))
print(inp_list)
for i in range(1, len(inp_list), 2):
    inp_list[i-1], inp_list[i] = inp_list[i], inp_list[i-1]
print(inp_list)


# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

month = int(input("Введите номер месяца: "))
month_dict = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август",
              9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}
season_list = ["весна", "лето", "осень", "зима"]
if month in month_dict:
    print(month_dict[month])
    print(season_list[month // 3 - 1])
else:
    print("error")

# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
# слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить
# только первые 10 букв в слове.
text = input("введите слова разделенные пробелами")
split_text = text.split(" ")
print(text)
print(split_text)
for i, p in enumerate(split_text, 1):
    print(f"{i}, {p[:10]}")


# Реализовать структуру Рейтинг, представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если
# в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
# значением должен разместиться после них.

score = [7, 6, 4, 3, 1]
print(score)
number = int(input("введите число"))
#i = 0
#for n in score:
#    if number <= n:
#        i += 1
#score.insert(i, number)
#print(score)


if number <= min(score):
    score.append(number)
elif number > max(score):
    score.insert(0, number)
else:
    s = score.count(number)
    if s > 0:
        score.insert(s + score.index(number), number)
    else:
        i = 0;
        for t in score:
            if number <= t:
                i+=1
        score.insert(i, float(number))

print(score)

goods = []
features = {"название:": "", "цена:": "", "количество:": "", "единица измерения:": ""}
features_dict = {"название:": [], "цена:": [], "количество:": [], "единица измерения:": []}
i = 0
while True:
    i += 1
    if input("для завершения ввода данных напишите Q для продолжения жмите enter").upper() =="Q":
        break
    else:
        for key in features.keys():
            features[key] = input(f"введите {key}")
            features_dict[key].append(features[key])
        print(f"{features}\n")
    goods.append((i, features))
    print(f"\n{goods}\n")
    print(f"\n{(features_dict)}\n")


