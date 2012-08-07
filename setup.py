# -*- coding: utf-8 -*-
""" eventbus setup.py script """

# system
from distutils.core import setup
from os.path import join, dirname


setup(
    name='eventbus',
    version='0.1.0',
    author='Rodrigo Sampaio Vaz',
    author_email='rodrigo.vaz@gmail.com',
    packages=['eventbus','eventbus.test'],
    url='http://',
    license='LICENSE.txt',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    install_requires=[''],
    test_suite='eventbus.test',
)
