"""
Ryan Pepper (2019-)

This script sets configuration options for setuptools for the FolderAnalyse
project.

"""
from setuptools import setup, find_packages
import os


setup(
    name='FolderAnalyse',
    version='0.1.1',
    description='A program that analyses files in a directory with '
                'word frequency statistics.',
    author='Ryan Pepper',
    author_email="ryan.pepper@soton.ac.uk",
    url="http://github.com/rpep/FolderAnalyse",
    packages=find_packages(),
    package_data={'FolderAnalyse': ['*.txt', os.path.join('FolderAnalyse', 
                                                          'tests'
                                                          'example_documents',
                                                          '*.txt')]
    },
    include_package_data = True,
    entry_points = {
        "console_scripts": [ "FolderAnalyse=FolderAnalyse.script:main" ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls = {
        "Documentation": "https://folderanalyse.readthedocs.io",
        "Source Code": "https://github.com/rpep/FolderAnalyse",
    },
    install_requires = ["pytest"],
    python_requires=">= 3.6",
)
