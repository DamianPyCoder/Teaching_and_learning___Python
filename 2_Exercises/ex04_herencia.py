class Persona():
    def __init__(self, nom, cognoms, sexe, edat, pes, altura):
        self.nom = nom
        self.cognoms = cognoms
        if sexe == 'M':
            self.sexe = 'M'
        else:
            self.sexe = 'H'
        self.sexe = sexe
        self.edat = edat
        self.pes = pes
        self.altura = altura

    def esMajorEdat(self):
        if self.edat >= 18:
            return True
        else:
            return False

    def calcularIMC(self):
        pesActual = self.pes / self.altura ** 2
        if pesActual >= 20 and pesActual <= 25:
            return 'PES_IDEAL'
        elif pesActual < 20:
            return 'INFRAPES'
        else:
            return 'SOBREPES'

    def saludar(self):
        print(f"Hola! Soc en {self.nom}.")

class Professsor(Persona):
    def __init__(self, nom, cognoms, sexe, edat, pes, altura, assignatura):
        super().__init__(nom, cognoms, sexe, edat, pes, altura)
        self.assignatura = assignatura
    
    def acomiadar(self):
        print(f"Adeu {self.nom} {self.cognoms}. La teva assignatura és {self.assignatura}")


nom = input('Introdueix el nom: ')
cognoms = input('Introdueix els cognoms: ')
sexe = input('Introdueix el sexe (H o M): ')
edat = int(input('Introdueix l\'edat: ' ))
pes = float(input('Introdueix el pes: ' ))
altura = float(input('Introdueix l\'altura: ' ))
assignatura = input("Introdueix l\'assignatura: ")

teacher1 = Professsor(nom, cognoms, sexe, edat, pes, altura, assignatura)

teacher1.saludar()
teacher1.acomiadar()
