String=input()
Vowels=['A','E','I','O','U']
Consonant=['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
Vow=[]
cons=[]
dic={}
for i in range(len(String)):
    for j in range(len(Vowels)):
        if String[i] in Vowels[j]:
           # print(Vowels[j])
            Vow.append(String[i:len(String)])

for i in range(len(String)):
    for j in range(len(Consonant)):
        if String[i] in Consonant[j]:
            cons.append(String[i:len(String)])
Vowel = Vow[0]
consonant = cons[0]
k=0
p=0
c=[]
for i in range(len(consonant)):
    for j in range(len(consonant)):
        for k in range(len(Consonant)):

            con = consonant[0:0]
            print(consonant[0:0])
            if con[0] in Consonant[k]:
                c.append(con)


print(c)
