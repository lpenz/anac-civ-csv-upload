try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Uploads CSV data to brazilian ANAC',
    'author': 'Leandro Penz',
    'url': 'https://github.com/lpenz/anac-civ-csv-upload',
    'author_email': 'lpenz@lpenz.org',
    'version': '0.1',
    'install_requires': ['nose','mechanize'],
    'packages': ['anac'],
    'scripts': ['bin/anac-civ-csv-upload'],
    'name': 'anac-csv-upload'
}

setup(**config)
