#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(name='funsliders',
      version='0.0.0.1',
      author='Zulko 2013',
    description= "Funsliders are user-friendly Matplotlib sliders",
    long_description=open('README.md').read(),
    license=open('LICENSE.txt').read(),
    keywords="pylab matplotlib slider interactive function",
    packages= find_packages(exclude='docs'))
