def first():
    string = input("Type a sentence ")
    for char in string:
        if char == " ":
            break
        print(char, end="")

first()