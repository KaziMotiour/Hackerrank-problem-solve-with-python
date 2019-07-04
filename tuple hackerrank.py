x = int(input())
integer_list = tuple(map(int, input().split()))
list=[]
for i in range(x):
    list.append(integer_list[i])
a=tuple(list)
print(hash(a))
