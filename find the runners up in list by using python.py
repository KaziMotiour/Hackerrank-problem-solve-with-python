
list=[]
number=int(input("Enter the array size: "))
print("Enter the array element: ")

for i in range(number):
    data=int(input())
    list.append(data)

a=max(list)

while max(list)==a:
    list.remove(max(list))

print(max(list))
