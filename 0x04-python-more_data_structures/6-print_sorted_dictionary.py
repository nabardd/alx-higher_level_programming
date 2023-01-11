#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    dict_keys = sorted(a_dictionary.keys())

    for i in dict_keys:
        print(f"{i}: {a_dictionary[i]}")
