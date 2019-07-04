import string
alpha = string.ascii_letters
n = int(input())
l = []
for i in range(n):
    s='-'.join(alpha[i:n])
    print((s[::-1]+s[1:]).center(4*n))


#def print_rangoli(size):
#    import string
 #   alpha = string.ascii_letters
 #   n = size
 #   for i in range(n,0,-1):
  #      if len(alpha[i:n])!=0:
   #         s='-'.join(alpha[i:n])
    #        print((s[::-1]+s[1:]).center(4*n-3,'-'))
   # for i in range(n):
   #     s='-'.join(alpha[i:n])
   #     print((s[::-1]+s[1:]).center(4*n-3,'-'))


#if __name__ == '__main__':
#    n = int(input())
#    print_rangoli(n)