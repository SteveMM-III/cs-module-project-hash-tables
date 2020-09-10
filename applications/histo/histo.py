# Your code here

import re

file = open( 'robin.txt' ).read()


def word_count(s):
    d = {}

    filtered = re.sub( r"[^\w'\s]", '', s )

    for word in filtered.lower().split():
        if word not in d.keys():
            d[ word ]  = '#'
        else:
            d[ word ] += '#'

    return d


data = word_count( file )

for k in sorted( data, key = lambda k: len( data[ k ] ), reverse = True ):
    print( "{0:<16} {1}".format( k, data[ k ] ) )