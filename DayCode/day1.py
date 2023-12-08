def runPart1():
    inputFile = open('InputFiles/day1Input.txt', 'r')
    lines = inputFile.readlines()
    total = 0
    for line in lines:
        firstDigit = ""
        secondDigit = ""
        #from front
        for char in line:
            if char.isnumeric():
                firstDigit = char
                break
        #from back
        for char in reversed(line):
            if char.isnumeric():
                secondDigit = char
                break
        total = total + int(firstDigit + secondDigit)
    return(total)

def runPart2():
    inputFile = open('InputFiles/day1Input.txt', 'r')
    lines = inputFile.readlines()
    total = 0
    for line in lines:
        firstDigit = ""
        secondDigit = ""
        foundNum = ""
        index=0
        for char in line:
            #check numerals
            if char.isnumeric():
                foundNum = char
            #check words
            else:
                if index+3 <= len(line):
                    threeChar = line[index:index+3]
                    if threeChar == "one":
                        foundNum = "1"
                    if threeChar == "two":
                        foundNum = "2"
                    if threeChar == "six":
                        foundNum = "6"
                if index+4 <= len(line):
                    fourChar = line[index:index+4]
                    if fourChar == "four":
                        foundNum = "4"
                    if fourChar == "five":
                        foundNum = "5"
                    if fourChar == "nine":
                        foundNum = "9"
                if index+5 <= len(line):
                    fiveChar = line[index:index+5]
                    if fiveChar == "three":
                        foundNum = "3"
                    if fiveChar == "seven":
                        foundNum = "7"
                    if fiveChar == "eight":
                        foundNum = "8"
            #set digits with found number
            if firstDigit == "":
                firstDigit = foundNum
            secondDigit = foundNum
            index = index + 1
        numToAdd = int(firstDigit + secondDigit)
        total = total + numToAdd
        
    return total