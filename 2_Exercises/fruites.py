fruites = [{'fruita': 'platan', 'preu': 2.35},
           {'fruita': 'poma', 'preu': 2.80},
           {'fruita': 'pera', 'preu': 1.85},
           {'fruita': 'taronja', 'preu': 1.70}
          ]

fruita_sel = input('Quina fruita vols? ').lower()
num_kilos = int(input('Quants kilos? '))

found = False
for fruita in fruites:
    if fruita['fruita'] == fruita_sel:
        preu = fruita['preu']*num_kilos
        print('El preu és igual a',preu,'€')
        found = True
        break

if not found:
    print('La fruita seleccionada no hi és a la llista')
