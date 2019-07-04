arr=[]
n=int(input())
list=[[input(),float(input())] for _ in range(n)]
x=10000.0
a=0
i=0
j=1
while(n!=0):
    if(list[i][j]<x ):
        x=list[i][j]
        i+=1
        n-=1
        a+=1
    else:
        i+=1
        n-=1
        a+=1
i=0
j=1
y=1000.0
p=0
for i in range(len(list)):
    if(list[i][j]>x):
        if(list[i][j]<y):
            y=list[i][j]
            z = list[i][j]
            i+=1
            a-=1
            n+=1

        else:
            pass

    else:
        i+=1
        a-=1
        n+=1

i=0
j=1
for i in range(len(list)):
    if list[i][j]==y:
        arr.append(list[i][j-1])
        i+=1
        p+=1


    else:
        i+=1
        a+=1

arr.sort()
for i in range(len(arr)):
    print(arr[i])
