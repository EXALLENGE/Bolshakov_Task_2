import random


def open_letter(a, word):
    return [i if i in a else "*" for i in word]


d = {1:"orange", 2:"pizza", 3:"satellite"}

word = d[list(d.keys())[random.randint(1,len(d)-1)]]
life = 5
k = len(word)
hideword = ["*" for i in word]
print("Отгадайте слово: \n")
letters = []
while life != 0 and ''.join(hideword).find('*') != -1:
    print(''.join(hideword))
    a = str(input('Введите букву:\n'))
    if word.count(a) > 0:
        letters.append(a)
        hideword = open_letter(set(letters), word)
    else:
        print("Wrong letter")
        life -= 1
if life!=0:
    print(''.join(hideword))
    print("You won!")
else:
    print("Ypu lost!")
