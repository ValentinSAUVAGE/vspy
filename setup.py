#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='vspy',
    version='0.0.1',
    plateformes = 'Mixte (Windows, MacOS, Linux)',
    packages=find_packages(),
    packages_dir = {'' : 'vspy'},
    author='Valentin SAUVAGE',
    description='Bibliothèque Python pour le développement',
    url='https://valentinsauvage.fr',
    download_url='https://github.com/sergeLabo/pymultilame',
    license='GPL Version 3',
    long_description=open('README.md').read()
