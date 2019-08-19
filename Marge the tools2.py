def merge_the_tools(string, k):
    def ops(y):
        y[0] += k
        y[1] += k
        return y[1]

    y = [-k, 0]
    subString = [string[y[0]:y[1]] for i in range(len(string)) if ops(y)<=len      (string)]
    j = 0
    s = ''
    for i in range(len(subString)):
        s += [i for i in subString[j] if (1 if i not in s else i)]
        j += 1
        print(s)
        s = ''

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)