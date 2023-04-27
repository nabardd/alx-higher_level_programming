#!/usr/bin/python3

"""---Find Peak---"""

def find_peak(list_of_integers):
    """Find the peak from a list of unsirted numbers"""
    
    if list_of_integers == []:
        return None
    
    length = len(list_of_integers)
    if length == 1:
        return max(list_of_integers)
    elif length == 2:
        return max(list_of_integers)

    mid = int(length / 2)
    peak = list_of_integers[mid]

    if peak > list_of_integers[mid - 1] & peak > list_of_integers[mid - 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
