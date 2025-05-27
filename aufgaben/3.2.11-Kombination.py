print("Füge eine ganze Zahl ein oder 'stop' um zu beenden")
zahlen = []
while True:
    user_input = input("Gib eine ganze Zahl ein: ")
    if user_input.strip().lower() == "stop":
        break
    
    try:
        zahlen.append(int(user_input))
    except:
        print("Ungültige Eingabe!")

if zahlen:
    acc = 0
    max = min = zahlen[0]
    for zahl in zahlen:
        acc += zahl
        if max < zahl:
            max = zahl
        if zahl < min:
            min = zahl
    durchschnitt = acc / len(zahlen)
    print(f"""\
Größte Zahl: {max}
Kleinste Zahl: {min}
Durchschnitt: {round(durchschnitt, 2)}""")

zahlen.sort()   
print(zahlen)