#Auswahl
def main_menu ():
    print("")
    print("Die möglichen Rechner:")
    print("Temperatur      = 1,")
    print("Geschwindigkeit = 2,")
    print("Kraft/Gewicht   = 3,")
    print("Distanz         = 4,")
    print("Währung         = 5.")

while True:
    main_menu()
    print("")
    rechner = float(input("Wähle einen Rechner: "))

#Fahrenheit und Celsius
    if rechner == 1:
        while True:
            wahl = float(input("Wählen der vorhandenen Temperatureinheit (Celsius=1 oder Fahrenheit=2): "))
            temp1 = float(input("Gib die Temperatur ein: "))
        
            if wahl == 1:
                temp2 = temp1 * 18 / 10 + 32
                print("Deine Temperatur in Fahrenheit ist:", temp2, "°F")
        
            elif wahl == 2:
                temp2 = (temp1 - 32) * 5 / 9
                print("Deine Temperatur in Celsius ist:", temp2, "°C")
            print("")
            if input("Möchtest du nochmal eine Temperatur rechnen? (ja/nein): ").lower()!= 'ja':
                break
    
#km/h und m/s
    elif rechner == 2:
        while True:
            wahl = float(input("Wählen der vorhandenen Geschwindigkeitseinheit (km/h=1 oder m/s=2): "))
            ges1 = float(input("Gib die Geschwindigkeit ein: "))
        
            if wahl == 1:
                ges2 = ges1 / (36 / 10)
                print("Deine Geschwindigkeit in m/s ist:", ges2, "m/s")
        
            elif wahl == 2:
                ges2 = ges1 * (36 / 10)
                print("Deine Geschwindigkeit in km/h ist:", ges2, "km/h")
            print ("")
            if input("Möchtest du nochmal eine Geschwindigkeit rechnen? (ja/nein): ").lower() != 'ja':
                break

#Newton und Kilogramm
    elif rechner == 3:
        while True:
            wahl = float(input("Wählen der vorhandenen Einheit (Newton=1 oder kg=2): "))
            kraft1 = float(input("Gib den Wert ein: "))
        
            if wahl == 1:
                kraft2 = kraft1 / (980665 / 100000)
                print("Deine aufgewendete Kraft ist ca.:", kraft2, "kg")
        
            elif wahl == 2:
                kraft2 = kraft1 * (980665 / 100000)
                print("Dein Gewicht hat eine Kraft von ca.:", kraft2, "N")
            print("")
            if input("Möchtest du nochmal eine Kraft rechnen? (ja/nein): ").lower()!= 'ja':
                break

#Meile und Kilometer
    elif rechner == 4:
        while True:
            wahl = float(input("Wählen der vorhandenen Längeneinheit (Meile=1 oder km=2): "))
            lae1 = float(input("Wie lang ist deine Strecke?: "))
        
            if wahl == 1:
                lae2 = lae1 * (1609344 / 1000000)
                print("Deine Distanz sind ca.:", lae2, "km")
        
            elif wahl == 2:
                lae2 = lae1 * (62137119 / 100000000)
                print("Deine Distanz ist ca.:", lae2, "Meilen")
            print("")
            if input("Möchtest du noch eine Länge rechnen? (ja/nein): ").lower() != 'ja':
                break
    
#Euro und Yen
    elif rechner == 5:
        while True:
            wahl = float(input("Wählen der vorhandenen Währung (Stand 20.08.2024) (Euro=1 oder Yen=2): "))
            wae1 = float(input("Geben Sie den Betrag an: "))
        
            if wahl == 1:
                wae2 = wae1 * (1622 / 10)
                print("Dein Betrag ist ca.:", wae2, "yen")
        
            elif wahl == 2:
               wae2 = wae1 * (62 / 10000)
               print("Dein Betrag ist ca.:", wae2, "€")
            print("")
            if input("Möchtest du noch eine Währung rechnen? (ja/nein): ").lower() != 'ja':
                break
    
    if input("Möchtest du einen anderen Rechner auswählen? (ja/nein): ").lower() != 'ja':
        break
    
print("")
print ("Das Programm ist beendet")

#Programmende