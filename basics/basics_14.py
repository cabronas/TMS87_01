"""
Пользователь вводит цены 1 кг конфет и 1 кг печенья.
Найдите стоимость:
а) одной покупки из 300 г конфет и 400 г печенья;
б) трех покупок, каждая из 2 кг печенья и 1 кг 800 г конфет.
"""
conf, pech = float(input()), float(input())
aconf = conf * 0.3
apech = pech * 0.4
print(aconf, apech)
b = ((2 * pech) + (1.8 * conf)) * 3
print(b)
"""
1000 = 25
300 = x
"""
