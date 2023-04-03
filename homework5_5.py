from random import randint

with open("number_text.txt", "w+", encoding="Utf-8") as t:
    number_list = [randint(1, 1000) for _ in range(100)]
    t.write(" ".join(map(str, number_list)))
    t.seek(0)
    print(sum(int(el) for el in t.read().split()))

