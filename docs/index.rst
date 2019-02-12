Welcome to FolderAnalyse's documentation!
=========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Installation
============

FolderAnalyse requires Python 3.6 or above, and has been tested on Linux and MacOS.

Once Python in installed, simply install the package from Python.org, via:

.. code-block:: bash

   pip3 install FolderAnalyse


Alternatively, you can install the development version from GitHub via:

.. code-block:: bash

   pip3 install git+https://github.com/rpep/FolderAnalyse


Tutorial
========

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


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`modules`
* :ref:`search`
