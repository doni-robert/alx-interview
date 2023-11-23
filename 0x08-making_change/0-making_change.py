#!/usr/bin/python3
""" makeChange module """


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given
    amount 'total'

    Args:
        coins(int): a list of coin values
    Return:
        the fewest number of coins needed
    """
    mergeSort(coins, 0, len(coins) - 1)
    count = 0

    return recurs_make_change(coins, total, count)


def recurs_make_change(coins, total, count):
    """
    Recursively determines the fewest number of coins needed to meet a given
    amount 'total
    """
    coin = binary_search(coins, 0, len(coins) - 1, total)
    if coin > 0:
        count += total // coin
        rem = total % coin

        if rem == 0:
            return count
        else:
            return recurs_make_change(coins, rem, count)
    return -1


# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    """
    Searches for the maximum lesser value of a number x from the
    array 'arr'

    Args:
        arr(int): the array to search in
        low(int): the lower index from where to search
        high(int): the higher index from where to search
        x(int): the number to search

    Return:
        The maximum lesser value of x
    """
    # Check base case
    if high >= low:

        if high - low == 1 or high - low == 0:
            if arr[low] < x and arr[high] < x:
                return arr[high]
            elif arr[low] < x and arr[high] > x:
                return arr[low]
            elif arr[low] > x and arr[high] > x:
                if low != 0:
                    return arr[low - 1]
                else:
                    return -1

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return arr[mid]

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


def merge(arr, low, mid, high):
    """
    Merges two subarrays of arr[].
    First subarray is arr[low..mid]
    Second subarray is arr[mid+1..high]
    """
    n1 = mid - low + 1
    n2 = high - mid

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[low + i]

    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]

    # Merge the temp arrays back into arr[l..high]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = low     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    # l is for left index and r is right index of the
    # sub-array of arr to be sorted


def mergeSort(arr, low, high):
    """
    Mergesorts the array 'arr'

    Args:
        low(int): the left most index
        high(int): the right most index
    """
    if low < high:

        # Same as (low+high)//2, but avoids overflow for
        # large low and h
        mid = low+(high-low)//2

        # Sort first and second halves
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)
        merge(arr, low, mid, high)
