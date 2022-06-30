#\n - перенос строк
#\a - перевод формата
#\t - табуляция - 4 пробела
#\r - возврат каретки
#\t \v - горизонтальная/вертикальная табуляция
#r'' - экранирование всех служебных символов в строке
print('/\_/\\\n>^,^<\n / \\\n(|_|)_/');
print('  /~~~\\\n //^ ^\\\\\n(/(_*_)\)\n_/\'\'*\'\'\_\n(/_)^(_\)')
#"первый - {1}, второй - {2}".forman(first, second)
#'Первый - {first}, второй - {second}, третий - {third}'.format(first=first, first=second, third=first)

print('Что Вы сказали? {}? Какое интересное слово'.format(input()))
print('Здравствуйте, {1} {0}!'.format(input(), input()))
print((lambda number: f'Для числа {number} предыдущим будет число {number-1}.\nДля числа {number} следующим будет число {number+1}.')(int(input())))

#f - cтроки
name = 'Семён';
text = f"""Дорогой {name}.lower(), 
баланс Вашего лицевого счёта составляет {34.2} руб.""" #в фигурных скобках переменные
print(text)

#1
print(f'Мое имя {input()}!')

#2
print(f'Hello {input().upper()}. You are {input()} years old.');

#3
print(f'{input()}, вам исполнится 77 лет в {int(input())+77}')

#4
print((lambda number: f'{number} сек - это {number//60} мин. {number%60} сек.')(int(input())));

#5
print((lambda size: f'Разрешение экрана: {size[0]} x {size[1]}.\nОбщее количество пикселей = {int(size[0])*int(size[1])}.')(input().split()))

#6
print((lambda div1, div2: f'{div1} / {div2} = {div1/div2}\n{div1} // {div2} = {div1//div2}\n{div1} % {div2} = {div1%div2}')( int(input()),int(input()) ))

#7
print((lambda x,y,z: f'Vector A({x}, {y}, {z})\nVector B({x+5}, {y+5}, {z+5})')(*[int(input()) for _ in range(3) ]) )

#8
print((lambda dollar, amount: f'Current dollar rate is {dollar}. You want buy {int(amount)} dollars\nYou must pay {dollar*amount}')( float(input()), int(input()) ))
