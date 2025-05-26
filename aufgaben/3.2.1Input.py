class Zimmer:
    def __init__(self):
        self.groesse = input("Größe:")
        #9 Weitere Eigenschaften einfügen

    def print_data(self):
        print("Das Zimmer ist", self.groesse, "groß.")
        #9 Weitere Eigenschaften einfügen

zimmer = Zimmer()
zimmer.print_data()
