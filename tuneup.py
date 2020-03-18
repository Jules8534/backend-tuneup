#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Julita Marshall"

import timeit
import cProfile
import pstats
import functools


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.

    def inner(*args, **kwargs):
        profile_object = cProfile.Profile()
        profile_object.enable()
        result = func(*args, **kwargs)
        profile_object.disable()

        # stats_object = pstats.Stats(profile_object)
        # stats_object.strip_dirs()
        # stats_object.sort_stats('cumulative')
        # stats_object.print_stats()

        ps = pstats.Stats(profile_object).sort_stats('cumulative')
        ps.print_stats(10)
        return result
    return inner
    # raise NotImplementedError("Complete this decorator function")


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    # for movie in movies:
    #     if movie.lower() == title.lower():
    if title in movies:
        return True
    else:
        return False

@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(
        stmt="""find_duplicate_movies("movies.txt")""",
        setup="""from __main__ import find_duplicate_movies"""
        )
    runtime = t.repeat(repeat=7, number=3)
    return ("From timeit_helper, find_duplicate_movies takes an average of {} \n \seconds to run.".format(min(runtime)/3))   


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
