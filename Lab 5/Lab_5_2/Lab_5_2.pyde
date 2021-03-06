# Made by Ronald van Egdom.
# For HKU Creative Programming with Python.
# Lab 5.2.


def setup():
    size(800,800) # Grootte van het scherm.
    int_amount = 8 # Het aantal hokjes.
    int_size = width/int_amount # Grootte van een hokje is de breedte / het aantal hokjes.
    drawCheckboard(int_amount,int_size) # Het tekenen van het schaakbord op een int_amount(8)xint_amount(8) grid te voldoen.
    drawRedMarks(int_amount*2,int_size/2) #Het tekenen van de rode vierkantjes, geef ik het dubbele aantal mee en de helft van de grootte om aan een 16x16 grid te voldoen.

def drawCheckboard(int_amount,int_size): # Het tekenen van het schaakbord op een int_amount(8)xint_amount(8) grid te voldoen.
    for x in range (0, int_amount): # For loop ter lengte van het aantal vakjes om de x positie te bepalen.
        for y in range (0,int_amount): # For loop ter lengte van het aantal vakjes om de y positie te bepalen.
            if(x % 2 == 0): # Als X een meerfout van 2 is.
                f = 255 if y % 2 == 0 else 0  # Als y meerfout van 2 is dan wit, anders zwart.
            else: # Als X geen meerfout van 2 is.
                f = 0 if y % 2 == 0 else 255 # Als y meerfout van 2 is dan zwart, anders wit.
            fill(f) #Stel kleur in.
            rect(x*int_size,y*int_size,int_size,int_size) # Teken rectangle.
            
def drawRedMarks(int_amount,int_size): #Het tekenen van de rode vierkantjes, geef ik het dubbele aantal mee en de helft van de grootte om aan een 16x16 grid te voldoen.
    for x in range (0, int_amount): # For loop ter lengte van het aantal vakjes om de x positie te bepalen.
        for y in range (0,int_amount): # For loop ter lengte van het aantal vakjes om de y positie te bepalen.
            if(x >= int_amount/2-2 and x <= int_amount/2+1): # Het bepalen van de positie van de rode vierkantjes op de X axis.
                if(y >= int_amount/2-2 and y <= int_amount/2+1): # zelfde voor y.
                    fill(255,0,0) # Rood
                    rect(x*int_size,y*int_size,int_size,int_size) # Teken rectangle.
            
           
        
        
        
        
    
    
        