#1 check positive
print(int(input())>0);

#2 Parity check
print((int(input())%2)==0);

#3 Div six
print((int(input())%6)==0);

#4 nan div six
print((int(input())%9)!=0);

#5
print(int(input())%10==2);

#6 div7
a,b = map(int, input().split())
print(a%7==0 and b%7==0)
#print(all([not int(i) % 7 for i in input().split()])) - хорошее решение

#7
i,j,d = input().split();
print(i == j == d);
#print(len(set(input().split())) == 1)
#вариант преобразования к множеству и сравнения его размера с одинм!

#8
print(5<int(input())<=19);

#9
print(input()=='awesome' or input()=='awesome')

#10
print(len(set(input().split()))<=2);

#11
print(len(input())==2);

#12
array = list(map(int, input().split()));
maxArray = max(array);
array.pop(array.index(max(array)));
print(pow(maxArray, 2) == ( pow(array[0], 2)+pow(array[1], 2) ));
#Усложнил, нужен был сортед и взять первый элемент...

