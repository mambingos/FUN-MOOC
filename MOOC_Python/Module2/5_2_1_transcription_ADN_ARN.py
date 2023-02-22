"""     Auteur:         Samuel MAMBINGO
        Date:           20/02/2022
        But:            Écrire une fonction transcription_arn(brin_codant) qui reçoit une chaîne de caractères en paramètre,
                        correspondant à un brin codant d'ADN, et qui retourne la chaîne de caractère représentant le brin d' ARN correspondant.".
                        Nous rappelons qu'un brin d'ADN peut être modélisé par une chaîne de caractères, dont les caractères sont pris parmi les quatre suivants  :
                        'A'(Adénine), 'C' (Cytosine),'G' (Guanine) et 'T' (Thymine).
                        La transcription en ARN se traduit par le remplacement des nucléotides de Thymine par des nucléotides d'Uracile,
                        que l'on représentera par le caractère 'U'."""

# nom.replace ("T", "U") fait exactement la même chose

def transcription_arn(nom):
    a = list(nom)
    for i in range (len(a)):
        if a[i] == "T":
            a[i] = "U"

    a = "".join(a)

    return a




    return nom.replace("T","U")

print(transcription_arn('TGTCTTACCGATCCAT'))