from collections import Counter
shoesNumber,shoesSize = int(input()),list((int(i) for i in input().split()))
#shoesSize = list((int(i) for i in input().split()))
sizeAvailable = Counter(shoesSize)
total = 0
for i in range(int(input())):
    a=list(int (i) for i in input().split())
    if a[0] in sizeAvailable.keys() and sizeAvailable[a[0]] > 0:
        sizeAvailable[a[0]]-=1
        total += a[1]
print(total)
#print(sizeAvailable[6])
#print(sizeAvailable.items())
# print(sizeAvailable.keys())
# print(sizeAvailable.values())