n=int(input())

#solve useing dictonary
check={True:'not wired', False:'wired'}
print(check[n%2==0 and (n in range(2,5) or n>20)])

#sove using if statement:
if n%2==0 and (n in range(2,5) or n>20):
    print('not wired')
else:
    print('wired')


