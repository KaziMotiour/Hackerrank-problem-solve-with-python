# import math
# string,factor=input(),int(input())
# subString=[]
# j,k=0,factor
# x=math.ceil(len(string)/factor)
# for i in range(x):
#        subString.append(string[j:k])
#        j+=factor
#        k+=factor
# print(subString)

# def opp(x):
#     x[0]+=1
#     x[1]+=1
#     return x[1]
# string,factor=input(),int(input())
# subString=[]
# q=len(string)
# while q>factor:
#        subString.append(string[q-factor:q])
#        q-=factor
# subString.append(string[0:q])
# print(subString)
# x=[0,1]
# ti=[string[x[0]:x[1]] for i in range(len(string)) if opp(x)<=len(string)]
# print(ti)

import math
string,factor=input(),int(input())
def ops(y):
    y[0]+=factor
    y[1]+=factor
    return 1
y=[-factor,0]
subString=[string[y[0]:y[1]] for i in range(math.ceil(len(string)/factor)) if ops(y)]
#print(subString)
j=0
s=''
for i in range(len(subString)):
    for i in subString[j]:
        if i not in s:
            s += i
    j+=1
    print(s)
    s=''
#[print(i,end='') for i in final[0]]
