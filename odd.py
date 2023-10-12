def odd():
    list = input("Enter numbers ")
    for num in list:
        if int(num) % 2 == 0:
            continue
        print(num)
odd()