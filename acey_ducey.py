'''Acey Ducy - in Pythom Basic Games Project
            Or Aloni 02/06/2020          v/1/0'''

import random
import sys




print('''\n                                   Acey-Ducey\n
                        Acey-Ducy is played in the following manner:
                        The dealer deals two cards face up.
                        you have an option to bet or not to bet,
                        depending whether or not you feel the
                        next card will have a value between the 
                        first two.
                        If you dont want to bet just enter 0
                        Ifyou want to quit the game enter nothing\n''')

amountofmoney = 100

# Initial amount of money
print("You have: " + str(amountofmoney) + "$\n")

while 0 < amountofmoney:

    # card name Dictunary - identifing numbers with card's name
    card_names = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack (11)", "Queen (12)", "King(13)", "Ace (14)")

    # Pick two random numbers *between 1 - 14*
    random.seed()

    f_card_random = random.randrange(1, 14)
    s_card_random = random.randrange(1, 14)

    cardlist = (f_card_random, s_card_random)
    sortedcardlist = sorted(cardlist)
    first_card = sortedcardlist[0]
    second_card = sortedcardlist[1]

    # Two open cards to user
    print("Cards: ", card_names[first_card], "and ", card_names[second_card], "\n")

    # Get user bet (leave empty to exit)
    user_bet = input("Place your bet (leave empty to exit): ")

    # Check to see if user input is empty
    if user_bet == "":
        print('''\n                       Thank you for playing. Goodbye''')
        sys.exit(0)

    user_bet = int(user_bet)

    # Pick random number - third_card
    third_card = random.randrange(1, 14)



    if (0 < user_bet <= amountofmoney):
        print("\nYou bet " + str(user_bet) + "$\n")
        print("\nThird card: " + str(third_card) + "\n")

        if (first_card <= third_card <= second_card):
            print("Good for you!\n")
            amountofmoney = amountofmoney + user_bet
            print("\n\nYou got "+ ("\033[1m" + str(amountofmoney) + "\033[0m") + "$ left\n\n")

        else:
            print("Show me the money!\n")
            amountofmoney = amountofmoney - user_bet
            print("\n\nYou got " + ("\033[1m" + str(amountofmoney) + "\033[0m") + "$ left\n\n")

    elif (user_bet == 0):
        print("\nNo bets\n")

    elif (user_bet > amountofmoney):
        print("\nYou do not have enough money\n")

    elif (user_bet == None):
        print("\nPlease enter your bet\n")

    else:
        print("\nError, please enter a valid number\n")


