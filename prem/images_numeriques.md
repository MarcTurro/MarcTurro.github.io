---
hide:
  - navigation
  - toc
  - footer
---


# Travail sur les images numériques

## Genèse
Les images numériques sont comme toutes données informatiques, des objets définis selon une certaine norme. Par exemple, les images au format **png**(portable network graphic) sont définis par :
<center>

- leur signature: 8 octets
- le chunk ```IHDR``` pour l'en-tête : 25 octets
- le chunk ```IDAT``` pour les données : poids variable selon l'image
- le chunk ```IEND``` pour la fin du fichier : 12 octets
</center>
Donc une image dans ce format pèse au moins 45 octets... 

Le chunk IHDR donne entre autres les informations sur la largeur, la hauteur de l'image. Nous y reviendrons plus tard en disséquant une image pour explorer ses entrailles ...

Rappelons que **l'extension** du fichier précise notamment sa nature. Le cas du format **.png** est important: standard développé par le W3C( comme Html, Css ou Javascript...), il est particulièrement adapté pour publier des images sur des sites internet. Il trouve ses origines dans la volonté de concurrencer le fichier compressé **.gif**, dont le propriétaire réclamait les droits d'utilisations.

!!! caution "le format jpeg"
    Attention! les fichiers **.jpeg** ne sont pas à proprement dit des fichiers images mais des fichiers **compressés** d'une image. Souvent, on commet une confusion, pas bien grave au final!

