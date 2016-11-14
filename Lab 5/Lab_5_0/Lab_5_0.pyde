# Made by Ronald van Egdom.
# For HKU Creative Programming with Python.
# Lab 5.0.

int_aantalRays = 0 # Ter ere aan Ray, die mij uitleg vroeg over loops. :-)

def draw():
    global int_aantalRays
    while(int_aantalRays <= 100): # Als het aantal rays kleiner of gelijk is aan honderd wordt deze loop uitgevoerd.
        if(int_aantalRays % 5 == 0):
            if(int_aantalRays % 3 == 0):
                print("highfive") # Als het aantal rays een meerfout is van 3 EN 5 print dan highfive.
            else:
                print("five") #Als het aantal rays een meerfout is van 5 print dan five.
        elif(int_aantalRays % 3 == 0):
            print("high") # Als het aantal rays een meerfout is van 3 print dan high.
        else:
            print(int_aantalRays)
        int_aantalRays += 1 # Elke draw wordt het aantal rays met 1 opgeteld.
    
        