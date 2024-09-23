
"""Library to calculate the number of digits for different algorithms
"""

from math import factorial

def factorial_length(number):
    """_summary_

    Args:
        number (_type_): integer value to calculate factorial

    Returns:
        _type_: number of digits for factorial of output
    """
    length = factorial(number)
    length = str(length) # convert to str
    return len(length) # return number of elements 
    # return len(str(factorial(number))) # return number of elements in one line

def main():
    """Driven Function
    """

    number = 5
    digits = factorial_length(5)
    print(f'you have {digits} digits in factorial({number})')

if __name__ == '__main__':
    main()