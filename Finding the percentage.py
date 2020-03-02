# this function use to print dictionary data using list comprehension
# dic={}
dic={}
for i in range(int(input())):
    key, *value=input().split()
    dic[key]=list(map(float,value))
numbers = dic[input()]
print("{0:.2f}".format(sum(numbers)/len(numbers)))


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

