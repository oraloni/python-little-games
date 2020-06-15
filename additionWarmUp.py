'''Addition Warm-up - in Pythom Basic Games Project
            Or Aloni 13/06/2020          v/1/0'''


import random
import sys

# Get two random number and return tuple
def get_numbers(range):
    num_range = int(range)
    first_num = random.randrange(num_range)
    second_num = random.randrange(num_range)
    return (first_num, second_num)

# Ask if replay
def new_game():

    while True:

        repeat_game = str(input("Would you like to play another round? "))
        yes = repeat_game.lower().strip("es")
        no = repeat_game.lower().strip("o")

        if yes == "y":
            continue
        elif no == "n":
            print("\nThank you for playing. Have a nice day")
            exit()
        else:
            print("Please enter y/n answer please")

# Check if user was right
def answer(num_sum, u_answer):
    if u_answer == "":
        print("Enter a number please")
    elif int(num_sum) != int(u_answer):
        return 2
    elif int(num_sum) == int(u_answer):
        return 1


# Exit when input == None
def nullexit(input):
    if input == "":
        print('''\n                       Thank you for playing. Goodbye''')
        sys.exit(0)



# Main program
print('''                    
                               **********************
                               *                    *
                               *  Addition Warm-up  *
                               *                    *
                               **********************
                                 
        The object of this game is to improve your skill at adding numbers.
        Remember - as you play more turns, the problems get more complex \n''')

how_many_turns = input("How many problems do you want to solve? (type 0 to exit game) ")

while int(how_many_turns) > 0:

    how_many_turns = int(how_many_turns) + 1

    turn = 1
    num_right_answer = 0

    while turn < how_many_turns:

        numtpl = get_numbers(int(turn) * 50)
        rightnum = numtpl[0]
        leftnum = numtpl[1]
        numsum = rightnum + leftnum
        # TODO: fix bug when user doesnt enter an integer
        user_answer = input("\nHow much is " + str(rightnum) + " + " + str(leftnum) + "? ")

        rightOrWorng = answer(numsum, user_answer)

        if rightOrWorng == 1:
            print("Your right! good work.\n")
            num_right_answer = num_right_answer + 1

        elif rightOrWorng == 2:
            print("You are worng. The sum of "+ str(rightnum) + " and " + str(leftnum) + " is: " + str(numsum) + "\n")


    turn = turn - 1
    print("\nNice job. You got " + str(num_right_answer) + " out of " + str(turn) + " problems right!\n")

    new_game()
