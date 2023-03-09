"""
Ввести почтовый адрес. Проверить доменное имя.
В случае если оно gmail.com, вывести на экран имя почтового ящика.
Иначе вывести надпись “DOMAIN NAME is not supported’
"""
s = input()
mail = s.split("@")
if mail[1] == "gmail.com":
    print(mail[0])
else:
    print("DOMAIN NAME is not supported")
