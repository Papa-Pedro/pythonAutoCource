#1
print(int(input()//1000));

#2
a=int(input());
b=int(input())
print( int(b//a))
#print(*[j // i for i, j in [[int(input()), int(input())]]])

#3
print(int(int(input())//int(input())))

#4
print(int(input())%10);

#5
print((int(input())//100)%10);

#6
print(sum(map(int,input())))

#7
def howBills(x,y):
    return x%y, x//y

how = 0
howAll = 0
bills = [100, 20, 10, 5, 1];
evro = int(input());
i = 0;

while evro != 0:
    evro, how = howBills(evro, bills[i]);
    howAll +=how;
    i+=1;

print(howAll)

#8 from the beginning of the day n - minuts, time is now?
minuts = int(input())
print(minuts%1440//60, minuts%60)
#Хорошее решение - print(*divmod(int(input()) % 1440, 60))

#9 Вывести след. четное
numbers = int(input())
print(numbers-numbers%2+2)

#10 h:mm:ss
n = int(input())%86400;
mm, ss = divmod(n%3600, 60)
if len(str(mm))<2: mm = "0"+str(mm)
if len(str(ss))<2: ss = "0"+str(ss) 
print(n//3600, mm, ss, sep = ':')
