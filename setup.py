#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


long_description = """
Django URL routing system rethinked.
"""


requirements = [
    'django>=1.8',
    'six',
]

test_requirements = [
    'mock'
]

setup(
    name='urljects',
    version='0.2.2',
    description="Django URLS rethinked",
    long_description=long_description,
    author="Visgean Skeloru",
    author_email='visgean@gmail.com',
    url='https://github.com/visgean/urljects',
    packages=[
        'urljects',
    ],
    package_dir={'urljects': 'urljects'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='urljects',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