Une image Portable Network Graphics (PNG) est un format ouvert, on peut donc explorer son contenu!
!!!NOTE "À faire"      
    1. Récupérer l'image ```firefox.png``` ( <a href="../img/Firefox.png"   download="Firefox.png">Télécharger l'image</a>).
    2. Ouvrez l'image avec les routines Python habituelles, en mode lecture binaire et visualisez l'entête du fichier(le **programme** est donné juste après).
    3. Déterminer le nombre d'octets constituants ce fichier. Le comparer à la valeur obtenue par un clic droit sur l'image puis propriétés.
    4. Trouvez d'autres fichiers **.png** et vérifier qu'ils ont tous la même signature(ils commencent tous par la même série d'octets qui est leur signature...).Affichez la liste des octets dans votre console.Donnez cette signature.
  
``` py
#Rappel sur les ouvertures en lecture ou ecritures de fichiers
fichier_src = open("........","rb")#Completer avec le chemin relatif vers l'image
#l'ouverture en mode rb ouvre le fichier en binaire (octet...)
listeOctet = [elt for elt in fichier_src.read()]
print(len(listeOctet))#affiche la longueur de la liste, le nombre d'octets en fait!
print(listeOctet[:100])# affiche seulement les 100 premiers octets sinon...
fichier_src.close()
```
En général, les images numériques sont des **images matricielles**, par opposition aux images **vectorielles** définies par des courbes mathématiques. Les fichiers ```.svg``` développés par le W3C, sont des images vectorielles très adaptées à la construction de logo, comme celui de Firefox, décomposable en éléments géométriques.

!!!NOTE "À faire" 
    1. Observez le logo Firefox défini sous ```.svg``` à cette [adresse](https://upload.wikimedia.org/wikipedia/commons/2/28/Firefox_logo%2C_2017.svg?uselang=fr) et trouvez sa description ```.svg``` (clic droit-> code source de la page).
    2. Zoomez(touche ```Crtl + molette```).
    3. Ouvrez le fichier [**firefox.png**](../img/Firefox.png) dans le navigateur Firefox(cliquez sur le lien précédent...). Zoomez et comparez avec la manipulation précédente.
    4. Quelle différence entre une image matricielle et vectorielle?

## Image matricielle
!!!TIP "À retenir!"
    Une photo, une image est donc définie généralement par un tableau de valeurs, appelée **matrice**, définissant ainsi le niveau d'intensité de chaque pixel de cette image. On retrouvera en général:

    * des images en **niveaux de gris** en mode ```L```: lorsque les couleurs sont codées sur 8 bits, c'est-à-dire 1 octet, il y a donc 256 niveaux de quantifications possibles allant du 0(noir) au blanc(255).
    * des images **couleurs** codées en mode ```RGB``` pour Red Green Blue: chaque couleur est codée sur 8 bits soit un octet.
    * des images **couleurs** avec **un canal alpha** en mode ```RGBA``` permettant de contrôler la transparence d'une image, notamment lorsque l'on souhaite superposer l'une sur l'autre.

Dans une image matricielle contenant des pixels, le premier pixel est celui en haut à gauche et le dernier, celui en bas à droite. Puis on parcourt une image ligne par ligne, de gauche à droite. Ceci est important pour comprendre comment on peut lire ou écrire sur une image!

On entend par:  
!!!abstract "À savoir!"
    1. **lire un pixel**, donner la valeur de sa couleur qui se présente sous différentes formes (entier, triplet ou quadruplet d'entiers) selon le mode de représentation (L, RBG ou RGBA)
    2. **écrire un pixel**, définir sa couleur par la donnée d'un entier, d'un triplet ou un quadruplet selon le mode de représentation... 

!!!NOTE "À faire" 
    Dans une image couleur où chaque couleur est codée sur un octet, combien de couleurs différentes peut-on obtenir?

## Enfin du Python!

Cette section propose de manipuler des images numériques à l'aide d'un bibliothèque Python appelée **PIL**.

!!!NOTE "À faire" 
    Installer la bibliothèque PILLOW dans Thonny(lors de l'import il faudra l'appeler sous sous ancien nom PIL...).

Il s'agit de traduire en Python l'idée de:

!!!TIP "Les routines !"
    1. ouvrir un fichier image ```img``` sur lequel on travaille;
    2. déterminer les propriétés de cette image(```mode,size,format```);
    3. créer une nouvelle image;
    4. lire et écrire sur une image (attention on lit dans l'une on écrit dans l'autre!)
    5. montrer ou enregistrer l'image obtenue.

Pour illustrer les commandes python répondant à ces besoins, nous allons utiliser la photo ```puppy.png``` ( <a href="img/puppy.png"   download="puppy.png">Télécharger ici</a>).
**Attention** tous les programmes doivent avoir en en-tête, l'import des bibliothèques:

``` py
from PIL import Image
```

## Ouvrir une image et lire des informations

``` py 
from PIL import Image
#Ouverture de l'image existante, le chemin relatif doit être donné à partir de votre fichier!
im = Image.open("Images\puppy.png")#pour ma part je mets les images dans un dossier Images
#On peut connaître les informations suivantes
print(im.mode,im.size,im.format)
im.close()
```

L'objet ```im``` n'est pas une image mais un objet **tampon** sur lequel nous travaillerons avant de le fermer.
## Déterminer les caractéristiques de l'image
Une image possède toujours une taille, un format et un mode de représentation (niveaux de gris, couleurs avec alpha éventuel).
!!!NOTE "À faire" 
    Quelles sont les caractéristiques de l'image ```puppy.png```(mode, taille, format)?

## Création d'une nouvelle image

``` py
from PIL import Image
#Ouverture d'une nouvelle image
IM = Image.new('L', (750,200))
IM.save("Images\img_new1.png")#pour créer l'image dans le dossier Images...
IM.close()
```

!!!NOTE "À faire" 
    Donner le mode et la taille de l'image créée précédemment

## Lire la valeur d'intensité d'un pixel

``` py
from PIL import Image
#Ouverture de l'image existante
#Le chemin relatif doit être donné
im = Image.open("Images\puppy.png")
pix = im.getpixel((20, 30))
print(pix)
im.close()
```

**Attention**, la méthode ```getpixel``` prend en paramètre un couple correspondant aux coordonnées ```(colonne, ligne)``` du pixel dans l'image: dans l'exemple, 20 ième colonne et 30ième ligne(il faut bien sûr s'assurer que ce pixel existe...) . Donc on ne tape pas ```im.getpixel(20,30)``` mais bien ```im.getpixel((20,30))```

!!!NOTE "À faire" 
    En s'utilisant le code précédent, 

    1. donner l'intensité des pixels $(105,42)$ de l'image ```puppy.png```.
    2. quelles sont les coordonnées du dernier pixel de l'image(en bas à droite).Donnez son intensité

## Écrire l'intensité d'un pixel
On rappelle qu'on entend par écrire un pixel, définir sa valeur d'intensité!
``` py
from PIL import Image
#Ouverture d'une nouvelle image
IM = Image.new('L', (750,200))
IM.putpixel((425,100), 150)
IM.save("Images\img_new2.png")
IM.close()
```
La méthode ```putpixel```s'applique à l'objet ```IM``` et prend en paramètres l'endroit où l'on veut écrire ```(c,l)```(425 et 100 dans notre exemple) et la valeur d'intensité ```p```(150 dans l'exemple). Attention dans le cas d'une image couleur l'intensité est un triplet ```(r,g,b)``` voire ```(r,g,b,a)```. 

!!! info "Par défaut..."
    Lorsque vous créez une image, tous les pixels sont noirs par défaut. Donc à 0 sur tous les canaux!

!!!NOTE "À faire" 
    1. Créez une image de largeur 500 et de hauteur 100, où tous les pixels de la ligne 50 sont rouges, les autres restant noirs...
    2. Créez une image de largeur 500 et de hauteur 100, où tous les pixels de la colonne 250 sont rouges, les autres restant noirs...
    3. Créez une image de largeur 500 et de hauteur 500, où tous les pixels des diagonales sont rouges, les autres restant noirs...


## Parcourir une image pixel par pixel
Pour parcourir une image pixel par pixel, on va utiliser une double boucle: l'une pour parcourir les lignes, l'autre  pour parcourir les colonnes.


!!!TIP "Algorithme à suivre"

    1. ouvre une image en lecture
    2. crée une nouvelle image de caractéristiques identiques
    3. parcoure et lit la valeur d'intensité de chaque pixel de l'image initiale
    4. parcoure et écris au même endroit sur l'image finale la valeur capturée à laquelle on ajoute 100 (on travaille modulo 256 pour rester dans la plage $[0;255]$).
    5. on enregistre l'image ainsi créée.

L'implémentation de l'algorithme précédent donne en Python, le programme suivant:
``` py
from PIL import Image
#Ouverture de l'image
#Le chemin relatif doit être donné
imInit = Image.open("Images\puppy.png")
#Ouverture d'une nouvelle image
#Même mode et taille que l'image déjà ouverte
ImFin = Image.new(imInit.mode, imInit.size)
#La double boucle permet de parcourir l'image de haut en bas de gauche à droite 
for l in range(imInit.size[1]):#l comme ligne
    for c in range(imInit.size[0]):#c comme colone
        pix = imInit.getpixel((c,l))# getpixel capture la valeur de couleur du pixel (x,y)
        #on fait un get sur im: c'est une lecture!
        ImFin.putpixel((c,l), (pix + 100)%256)#putpixel colore le pixel (x,y) de l'image IM avec la valeur de (pix + 100)%256
        #on fait donc une écriture sur Im.
ImFin.show()
ImFin.save("Images\ImageTranslate100.png")
imInit.close()
ImFin.close()
```
Quelques informations sur le programme précédent:

- ```imInit``` est un objet tampon de l'image initiale;
- ```imInit.size``` renvoie donc la taille de l'image de départ sous le forme d'un tuple
- ```imInit.size[0]``` est donc le premier élément de ```imInit.size```, soit la largeur de l'image. Et ```imInit.size[1]``` donne donc la hauteur. Et ```imInit.size[2]``` n'existe pas !
- Donc l'instruction ```ImFin = Image.new(imInit.mode, imInit.size)``` construit une nouvelle image de **même** mode et taille que celle qui a été ouverte.
- ```c``` est la variable qui prend ses valeurs de 0 à ```imInit.size[0] - 1``` correspondant au numéro de chaque colonne de l'image
- ```l``` est la variable qui prend ses valeurs de 0 à ```imInit.size[1] - 1``` correspondant au numéro de chaque ligne de l'image

!!!NOTE "À faire" 
    Construire de la même façon les images translatées de 10 pixels et de 255 pixels. Pensez à changer le nom de sauvegarde sinon vous écraserez les fichiers précédemment construits.

# Le coin des exercices
En n'utilisant que les routines précédentes (il y  a des méthodes de la bibliothèque Pil qui permettent de réaliser directement les transformations demandées...), réalisez les exercices suivants.
!!!NOTE "À faire" 
    1. Créer une image en niveaux de gris de dimension 500 sur 100 pixels où chaque pixel a une intensité égale à un nombre aléatoire entre 0  et 255. On sauvegardera sous le nom ```hasard.png``` cette image.
    2. Créer une image en couleur de dimension 500 sur 100 pixels où chaque pixel a une intensité de rouge, de vert et de bleu est égale à un nombre aléatoire entre 0  et 255. On sauvegardera cette image sous le nom ```hasardcouleur.png``` .

!!!NOTE "À faire"
    Créer l'image ```puppynegative.png``` obtenu à partir de l'image ```puppy.png``` en transformant le pixel ```p```en le pixel ```255 - p```.

!!!NOTE "À faire"
    Créer une image de dimension 600(width) sur 400(height) pixels qui est le drapeau français.
    
    On sauvegardera cette image sous le nom ```drapeau.png```.


!!!NOTE "À faire"
    Créer une image en niveaux de gris de dimension 500 sur 100 pixels où chaque pixel de ligne de rang pair est blanc et les autres noir. 
    
    On sauvegardera cette image sous le nom ```ligneblanche.png``` .


!!!NOTE "À faire"
    L'image ```Firefox.png``` est une image couleur qui est donc la superposition de trois images: l'une contient les composantes de rouge, l'autre de vert et la dernière de bleu.

    Construire ces trois images que vous sauvegarderez sous le nom ```filtreRougeFirefox.png```,....


!!!NOTE "À faire"
    Construire l'image obtenue par une symétrie verticale. On sauvegardera l'image sous le nom ```puppyV.png```.
    Construire l'image obtenue par une symétrie horizontale.On sauvegardera l'image sous le nom ```puppyH.png```.
    

!!!NOTE "À faire"
    **Effet de seuillage**: L'idée est d'effectuer un seuillage sur l'image en construisant une nouvelle image selon le principe suivant: tous les pixels dont l'intensité est inférieure ou égal à 127 sont transformés en pixel d'intensité 0 et ceux d'intensité strictement supérieur à 127 transformés en pixel d'intensité 1.
    
    On sauvegardera l'image sous le nom ```puppySeuil127.png```.

!!!NOTE "À faire"
    Même exercice que précédemment mais le choix du seuil $s$ est fait par l'utilisateur.
    
    On sauvegardera l'image sous le nom ```puppySeuilS.png```.

!!!NOTE "À faire"
    Même exercice que précédemment mais ```n``` (un entier compris entre 2 et 25) seuils seront créés.

    On sauvegardera l'image sous le nom ```puppyQuantificationN.png```.


!!!NOTE "À faire"
    À l'aide la bibliothèque ```matplotlib```que vous connaissez déjà, construire l'histogramme des intensités de niveaux de gris de l'image ```puppy.png```: en abscisse, on trouve une intensité $i$ de 0 à 255 et en ordonnée le nombre de pixels d'intensité $i$ dans l'image.
