#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
ttweb - 2023 - por jero98772
ttweb - 2023 - by jero98772
"""
from setuptools import setup, find_packages
setup(
	name='ttweb',
	version='1.0.0',
	license='GPLv3',
	author_email='jero98772@protonmail.com',
	author='jero98772',
	description='is a bash script that use ledger for time counting in different activities and subactivities.\nttweb is a web interface tt ,that can handle multiple users ',
	url='https://jero98772.pythonanywhere.com/',
	packages=find_packages(),
    install_requires=['Flask'],
    include_package_data=True,
	)