"""     Auteur:         Samuel MAMBINGO
        Date:           01/03/2022
        But:            Écrire une fonction store_email(liste_mails) qui reçoit en paramètre une liste d’adresses e-mail et
                        qui renvoie un dictionnaire avec comme clés les domaines des adresses e-mail et comme valeurs les listes d’utilisateurs correspondantes,
                         triées par ordre croissant (UTF-8).."""

def store_email(liste_email):
    d = {}
    for email in liste_email:

        email = str(email).replace("@"," ").split()
        if email[1] not in d:
            d[email[1]] = [email[0]]
        else:
            d[email[1]].append(email[0])
            d[email[1]] = sorted(d[email[1]])


    return d



store_email(["ludo@prof.ur", "andre.colon@stud.ulb",
             "thierry@profs.ulb", "sébastien@prof.ur",
             "eric.ramzi@stud.ur", "bernard@profs.ulb",
             "jean@profs.ulb" ])
print(store_email(['ludo@prof.ur', 'andre.colon@stud.ulb', 'thierry@profs.ulb', 'sébastien@prof.ur', 'eric.ramzi@stud.ur', 'bernard@profs.ulb', 'jean@profs.ulb']))