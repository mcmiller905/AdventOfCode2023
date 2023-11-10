# AdventOfCode2023
![](https://img.shields.io/badge/stars%20⭐-0-yellow)

mcmiller905's repository for Advent of Code 2023 work. I'm still using Python, I've found this ito be a fun way to practice with it. I have a *main.py* file that serves as the main starting point for each day of code. Each day's code is stored in a DayCode directory, and the same is true for the input files in InputFiles.

If you want to run it, there are 3 variables at the top of *main.py* that control what day and part get run. Set "day" to the number of the day you want to run (or 0 to run all in succession) and set "runPart1" and "runPart2" to True if you want to run their respective parts.

You can also use command line args to control what day and part are run:

    python3 main.py [dayNum] [runPart2]
 - [dayNum]: (String) the number of the day you want to run, with '0' meaning run all in succession
 - [runPart2]: (Boolean) if 'True', or 'true', the code will run both Part 1 and Part 2. If 'False', or 'false', the code will only run Part 1
 
 If either of these are blank, the code will default to the values specified in *main.py*