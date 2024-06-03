count = 0

def hello():
    global count
    count += 1
    print("Hi There ", count)
    hello()

hello()