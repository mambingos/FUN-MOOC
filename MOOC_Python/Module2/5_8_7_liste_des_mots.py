"""     Auteur:         Samuel MAMBINGO
        Date:           25/02/2022
        But:            Écrire une fonction liste_des_mots qui reçoit en paramètre le nom d’un fichier texte,
                        que la fonction doit ouvrir, et qui renvoie la liste des mots contenus dans le fichier.."""

def liste_des_mots(document):

   res = []
   with open(document, encoding= "utf-8") as file_1:
       l = file_1.read()
       l = l.lower()
       l = l.replace("?"," ").replace("'"," ").replace("\'"," ").replace("\""," ").replace("-"," ").replace("!", " ").replace(","," ").\
           replace(":", " ").replace(";", " ").replace(".", " ").replace("*"," ").replace("=", " ").replace("0"," ").replace("1"," ").\
           replace("2"," ").replace("3"," ").replace("4"," ").replace("5", " ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9", " ").\
           replace("(", " ").replace(")"," ").replace("\n"," ").replace("\t"," ").replace("*", " ")

       l = l.split()
       l.sort()
   for i in range(len(l)):
       if l[i] not in res:
           res.append(l[i])




   return res



print(liste_des_mots("Zola.txt"))
print(liste_des_mots("petit.txt"))