#!/usr/bin/python3

def main():
    while True:
        try:
            print('Lets div x by y!')
            x = int(input('What is the value of x? '))
            y = int(input('What is the value of y? '))
            print('The value of x/y is:', x/y)
        except ZeroDivisionError:
            print('Cannot divide by 0... restarting')
        except ValueError:
            print('Seems that you are providing a non-numeric value. Please try again. This is math!')

main()

