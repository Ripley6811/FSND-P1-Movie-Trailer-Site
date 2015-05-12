#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Single page movie trailer website creator.

Main program that reads in a JSON structure containing movie data. Data is
loaded into a list of MovieTrailer objects which is passed to fresh_tomatoes'
open_movies_page method for creating a single page website.
"""
import fresh_tomatoes
import media
import json


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
