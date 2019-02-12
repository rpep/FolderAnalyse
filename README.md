# FolderAnalyse

[![Build Status](https://travis-ci.com/rpep/folder-analyse.svg?branch=master)](https://travis-ci.com/rpep/folder-analyse)

The problem definition:

> Consider a folder containing a number of text files.

> It is required to find the top 10 most frequently used words in each file, and report this. Additionally, it must be possible to report on the top 10 most frequently used words across all the files analysed.

> It must be possible to generate a report, suitable for archiving, summarising the results.

Requirements are that the software is:

* Easy to understand
* Robust
* Documented
* Testable
* Can be extended if necessary

# Using the application:

To generate statistics about a particular file:

```bash
FolderAnalyse /path/to/a/file.txt
```

To generate statistics about all *.txt files in a folder:
```
FolderAnalyse /path/to/a/folder
```

To generate statistics about all *.md files in a folder:
```
FolderAnalyse /path/to/a/folder -t ".md"
```

Tests make use of out-of-copyright Project Gutenberg books as useful reference cases.
These are included in the tests/ folder.
