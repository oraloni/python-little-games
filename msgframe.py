#v/1/ - Or Aloni 14/06/2020
# Create a string with a frame of asterixs

class msgframe:

    def position(self):
        pass

    def strframe(side_dots, hight, message):

        # Print up bar
        side_dots = side_dots * "*"
        msg_dots = len(message) * "*"
        bar = side_dots + msg_dots + side_dots

        # Prints side bar above and below message
        def side_hight(hight):
            long_spc = str((len(bar) - 2) * " ")
            while hight > 0:
                print("*" + long_spc + "*")
                hight = hight - 1

        # Prints side spaces
        short_spc = ((len(side_dots) - 1) * " ")

        # Prints frame around message
        print(bar)
        side_hight(hight)
        print("*" + short_spc + message + short_spc + "*")
        side_hight(hight)
        print(bar)
