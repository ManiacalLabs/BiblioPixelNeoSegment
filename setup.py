from __future__ import print_function
from setuptools import setup, find_packages
import json
import sys
import datetime
from sys import version_info as vi


setup(
    name='BiblioPixelNeoSegment',
    version="1.0.0",
    description='Adds BiblioPixel support for the NeoSegment: https://www.crowdsupply.com/maksmakes/neosegment',
    author='Adam Haile',
    author_email='adam@maniacallabs.com',
    url='https://github.com/ManiacalLabs/BiblioPixelNeoSegment',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
