"""
Ryan Pepper (2018)

test_process.py

Tests for the fileparser.py module
"""
import FolderAnalyse.fileparser as p
import os

file_dir = os.path.dirname(__file__)


def test_read():
    """
    test_read()

    This test checks the fileparser._read function's ability
    to handle files of different encodings.

    It opens files of each encoding, writes them, and
    then tries to open the file.
    """

    encodings = ['utf-8', 'utf-16', 'latin-1', 'ascii']
    for encoding in encodings:
        f = open('test.txt', 'w', encoding=encoding)
        f.write("Some text to handle!")
        f.close()
        p._read("test.txt")


def test_parser_unsorted():
    """
    test_parser_unsorted()

    This test checks the file parser, checking a variety of properties are as
    as expected including when the sorted option is not selected.

    """
    file = os.path.join(file_dir, "example_documents",
                        "a-tale-of-two-cities.txt")
    print(file)
    freq_dict = p.parse(file, case_sensitive=False, sort=False)

    # Check keys are not empty
    assert len(freq_dict.keys()) > 0, "No words found in document with words!"

    # Check keys are all lower case
    for key in freq_dict.keys():
        assert key == key.lower(), "Upper case words found when lower case " \
                                   "option was chosen in parser."

    # Check that new line character is not in keys, given it isn't a word.
    assert '\n' not in freq_dict.keys(), "'\n' was found in the keys dict."

    # Check that frequencies are non-zero for words in the dictionary
    for key, freq in freq_dict.items():
        assert freq > 0, f"freq_dict[{key}] had 0 as frequency when the word" \
                          "had been found in the body of the text."


def test_parser_sorted():
    """
    test_parser_unsorted()

    This test checks the file parser, checking a variety of properties are as
    as expected. This, however, checks that the items are sorted correctly.

    """
    file = os.path.join(file_dir, "example_documents",
                        "a-tale-of-two-cities.txt")
    freq_dict = p.parse(file, case_sensitive=True, sort=True)

    # Check keys are not empty
    assert len(freq_dict.keys()) > 0, "No words found in document with words!"

    # Check that new line character is not in keys, given it isn't a word.
    assert '\n' not in freq_dict.keys(), "'\n' was found in the keys dict."

    # Check that frequencies are non-zero for words in the dictionary
    for key, freq in freq_dict.items():
        assert freq > 0, f"freq_dict[{key}] had 0 as frequency when the word" \
                          "had been found in the body of the text."

    for i, (key, freq) in enumerate(freq_dict.items()):
        if i == 0:
            last_freq = freq
        else:
            assert last_freq > freq, "Sorting wrong. Last freq is smaller."


if __name__ == "__main__":
    test_parser_unsorted()
    test_parser_sorted()
