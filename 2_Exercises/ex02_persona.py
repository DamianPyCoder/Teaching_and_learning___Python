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

persones = []
while True:

    nom = input('Introdueix el nom: ')
    cognoms = input('Introdueix els cognoms: ')
    sexe = input('Introdueix el sexe (H o M): ')
    edat = int(input('Introdueix l\'edat: ' ))
    pes = float(input('Introdueix el pes: ' ))
    altura = float(input('Introdueix l\'altura: ' ))
    persones.append(Persona(nom,cognoms,sexe,edat,pes,altura))

    resposta = input('Vols afegir mes persones? ')
    if resposta[0].lower() == 'n':
        break   

for persona in persones:
    print(persona.nom,'és' if persona.esMajorEdat() else 'no és','major d\'edat i té',persona.calcularIMC())
