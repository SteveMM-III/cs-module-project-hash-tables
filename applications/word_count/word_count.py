import re

def word_count(s):
    # Your code here
    d = {}

    # regex reference: https://docs.python.org/3/library/re.html
    filtered = re.sub( r"[^\w'\s]", '', s )

    for word in filtered.lower().split():
        if word not in d.keys():
            d[word] = 1
        else:
            d[word] += 1
    
    return d


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))