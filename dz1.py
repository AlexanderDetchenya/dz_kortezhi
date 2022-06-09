# Задание №1
#
# Найти самое длинное слово в строке.

stroka = input('Введите строку, чтобы слова разграничивались пробелом: ')
slova = stroka.split(' ')
dlina = []


for i in slova:
    k = len(i)
    dlina.append(k)

for i in dlina:
    if i == max(dlina):
        print(i)
        print('Самое длинное слово/слова: ', slova[dlina.index(i)])


print('Самое длинное слово/слова: ', slovar.keys[i])