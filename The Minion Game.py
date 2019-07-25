String=input()
Vowels=['A','E','I','O','U']
Vow=[]
cons=[]
dic={}
for i in range(len(String)):
    for j in range(len(Vowels)):
        if String[i] == Vowels[j]:
            Vow.append(String[i:len(String)])
        else:
            cons.append(String[i:len(String)])
Vowel=Vow[0]
Consonant=cons[0]
k=0
v=0
print(dic.items())