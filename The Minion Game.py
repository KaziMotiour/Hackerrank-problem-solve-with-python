def minion_game(string):
    String = string
    Vowels = "AEIOU"
    length = len(String)
    STUART = 0
    KEVIN = 0
    dicCon = {}
    dicVowl = {}
# find out consonant and vowel string
    vowel = [String[i:length] for i in range(length) if String[i] in Vowels]
    conso = [String[i:length] for i in range(length) if String[i] not in Vowels]
    vow = vowel[0]
    cons = conso[0]
# for consonant

    FCElement=set()
    FVElement=set()
    for i in range(len(cons)):
        for j in range(i,len(cons)):
            test = cons[i:j+1]
            if test[0] not in Vowels:
                FCElement.add(test)
   # print(FCElement)
    for i in FCElement:
        x=len(i)
        #for j in range(len(cons)):
        if i in cons:
            if i in dicCon:
                dicCon[i]+=1
                STUART += 1
            else:
                dicCon[i]=1
                STUART += 1

            #x+=1

# for vowel

    for i in range(len(vow)):
        for j in range(i,len(vow)):
            test = vow[i:j+1]
            if test[0] in Vowels:
                FVElement.add(test)
    for i in FVElement:
        x=len(i)
        for j in range(len(vow)):
            if i in vow[j:x]:
                if i in dicVowl:
                    dicVowl[i]+=1
                    KEVIN+=1
                else:
                    dicVowl[i]=1
                    KEVIN += 1
            x+=1


    print("Keivns score")
    for i,j in sorted(dicVowl.items()):
        print(i," ",j)
    print("Total: ",KEVIN)
    print("\n\nStuart score")
    for i,j in sorted(dicCon.items()):
        print(i," ",j)
    print("Total: ",STUART,"\n")
    print("Wining score: " ,end=" ")
    if STUART > KEVIN:
         print("Stuart",STUART)
    elif STUART == KEVIN:
        print("Draw")
    else:
        print("Kevin", KEVIN)

if __name__ == '__main__':
    s = input()
    minion_game(s)