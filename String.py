#String
#инициализация
a = '1';
b = "String";
c = '''Привет
Это
Строка''';
d = 'Привет\nЭто\nСтрока';
a = a+b;
#len - длинна строки
#in - вхождение строки ("hellow" in 'l')
#> - сравнение, чем дальше в алфавите буква, тем больше ее значение.
#ord - получить числовое значение симовла
#print (a,b,c,d, a*5)

#1
print(*['Я стану крутым программистом!']*3, sep='\n');

#2
print('W'*777);

#3
print('Лев Николаевич Толстой написал "Война и мир"');
'''
#4
print(input(), input(), sep='\n');

#5
a, b, c = input(), input(), input();
print(c, b, a, sep='\n');
#print("{2}\n{1}\n{0}".format(input(),input(),input()))

#6
print((input()+' ')*4);

#7
print(len(input()));

#8
print( "{1}{0}".format(input(),input()) );

#9
print(input()*3);
'''
#10

for string in (input().split()):
    print("Simvol code %s is %d." % (string, ord(string)))












