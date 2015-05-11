#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Class for movie trailer information.

Class for use in fresh_tomatoes.py application.

:REQUIRES:

:TODO:

:AUTHOR: Ripley6811
:ORGANIZATION: None
:CONTACT: python@boun.cr
:SINCE: Sun May 10 15:07:38 2015
:VERSION: 0.1
"""
#==============================================================================
# PROGRAM METADATA
#==============================================================================
__author__ = 'Ripley6811'
__contact__ = 'python@boun.cr'
__copyright__ = ''
__license__ = ''
__date__ = 'Sun May 10 15:07:38 2015'
__version__ = '0.1'

#==============================================================================
# IMPORT STATEMENTS
#==============================================================================


#==============================================================================
# METHODS
#==============================================================================
class MovieTrailer(object):
    def __init__(self, title, image_url, trailer_url, website_url, description):
        self.title = title
        self.image_url = image_url
        self.trailer_url = trailer_url
        self.website_url = website_url
        self.description = description


#==============================================================================
# MAIN METHOD AND TESTING AREA
#==============================================================================
def main():
    """Description of main()"""



if __name__ == '__main__':
    main()

