class Frage:
    def __init__(self, frage, antworten, loesung):
        self.frage = frage
        self.antworten = antworten
        self.loesung = loesung
    
    def abfragen(self):
        print(self.frage)
        for index, antwort in enumerate(self.antworten):
            print('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[index] + ') ' + antwort, end=' ')
        auswahl = input().strip().lower()
        if auswahl == self.antworten[self.loesung].lower():
            return True
        if auswahl == str(self.loesung + 1):
            return True
        if auswahl == 'abcdefghijklmnopqrstuvwxyz'[self.loesung]:
            return True
        return False


frage1 = Frage("Wer ist President Chinas?", ["Mao Mao", "Dao Chi", "Xi Jinping", "Sun Tzu"], 2)

if frage1.abfragen():
    print("Das war richtig.")
else:
    print("Das war leider falsch.")