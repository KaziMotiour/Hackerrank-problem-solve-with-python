from itertools import permutations
#solution 1
a = input().split()
print(a[0],int(a[1]))
List = sorted(list(permutations(a[0],int(a[1]))))
List1=[]
a = ''
for i in range(len(List)):
    for j in range(len(List[0])):
        a += List[i][j]
    print(a)

#solution 2
a,b=input().split()
List = sorted(list(permutations(a,int(b))))
for i in List:
    print(*[''.join(i) for i in List],sep='\n')

#solution 3
from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')

# testing * and join()
List=[('w','q'),('c','d')]
print(*['\n'.join(List[0])])