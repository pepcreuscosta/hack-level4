# Nom\tCognom\tTelefon\tCiutat

# arguments> python agenda.py [afegir|llegir|tots] [informacio]
#
# exemples: python agenda.py afegir Eduard Valera 678990011 Barcelona
#           python agenda.py llegir Eduard Valera --> Retornar telefon i ciutat
#           python agenda.py tots --> Retornar tots els contactes

import sys

def afegir_contacte(dades):
  # Mode 'a' per fer append al nou fitxer
  if len(dades) != 4:
    print ("Error")
    sys.exit(1)

  with open('agenda.txt', 'a') as f:
    for i in dades:
      f.write(i)
      f.write('\t')
    f.write('\n')

def llegir_contacte(contacte):
  if len(contacte) != 2:
    print ("Error")
  with open('agenda.txt', 'r') as f:
    for line in f:
      paraules = line.split('\t')
      if contacte[0] == paraules[0] and contacte[1] == paraules[1]:
          print line.rstrip()
          return line
    print("Error: no es troba el contacte")

def llegir_tots():
  with open('agenda.txt', 'r') as f:
    for line in f:
      print line.rstrip()


if sys.argv[1] == "afegir":
  afegir_contacte(sys.argv[2:])

elif sys.argv[1] == "llegir":
  llegir_contacte(sys.argv[2:4])

elif sys.argv[1] == "tots":
  llegir_tots()

else:
  print ("Opcio incorrecta:", sys.argv[1])
