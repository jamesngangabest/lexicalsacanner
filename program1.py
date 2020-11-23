import sys

def isFloat(string): #defining isFloat() to verify it is a floating number
    try:
        float(string)
        return True
    except ValueError:
        return False

file = open(sys.argv[1], "r") #open file that is passed by program then name in terminal "r" just read
lines = file.readlines() #Lines reads file line by line
keyword_lib = ['begin','end','if','else','then'] #keyword library to check against the words parced together
character_lib = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] character = [] '''this is the definition of an array, so that later on I will be able to store values inside of this character array'''
digit = [] #stores all digits in file
symbols = [] #stores all symbols in file
keywords = [] #stores all keywords in file
real = [] #stores all real in file
characterIdentifier = [] #stores all characters identifiers in file
identifiers = 0 #keeps track of amount of identifiers in file
for line in lines:# Loop to go through all lines
    for x in range(0,len(line.split())): # x represents first peice
        var = line.split() ''' this stores the word from the imported page into a variable '''#stores the word
        if var[x].isdigit():# checks the first num/char/sym to see if it is a digit
            digit.append(var[x]) ''' if it is a digit it adds the variable inot the digit array '''#if it is a digit stores the variable in digit array
        elif isFloat(var[x]): # if it is a floating number stored in real array
            real.append(var[x])
        elif var[x].isalpha(): # checks to see if it is a character
            flag = 1 # sets flag as true to for testing perameters
            for y in range(0,len(character_lib)): # runs throught the library to compare library with the word from the file
                word = character_lib[y]
                if var[x] == word:
                    character.append(var[x])
                    identifiers += 1
                    flag = 0
            for z in range(0,len(keyword_lib)): # runs throught the library to compare library with the word from the file
                word = keyword_lib[z]
                if var[x] == word:
                    keywords.append(var[x])
                    flag = 0
            if flag == 1:
                characterIdentifier.append(var[x])
                identifiers += 1
        else:
            symbols.append(var[x])
print "Keywords: ", keywords, "|", len(keywords)
print "Identifier: ", identifiers
print "Character: ", character, "|", len(character)
print "Real: ", real, "|", len(real)
print "Special: ", symbols, "|", len(symbols)
print "digit: ", digit, "|", len(digit)
print "character Identifier: ", characterIdentifier, "|", len(characterIdentifier)



