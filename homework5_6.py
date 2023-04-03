mydict = {}
with open("text_6.txt", "r", encoding="Utf-8") as t:
    for line in t:
        name, stats = line.split(":")
        stats_num = ''.join(letter if letter in("1234567890") else "" for letter in stats)
        mydict[name] = sum(map(int, stats_num.split()))
print(mydict)
