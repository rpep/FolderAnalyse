Welcome to FolderAnalyse's documentation!
=========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   source/*

Installation
============

FolderAnalyse requires Python 3.6 or above, and has been tested on Linux and MacOS.

Once Python in installed, simply install the package from Python.org, via:

.. code-block:: bash

   pip3 install FolderAnalyse


Alternatively, you can install the development version from GitHub via:

.. code-block:: bash

   pip3 install git+https://github.com/rpep/FolderAnalyse


Quick Tutorial
==============

Here we give some information about the module FolderAnalyse.

To generate statistics about a particular file:

.. code-block:: bash

   FolderAnalyse /path/to/a/file.txt

To generate statistics about all *.txt files in a folder:

.. code-block:: bash

   FolderAnalyse /path/to/a/folder

To generate statistics about all *.md files in a folder:

.. code-block:: bash

   FolderAnalyse /path/to/a/folder -t ".md"


Tests make use of out-of-copyright Project Gutenberg books as useful reference cases.
These are included in the tests/ folder.


API
===

In general FolderAnalyse is designed to be used from the command line, but
here I'll show how you can use the functions in your own projects.

The bulk of the interesting code is in :mod:`FolderAnalyse.process`.




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
