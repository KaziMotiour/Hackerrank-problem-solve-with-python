import math
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
    for i in range(len(subString)):
        for k in subString[j]:
            if k not in s:
                s+=k

        j += 1
        print(s)
        s = ''


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)