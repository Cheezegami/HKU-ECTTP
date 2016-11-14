# ECTTP Toets 1
# Author: Ronald van Egdom uit GI-1C op HKU Games en Interactie.
# Studentnummer 3018119
# Date: Gemaakt op 21-10-2016 van 11:45 tot 12:45


#Ruimte voor leerkracht om antwoorden te testen.
def setup():
    print "Vul hier de vragen in om de antwoorden te controleren! :)"

#Vraag 1.- Variabelen.

#Zelfde getallen als hoogste en laagste mogen wel.
def inrange(int_input,int_laag,int_hoog):
    if(int_input >= int_laag and int_input <= int_hoog):
        return(True)
    else:
        return(False)
#Zelfde getallen als hoogste en laagste mogen niet.
def inrangeExl(int_input,int_laag,int_hoog):
    if(int_input > int_laag and int_input < int_hoog):
        return(True)
    else:
        return(False)
      
      
#Vraag 2.- If-statements.

# Returned False wanneer er onvoldoende obers zijn.
# Als het zondag is kunnen er 5 bezoekers per ober bediend worden, anders 8.
def party(int_bezoekers,int_obers,bool_isZondag):
    if(bool_isZondag == True):
        if(int_bezoekers/int_obers <= 5): # Als het aantal bezoekers op zondag gedeeld door het aantal obers kleiner dan of gelijk is aan 5.
            return(True)
        return(False)
    else:
        if(int_bezoekers/int_obers <= 8): # Als het aantal bezoekers anders gedeeld door het aantal obers kleiner dan of gelijk is aan 8.
            return(True)
        return(False)

#Vraag 3.- Loops.

# Neemt de 1e helft van de ingevoerd string(ex. "Appeltaart" wordt "Appel".
def halfwoord(String_input):
    String_output = String_input[:len(String_input)/2] # Neemt de 1e helft van de string.
    return(String_output) # Retourneerd de output. (uitkomst)
    
#Vraag 4.- Booleans.

#Een functie die True geeft als je een paraplu nodig hebt.
#Als het regent heb je een paraplu nodig tenzij je binnen bent of een regenpak hebt.
def paraplu(bool_isRaining,bool_heeftRegenpak,bool_isInside):
    if(bool_isRaining == True): # Als het regent.
        if(bool_heeftRegenpak == True or bool_isInside == True): # Als de persoon een regenpak aanheeft of binnen is.
            return(False)
        else:
            return(True)
    else:
        return(False)
    
#Vraag 5.- Modulo.

#Rond een getal af op tientallen, rond naar boven af wanneer hoger dan of gelijk aan 5.
def rondaf(int_nummer):
    if(int_nummer % 10 >= 5):
        int_nummer = int_nummer - int_nummer % 10 + 10
    else:
        int_nummer = int_nummer - int_nummer % 10
    return(int_nummer)