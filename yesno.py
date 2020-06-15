
class Yesno:

    def new_game(self):

         repeat_game = str(input("Would you like to repeat game? "))
         yes = repeat_game.lower().strip("es")
         no = repeat_game.lower().strip("o")
         print(repeat_game)

         while True:
             if yes == "y":
                continue
             elif no == "n":
                print("Thank you for playing. Have a nice day")
                break
             else:
                print("Please enter a yes/no answer")









y = Yesno.restart()

print(y)

