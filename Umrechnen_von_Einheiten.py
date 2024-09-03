#Definition Menü
def main_menu ():
    print("")
    print("Die möglichen Rechner:")
    print("Temperatur      = 1,")
    print("Geschwindigkeit = 2,")
    print("Kraft/Gewicht   = 3,")
    print("Distanz         = 4,")
    print("Währung         = 5.")

#Start Menüschleife
while True:
    main_menu()
    print("")
    rechner = float(input("Wähle einen Rechner: "))

#Temperaturrechner und Beginn der 2. While-Schleife
    if rechner == 1:
        while True:
            wahl = float(input("Wählen der vorhandenen Temperatureinheit (Celsius=1 oder Fahrenheit=2): "))
            temp1 = float(input("Gib die Temperatur ein: "))
        
            #Rechnung Celsius in Fahrenheit
            if wahl == 1:
                temp2 = temp1 * 18 / 10 + 32
                temp3 = round (temp2, 2)
                print("Deine Temperatur in Fahrenheit ist:", temp3, "°F")
        
            #Rechnung Fahrenheit in Celsius
            elif wahl == 2:
                temp2 = (temp1 - 32) * 5 / 9
                temp3 = round(temp2, 2)
                print("Deine Temperatur in Celsius ist:", temp3, "°C")
                
            #Ende der Temperatur While-Schleife
            print("")
            if input("Möchtest du nochmal eine Temperatur rechnen? (ja/nein): ").lower()!= 'ja':
                break
    
#Geschwindigkeitsrechner und Beginn der 3. While-Schleife
    elif rechner == 2:
        while True:
            wahl = float(input("Wählen der vorhandenen Geschwindigkeitseinheit (km/h=1 oder m/s=2): "))
            ges1 = float(input("Gib die Geschwindigkeit ein: "))
        
            #Rechnung km/h in m/s
            if wahl == 1:
                ges2 = ges1 / (36 / 10)
                ges3 = round(ges2, 2)
                print("Deine Geschwindigkeit in m/s ist:", ges3, "m/s")
        
            #Rechnung m/s in km/h
            elif wahl == 2:
                ges2 = ges1 * (36 / 10)
                ges3 = (ges2, 2)
                print("Deine Geschwindigkeit in km/h ist:", ges3, "km/h")
                
            #Ende der Geschwindigkeits While-Schleife
            print ("")
            if input("Möchtest du nochmal eine Geschwindigkeit rechnen? (ja/nein): ").lower() != 'ja':
                break

#Kraftrechner und Beginn der 4. While-Schleife
    elif rechner == 3:
        while True:
            wahl = float(input("Wählen der vorhandenen Einheit (Newton=1 oder kg=2): "))
            kraft1 = float(input("Gib den Wert ein: "))
        
            #Rechnung Newton in Kilogramm
            if wahl == 1:
                kraft2 = kraft1 / (980665 / 100000)
                kraft3 = (kraft2, 2)
                print("Deine aufgewendete Kraft ist ca.:", kraft3, "kg")
        
            #Rechnung Kilogramm in Newton
            elif wahl == 2:
                kraft2 = kraft1 * (980665 / 100000)
                kraft3 = round(kraft2, 2)
                print("Dein Gewicht hat eine Kraft von ca.:", kraft3, "N")
                
            #Ende der Kraft While-Schleife
            print("")
            if input("Möchtest du nochmal eine Kraft rechnen? (ja/nein): ").lower()!= 'ja':
                break

#Distanzrechner und Beginn der 5. While-Schleife
    elif rechner == 4:
        while True:
            wahl = float(input("Wählen der vorhandenen Längeneinheit (Meile=1 oder km=2): "))
            lae1 = float(input("Wie lang ist deine Strecke?: "))
        
            #Rechnung Meilen in Kilometer
            if wahl == 1:
                lae2 = lae1 * (1609344 / 1000000)
                lae3 = round(lae2, 2)
                print("Deine Distanz sind ca.:", lae3, "km")
        
            #Rechnung Kilometer in Meilen
            elif wahl == 2:
                lae2 = lae1 * (62137119 / 100000000)
                lae3 = round(lae2, 2)
                print("Deine Distanz ist ca.:", lae3, "Meilen")
                
            #Ende der Distanz While-Schleife
            print("")
            if input("Möchtest du noch eine Länge rechnen? (ja/nein): ").lower() != 'ja':
                break
    
#Währungsrechner und Beginn der 6. While-Schleife
    elif rechner == 5:
        while True:
            wahl = float(input("Wählen der vorhandenen Währung (Stand 20.08.2024) (Euro=1 oder Yen=2): "))
            wae1 = float(input("Geben Sie den Betrag an: "))
        
            #Rechnung Euro in Yen
            if wahl == 1:
                wae2 = wae1 * (1622 / 10)
                wae3 = round(wae2, 2)
                print("Dein Betrag ist ca.:", wae3, "yen")
        
            #Rechnung Yen in Euro
            elif wahl == 2:
               wae2 = wae1 * (62 / 10000)
               wae3 = round(wae2, 2)
               print("Dein Betrag ist ca.:", wae3, "€")
               
            #Ende der Währungs While-Schleife
            print("")
            if input("Möchtest du noch eine Währung rechnen? (ja/nein): ").lower() != 'ja':
                break
    
    #Ende der Menü While-Schleife
    if input("Möchtest du einen anderen Rechner auswählen? (ja/nein): ").lower() != 'ja':
        break
    
#Programmende
print("")
print ("Das Programm ist beendet")