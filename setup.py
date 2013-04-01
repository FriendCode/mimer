#!/usr/bin/python


try:
    from setuptools import setup, Extension
    has_setuptools = True
except ImportError:
    from distutils.core import setup, Extension
    has_setuptools = False


# Constants
version_string = '0.0.1'


setup_kwargs = {}

setup(name='mimer',
      description='A helper module for working with mimetypes',
      keywords='mimetypes file extensions',
      version=version_string,
      url='git+ssh://git@friendco.de:friendcode/mimer.git',
      license='MIT',
      author="Aaron O'Mullan",
      author_email='aaron.omullan@gmail.com',
      long_description="",
      packages=['mimer'],
      **setup_kwargs)
