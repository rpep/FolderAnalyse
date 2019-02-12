import glob
import os
from FolderAnalyse import fileparser
from textwrap import dedent

    
def top_frequencies(freq_dict, nterms=10):
    """
    top_frequencies(freq_dict, name, nterms)
    
    Returns the first nterms in the dictionary.
    
    Note:
    This wrapper is needed just to handle
    files with less than 10 words.
    """
    items = list(freq_dict.items())
    if len(items) < nterms:
        return dict(items)
    else:
        return dict(items[:nterms])
    
    

def process_file(file, N=10, report=False):
    stats_text = f"{file} Top {N} Word Frequencies:"
    frequency_dict = fileparser.parse(file, sort=True)

    freqs = top_frequencies(frequency_dict, nterms=N)

    for key, value in freqs.items():
        stats_text += f"{key}, value"

    return stats_text, frequency_dict


def process_dir(dirname, extension, exclusions=[], report=False):
    stats_text = ""
    report_text = ""
    files = glob.glob(os.path.join(dirname, f'*.{extension}'))
    
    dicts = []
    for file in files:
        stat, rep, dic = fileparser.process_file(file, exclusions, report)
        stats_text += stat
        report_text += rep
        dicts.append(dic)
        
    combined_dict = fileparser.sort_dict(fileparser.combine_dicts(dicts))
    

    return stats_text, report_text, files, dicts, combined_dict