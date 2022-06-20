#!!!Типы данных!!
#Целое число int
i2 = 43;
i3 = 344;
print(i2, type(i2));
#Вещественное число float
f1 = 3.2;
f2 = 42.0;
print(f1, type(f1));
#Строка str
str1 = "First Attemption";
str2 = 'firest attrmption';
print(str1, type(str1));
#Булевая bool
bTrue = True;
bFalse = False;
print(bTrue, type(bTrue));
#Список list (массив)
lst = [i2, f2, str1, str2, bTrue];
print(lst, type(lst))
#Словарь disk ('ключ': значение)
dsk = {'a': i2, 'b': f1};
print(dsk, type(dsk))
#Кортеж typle (не изменяем массив)
tpl = (i2, f2, str1);
f1 = f2+f1;
print(tpl, type(tpl)) #в кортеже i будет равно 43, инициализация при объявлении
#Множество set (набор эксклюзивных объектов)
st = {i2, f1, i2};
print(st, type(st)) #на выходе последний элемент не отобразится
#Файлы file
input = open('D:\Python3105\Example\exemple.txt', 'r');
fl = input.read();
print(fl, type(f1));

#!!!Операции!!

print (i2+i3, i2+f2, f1+f2, i2-i3, 12*f1, i3/i2, i2/f1, i2 ** 3);
#387 85.0 87.2 -301 542.4000000000001 8.0 0.9513274336283185 79507
print('Целая часть от деления 344//43 = ', i3 //i2) #8
print('Остаток от деления 344%43 = ', i3%i2) #0
#Приоритет: скобки -> степерь -> * / // % -> + -
#Встроенные операции
print(abs(-7), abs(7), min(-45, 90, 22.9, -3333 / 11), max(-45, 90, 22.9, -3333 / 11));
#7 7 -303.0 90
print(pow(2,5), round(3.5), round(5.13123, 2));
#32 4 5

a=input();
a=a+12;
#d=int(input());
print('я прибавил 12 получил', a);

