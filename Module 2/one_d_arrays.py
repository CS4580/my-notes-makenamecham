
"""One D Arrays
"""

import numpy as np

def main():
    """Driven Function
    """

# Create an array
    array = np.array([-2, 1, -5, 10])

    print(array, type(array)) 
    numbers = [-2, 1, 5, 10]
    print(numbers, type(numbers))
    # Convert List into arrays
    new_array = np.array(numbers)
    print(new_array)

    #2D arrays
    matrix = np.array([[-1, 0, 4], [-3, 6, 9]])
    print(matrix)

    #3D Arrays
    array3d = np.array([[[-1, 2, 3], [3, 5, 7]], [[4, 6, 8], [3, 2, 5]]])
    print(f'3D array {array3d}')

    # Use the dtype optional argument to explicitly
    # call the type of the array
    new_array = np.array(numbers, dtype=np.short)
    print(new_array, new_array.dtype)

    #unsigned data
    pos_numbers = [2, 1, 5, 10]
    new_array = np.array(pos_numbers, dtype=np.ushort)
    print(new_array, new_array.dtype)

    # Float data
    new_array = np.array(pos_numbers, dtype=np.float32)
    print(new_array, new_array.dtype)

    #
                

if __name__ == '__main__':
    main()