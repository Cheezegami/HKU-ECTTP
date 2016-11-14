int_aantalRays = 0

def draw():
    global int_aantalRays
    while(int_aantalRays <= 100):
        if(int_aantalRays % 5 == 0):
            if(int_aantalRays % 3 == 0):
                print("highfive")
            else:
                print("five")
        elif(int_aantalRays % 3 == 0):
            print("high")
        else:
            print(int_aantalRays)
        int_aantalRays += 1
    
        