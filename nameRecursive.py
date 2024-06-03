count = 0

def hello():
    # don't forget to use global here since python uses local variables.And by using global you say check the global variable for this name.
    global count

    # count ++ is invalid in python, I always mix this up
    count += 1
    print("Hi There ", count)
    hello()

hello()