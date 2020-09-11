"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
def sumdiff():

    sums  = {}
    diffs = {}

    for x in q:
        for y in q:
            sums [ ( x, y ) ] = f( x ) + f( y ) 
            diffs[ ( x, y ) ] = f( x ) - f( y )

    for x in sums.keys():
        for y in diffs.keys():
            if sums[ x ] == diffs[ y ]:
                left_side  = f'f({x[0]}) + f({x[1]}) = f({y[0]}) - f({y[1]})   '
                right_side = f'{f( x[0] )} + {f( x[1] )} = {f( y[0] )} - {f( y[1] )}'

                print( left_side + right_side )


sumdiff()