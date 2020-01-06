# Comma Code
def commaCode(aList):
    result = ''
    for word in aList:
        if word != aList[-1]:
            result += word + ', '
        else:
            result += 'and ' + word
    return result

# print(commaCode([]))
# print(commaCode(['apples', 'bananas', 'tofu', 'cats']))

# Coin Flip Streaks
import random

def generateValues(numberOfVals):
    result = []
    for i in range(numberOfVals):
        result.append(random.randint(0, 1))
    return result

def areThereAnyStreaks(aList):
    numInARow = 0
    for (index, item) in enumerate(aList):
        if index == len(aList) - 1:
            return 0
        if item == aList[index + 1]:
            numInARow += 1
        else:
            numInARow = 0
        if numInARow >= 6:
            return 1
    return 0

numberOfStreaks = 0
for experimentNumber in range(10000):
    tempList = generateValues(100)
    numberOfStreaks += areThereAnyStreaks(tempList)

print('Chance of streak: %s%%'%(numberOfStreaks / 100))

# Character Picture Grid
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], end='')
    print()