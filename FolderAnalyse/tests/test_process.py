#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:06:10 2019

@author: ryan
"""
from FolderAnalyse.process import top_frequencies
from FolderAnalyse.fileparser import sort_dict


def test_top_frequencies_list_exceeds_dict():
    """
    test_top_frequencies_list_exceeds_dict()
    
    This test generates some junk data, and checks that 
    the top_frequencies function works as expected, 
    by testing against manually constructed data.
    
    A dictionary is created with the alphabet, 
    with values running backwards from 25 to 0
    assigned to a-z. top_frequencies is called with
    the argument 10 and then each key value pair
    is checked against the known answer.
    """
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


def test_top_frequencies_less():
    """
    test_top_frequencies_list_exceeds_dict()
    
    This test generates some junk data, and checks that 
    the top_frequencies function works as expected, 
    by testing against manually constructed data.
    
    In this test, we check that if a dictionary is
    smaller than the size of top frequencies requested,
    we just get the same dictionary back.
    """
    keys = "abcdefghijklmnopqrstuvwxyz"
    N = len(keys)

    freq_dict = {}

    for i in range(N-1, -1, -1):
        freq_dict[keys[N - i - 1]] = i

    freq_dict = sort_dict(freq_dict)

    top_freqs = top_frequencies(freq_dict, nterms=27)

    assert top_freqs == freq_dict, "The two dictionaries are not the same!"