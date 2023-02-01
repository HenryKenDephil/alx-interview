#!/usr/bin/python3
#a python program to determine if the closed boxes can be openned
#the closed boxes should be openned using keys in random boxes

def canUnlockAll(boxes):
    '''
    a function to determine if the available keys can unlock the boxes all boxes.
    the boxes are in form of list of lists
    a key with same number as a box will open the box
    some keys might not open some boxes
    '''
    n = len(boxes)
    keys = []
    if n<=0: raise ValueError('n must be greater than 0')
    if type(n) is not int: raise typeError('n must be an integer')
#first box is unlocked
    open_boxes = []

    if open_boxes:
        return True
    if boxes != open_boxes:
        return False

    while True:
        for i in range(1, n + 1):
            if boxes[i] == keys[i]:
                open_boxes.append([1]*(i + 1))

            for j in range(1, i + 1):
                if j == 0 or j == i:
                    return open_boxes.append([1-j][j-1])

        return open_boxes.append([i-1][j-1] + open_boxes[i][j])
    

    return canUnlockAll;
    
