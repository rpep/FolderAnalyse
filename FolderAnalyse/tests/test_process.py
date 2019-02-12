#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:06:10 2019

@author: ryan
"""
from FolderAnalyse.process import top_frequencies, process_dir, process_file
from FolderAnalyse.fileparser import sort_dict
import os
import tempfile

docs_path = os.path.join(os.path.dirname(__file__), 'example_documents')


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
    
    
def test_process_file_case_insensitive():
    """
    test_process_file_case_insensitive()

    This test checks that a file is processed correctly.
    """

    stats, freqs, top_freqs = process_file('simple.txt', 
                                           N=2,
                                           case_sensitive=False)
    assert freqs['the'] == 4
    # Check postition of 'the' in the list.
    print(list(top_freqs.items()))
    assert list(top_freqs.items())[0][0] == 'the'
    assert list(top_freqs.items())[0][1] == 4


def test_process_file_case_sensitive():
    """
    test_process_file_case_sensitive()

    This test checks that a file is processed correctly when
    case sensitivity is used.
    """

    stats, freqs, top_freqs = process_file('simple.txt', 
                                           N=2,
                                           case_sensitive=True)

    assert freqs['the'] == 2
    assert freqs['The'] == 2




def test_process_dir_case_insensitive():
    """
    test_process_dir()

    This function tests that process_dir works correctly on the files in
    example_documents.

    We do this by checking incidences of 'the', 'The' and the combined total
    when the case sensitivity is selected.
    """
    
    _, dicts, top_dict, c_dict, top_c = process_dir(docs_path,
                                                    extension="txt",
                                                    N=10,
                                                    case_sensitive=False)
    
    
    assert top_c['the'] == 46597


def test_process_dir_case_sensitive():
    """
    test_process_dir()

    This function tests that process_dir works correctly on the files in
    example_documents.

    We do this by checking incidences of 'the', 'The' and the combined total
    when the case sensitivity is selected.
    """

    _, dicts, top_dict, c_dict, top_c = process_dir(docs_path,
                                                    extension="txt",
                                                    N=10,
                                                    case_sensitive=True)


    assert top_c['the'] == 43932
    assert top_c['and'] == 28104
    assert c_dict['The'] + c_dict['the'] + c_dict['THE'] == 46597
    
    
    