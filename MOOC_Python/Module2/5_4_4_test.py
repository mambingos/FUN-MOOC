def lecture(invite):
  """Lit et renvoie une liste d'entiers.
   Les données peuvent être sur plusieurs lignes.
  """

  res = []
  x = input(invite)
  while x != '':
     decoupe = x.split()
       # liste des parties de x séparées par une/des espace(s) ou tab
     for elem in decoupe:
        res.append(int(elem))
     x = input()
  return res

# utilisation de la fonction lecture
print(lecture("liste d'entiers terminée par une ligne vide : "))