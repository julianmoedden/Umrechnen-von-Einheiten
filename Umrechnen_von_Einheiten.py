#Fahrenheit und Celsius
#wahl = float(input("Wählen der Temperatureinheit (C=1 oder F=2): "))
#temp1 = float(input("Gib die Temperatur ein: "))

#if wahl == 1:
 #   temp2 = temp1 * 18 / 10 + 32
  #  print("Deine Temperatur in Fahrenheit ist:", temp2, "°F")

#elif wahl == 2:
   # temp2 = (temp1 - 32) * 5 / 9
    #print("Deine Temperatur in Celsius ist:", temp2, "°C")
    
#km/h und m/s
#wahl = float(input("Wählen der Geschwindigkeitseinheit (km/h=1 oder m/s=2): "))
#ges1 = float(input("Gib die Geschwindigkeit ein: "))

#if wahl == 1:
  #  ges2 = ges1 / (36 / 10) 
   # print("Deine Geschwindigkeit in m/s ist:", ges2, "m/s")
    
#elif wahl == 2:
 #   ges2 = ges1 * (36 / 10)
  #  print("Deine Geschwindigkeit in km/h ist:", ges2, "km/h")

#Newton und Kilogramm
#wahl = float(input("Wählen der Einheit (Newton=1 oder kg=2): "))
#kraft1 = float(input("Gib den Wert ein: "))

#if wahl == 1:
 #   kraft2 = kraft1 / (980665 / 100000)
  #  print("Deine aufgewendete Kraft ist ca.:", kraft2, "kg")
    
#elif wahl == 2:
 #   kraft2 = kraft1 * (980665 / 100000)
  #  print("Dein Gewicht hat eine Kraft von ca.:", kraft2, "N")

#Meile und Kilometer
#wahl = float(input("Wählen der Längeneinheit (Meile=1 oder km=2): "))
#lae1 = float(input("Wie lang ist deine Strecke?: "))

#if wahl == 1:
 #   lae2 = lae1 * (1609344/1000000)
  #  print("Deine Distanz sind ca.:", lae2, "km")
    
#elif wahl == 2:
 #   lae2 = lae1 * (62137119/100000000)
  #  print("Deine Distanz ist ca.:", lae2, "Meilen")
    
#Euro und Yen
wahl = float(input("Wählen der Währung(Euro=1 oder Yen=2: "))
wae1 = float(input("Geben Sie den Betrag an: "))

if wahl == 1:
    wae2 = wae1 * (1622/10)
    print("Dein Betrag ist ca.:", wae2, "yen")
    
elif wahl == 2:
    wae2 = wae1 * (62 / 10000)
    print("Dein Betrag ist ca.:", wae2, "€")