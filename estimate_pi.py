def estimate():
    pi =  0
    for i in range(1000):
        pi += (((-1) ** i) * (1 / ((2 * i) + 1))) * 4
        print(pi)
    
    print("Final estimate of pi is {}".format(pi))

estimate()