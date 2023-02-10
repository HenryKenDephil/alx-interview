#!/usr/bin/python3
'''
    minimum operations in an array
'''


def minOperations(n):
    '''
        a function to calculate the minimu number of operations
        to result in exactly n H characters in the given file

        Args:
            n: number of operations
            fewer_operations: number of minimum operations
            possible_operations: number of achievable operations
        Returns: return the minimu number of operations
                : returns 0 if n is impossible
    '''

    if n < 2 or type(n) is not int:
        return 0
    count = 1
    arr = list()
    operations = n
    while operations != 1:
        count += 1
        if operations % count == 0:
            while operations % count == 0 and operations != 1:
                operations /= count #operations = operations/count
                arr.append(count)

    return sum(arr)

#minOperations(4)




