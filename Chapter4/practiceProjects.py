## Comma Code
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

## Coin Flip Streaks
import random

# This function could be replaced by the list comprehension:
# [ random.randint(0, 1) for i in range(0, 100) ]
def generateValues(numberOfVals):
    result = []
    for i in range(numberOfVals):
        result.append(random.randint(0, 1))
    return result

# Returns 0 if there are no streaks of 6 or more
#     and 1 if there are
def areThereAnyStreaks(aList):
    numInARow = 0
    for (index, item) in enumerate(aList):
        # If we've made it to the last item in the list,
        #    Then we can't look at the next item (doesn't exist)
        if index == len(aList) - 1:
            if numInARow == 5 and item == aList[index - 1]:
                numInARow += 1
            else:
                return 0
        else:
            if item == aList[index + 1]:
                numInARow += 1
            else:
                numInARow = 0
        if numInARow >= 6:
            return 1

numberOfStreaks = 0
for experimentNumber in range(10000):
    tempList = generateValues(100)
    numberOfStreaks += areThereAnyStreaks(tempList)

print('Chance of streak: %s%%'%(numberOfStreaks / 100))

## Character Picture Grid
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