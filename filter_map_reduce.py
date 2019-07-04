from functools import reduce
lists=[1,2,3,4,5]
a=list(filter(lambda a:a%2==0,lists)) # use of filter to filter data from lists
print(a)

b=list(map(lambda a:a*2,a))
print(b)

c=reduce(lambda a,b:a+b,b)
print(c)