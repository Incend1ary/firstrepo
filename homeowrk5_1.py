with open("text_1.txt", "w", encoding="utf-8") as f:
    while True:
        line = input("введите строку: ")
        if not line:
            break
        f.write(f"{line}\n")

print("введите значение \n для окончания ввода введите пустую строку")
with open("text_1.txt", "w", encoding="utf-8") as f:
    while True:
        line = input()
        if not line:
            break
        f.write(f"{line}\n")