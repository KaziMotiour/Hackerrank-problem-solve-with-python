# this function use to print dictionary data using list comprehension
# dic={}
dis={}
for i in range(int(input())):
    kay,*value=input().split()
    data=list(value)
    dis[kay]=data
[print(k,":",v) for k,v in dis.items()]

# d={input(): list(map(float,input().split())) for _ in  range(int(input()))}
# print(d)

# it's use to return average value of student subjects mark

# for _ in  range(int(input())):
#     key,*value=input().split()
#     data=list(map(float,value))
#     dis[key]=data
# a=dis.get(input())
# b = 0
# for i in a:
#     b += i
# print("{:.2f}".format(b/len(a))) # it return average marks of student

