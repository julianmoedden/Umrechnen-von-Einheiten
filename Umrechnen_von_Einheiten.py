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
wahl = float(input("Wählen der Geschwindigkeitseinheit (km/h=1 oder m/s=2): "))
ges1 = float(input("Gib die Geschwindigkeit ein: "))

if wahl == 1:
    ges2 = ges1 / (36 / 10) 
    print("Deine Geschwindigkeit in m/s ist:", ges2, "m/s")
    
elif wahl == 2:
    ges2 = ges1 * (36 / 10)
    print("Deine Geschwindigkeit in km/h ist:", ges2, "km/h")