#!/usr/bin/python
# -*- coding: utf-8 -*-

# SerializedRedis
# author: Evandro Leopoldino Gonçalves <evandrolgoncalves@gmail.com>
# https://github.com/evandrolg
# License: MIT

from setuptools import setup


setup(
    name='serialized-redis',
    version='0.1.0',
    description='A solution to have lists and dictionaries serialized using redis-py.',
    author='EvandroLG',
    author_email='evandrolgoncalves@gmail.com',
    keywords=['Redis', 'redis-py', 'serialized datas'],
    url='http://github.com/EvandroLG/serialized-redis',
    license='MIT',
    tests_require='pytest>=2.5.0',
    install_requires=[
        'redis',
    ],
    packages=['serialized-redis']
)