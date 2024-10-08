
"""Iterator Protocols
"""
import numpy as np

def main():
    """Driven Function
    """
    iterable = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    # Create an iterator
    iterator = iter(iterable)
    # Get the first element
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

    # TODO: Add a function with a try: catch: to test the iterator

    # TODO: Then, Use a generator



    print('Main Function')

if __name__ == '__main__':
    main()