#Auswahl Fahrenheit Celsius
wahl = float(input("Wählen der Temperatureinheit(C=1 oder F=2): "))
temp1 = float(input("Gib die Temperatur ein: "))

if wahl == 1:
    temp2 = temp1 * 18 / 10 + 32
    print("Deine Temperatur in Fahrenheit ist:", temp2, "°F")

elif wahl == 2:
    temp2 = (temp1 - 32) * 5 / 9
    print("Deine Temperatur in Celsius ist:", temp2, "°C")