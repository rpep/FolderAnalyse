.. FolderAnalyse documentation master file, created by
   sphinx-quickstart on Tue Feb 12 15:09:22 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to FolderAnalyse's documentation!
=========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Installation
============

FolderAnalyse requires Python 3.6 or above, and has been tested on Linux or MacOS.

Once Python in installed, simply install the package from Python.org, via:

.. code:: bash
   pip3 install FolderAnalyse


Alternatively, you can install the development version from GitHub via:

.. code:: bash
   pip3 install git+https://github.com/rpep/FolderAnalyse


Tutorial
========

Here we give some information about the module FolderAnalyse.

To generate statistics about a particular file:

.. code:: bash
   FolderAnalyse /path/to/a/file.txt


To generate statistics about all *.txt files in a folder:

.. code:: bash
   FolderAnalyse /path/to/a/folder


To generate statistics about all *.md files in a folder:
```
FolderAnalyse /path/to/a/folder -t ".md"
```

Tests make use of out-of-copyright Project Gutenberg books as useful reference cases.
These are included in the tests/ folder.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
