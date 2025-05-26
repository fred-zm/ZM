def anweisung(farbe):
    farbe = farbe.strip().lower()
    if farbe == 'rot':
        print("Stehen bleiben!")
    elif farbe == 'gelb':
        print("Bereit machen!")
    elif farbe == 'grün':
        print("Gehen!")
    else:
        print("Unbekannte Farbe")

farbe = input("Gib die aktuelle Farbe der Ampel ein: ")
anweisung(farbe)