#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from setuptools import setup

setup(
    name = 'LatestTweetMacro',
    version = '1.0',
    packages = ['latestTweet'],
    author = 'Michael Caron',
    author_email = 'mike@cruxus.com',
    description = 'A Trac wiki macro to display user\'s latest tweet.',
    license = 'BSD',
    keywords = 'trac plugin macro twitter',
    classifiers = [
        'Framework :: Trac',
    ],
    
    install_requires = [],

    entry_points = {
        'trac.plugins': [
            'latestTweet.macro = latestTweet.macro',
        ]
    },
)
