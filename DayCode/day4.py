def runPart1():
    inputFile = open('InputFiles/day4Input.txt', 'r')
    lines = inputFile.readlines()
    newLines = []
    for line in lines:
        newLines.append(line.rstrip())
    lines = newLines
    #Card   1: 13  4 61 82 80 41 31 53 50  2 | 38 89 26 79 94 50  2 74 31 92 80 41 13 97 61 82 68 45 64 39  4 53 90 84 54
    total = 0
    for line in lines:
        points = 0
        hits = 0
        cardTextSplit = line.split(": ")[1].split(" | ") #[winningNums, cardNums]
        winningNums = cardTextSplit[0].split(" ")
        ourNums = cardTextSplit[1].split(" ")
        for num in ourNums:
            if num != "":
                if num in winningNums:
                    hits = hits + 1
        for x in range(hits):
            if points == 0:
                points = 1
            else:
                points = points * 2
        total = total + points
    return total

def runPart2():
    inputFile = open('InputFiles/day4Input.txt', 'r')
    lines = inputFile.readlines()
    newLines = []
    for line in lines:
        newLines.append(line.rstrip())
    lines = newLines
    #Card   1: 13  4 61 82 80 41 31 53 50  2 | 38 89 26 79 94 50  2 74 31 92 80 41 13 97 61 82 68 45 64 39  4 53 90 84 54
    lineIndex = 0
    cardArray = [1] * len(lines)
    for line in lines:
        alreadyFoundHits = False
        hits = 0
        iter = cardArray[lineIndex]
        for card in range(iter):
            if not alreadyFoundHits:
                hits = 0
                cardTextSplit = line.split(": ")[1].split(" | ") #[winningNums, cardNums]
                winningNums = cardTextSplit[0].split(" ")
                ourNums = cardTextSplit[1].split(" ")
                for num in ourNums:
                    if num != "":
                        if num in winningNums:
                            hits = hits + 1
                alreadyFoundHits = True
            for x in range(hits):
                lineToAdd = x+lineIndex+1
                cardArray[lineToAdd] = cardArray[lineToAdd] + 1
        lineIndex = lineIndex + 1
    return sum(cardArray)