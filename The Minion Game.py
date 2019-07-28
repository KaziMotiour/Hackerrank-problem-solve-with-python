String = input()
Vowels = ['A','E','I','O','U']
vow = 0
cons = 0
length = len(String)
dic = {}
for i in range(len(String)):
    if String[i] in Vowels:
        vow = String[i:length] if vow == 0 else vow
    else:
        cons = String[i:length] if cons == 0 else vow

print(vow)
print(cons)