import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

words = words.split()

# TODO: analyze which words can follow other words
# Your code here
cache = {}

for i in range( len( words ) - 1 ):
    word = words[ i ]
    nxt  = words[ i + 1 ]

    if word not in cache:
        cache[ word ] = [ nxt ]
    else:
        cache[ word ].append( nxt )

starters = []

for key in cache.keys():
    if key[ 0 ].isupper() or len( key ) > 1 and key[ 1 ].isupper():
        starters.append( key )

def create_sentence():
    stoppers = '!.?'

    word = random.choice( starters )

    creating = True
    words    = []

    while creating:
        words.append( word )

        if word[ -1 ] in stoppers:
            creating = False
        
        nxt = cache[ word ]

        word = random.choice( nxt )
    
    return ' '.join( words )


# TODO: construct 5 random sentences
# Your code here

sentence1 = create_sentence()
sentence2 = create_sentence()
sentence3 = create_sentence()
sentence4 = create_sentence()
sentence5 = create_sentence()

print( sentence1 )
print( sentence2 )
print( sentence3 )
print( sentence4 )
print( sentence5 )