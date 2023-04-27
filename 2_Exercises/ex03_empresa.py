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

class Empresa():
    def canJoin (self, persona):
            return persona.edat < 50 and persona.calcularIMC != 'SOBREPES'

emp = Empresa()

persones = [Persona('Pepe','Lopez','H',34,80,1.70), Persona('Juan','Perez','H',55,72,1.74), 
            Persona('Luisa','Romero','M',48,55,1.60), Persona('Ramon','Bilbao','H',25,60,1.80)]

for persona in persones:
    print(persona.nom,'sí' if emp.canJoin(persona) else 'no', 'pot ser','contractat' if persona.sexe == 'H' else 'contractada')

