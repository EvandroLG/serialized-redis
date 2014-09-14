#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='SerializedRedis',
    version='0.1.0',
    description='A solution to have lists and dictionaries serialized using redis-py.',
    author='EvandroLG',
    author_email='evandrolgoncalves@gmail.com',
    keywords=['Redis', 'redis-py', 'serialized datas']
    url='http://github.com/EvandroLG/serialized-redis',
    licence='MIT',
    tests_require='pytest>=2.5.0',
    install_requires=[
        'redis',
    ]
)