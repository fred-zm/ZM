import random
target_num = int(random.random() * 100 + 1)
versuche = 0
guess = 0
print("Erate die Zahl zwischen 1 und 100")
while guess != target_num:
    try:
        guess = int(input().strip())
    except:
        print("Ungültige Eingabe")
    else:
        versuche += 1
        if guess < target_num:
            print("Zu niedrig, versuch nochmal!")
        if target_num < guess:
            print("Zu hoch, versuch nochmal!")

print(f"Das ist richtig. Du hast {versuche} Versuche gebraucht.")