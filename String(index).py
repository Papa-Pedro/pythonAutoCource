#1
print(input()[0]);

#2
print(input()[-1]);

#3
print(input()[0:4]);

#4
print(input()[-4:]);
#print(type([i for i in string]))
#print('{}'[len('{}')-4:len('{}'-1)].format(string))

#5
print(input()[::2])

#6
print(input()[1::2])

#7
print(input()[::-1]);

#8
print(input()[::-3])

#9
string = input()
print(string[-1]+string[:-1])
#(lambda x: x[-1] + x[:-1])(input())
