def runPart1():
    inputFile = open('InputFiles/day2Input.txt', 'r')
    lines = inputFile.readlines()
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    total = 0
    for line in lines:
        # Game 1: 7 blue, 4 red, 11 green; 2 red, 2 blue, 7 green; 2 red, 13 blue, 8 green; 18 blue, 7 green, 5 red
        line = line.strip()
        #get id
        idSplit = line.split(": ")
        #print(idSplit)
        id = idSplit[0].split(" ")[1]
        possibleFlag = True
        #loop through each pull
        pulls = idSplit[1].split("; ")
        for pull in pulls:
            typeSplit = pull.split(", ")
            for type in typeSplit:
                num = int(type.split(" ")[0])
                color = type.split(" ")[1]
                if color == "red" and num > maxRed:
                    possibleFlag = False
                if color == "green" and num > maxGreen:
                    possibleFlag = False
                if color == "blue" and num > maxBlue:
                    possibleFlag = False
        if possibleFlag:
            total = total + int(id)
    return total

def runPart2():
    inputFile = open('InputFiles/day2Input.txt', 'r')
    lines = inputFile.readlines()
    total = 0
    for line in lines:
        # Game 1: 7 blue, 4 red, 11 green; 2 red, 2 blue, 7 green; 2 red, 13 blue, 8 green; 18 blue, 7 green, 5 red
        line = line.strip()
        topRed = 0
        topGreen = 0
        topBlue = 0
        #get id
        idSplit = line.split(": ")
        #print(idSplit)
        id = idSplit[0].split(" ")[1]
        #loop through each pull
        pulls = idSplit[1].split("; ")
        for pull in pulls:
            typeSplit = pull.split(", ")
            for type in typeSplit:
                num = int(type.split(" ")[0])
                color = type.split(" ")[1]
                if color == "red" and num > topRed:
                    topRed = num
                if color == "green" and num > topGreen:
                    topGreen = num
                if color == "blue" and num > topBlue:
                    topBlue = num
        power = topRed * topGreen * topBlue
        total = total + power
    return total