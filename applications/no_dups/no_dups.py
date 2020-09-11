def no_dups(s):
    # Your code here
    
    # create a new dict spliting the string which
    # removes duplicates and convert to list
    arr = list( dict.fromkeys( s.split() ) )

    # return the space separated list values
    return " ".join( arr )


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))