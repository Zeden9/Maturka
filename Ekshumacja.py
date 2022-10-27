def splitDataType(table:list, character): #funkcja dzielaca tabele na 2 osobne elementy oddzielone spacja
    strings = []
    integers = []

    for n in range(0, len(table)):      #petla przechodzaca przez kazdy znak w linii
        x = table[n].splitlines()        #tworzenie tabeli przechowujacej jedna linie z tabeli
        y = x[0].split(character)   #tworzenie tabeli przechowujacej liczby i litery w osobnym indexie

        integers.append(y[0])     #dodawanie liczb do osobnej tablicy
        strings.append(y[1])      #dodawanie liczb do osobnej tablicy

    return integers, strings

def maxRepeatValue(table):       
    currentRepeat = 1
    maxRepeat = 1

    for n in range(0, len(table)):
        temp = table[n]             #tabela do przechowywania jednej linie z tabeli

        for i in range(0, (len(temp)-1)): #petla przechodzaca przez kazdy znak w linii
            if(temp[i] == temp[i+1]):     #porownywanie znaku z kolejnym
                currentRepeat += 1

                if(currentRepeat>maxRepeat): 
                    maxRepeat = currentRepeat
                    character = temp[i]
            else:
                currentRepeat = 1

    return maxRepeat, character

def isPrime(value):
    dividerCount = 1
    for n in range(2, value+1):
        if(value%n == 0):
            dividerCount+=1
    if(dividerCount==2):
        return True
    else:
        return False

def goldbach(value):
    maxDifference = 0
    difference = 0
    pierwsze = []
    for n in range(2, value):
        if(isPrime(n)):
            pierwsze.append(n)

    for n in range(0, len(pierwsze)):

        for i in range(0, len(pierwsze)):
            if(pierwsze[n]+pierwsze[i]==value):
                difference = abs(int(pierwsze[n]) - int(pierwsze[i]))

                if(difference > maxDifference or difference==0):
                    value1, value2, maxDifference = pierwsze[n], pierwsze[i], difference

    return value1, value2, maxDifference


myFile = open('pary.txt', 'r') #otwieranie pliku
pary = myFile.readlines()      #przypisanie danych do tablicy

liczby, litery = splitDataType(pary, " ")
print(litery, liczby)

maxPowtorzenia, znak = maxRepeatValue(pary)

print("Najczesciej pojawia sie znak {}, i powtarza sie {} razy.".format(znak, maxPowtorzenia))

for n in range(0, len(liczby)):
    if(int(liczby[n])%2==0):
        value1, value2, maxDifference = goldbach(int(liczby[n]))
        print(liczby[n], value1, value2)