#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-dragons',
    version='0.1.0',
    author='Gemini Data Processing Software Group',
    author_email='sus_inquiries@gemini.edu',
    url='http://www.gemini.edu',
    maintainer='Science User Support Department',
    license='BSD',
    description='A simple plugin to use with pytest',
    long_description=read('README.rst'),
    py_modules=['pytest_dragons'],
    python_requires='>=3.5',
    install_requires=['pytest>=3.5.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        "pytest11": [
            "pytest_dragons = pytest_dragons.plugin",
        ]
    },
)
