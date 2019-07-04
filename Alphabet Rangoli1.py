import string
n = int(input())
Asci = string.ascii_letters
j=0
#a=['a','b','c']
#l=['f','k','l']
#for i in range(n):
#    print('\n'.join(l[j]+Asci[i]+Asci[j]))
 #   j+=1
L = []
#solution 1
for i in range(n):
    s = '-'.join(Asci[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, '-'))

print('\n'.join(L[::-1]+L[1:]))