#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
summary

description

:REQUIRES:

:TODO:

:AUTHOR: Ripley6811
:ORGANIZATION: None
:CONTACT: python@boun.cr
:SINCE: Sun May 10 17:32:08 2015
:VERSION: 0.1
"""
#===============================================================================
# PROGRAM METADATA
#===============================================================================
__author__ = 'Ripley6811'
__contact__ = 'python@boun.cr'
__copyright__ = ''
__license__ = ''
__date__ = 'Sun May 10 17:32:08 2015'
__version__ = '0.1'

#===============================================================================
# IMPORT STATEMENTS
#===============================================================================
import fresh_tomatoes
import media
import json
#===============================================================================
# METHODS
#===============================================================================






#===============================================================================
# MAIN METHOD AND TESTING AREA
#===============================================================================
def main():
    """Description of main()"""
    trailer_list = []
    with open('movie_trailers_list.txt') as rfile:
        js = json.load(rfile)
        for each in js:
            trailer_list.append(media.MovieTrailer(**each))

    print trailer_list
    print json.dumps([each.__dict__ for each in trailer_list], indent=True)
    fresh_tomatoes.open_movies_page( trailer_list )




if __name__ == '__main__':
    main()

