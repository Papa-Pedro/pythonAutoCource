#s.upper() регистр up

print( input().upper() )

#s.lower() регистр down

print( input().lower() )
print( (lambda s: s[0:3].upper()+s[3:-3].lower()+s[-3:].upper()) (input()) )

#s.count(n) or s.count(n, {2}, {7}) = вхождение подстроки n в строку s, искать с 2 по 7 элемент

print(input().lower().count('e'))

#s.find('o') or s.find('o', {2}, {7}) = поиск индекса элемент o со 2 по 7 элемент в строке s, если ничего не нашел -1

print(input().find('a'))

#s.rfind() - find() с другой стороны

print(input().rfind('a'))

#s.index('0') - find, но при отсутсвия подстроки вернет ошибку
#s.replace('e', 'a', {2}) - замена символа e на a два раза

print( input().replace('w', '').replace('z', '') )
print(input().replace(' ', ','))

#s.isalpha() - строка целиком буквенная - true, нет - false
#s.isdigit() - строка целиком буквенная - false, нет - true
#s.ljust(5, {'a'}) = если строка короче 5 символов добавляет символ а в начало, если a-NaN то пробел
#s.rjust(5) - тоже самое справа
#s.split({n}) - разбивает строку на массив, разделительный символ n, если n-NaN то пробел

print(len(input().split()))

#s.join(n) - объединение списка строк
#s.strip() -  удаляя как начальные, так и конечные символы (rstrip - справа, lstrip - слева)

import re
s = 'Codeforces'
print(type())
print( re.sub( "[A,a,O,o,Y,y,E,e,u,U,I,i]",'',( s.lower() ) ) )
print('.'+'.'.join( re.sub( "[A,a,O,o,Y,y,E,e,u,U,I,i]",'',( s.lower() ) )) )
