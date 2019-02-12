"""
Ryan Pepper (2018)

fileparser.py

This file contains a parser function that processes a text file.

"""


def parse(filename, exclusions=[], case_sensitive=False, sort=False):
    """
    parse(filename)

    Opens a file, and reads it line by line, returning a dictionary
    containing key-value pairs of words and their frequency in the file.
    Note: newline characters are *always* removed from the file!

    >>> text = "The quick brown fox jumped over the lazy dog."
    >>> f = open('example.txt', 'w')
    >>> f.write(text)
    >>> f.close()
    >>> parse('example.txt', case_sensitive=True)
    {}

    """
    try:
        f = open(filename, 'r')
    except:
        raise FileNotFoundError(
            "Could not open file - are you sure it exists?"
            )

    # Here we make the assumption that the files are independently
    # small enough to fit in memory. This may not be the case, but can be
    # handled. We replace the characters in the exclusions list
    # with a space, in order to separate words out. This is mainly designed
    # for punctuation, but it is not turned on by default.
    text = f.read()
    exclusions = ['\n'] + exclusions
    for exclusion in exclusions:
        text = text.replace(exclusion, ' ')

    # If case_sensitive is true we make the text all lower case.
    if case_sensitive:
        text = text.lower()

    frequency_dict = {}

    for word in text.split(' '):
        # O(N) lookup over the keys, where N is the number of keys. Even though
        # we are checking the existence of the key in the dictionary, this
        # should be faster than finding the set(text.split(' ')) of the words
        # and then calling text.count(word), because the cost of doing that is
        # M * O(N) look-ups over the text, where M is the number of unique
        # words and N is the number of words in the file.
        if word in frequency_dict.keys():
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    if sort:
        # Sort the dictionary by the values. Dictionarys are ordered in Python
        # 3.6 and above but that is not the case for old versions where you
        # must use collections.OrderedDict.
        sort_dict(frequency_dict)

    else:
        return frequency_dict


def sort_dict(frequency_dict, reverse=True):
    """
    sort_dict(dictionary)

    Sorts a dictionary based on the numerical values stored in the dict.

    >>> a = {'a': 2, 'b': 1, 'c': 5}
    >>> sort_dict(a, reverse=True)
    {'c': 5, 'a': 2, 'b': 1}
    >>> sort_dict(a, reverse=False)
    {'b': 1, 'a': 2, 'c': 5}

    Note:
    ----
    Dictionarys are ordered in Python 3.6 and above but that is not the
    case for old versions where you must use collections.OrderedDict.
    """
    sorted_dict_keys = sorted(frequency_dict, key=frequency_dict.get,
                              reverse=reverse)
    sorted_dict = {key: frequency_dict[key] for key in sorted_dict_keys}
    return sorted_dict


def combine_dicts(dicts_list):
    """
    combine_dicts(dicts_list)

    Combines dictionaries by summing the numerical values of any keys
    which are shared between them.

    Example
    -------

    >>> a = {'a': 2, 'b': 1, 'c': 5}
    >>> b = {'b': 4, 'c': 12, 'e': 4}
    >>> combine_dicts([a, b])
    {'a': 2, 'b': 5, 'c': 17, 'e': 4}
    """

    all_keys = []
    for freq_dict in dicts_list:
        all_keys += list(freq_dict.keys())

    keys = set(all_keys)

    combined_dict = {key: 0 for key in keys}

    # Iterate over the list of keys so that
    # the memory access pattern to the combined_dict
    # avoids jumping around.
    for key in keys:
        for fdict in dicts_list:
            try:
                combined_dict[key] += fdict[key]
            except:
                pass
        print(key, combined_dict[key])
    return combined_dict
