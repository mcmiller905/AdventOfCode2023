# Main runner of all the Advent of Code 2021 code. Change the 'day' variable to
# run the different day's code, or set to 0 to run all
from importlib import import_module
import time, sys, os

############################
# DEFAULT CONTROL PANEL    #
day = 0                    #
runPart1 = True            #
runPart2 = False           #
#                          #
############################

def runDay(dayNum):
    print()
    print("*--------------------")
    print("*  DAY " + str(dayNum))
    print("*--------------------")
    print()
    module = import_module('DayCode.day'+str(dayNum))
    if(runPart1):
        part1 = getattr(module, 'runPart1')
        startTime = time.perf_counter()
        answer = part1()
        endTime = time.perf_counter()
        print(f"Part 1: - {1000 * (endTime - startTime):0.2f}ms")
        print(str(answer))
    if(runPart2):
        part2 = getattr(module, 'runPart2')
        startTime = time.perf_counter()
        answer = part2()
        endTime = time.perf_counter()
        print(f"Part 2: - {1000 * (endTime - startTime):0.2f}ms")
        print(str(answer))

def printHelp():
    print()
    print("Welcome to my Advent of Code 2022 program!")
    print("To control what gets executed, there are variables at the top of the main.py")
    print("or you could use the following command line args:")
    print(" - first arg is the number of the day to run (0 to run all)")
    print(" - second arg is whether or not you want to run part 2")
    print(" - - false runs only part 1")
    print(" - - true runs both part 1 and part 2")
    print()

run = True
if(len(sys.argv) > 1):
    if(sys.argv[1] == "--help" or sys.argv[1] == "-h"):
        printHelp()
        run = False
    else:
        try:
            day = int(sys.argv[1])
        except ValueError:
            print("'" + sys.argv[1] + "' not acceptable. dayNum arg must be a number")
            run = False
if(len(sys.argv) > 2):
    if(sys.argv[2].lower() == "true"):
        runPart2 = True
    elif(sys.argv[2].lower() == "false"):
        runPart2 = False
if(run):
    if(day == 0):
        numFiles = len(next(os.walk("DayCode"))[2]) + 1
        i = 1
        totalStartTime = time.perf_counter()
        while(i < numFiles):
            runDay(i)
            i+=1
        totalEndTime = time.perf_counter()
        runTime = 1000 * (totalEndTime - totalStartTime)
        runTimeText = f"{runTime:0.2f}ms"
        if(runTime > 1000):
            runTimeText = f"{(runTime/1000):0.2f}s"
        print()
        print(f"Total time: - " + runTimeText)
    else:
        runDay(day)
print()