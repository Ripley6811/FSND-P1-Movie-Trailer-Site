#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Class for movie trailer information.

For use in fresh_tomatoes.py application.
"""


class MovieTrailer(object):
    """Data structure for movie trailer information.

    Attributes:
        title: A string of the movie title.
        image_url: A string of the image url.
        trailer_url: A string of the Youtube trailer url.
        website_url: A string of the movie website url if available.
        description: A string containing a short description of the movie.
    """
    def __init__(self, title, image_url, trailer_url, website_url, description):
        self.title = title
        self.image_url = image_url
        self.trailer_url = trailer_url
        self.website_url = website_url
        self.description = description
