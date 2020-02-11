def collatz(number):
    if number % 2 == 0:
        return number // 2

    elif number % 2 == 1:
        return 3 * number + 1


while True:
    try:
        n = int(input('Please Enter a Number:'))
        value = collatz(n)
        print(value)
        break
    except ValueError:
        print('You must enter an integer')
