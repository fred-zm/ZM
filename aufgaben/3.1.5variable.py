class Fahrzeug:
    def __init__(self, farbe, groesse, tueren, kraftstoff, klasse, var6, var7, var8, var9, var10):
        self.farbe = farbe
        self.groesse = groesse
        self.tueren = tueren
        self.kraftstoff = kraftstoff
        self.klasse = klasse
        self.var6 = var6
        self.var7 = var7
        self.var8 = var8
        self.var9 = var9
        self.var10 = var10
        
    
    def fahrzeug_print(self):
        print("Farbe: ", self.farbe)
        print("Größe: ", self.groesse)
        print("Türen: ", self.tueren)
        print("Kraftstoff: ", self.kraftstoff)
        print("Fahrzeugklasse: ", self.klasse) 

lkw = Fahrzeug('blau', 'groß', '3Türen', 'Diesel', 'Lkw', 1, 2, 3, 4, 5)
lkw.fahrzeug_print()
print()
tmp = lkw.farbe
lkw.farbe = lkw.groesse
lkw.groesse = tmp
lkw.fahrzeug_print()
