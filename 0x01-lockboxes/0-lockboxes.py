#!/usr/bin/python3
""" Method for opening boxes"""


def unlock(boxes, indexes, keySet):
    """
    Recursive function for opening boxes

    Args:
        boxes(list): a list of boxes
        indexes(list): a list of indexes to check
        keySet(set): a set of keys that can open the boxes

    Return:
        True if the boxes can be opened, otherwise false
    """
    indexLength = len(indexes)
    if indexLength == 0:
        return True

    for i in indexes:
        if i in keySet:
            keySet.update(boxes[i])
            indexes.remove(i)
    if len(indexes) == indexLength and len(indexes) != 0:
        return False
    return unlock(boxes, indexes, keySet)


def canUnlockAll(boxes):
    """
    Unlocks a list of boxes that contain keys to other boxes

    Args:
        boxes(list): list of boxes to be opened

    Return:
        True if all the boxes can be opened, otherwise False
    """
    indexes = list(range(len(boxes)))
    keySet = {0}

    return unlock(boxes, indexes, keySet)
