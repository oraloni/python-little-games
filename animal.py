''' v/0/3                                       Animal

                                          Or Aloni 06.06.2020                                                        '''


import random
from  collections import defaultdict
import itertools
from msgframe import msgframe

# Finds out if computer randomly guessed user animal's property
def property_query():
    random_property = random.choice(properties)
    user_property = input("Does it " + random_property + "? ")
    if user_property == "y":
        return random_property
    elif user_property == "n":
        return random_property
    else:
        print("Please enter y/n")
        property_query()

 # Strip "Does it [...]" from user distinguish question, leaves only the user inputted property (see below)
def propstrip(user_prop):
    full_question = str(user_prop)
    left_strip = full_question.partition("it ")
    prop_strip = left_strip[2].strip("?")
    return prop_strip

# Finds out if computer guessed user animal
def user_animal_query():
    random_animal = random.choice(animals)
    animal_identity = input("Were you thinking about " + random_animal + "? ")

    if animal_identity == "y":
        print("good")

    elif animal_identity == "n":
        print("bad")

        # TODO: make sure user animal is capitalized
        user_animal = input("The animal you were thinking of was a? ")
        animals.append(user_animal)
        print(animals)
        distinguish = propstrip(input("Please type in a question that would distinguish a "
                            + random_animal + " from a " + user_animal + ": "))
        properties.append(distinguish)
        print(properties)

# attach animal to property - "computer psuedo lernning"
def attachToDict(start_list):
    res = defaultdict(list)

    for animal , property in start_list:
        res[animal].append(property)
    print(res)

# Removes all the animals with property
def normv(prop, dictionary):
    postRmv = {}

    for k, v in dictionary:

        if v == prop:
            postRmv.get(k)
            print(postRmv)
        else:
            continue

    # Main program

# TODO: print ruels of game
msgframe.strframe(20, 2, "Animal")
print("\nType 'n' to exit\n")

animals = ["Bird", "Lion"]
properties = ["have wings", "eat meat"]

rounds = 0

while True:

    start_questiom = input("Are you thinking about an animal? ")
    # TODO: yes-no
    if start_questiom == "y":

        counter = 0

        if rounds <= 3:

            while counter <= rounds:
                x = property_query()
                print(x)
                normv(animaldict, x)
                counter = counter + 1
        else:
            rounds = 0

        user_animal_query()

        #animaldict = attachToDict(animals, properties)
        lcombine = list(itertools.zip_longest(animals , properties))
        animaldict = attachToDict(lcombine)

        rounds = rounds + 1
        print(rounds)

        continue

    elif start_questiom == "n":

        print("\nOk, thank you for playing. Have a nice day")
        break

    else:
        continue




# attach animal in animal's list <----> property in proreties list
# |---------------> animal property question ("for user_animal the answer would be?}
                                # "no" ---> continue
                                 # | "yes" -----------> attach user_property to user animal
                                                     #BACK TO BEGINING
