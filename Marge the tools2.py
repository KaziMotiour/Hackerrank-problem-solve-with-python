import math
def merge_the_tools(string, k):
    def ops(y):
        y[0] += k
        y[1] += k
        return 1

    y = [-k, 0]
    subString = [string[y[0]:y[1]] for i in range(math.ceil(len(string) / k)) if ops(y)]
    j = 0
    s = ''
    m=0
    for i in range(len(subString)):
       # s += [p for p in subString[j] if (1 if p in s else p)]
        for i in subString[j]:
            if subString[j].index(i)==m:
                s+=i
            m+=1
        j += 1
        m=0
        print(s)
        s = ''

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

