# Nom\tCognom\tTelefon\tCiutat

# arguments> python agenda.py [afegir|llegir|tots] [informacio]
#
# exemples: python agenda.py afegir Eduard Valera 678990011 Barcelona
#           python agenda.py llegir Eduard Valera --> Retornar telefon i ciutat
#           python agenda.py tots --> Retornar tots els contactes

import sys

def afegir_contacte(dades):
  # Mode 'a' per fer append al nou fitxer
  if len(dades) != 4
  with open('', 'a') as f:
  for i in dades:
   
 #  
def llegir_contacte():
def llegir_tots():

if sys.argv[1] == "afegir":
  afegir_contacte(sys.argv[2:])

elif sys.argv[1] == "llegir":
  llegir_contacte(sys.argv[])

elif sys.argv[1] == "tots":
  llegir_tots()

else:
  print ("Opcio incorrecta:", sys.argv[1])