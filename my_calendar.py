def my_calendar():
    print("Sun   Mon   Tue   Wed   Thur  Fri  Sat")
    print()

    for i in range(1, 37):
        if i > 31:
            i = 1
        print(i, end="")
        if i < 10:
            print("     ", end="")
        else:
            print("    ", end="")
        if i % 7 == 0:
            print()

my_calendar()