#!/usr/bin/python

from setuptools import setup


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
      package_data={'mimer': '*.json'},
      include_package_data=True,
      **setup_kwargs)
