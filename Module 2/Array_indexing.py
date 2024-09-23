
"""Array indexing
"""

import numpy as np

def main():
    """Driven Function
    """

    arr_1d = np.arange(10)
    # Access the second element.  Index notation
    print(arr_1d[1])
    # Last element
    print(arr_1d[-1])
    # Access 2D array elements
    arr_2D = np.array([[21, 22, 23, 24],
              [31, 32, 33, 24],
              [41, 42, 43, 44]])
    print(f'The 0,0 element {arr_2D[0, 0]}')
    print(f'The 2,-2 element {arr_2D[2, -2]}')
    print(f'The first full row {arr_2D[0]}')
    
    # Slicing
    arr_1d = np.arange(10)
    print(f'All elements {arr_1d}')
    print(f'Slicing elements {arr_1d[1:4]}')
    print(f'Slicing elements {arr_1d[1:4:2]}')


    print('Main Function')

if __name__ == '__main__':
    main()