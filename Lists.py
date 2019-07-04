n=int(input())
List=[]
for i in range(n):
    Fuctions,*Data = input().split()
    Datas = list(map(int,Data))
    if Fuctions=='insert':
        List.insert(Datas[0],Datas[1])
    elif Fuctions == 'remove':
        List.remove(Datas[0])
    elif Fuctions == 'append':
        List.append(Datas[0])
    elif Fuctions == 'sort':
        print(List)
        List.sort()
    elif Fuctions == 'pop':
        List.pop()
    elif Fuctions == "reverse":
        List.reverse()
    elif Fuctions == 'print':
        print(List)