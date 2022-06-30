#trunc - оставление целой части от числа
#floor - округление в меньшию
#ceil - округление в большую
import math
array = list(map(int, input().split()))
print(math.ceil(2*array[2]*(array[1]+array[0])/16))

#3
print( sum([math.ceil(int(input())/2), math.ceil(int(input())/2), math.ceil(int(input())/2)]) )
#print(sum([ceil(int(input()) / 2) for _ in range(3) ])) - через фор было проще

#2
print(math.ceil(int(input())/4))

#1
print(math.ceil(int(input())/10))

