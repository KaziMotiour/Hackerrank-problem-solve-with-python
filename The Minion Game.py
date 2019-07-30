def minion_game(string):
    String = string
    Vowels = ['A','E','I','O','U']
    vow = 0
    cons = 0
    length = len(String)
    a=0
    b=0
    dicCon = {}
    dicVowl = {}
# find out consonant and vowel string
    for i in range(len(String)):
        if String[i] in Vowels:
            a+=1
            vow = String[i:length] if vow == 0 else vow
        else:
            b+=1
            cons = String[i:length] if cons == 0 else cons
# for consonant
    FCElement=set()
    FVElement=set()
    for i in range(len(cons)):
        for j in range(i,len(cons)):
            test = cons[i:j+1]
            TLength=len(test)
            if test[0] not in Vowels:
                    for k in range(len(cons)):
                        if test in cons:
                            FCElement.add(test)

    for i in FCElement:
        x=len(i)
        for j in range(len(cons)):
            if i in cons[j:x]:
                if i in dicCon:
                    dicCon[i]+=1
                else:
                    dicCon[i]=1

            x+=1

# for vowel

    for i in range(len(vow)):
        for j in range(i,len(vow)):
            test = vow[i:j+1]
            TLength = len(test)
            if test[0] in Vowels:
                    for k in range(len(vow)):
                        if test in vow:
                            FVElement.add(test)

    for i in FVElement:
        x=len(i)
        for j in range(len(vow)):
            if i in vow[j:x]:
                if i in dicVowl:
                    dicVowl[i]+=1
                else:
                    dicVowl[i]=1
            x+=1

    STUART=0
    KEVIN=0
    for i in dicCon.values():
        STUART+=i
    for i in dicVowl.values():
        KEVIN+=i
    if STUART > KEVIN:
         print("Stuart",STUART)
    elif STUART == KEVIN:
        print("Draw")
    else:
        print("Kevin", KEVIN)

if __name__ == '__main__':
    s = input()
    minion_game(s)