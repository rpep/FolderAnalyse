#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:06:10 2019

@author: ryan
"""
from FolderAnalyse.process import top_frequencies
from FolderAnalyse.fileparser import sort_dict


def test_top_frequencies_list_exceeds_dict():
    # Generate some junk data which is sorted
    # such that the lowest letters in the alphabet
    # have the largest values, descending.
    # This function tests the sorting and 
    # top frequency routines.
    keys = "abcdefghijklmnopqrstuvwxyz"
    N = len(keys)

    freq_dict = {}

    for i in range(N-1, -1, -1):
        freq_dict[keys[N - i - 1]] = i

    freq_dict = sort_dict(freq_dict)


    top_freqs = top_frequencies(freq_dict, nterms=10)

    solution = {'a': 25, 'b': 24, 'c': 23, 'd': 22, 'e': 21,
                'f': 20, 'g': 19, 'h': 18, 'i':17 , 'j': 16}

    for key, value in top_freqs.items():
        assert solution[key] == value, "Something has gone wrong with sorting."
