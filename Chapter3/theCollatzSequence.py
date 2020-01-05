def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    if result == 1:
        comma = '\n'
    else:
        comma = ', '
    print(result, end = comma)
    return result

while True:
    print('Enter number:')
    try:
        currentNumber = int(input())
        if currentNumber > 1:
            break
        else:
            int('puppy') # raise ValueError
    except ValueError:
        print('Please enter a positive integer greater than 1.')
while currentNumber != 1:
    currentNumber = collatz(currentNumber)