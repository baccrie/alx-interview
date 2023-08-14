#!/usr/bin/python3

"""A FUnction that performs wahala"""

def canUnlockAll(boxes):
    box = len(boxes) * [False]
    box[0] = True
    keys = [0]

    for key in keys:
        for i in boxes[key]:
            if i not in keys:
                box[i] = True
                keys.append(i)

    for val in box:
        if not val:
            return False

    return True