'''Which Hand - in Pythom Basic Games Project
            Or Aloni 13/06/2020          v/1/0'''



print("                                Which hand?\n")
print('''RULES: Pick up a dime in one hand and a penny in the other. I'll guess which hand holds
       which coin if you answer a couple of questions for me.
       Multiply the value of the coin in your right hand by an even number and multiply the value
       of the coin in your left hand by an odd number.\n''')


def new_game():

    while True:

        repeat_game = str(input("Would you like to repeat game? "))
        yes = repeat_game.lower().strip("es")
        no = repeat_game.lower().strip("o")

        if yes == "y":
            break
        elif no == "n":
            print("\nThank you for playing. Have a nice day")
            exit()
        else:
            print("Please enter a yes/no answer")



while True:

    user_answer = input("\nIs the sum of the two numbers you added odd or even? ").lower()
    if user_answer == "even":
        print("\nThe dime is in your left hand, and the penny in your right hand\n")
        new_game()
    elif user_answer == "odd":
        print("\nThe dime is in your right hand, and the penny in your left hand\n")
        new_game()
    else:
        print("\nPlease enter odd/even\n")
        continue



