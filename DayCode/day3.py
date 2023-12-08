def runPart1():
    inputFile = open('InputFiles/day3Input.txt', 'r')
    lines = inputFile.readlines()
    newLines = []
    for line in lines:
        newLines.append(line.rstrip())
    lines = newLines
    lineIndex = 0
    maxLines = len(lines)
    total = 0;
    while lineIndex < maxLines:
        currLine = lines[lineIndex]
        #iterate through line to get numbers
        charIndex = 0
        buildingNum = ""
        currentNum = 0
        numStartIndex = 0
        while charIndex < len(currLine):
            if currLine[charIndex].isnumeric():
                buildingNum = buildingNum + currLine[charIndex]
            else :
                if buildingNum != "":
                    currentNum = int(buildingNum)
                    numStartIndex = charIndex - len(buildingNum)
                    buildingNum = ""
                    #check around to for symbols
                    if isSymbolTouching(numStartIndex, len(str(currentNum)), lineIndex, lines):
                        total = total + currentNum
            charIndex = charIndex + 1
        if buildingNum != "":
            currentNum = int(buildingNum)
            numStartIndex = charIndex - len(buildingNum)
            buildingNum = ""
            #check around to for symbols
            if isSymbolTouching(numStartIndex, len(str(currentNum)), lineIndex, lines):
                total = total + currentNum
        lineIndex = lineIndex + 1
    return total

def runPart2():
    inputFile = open('InputFiles/day3Input.txt', 'r')
    lines = inputFile.readlines()
    newLines = []
    gearMap = {}
    for line in lines:
        newLines.append(line.rstrip())
    lines = newLines
    lineIndex = 0
    maxLines = len(lines)
    total = 0;
    while lineIndex < maxLines:
        currLine = lines[lineIndex]
        #iterate through line to get numbers
        charIndex = 0
        buildingNum = ""
        currentNum = 0
        numStartIndex = 0
        while charIndex < len(currLine):
            if currLine[charIndex].isnumeric():
                buildingNum = buildingNum + currLine[charIndex]
            else :
                if buildingNum != "":
                    currentNum = int(buildingNum)
                    numStartIndex = charIndex - len(buildingNum)
                    buildingNum = ""
                    #check around to for stars and check/add to gear map
                    coord = isStarTouching(numStartIndex, len(str(currentNum)), lineIndex, lines)
                    if coord != "":
                        if coord in gearMap:
                            gearRatio = currentNum * gearMap[coord]
                            total = total + gearRatio
                        else:
                            gearMap.update({coord: currentNum})
            charIndex = charIndex + 1
        if buildingNum != "":
            currentNum = int(buildingNum)
            numStartIndex = charIndex - len(buildingNum)
            buildingNum = ""
            #check around to for symbols
            coord = isStarTouching(numStartIndex, len(str(currentNum)), lineIndex, lines)
            if coord != "":
                if coord in gearMap:
                    gearRatio = currentNum * gearMap[coord]
                    total = total + gearRatio
                else:
                    gearMap.update({coord: currentNum})
        lineIndex = lineIndex + 1
    return total

def isSymbolTouching(startIndex, length, lineIndex, lines):
    checkLeft = True
    checkRight = True
    leftBound = startIndex - 1
    if leftBound < 0 :
        leftBound = 0
        checkLeft = False
    rightBound = startIndex + length + 1
    if rightBound > len(lines[0]):
        rightBound = startIndex + length
        checkRight = False
    #check above
    if lineIndex > 0:
        symbols = lines[lineIndex-1][leftBound:rightBound].replace(".", "")
        symbols = symbols.replace("\d", "")
        if(symbols != ""):
            return True
    #check around
    if checkLeft:
        if lines[lineIndex][leftBound] != ".":
            return True
    if checkRight:
        if lines[lineIndex][rightBound-1] != ".":
            return True
    #check below
    if lineIndex < len(lines)-1:
        symbols = lines[lineIndex+1][leftBound:rightBound].replace(".", "")
        symbols = symbols.replace("\d", "")
        if(symbols != ""):
            return True
    return False

def isStarTouching(startIndex, length, lineIndex, lines):
    retval = ""
    checkLeft = True
    checkRight = True
    leftBound = startIndex - 1
    if leftBound < 0 :
        leftBound = 0
        checkLeft = False
    rightBound = startIndex + length + 1
    if rightBound > len(lines[0]):
        rightBound = startIndex + length
        checkRight = False
    #check above
    if lineIndex > 0:
        symbols = lines[lineIndex-1][leftBound:rightBound]
        if "*" in symbols:
            starIndex = symbols.index("*")
            nudge = 0
            if(checkLeft):
                nudge = 1
            retval = str(lineIndex-1) + "," + str(startIndex+starIndex-nudge)
    #check around
    if checkLeft:
        if lines[lineIndex][leftBound] == "*":
            retval = str(lineIndex) + "," + str(startIndex-1)
    if checkRight:
        if lines[lineIndex][rightBound-1] == "*":
            retval = str(lineIndex) + "," + str(startIndex+length)
    #check below
    if lineIndex < len(lines)-1:
        symbols = lines[lineIndex+1][leftBound:rightBound]
        if "*" in symbols:
            starIndex = symbols.index("*")
            nudge = 0
            if checkLeft:
                nudge = 1
            retval = str(lineIndex+1) + "," + str(startIndex+starIndex-nudge)
    return retval