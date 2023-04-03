with open("text_4.txt", "r", encoding="Utf-8") as f:
    with open("text_new.txt", "w", encoding="Utf-8") as n:
        engl_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
        for i in f:
            line =i.split()
            line[0] = engl_dict[line[0].title()]
            str_text = " ".join(line)
            print(str_text, file=n)