
"""Do Array Operations
"""

import numpy as np

def main():
    """Driven Function
    """

    numbers_lst = [2, 4, 6, 8, 10]
    print(f'Before list {numbers_lst}')
    #increment each element by 3
    for item in range(len(numbers_lst)):
        numbers_lst[item] = numbers_lst[item] + 3
    print(f'After list {numbers_lst}')
    # Convert list to numpy array
    numbers_arr = np.array(numbers_lst)
    print(f'Before Array {numbers_arr}')
    # Add 3 to each element
    numbers_arr += 3
    print(f'After Array {numbers_arr}')

if __name__ == '__main__':
    main()