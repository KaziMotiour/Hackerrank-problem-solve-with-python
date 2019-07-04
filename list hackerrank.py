if __name__ == '__main__':
    n=int(input())
    list=[]
    for i in range(n):
        value=input().split()
        if value[0]=='insert':
            list.insert(int(value[1]),int(value[2]))
        elif value[0]=='remove':
            a=int(value[1])
            list.remove(a)
        elif value[0]=='append':
            list.append(int(value[1]))
        elif value[0]=='sort':
            list.sort()
        elif value[0]=='pop':
            c=list[-1]
            list.pop()
        elif value[0]=="reverse":
            list.reverse()
        elif value[0]=='print':
            print(list)
        else:
            pass
