import pytest
import FolderAnalyse.fileparser as p
import os

file_dir = os.path.dirname(__file__)

def test_parser_unsorted():
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
    file = os.path.join(file_dir, "example_documents", "a-tale-of-two-cities.txt")
    freq_dict = p.parse(file, case_sensitive=True, sort=True)

    # Check keys are not empty
    assert len(freq_dict.keys()) > 0, "No words found in document with words!"

    # Check that new line character is not in keys, given it isn't a word.
    assert '\n' not in freq_dict.keys(), "'\n' was found in the keys dict."

    # Check that frequencies are non-zero for words in the dictionary
    for key, freq in freq_dict.items():
        assert freq > 0, f"freq_dict[{key}] had 0 as frequency when the word had been found in the body of the text."


    for i, (key, freq) in enumerate(freq_dict.items()):
        if i == 0:
            last_freq = freq
        else:
            assert last_freq > freq, "Sorting wrong. Last freq is smaller."




if __name__ == "__main__":
    test_parser_unsorted()
    test_parser_sorted()