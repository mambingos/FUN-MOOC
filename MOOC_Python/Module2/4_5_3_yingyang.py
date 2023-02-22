""" Auteur: Samuel Mambingo
   date:   07/02/2020
   But:    code avec fonction yin_yang dessiné avec turtle """
import turtle

def yin_yang(rayon, color1='black', color2='white'):
    """ dessine un logo yin-yang de rayon rayon """

    def yang (rayon, couleur1, couleur2):
        """ dessin du yang à l'intérieur du yin (ou vice versa) """
        turtle.pen("black")  # couleur blanche
        turtle.up()  # on ne trace pas ce qui suit
        # déplace la tortue au bon endroit

        turtle.right(90)
        turtle.forward(80)
        turtle.left(90)
        # tracé du disque yang (blanc) interne au yin
        turtle.down()
        turtle.fillcolor(couleur1)
        turtle.begin_fill()
        turtle.circle(-20)
        turtle.end_fill()
        # se replace au centre
        turtle.up()
        turtle.left(90)
        turtle.forward(80)
        turtle.right(90)

        turtle.down()

        pass # code TODO

    def yin(rayon, couleur1, couleur2):
        """ dessine la moitié d'un yin-yang
            utilise la fonction yang """
        turtle.pen("black")  # le tracé et le remplissage seront en noir
        turtle.fillcolor(couleur1)
        turtle.begin_fill()  # la ou les formes suivantes seront remplies
        turtle.circle(-100, 180)  # demi cercle intérieur tournant vers la droite
        turtle.circle(-200, -180)  # demi cercle extérieur, en marche arrière
        turtle.circle(-100, -180)  # demi cercle intérieur qui complète le yin
        turtle.end_fill()  # remplissage

        yang(rayon, couleur2, couleur1)
        pass # code TODO


    #code de yin_yang
    turtle.reset()
    turtle.width(2)
    yin(rayon, color1, color2)
    yin(rayon, color2, color1)
    turtle.hideturtle()
    return

#code principal
yin_yang(200) #réalise le logo de rayon 200
turtle.mainloop()

