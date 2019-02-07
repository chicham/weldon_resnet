#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')

setup(
    name='weldon_resnet',
    version='0.1.0',
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    author="Hicham Randrianarivo",
    author_email='h.randrianarivo@qwant.com',
    url='https://github.com/chicham/weldon_resnet',
    packages=[
        'weldon_resnet',
    ],
    package_dir={'weldon_resnet':
                 'weldon_resnet'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='weldon_resnet',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
)
