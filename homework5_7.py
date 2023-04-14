import json
with open("text_7.txt", "r", encoding="Utf-8") as s:
    new_dict = {line.split()[0]: int(line.split()[2])-int(line.split()[3]) for line in s}
    result = [new_dict, {'average profit': sum(int(i) for i in new_dict.values() if int(i) > 0) /
                                           len([int(i) for i in new_dict.values() if int(i) > 0])}]
    with open("text_7.json", "w", encoding="utf-8") as write_f:
        json.dump(result, write_f, ensure_ascii=False, indent=4)

