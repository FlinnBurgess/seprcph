#!/usr/bin/python2.7
import os
from setuptools import setup
from setuptools import find_packages


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ""

setup(name='seprcph',
      packages=find_packages(),
      version='0.0.1',
      description='A game about trains in europe.',
      author='Harvey Hunt, Henry Jewell, Flinn Burgess, Peter Bryant, \
            Alex Corney, Ethan La Bonche Vince-Urwin',
      url='https://github.com/HarveyHunt/seprcph',
      keywords="python pygame trains europe",
      install_requires=['pygame'],
      long_description=read('README.md'),
      test_suite='tests',
      entry_points={'console_scripts': ['seprcph=seprcph.main:main']})
