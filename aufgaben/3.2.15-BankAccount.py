class BankAccount:
    def __init__(self, kontoinhaber:str, kontostand:float=0.0, ueberziehungsrahmen:float=-100.0):
        self.kontoinhaber = kontoinhaber
        self.kontostand = kontostand
        if ueberziehungsrahmen > 0.0:
            print("Warnung: Überziehungsrahmen ist positiv.")
        self.ueberziehungsrahmen = ueberziehungsrahmen

    def einzahlen(self, betrag:float):
        #Erhöht den Kontostand um den übergebenen Betrag.
        if betrag < 0.0:
            raise
        self.kontostand += betrag
        

    def abheben(self, betrag:float): 
         #Verringert den Kontostand um den übergebenen Betrag, aber nur, wenn genug Geld vorhanden ist. Andernfalls soll eine Warnung ausgegeben werden.
        if betrag < 0.0:
            raise
        if self.kontostand - betrag <= self.ueberziehungsrahmen:
            print("Warnung: Abhebebetrag zu hoch!")
            return
        self.kontostand -= betrag
       
    def  zinsen_berechnen(self, zinssatz:float):
        #Der aktuelle Kontostand wird mit dem übergebenen Zinssatz (in %) verzinst, aber nur wenn der Kontostand positiv ist.
        if self.kontostand > 0.0:
            self.kontostand += self.kontostand * (zinssatz/100)

    def zeige_kontostand(self): 
        #Gibt den aktuellen Kontostand aus.
        print(f"Kontostand: {self.kontostand}€")
        
    def __str__(self):
        return f"Konto von {self.kontoinhaber} - Kontostand: {self.kontostand} €"

def main():
    konto1 = BankAccount("Hans Peter")
    konto1.einzahlen(55)
    konto1.zinsen_berechnen(15)
    konto1.zeige_kontostand()
    konto1.abheben(10)
    print(konto1)
    konto1.abheben(57)
    print(konto1)

if __name__ == "__main__":
    main()
        