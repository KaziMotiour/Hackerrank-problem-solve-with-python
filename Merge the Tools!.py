import math
import time

def merge_the_tools(string, k):
    subString = []
    j, l = 0, k
    x = math.ceil(len(string) / k)
    for i in range(x):
        subString.append(string[j:l])
        l += k
        j += k
    j = 0
    s = ''
    i=0
    # def rec(i,j,s):
    #     for k in subString[j]:
    #         if k not in s:
    #             s+=k
    #     i+=1
    #     j += 1
    #     print(s)
    #     s = ''
    #     if i == len(subString):
    #         exit()
    #     else:
    #         rec(i,j,s)
    # rec(i,j,s)
    def rec(i,j,s ):
        for k in subString[j]:
            if k not in s:
                s+=k
        i+=1
        j += 1
        print(s)
        s = ''
        if i == len(subString):
            exit()
        else:
            rec(i,j,s)
    rec(i,j,s)



if __name__ == '__main__':
    print(time.ctime())
    string, k = input(), int(input())
    merge_the_tools(string, k)
    print(time.ctime())