import glob
import os

from FolderAnalyse import fileparser


    

def process_file(file, exclusions=[], N=10, report=False):
    stats_text = ""
    frequency_dict = fileparser.parse(file, exclusions=exclusions, sort=True)
     
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