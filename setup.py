#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'anac-csv-upload',
    'version': '0.1',
    'description': 'Uploads CSV data to brazilian ANAC',
    'author': 'Leandro Lisboa Penz',
    'author_email': 'lpenz@lpenz.org',
    'url': 'https://github.com/lpenz/anac-civ-csv-upload',
    'install_requires': ['nose', 'mechanize'],
    'packages': ['anac'],
    'scripts': ['bin/anac-civ-csv-upload'],
    'classifiers': [
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'License :: OSI Approved :: '
          'GNU General Public License v2 or later (GPLv2+)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          ],
    'license': "GPL2",
}

setup(**config)
