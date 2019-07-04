#Width=30
#print('hacarrank'.ljust(Width, '-'))
#print('hacarrank'.rjust(Width, '-'))
#print('hacarrank'.center(Width, '-'))
#print('matiour'.center(Width, '.'))
#print('matiour'.ljust(Width, '!'))

thickness = int(input()) #This must be an odd number
c = 'H'
j=thickness-1
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness+1)+c+(c*i).ljust(thickness))
for i in range(thickness+1):
    print((c*thickness).rjust(thickness+4),(c*thickness).rjust(thickness*4))
for i in  range((thickness+1)//2):
    print((c*thickness*6).center(thickness+32))
for i in range(thickness):
    print((c*thickness).rjust(thickness+4),(c*thickness).rjust(thickness*4))
for i in range(thickness+1):
    print((c*j).rjust(thickness+22)+c+(c*j).ljust(thickness+22))
    j-=1

