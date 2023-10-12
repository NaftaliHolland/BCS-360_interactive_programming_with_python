lives = 3

def play(*arg):
    global lives
    for q_number, q_answer in enumerate(arg, start = 1):
        print("question {}".format(q_number))
        for i in range(5):
            if lives == 0:
                print("Out of lives, better luck next time :)")
                break
            answer = input("What is you answer for question {} ".format(q_number))
            if answer == q_answer:
                print("You got it, good job")
                break
            else:
                print("Wrong answer try again")
        if answer != q_answer:
            lives -= 1
        print("you have {} lives left. On to the next question ".format(lives))

    if lives == 3:
        print("Nice you, made it to the next level good luck there")

play("Hello", "computer", "terminate")