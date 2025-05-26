while True:
    gewicht = input("Gewicht in kg: ").strip()
    if gewicht.isnumeric():
        break
    else:
        print("Bitte gib nur den Zahlenwert des Gewichts in kg ein!")

while True:
    groesse = input("Größe in cm: ")
    if groesse.isnumeric():
        break
    else:
        print("Bitte gib nur den Zahlenwert der Größe in cm ein!")

bmi = round(float(gewicht) / (float(groesse)/100) ** 2, 1)
ausgabe = "Sie haben ein BMI von " + str(bmi) + " und sind damit "
if bmi < 18.5:
    ausgabe = ausgabe + "untergewichtig"
elif bmi < 25:
    ausgabe = ausgabe + "normalgewichtig"
elif bmi < 30:
    ausgabe = ausgabe + "übergewichtig"
else:
    ausgabe = ausgabe + "adipös"

ausgabe = ausgabe + "."
print(ausgabe)