#print()
#print(value, ..., sep=' ', end='\n')
#sep - разделитель между значениями
#end - действие в конце ввода

#1
print("Привет", "Мир", sep=', ', end='!\n');
'''
#2
print(*input().split(),  sep=',')

#3
a = int(input())
print(a-1, a, a+1, sep='<');

#4
#print(input()+'---'+input()+'---'+input())
print(*[input() for _ in range(3)], sep='---')
'''
#5
print(*range(1,6), sep=input());

#5
print(input(), end=' - Сказала она!\n');

print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
print('Основатель', 'Питона', sep='_', end='!')
