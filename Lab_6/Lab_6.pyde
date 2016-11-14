# Made by Ronald van Egdom.
# For HKU Creative Programming with Python.
# Lab 6.


def setup():
    print(6.0)#6.0
    print "wheels(3,5,2)",wheels(3,5,2)
    print "wheels(5,1,1)",wheels(5,1,1)
    print(6.1)#6_1
    print "XOR(True,False)",XOR(True,False)
    print "XOR(True,True)",XOR(True,True)
    print(6.2)#6.2
    pancakes(6,2000,1000)
    pancakes(8,1000,1000)
#6.0
#Cars have four wheels, trikes have three wheels, bikes have two wheels.
#Return total amount of wheels.
def wheels(int_cars,int_trikes,int_bikes):
    return((int_cars*4)+(int_trikes*3)+(int_bikes*2)) #Returns cars times 4 + trikes times 3 + bikes times 2.

#6.1
#Boolean's of which only one must be true.
def XOR(Bool_a,Bool_b): #Exclusive or. (non-bitwise) 
    if Bool_a ^ Bool_b:
        return True
    else:
        return False
#6.2
# Eggs in wholes, Milk in milliliter, Flour in grams.
# Return how many pancakes can be made.
# You make pancakes in batches of 10, eveyr 10 needing 2 eggs, 500ml milk and 250 grams of flour.
def pancakes(int_eggs,int_milk,int_flour):
    int_pancakes = 0
    int_oldEggs = int_eggs
    int_oldMilk = int_milk
    int_oldFlour = int_flour
    while(int_eggs >= 2 and int_milk >=500 and int_flour >=250):
        int_eggs -= 2
        int_milk -= 500
        int_flour -= 250
        int_pancakes += 10
    # Er was een spelfout bij het volgende statement, er stond flower, om het accuraat te maken heb ik hier flour van gemaakt.
    print"You can make: "+ str(int_pancakes) +" pancakes, with "+ str(int_oldEggs) + " eggs, " + str(int_oldMilk) + " ml milk and " + str(int_oldFlour) + " grams of flour. You have "+ str(int_eggs) +" eggs, "+str(int_milk) +" ml milk and "+str(int_flour)+" grams of flour left."
    return(int_pancakes)
        