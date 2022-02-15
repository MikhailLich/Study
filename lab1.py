import numpy as np
from random import randint
b=3
a=0
array=[]
while a!=2:
    a=int(input("Введите число 2 = "))
print("----------------------------------------------------")
print(" Мат. операции с числом ",b)
print(" Сложение",a,"+ 3 =",a+b,"\n","Умножение",a,"* 3 =",a*b,"\n","Вычитание",a,"- 3 =",a-b,"\n","Возведение в степень",a,"^ 3 =",pow(a,b))
print("----------------------------------------------------")
array = np.random.randint(0, 10, size=(a, a))
print(array)