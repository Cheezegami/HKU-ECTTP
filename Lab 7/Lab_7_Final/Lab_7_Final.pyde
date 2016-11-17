# Made by Ronald van Egdom.
# For HKU Creative Programming with Python.
# Lab 7.


def setup():
    print 7.0
    print "(round_sum(16,17,18)",(round_sum(16,17,18)) # Totaal 51, dus moet 50 wezen.
    print "(round_sum(16,17,18)",(round_sum(22,39,55)) # Totaal 116, dus moet 116 wezen
    print 7.1
    print "scramble('scrambled', 'eggs')",scramble("scrambled", "eggs")
    print "scramble('kipje','kaasje')",scramble("kipje","kaasje")
    print 7.2
    print "unscramble('kkiapajsej0e')",unscramble('kkiapajsej0e')
    print "unscramble('uengsgcsr0a0m0b0l0e0d0')",unscramble('uengsgcsr0a0m0b0l0e0d0')
# 7.0
#Geeft een integer terug waarbij de som van de afronding van de drie getallen word berekend. Het getal wordt afgerond naar het dichtstbijzijnde meerfout van 10.
def round_sum(int_a,int_b,int_c):
    int_resultaat = int_a + int_b + int_c
    return(rondaf(int_resultaat))

#Afronden op 10 geleend van ECTTP toets.
def rondaf(int_nummer):
    if(int_nummer % 10 >= 5):
        int_nummer = int_nummer - int_nummer % 10 + 10
    else:
        int_nummer = int_nummer - int_nummer % 10
    return(int_nummer)

#7.1
#Gegeven twee woorden, schrijf een functie genaamd “def scramble(word1, word2):” die de woorden door elkaar husselt door om en om een letter van elk woord te pakken en daarmee een nieuw woord te vormen.
def scramble(String_word1, String_word2):
    String_newWord = ""
    for i in range (0, max(len(String_word1),len(String_word2))): #i is zo groot als het meest aantal letters van de twee woorden.
        try: # Probeer dit.
            String_newWord += String_word1[i] # Plak de letter dat op positite i staat binnen de array.
        except: # Bij een index out of range plak er dan een nul achter.
            String_newWord += "0"
        try:
            String_newWord += String_word2[i]
        except:
            String_newWord += "0"
    return(String_newWord.rstrip('0')) #Haalt nul op het einde weg.
        
#7.2        
#Gegeven een gescrambled woord van Opdracht 7_1, schrijf een functie “def unscramble(word):” ,wat het woord weer opdeelt in twee woorden en een tuple terug geeft met deze twee woorden (als string) als elementen erin.
def unscramble(String_scrambledWord):
    String_unscrambledWord1 = ""
    String_unscrambledWord2 = ""
    for i in range (0, len(String_scrambledWord)):
        if(i % 2 == 0 and String_scrambledWord[i] != "0"): #Als het een even getal is en geen nul is.
            String_unscrambledWord1 += String_scrambledWord[i] # Plaats de letter in het nieuwe woord.
        elif String_scrambledWord[i] != "0": # Als het binnen de String geen nul is.
            String_unscrambledWord2 += String_scrambledWord[i] # Plaats de letter in het andere nieuwe woord.
    return(String_unscrambledWord1,String_unscrambledWord2) # Breng de waarde terug.
        
    
        
    