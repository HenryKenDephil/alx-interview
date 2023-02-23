#!/usr/bin/python3

''' UTF-8 Validation '''

from typing import List


def validUTF8(data: List[int]) -> bool:
    '''
    a method that determines if a given data
    set represents a valid UTF-8 encoding
    
    Args:
        data: a list of of integers

    Returns:
        return True if data is a valid UTF-8 encoding
        else return False
    '''
        
    def check(num):
        '''
        a method that checks if the data/integer  is in byte form
        the integer must represent 1 byte of data
        '''
        mask = 1 << 7 #shifting integer to byte form (n-1 or 8-1)
        i = 0   #  counter
        
        while num & mask:
            mask >>= 1 # shifting mask by 1 to the right
            i += 1  # increment counter by  1 
        return i
    
    
    i = 0
    while i < len(data):
        j = check(data[i]) 
        k = i + j - (j!=0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        
        while i < len(data) and  i <= k:
            cur = check(data[i])
            if cur != 1:
                return False
            i += 1
            
    return True