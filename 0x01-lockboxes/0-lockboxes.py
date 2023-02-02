#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
    """
    - boxes is a list of lists
    - A key with the same number as the box will open that box
    - assuming all keys to be positive integers
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
    """
    canUnlockAll = False
    keys = {0: True}
    n = len(boxes)
    while (True):

        n_keys = len(keys)

        for i in range(n):
            if boxes[i] and keys.get(i, False):
                for j in boxes[i]:
                    if j < n:
                        keys[j] = True
                    boxes[i] = None

        if not (len(keys) > n_keys):
            break

    if n_keys == len(boxes):
        canUnlockAll = True

    return canUnlockAll
