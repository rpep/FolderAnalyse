Welcome to FolderAnalyse's documentation!
=========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   source/modules.rst

Installation
============

FolderAnalyse requires Python 3.6 or above, and has been tested on Linux and MacOS.

First, to install Python, visit Python.org, or try the Anaconda.org distribution.

Once Python is installed, simply install the package using the Python package manager
pip, by running on the command line:

.. code-block:: bash

   pip install FolderAnalyse


Alternatively, you can install the development version from GitHub via:

.. code-block:: bash

   pip install git+https://github.com/rpep/FolderAnalyse


Command Line Use
================

Here we give some information about the module FolderAnalyse.

To generate statistics about a particular file:

.. code-block:: bash

   echo "The quick brown fox jumped over the lazy dog" > test.txt
   FolderAnalyse test.txt

You should see some output like:

.. code-block:: bash

   File "test.txt" Top 10 Word Frequencies
   ---------------------------------------
   1. The, 1
   2. quick, 1
   3. brown, 1
   4. fox, 1
   5. jumped, 1
   6. over, 1
   7. the, 1
   8. lazy, 1
   9. dog, 1


To generate statistics about all files in a folder:

.. code-block:: bash

   FolderAnalyse /path/to/a/folder


To generate statistics about all "\*.md" files in a folder:

.. code-block:: bash

   FolderAnalyse /path/to/a/folder -t ".md"


To save the outputted text as a report:

.. code-block:: bash

   FolderAnalyse /path/to/a/folder -s report.txt


The tests for the project can be run from the command line with:

.. code-block:: bash

   FolderAnalyse . -r


For the test cases I made use of out-of-copyright Project Gutenberg books as useful reference cases.
These are included in the tests/example_docs folder.


API
===

In general FolderAnalyse is designed to be used from the command line, but
here I'll show how you can use the functions in your own projects.

The bulk of the interesting code is in :mod:`FolderAnalyse.process`, in the two functions
:func:`~FolderAnalyse.process.process_file` and :func:`~FolderAnalyse.process.process_dir`.

To process a file and get the frequency dictionary, simply:

.. code-block:: python

   >>> import FolderAnalyse.process as p
   
   >>> f1 = open('test1.txt', 'w')
   >>> f1.write("The quick brown fox jumped over the lazy dog")
   >>> f1.close()

   >>> stats_text, frequency_dict, top_freqs = p.process_file('test.txt',
                                                              N=5, 
                                                              case_sensitive=False)
   >>> print(top_freqs['the'])
   2

If we create another file, we can use directory processing:

.. code-block:: python

   >>> f2 = open('test2.txt', 'w')
   >>> f2.write("Writing words to the second file")
   >>> f2.close()

   # See the API documentation for more details:
   >>> text, dics, top_dic, cdic, top_cdic = sp.process_dir('.')
   
   >>> print(top_cdic['the'])
   3
   
If the word counts are all that is required, this can be handled just using
the function :func:`~FolderAnalyse.fileparser.parse`.

.. code-block:: python

   >>> import FolderAnalyse.fileparser as fp
   >>> print(fp.parse('test2.txt', sort=True))
   {'writing': 1, 'words': 1, 'to': 1, 'the': 1, 'second': 1, 'file': 1}
   

The tests for the project can be run directly from the Python interpreter with:

.. code-block:: python

   >>> import FolderAnalyse
   >>> FolderAnalyse.runtests()   



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
