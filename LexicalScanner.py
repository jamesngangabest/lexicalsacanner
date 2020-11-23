#Joshua C. Peckham
#Feb 8 2017

import sys
def isFloat(string): #this is a defined function to test if the variable is a floating variable  #defining isFloat() to verify it is a floating number
    try:
        float(string)
        return True  #this is a logical boolien to see if the string is a floating pint
    except ValueError:
        return False
dict = {'keyword': 'begin, end, if, else, then'  , 'character':{}} #diction stores a keywords to be printed at the bottem as an explanation of the diction aspect with character to be appended
file = open(sys.argv[1], "r") #open file that is passed by program then name in terminal "r" just read
lines = file.readlines() #Lines reads file line by line
keyword_lib = ['begin','end','if','else','then'] #keyword library to check against the words parced together
character_lib = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] #This is a library that stores all of the key character values, so when the program runs it'll varify if any of these are utilized and then record the amount inside of an array and how many of these keys have been generated.

# library for character tokens
Special_lib = ['(',')','[',']','+','-','=',',',';']
begin_ = end_ = if_ = else_ = then_ = lbrace = rbrace = lbracket = rbracket = plus = minus = equal = comma = semicolon = zero = one = two = three = four = five = six = seven = eight = nine = 0;
character = [] #stores all characters in file
digit = [] #stores all digits in file
symbols = [] #stores all symbols in file
keywords = [] #stores all keywords in file
real = [] #stores all real in file
characterIdentifier = [] #stores all characters identifiers in file
identifiers = 0 # this is an auto defined integer '''#keeps track of amount of identifiers in file
for line in lines:  #this is a for loop that takes in a line of the imported page and parses through each character to properly store them in there designated location within one of the arrays above  # Loop to go through all lines
    for x in range(0,len(line.split())): # x represents first peice
        var = line.split() #stores the word
        if var[x].isdigit():  # this splices the sting characted at an x location to verify if it is a digit ''' # checks the first num/char/sym to see if it is a digit
            digit.append(var[x])#if it is a digit it adds the variable inot the digit array ''' #if it is a digit stores the variable in digit array
        elif isFloat(var[x]): # if it is a floating number stored in real array
            real.append(var[x])
        elif var[x].isalpha(): # checks to see if it is a character
            flag = 1 # sets flag as true to for testing perameters
            for y in range(0,len(character_lib)): # runs throught the library to compare library with the word from the file
                word = character_lib[y]
                if var[x] == word:
                    character.append(var[x])
                    flag = 0
            for z in range(0,len(keyword_lib)): # runs throught the library to compare library with the word from the file
                word = keyword_lib[z]
                if var[x] == word:
                    if var[x] == 'begin':
                        begin_ += 1
                    if var[x] == 'end':
                        end_ += 1
                    if var[x] == 'if':
                        if_ += 1
                    if var[x] == 'else':
                        else_ += 1
                    if var[x] == 'then':
                        then_ += 1
                    keywords.append(var[x])
                    flag = 0
            if flag == 1:
                characterIdentifier.append(var[x])
                identifiers += 1
        else:
            for z in range(0,len(Special_lib)):
                word = Special_lib[z]
                if var[x] == word:
                    if var[x] == '(':
                        lbrace += 1
                    if var[x] == ')':
                        rbrace += 1
                    if var[x] == '[':
                        lbracket += 1
                    if var[x] == ']':
                        rbracket += 1
                    if var[x] == '+':
                        plus += 1
                    if var[x] == '-':
                        minus += 1
                    if var[x] == '=':
                        equal += 1
                    if var[x] == ',':
                        comma += 1
                    if var[x] == ';':
                        semicolon += 1
                    if var[x] == 'then':
                        then_ += 1
                    symbols.append(var[x])

print "Keywords: ", "|", len(keywords)
print "begin: ", begin_
print "end: ", end_
print "if: ", if_
print "else: ", else_
print "then: ", then_
print "Identifier: ", identifiers
print "Character: ", character, "|", len(character)
print "Real: ", real, "|", len(real)
print "Special: ", len(symbols)
print "(:", lbrace
print "):", rbrace
print "[:", lbracket
print "]", rbracket
print "+", plus
print "-", minus
print "=", equal
print ",", comma
print ";:",semicolon
print "digit: ", len(digit)
print "character Identifier: ", len(characterIdentifier)
print dict["keyword"]; # prints dictionary
dict["character"] = "a" #appends character to equal a value
print dict["character"]
h = 'Hello' #string used to splice through
def hello(): #for switch case
    print  h
def world(): #for swith case
    print "world"
options = { #switch case used to test out the switch case functionality
    1 : hello,
    2 : world
}
options[1](); #execute switch case to have it utilize the defintion functions
length = 0
while length != len(keyword_lib): #prints all words in the keyword lib
    print keyword_lib[length]
    length += 1

print h[:3], h[3:] #utilizes the splice aspect
tup = ('you', 'are', 'here' ) #tuples example of tuples
print tup[:2],     tup[2:] #print tuples w/splice
