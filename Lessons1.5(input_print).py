#input
a=int(input("Введите целое число - "));
#input().split()
print('К введеному числу прибавили 12, получили - ',a+12);
a, b = input('Введите два числа через пробел - ').split();
a = int(a);
b = int(b);
print('Мы перемножили эти два числа - ',a*b);
#map( , input().split)
a, b, c = map(int, input().split())

#Упражнения
#1
age = int(input());
print(age+1);
#2
a,b = map(int, input().split());
print(a+b)
#3
crane=int(input())/3;
print(round(crane/2),round(crane*2),round(crane/2));
#4
#X Y Z
#Y-2=X
#Y+7=Z
#X = 3
#Y = 5
#Z = 12
office = list(map(int, input().split()));
print(sum([office[0]*3, office[1]*5, office[2]*12]));
#5
#Итеративная распаковка
print(*[n*a*b*2 for n, a, b in [map(int, input().split())]]);
#6
from statistics import mean;
print(mean(map(int, input().split())));

#7 3600 60 1
def sumMinutes():
    day = 0
    for i in range(3):
        day = day + int(input())*60**(2-i)
    return day
print(abs(sumMinutes()-sumMinutes()))

#8 Garry + Larry = All Garry = Larry - 1 Larry = Garry - 1
Garry, Larry = map(int, input().split());
print(Larry - 1, Garry - 1)

#9
print(abs(int(input()))+abs(int(input())))

#10
print(*[max(x,y) - min(x,y) for x,y in [map(float, input().split())]])

#11
print(*[max(grade) for grade in [map(int, input().split())]])

#12
a, b, c = (int(input()) for _ in range(3))
print(max(a+b*c, a*(b+c), a*b*c, (a+b)*c, a+b+c))

#13
print(*(lambda x=float(input()): (round(x,2), round(x, 3)))());
