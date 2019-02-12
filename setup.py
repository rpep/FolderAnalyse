"""
Ryan Pepper (2018)

This script sets configuration options for setuptools for the FolderAnalyse
project.

"""
from setuptools import setup

setup(
   name='FolderAnalyse',
   version='0.1',
   description='A program that analyses files in a directory with '
               'word frequency statistics.',
   author='Ryan Pepper',
   author_email='ryan.pepper@soton.ac.uk',
   packages=['FolderAnalyse'],
   entry_points = {
        "console_scripts": [ "FolderAnalyse=FolderAnalyse.script:main" ]
       },
   classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
