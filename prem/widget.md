---
hide:
  - navigation
  - toc
  - footer
---

# CREATION DE WIDGET PAR LA BIBLIOTHEQUE TKINTER

Il s'agit dans ce travail d'utiliser les constructeurs et les méthodes de la bibliothèques ```Tkinter``` afin de réaliser des interfaces graphiques (bouton, champ de saisie, échelle, label, fenêtre,...) et tout cela dans le langage ```python```.

L'apprentissage se résume à l'élaboration de la fenêtre ci-dessous qui donne la couleur obtenue dans le mélange des trois composantes ```RGB```(Red Green Blue):

<center>
![fenetre_a_realiser](<img/interface_couleur.png>)
</center>

!!! example "Étape1: Construction de la fenêtre mère"
    L'idée principale est de construire un conteneur principal, l'élément **mère** qui va contenir d'autres éléments **filles**. Le code Python est donné ci-après.

``` python
from tkinter import *

###################################################
fen = Tk()
fen.title( "Visualisation des couleurs")
fen.resizable(False, False)
fen.iconbitmap('logoNSIsite.ico')
###################################################
######################CONSTRUCTEURS ################



###################################################
fen.mainloop()
```

Le constructeur principal est l'élément ```fen```: on lui applique des méthodes explicites qui changent son titre, la possibilité de redimensionner et l'icône de la fenêtre principale.Il y a d'autres possibilités que je vous laisse découvrir en toute autonomie...

!!! note "À faire: personnaliser sa fenêtre"
    1. Recopier le code précédent que vous enregistrez sous le nom ```interface_couleur.py``` dans un dossier ```TP_interface_graphique```
    2. Personnalisez votre fenêtre en changeant le titre et en trouvant un logo qui vous correspond. Attention ce logo doit être un fichier ```.ico``` et doit être situé à la racine de votre projet(ou alors dans un dossier dédié...)!

Il existe de nombreuses façons de convertir une image au format ```png``` vers le format ```ico```.

!!! example "Étape2: ajouter les éléments filles"
    La fenêtre que nous devons réaliser contient plusieurs **widgets** (composants graphiques): un **bouton** pour valider, trois **champs de saisies** pour le choix des couleurs, et une zone de dessin, appelée **canvas** dont la couleur d'arrière plan (le **bg**) correspond aux choix faits dans les zones de saisies et une zone de texte, le **label** contenant le titre général de la fenêtre.

On appelle les **constructeurs** correspondant pour la conception de ces widgets en les stockant dans des variables aux noms explicites. Les constructeurs sont par exemple ```Label,Button``` ou ```Entry```...

!!! note "À faire: Ajouter les widgets"
    1. Ajouter le code python suivant au programme précédent à l'endroit indiqué.
    2. Changer la couleur d'arrière plan du canvas
    3. On peut aussi exprimer la couleur en hexadécimal. Essayez l'instruction ```bg= '#FF00FF'``` puis une autre de votre choix.

```python
######################CONSTRUCTEURS ###########################
text1 = Label(fen, text =" Choix des couleurs", font="arial 30")
text1.grid(row = 0, column = 0, columnspan = 5)
btn1 = Button(fen, text = "visualiser", width = 10, command = fen.destroy)
btn1.grid(row = 1, column = 0, columnspan = 5)
rou = Entry(fen)
rou.grid(row = 4, column = 2)
ver = Entry(fen)
ver.grid(row = 4, column = 3)
bleu = Entry(fen)
bleu.grid(row = 4, column = 4)
zone_couleur = Canvas(fen, bg = 'white')
zone_couleur.grid(row = 5, column = 0, columnspan = 5)
################################################################
```

Vous remarquerez qu'à chaque fois qu'un élément est créé il est **positionné** par la méthode **grid** dans une grille virtuelle contenant des lignes et des colonnes. Par exemple, le ```Label``` nommé ```text1``` est positionné dans la **première** ligne (```row = 0 ```), dans la première **colonne**(``` column = 0```) et s'**étend** sur 5 colonnes(```columnspan = 5```).

Il existe plusieurs gestionnaires de positionnement mais nous utiliserons en général la méthode ```grid```.


!!! warning " Attention!"
    Si vous oubliez de positionner un widget, il ne sera pas pris en compte.

  

Tous les **widgets** créés ont des **attributs**: par exemple l'élément ```btn1``` est situé dans le conteneur parent ```fen```, possède un attribut ```text``` de type chaîne de caractères, correspondant au texte affiché sur le bouton. L'attribut ```command``` désigne l'action à réaliser lorsque on appuie sur le bouton. Ici, l'appui sur le bouton détruit l'élément parent ```fen``` et donc aussi, tous ses fils et filles... donc tous les autres widgets. On changera cette fonction plus tard dans ce travail pour que l'action du bouton colore la partie ```canvas```.

!!! example "Étape3: les variables globales"
    Une variable **globale** est une variable qui peut être appelée partout dans le programme. Nous souhaiterions ici créer **trois variables** qui seront associer à la valeur saisie dans les champs prévus à cet effet. 

