# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

cipher = open( 'ciphertext.txt' ).read()
# letters arranged by frequency %
letters = 'ETAOHNRISDLWUGFBMYCPKVQJXZ'


def get_frequency( text ):
    text = text.upper()

    letter_freq = {}

    for letter in letters:
        letter_freq[ letter ] = 0

    for letter in text:
        if letter in letters:
            letter_freq[ letter ] += 1
            
    return letter_freq


freq = get_frequency( cipher )

ordered_freq = ''.join( sorted( freq, key = lambda k: freq[ k ], reverse = True ) )

def decrypt( text ):

    revealed = ''

    for c in text:
        ndx = ordered_freq.find( c )
        
        if ndx == -1:
            revealed += c
        else:
            revealed += letters[ ndx ]
    
    return revealed


print( decrypt( cipher ) )