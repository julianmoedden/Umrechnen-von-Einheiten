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
wahl = float(input("Wählen der Einheit (Newton=1 oder kg=2): "))
kraft1 = float(input("Gib den Wert ein: "))

if wahl == 1:
    kraft2 = kraft1 / (980665 / 100000)
    print("Deine aufgewendete Kraft ist ca.:", kraft2, "kg")
    
elif wahl == 2:
    kraft2 = kraft1 * (980665 / 100000)
    print("Dein Gewicht hat eine Kraft von ca.:", kraft2, "N")
