#!/usr/bin/env python3
""" ValidateUtf8 module """


def validUTF8(data):
    """
    Determines of a data set represents vlid UTF-8 encoding

    Args:
        data(set): a set of integers
    Return:
        True if the data is valid, else False
    """
    for i in data:
        if i > 127:
            return False
    return True
