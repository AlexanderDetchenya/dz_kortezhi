text = input("Введите ваш текст: ")
spisok = text.split(' ')
print(spisok)
znaki = [',', '!', ':', ';', '?', '.']
g = 0
for i in spisok:
    if i[-1] in znaki:
        spisok[g] = i[:-1]
        i = spisok[g]
    if i[0] in znaki:
        spisok[g] = i[1:]
    g += 1
for i in spisok:
    print(i, end=' ')
# print()

#привет! как твои дела?