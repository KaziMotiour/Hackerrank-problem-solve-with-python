import string
Text=string.ascii_letters
Length = int(input('Enter the size: '))
N=Length
List=[]
for i in range(Length):
    a=Text[0:N]
    N-=1
    List.append('  '.join(a[::-1]+a[1:]).center(5*Length))

print('\n'.join((List[::-1])))
print('\n')
print('\n'.join((List[::])))


List=[]
N=Length
for i in range(Length):
    a=Text[0:N]
    N-=1
    List.append(' '.join(a[::]))
print('\n'.join((List[::-1]+List[1:])))
List=[]
N=Length
for i in range(Length):
    a=Text[0:N]
    N-=1
    List.append(' '.join(a[::]).rjust(10))
print('\n'.join((List[::-1]+List[1:])))