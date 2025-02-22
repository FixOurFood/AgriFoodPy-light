import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'AgriFoodPy'
AUTHOR = 'FixOurFood'
AUTHOR_EMAIL = 'juanpablo.cordero@york.ac.uk'
URL = 'https://github.com/FixOurFood/AgriFoodPy'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'A package for modelling food systems'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'numpy',
      'pandas',
      'xarray',
      'matplotlib',
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      include_package_data=True
      )
