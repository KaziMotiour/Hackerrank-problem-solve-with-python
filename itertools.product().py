from itertools import product
a = map(int, (input()).split(" "))
b = map(int, (input()).split(" "))
print(c,d)
List = list(product(a, b))
[print(i, end='') for i in List]


x='12'
a=list(x)
b=[map(int,i) for i in a]
print(b)