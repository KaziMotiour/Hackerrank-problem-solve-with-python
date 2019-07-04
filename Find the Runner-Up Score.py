import array
n=int(input())
arr=array.array('i',map(int,input().split()))
sat=set(arr)
a=max(sat)
sat.remove(a)
print(max(sat))