Dans ```tkinter```, les variables globales sont les **variables de contrôle**(voir [ici](http://tkinter.fdex.eu/doc/ctrvar.html)): elles sont associées à la valeur ou au texte saisie dans les widgets qui le permettent!

!!! note "À faire: Ajouter des variables de contrôles"
    1. Ajouter le code ```python``` suivant juste après l'instruction ```fen.iconbitmap```.
    ```python
    r = StringVar(value = '12')
    ```
    2. Modifier le constructeur ```Entry``` nommé ```rou``` en lui ajoutant l'attribut ```textvariable = r ``` comme ceci:
    ```python
    rou = Entry(fen, textvariable = r)
    ```

Quelques explications! La variable ```r``` est une variable globale de stype ```string```, initialisée à 12, associée à la valeur saisie dans l'entrée ```rou```. 

Si vous proposez une valeur dans cette entrée elle sera alors affectée à la valeur de ```r```. Cette association est possible grâce à l'attribut ```textvariable``` du constructeur ```rou``` auquel on a associé la variable ```r```.

!!! note "À faire: Compléter les variables de contrôles"
    1. Créer les variables de contrôles ```v``` et ```b```, de type chaîne de caractère, initialisée respectivement à 200 et 100.
    2. Ajouter les attributs ```textvariable``` aux entrées ```ver``` et ```bleu``` en leur affectant les variables précédemment définies.

!!! example "Étape4: Colorer le canvas"
    La prochaine étape consiste à colorer le background du canvas ```zone_couleur``` avec la couleur définie à l'aide des valeurs des variables ```r,v``` et ```b```.

C'est l'appui sur le bouton qui déclenchera l'action de coloriage.

!!! warning "Les couleurs acceptées"
    L'attribut ```bg``` d'un canvas n'accepte des couleurs que sous deux formes:

    - sous forme de nom comme ``` 'white' , 'red', 'blue', ...```
    - sous forme hexadécimale ```#FF00AA``` par exemple

Mais problème! Les couleurs saisies sont décimales. Il faut donc construire un outil qui prend en entrée un triplet comme ```(12,200,100)``` et le transforme en ```'#0CC864'```. 

Nous allons pour cela créer la fonction ```rgb_10to16``` qui prend en paramètre un tuple de trois couleurs et retourne une chaîne de caractères formatée et répondant à notre besoin.

!!! note "À faire: Ajouter une fonction"
    1. Ajouter le code python suivant après la variable b:
    ``` python
    ############# ACTIONS  ############################
    def rgb_10to16(t):
        return "#%.2x" %t[0] + "%.2x" %t[1] + "%.2x" %t[2]
    ```
    2. Rappelez le nom de l'opération ```+``` pour les chaînes de caractères.
    3. Expliquer le rôle de l'instruction ```.2x```
    4. Justifier que cette fonction retourne une chaîne de caractères.
    5. Testez votre fonction en console sur des entrées simples comme ```(255, 0, 0)```


À ce stade, il reste l'étape qui consiste à colorer le canvas à l'appui sur le bouton ```visualiser```...

!!! example "Étape5: Création de la fonction de coloriage"
    Nous allons créer la fonction ```colorer``` qui:

    - récupère la valeur décimale des trois entrées
    - convertit le triplet en chaîne hexadécimale
    - change la couleur du background du canvas en conséquence.

!!! note " À faire: Compléter le code "
    1. Ajouter la fonction suivante après la précédente:
    ```python
    def colorer():
        rouge = int(r.get())
        vert = int(v.get())
        bleu = int(b.get())
        zone_couleur['bg'] = rgb_10to16((rouge, vert, bleu))
    ```
    2. Changer la valeur de l'attribut ```command``` du bouton ```btn1``` en lui donnant la valeur ```colorer```(sans parenthèses...)
    2. Exécuter le code, tout devrait bien fonctionner!

Pour récupérer la valeur d'une variable globale (```r``` par exemple), on lui applique la méthode ```.get()```. Ainsi l'instruction ```r.get()``` contient la valeur de ```r``` mais prudence : cette instruction retourne une chaîne de caractères. On comprend mieux alors l'instruction ```int``` dans ```int(r.get())``` qui transforme la chaîne de caractères en entier...

Enfin, l'instruction ```zone_couleur['bg'] = rgb_10to16((rouge, vert, bleu))``` redéfinit clairement l'attribut ```'bg'``` de ```zone_couleur```! 

!!! info "Pour information"
    Nous n'avons pas justifier l'instruction ```fen.mainloop()```: elle rend l'objet ```fen``` sensible aux événements extérieurs comme l'appui d'un clic de souris ou du clavier. Elle écoute en continue ce qui se passe autour de ses constructeurs. Dommage que cette fonction n'existe pas chez nos élèves 😊!

!!! note " À faire:utiliser une échelle "
    Au lieu de saisir les valeurs, on souhaite utiliser des échelles qui permettent à l'aide de curseur de choisir la valeur de la composante de rouge, de vert ou de bleu(voir ci-dessous...).

    Documentez-vous par exemple [ici](http://tkinter.fdex.eu/doc/scw.html) et remplacez les entrées par trois échelles.

<center>
![fenetre_a_realiser](<img/interface_couleur_scale.png>)
</center>