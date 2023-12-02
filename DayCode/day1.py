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
            if index+3 <= len(line):
                if line[index:index+3] == "one":
                    foundNum = "1"
                if line[index:index+3] == "two":
                    foundNum = "2"
                if line[index:index+3] == "six":
                    foundNum = "6"
            if index+4 <= len(line):
                if line[index:index+4] == "four":
                    foundNum = "4"
                if line[index:index+4] == "five":
                    foundNum = "5"
                if line[index:index+4] == "nine":
                    foundNum = "9"
            if index+5 <= len(line):
                if line[index:index+5] == "three":
                    foundNum = "3"
                if line[index:index+5] == "seven":
                    foundNum = "7"
                if line[index:index+5] == "eight":
                    foundNum = "8"
            #set digits with found number
            if firstDigit == "":
                firstDigit = foundNum
            secondDigit = foundNum
            index = index + 1
        numToAdd = int(firstDigit + secondDigit)
        total = total + numToAdd
        
    return total