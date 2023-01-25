---
hide:
  - navigation
  - toc
  - footer
---

# Faire des graphiques avec Python

Pourquoi faire des graphiques? C'est une habitude pour visualiser une quantité de données:

- en physique, on réalise une expérience et on obtient des données dans un tableau que l'on exploite pour faire un graphique. 
- en maths, pour déterminer la courbe représentative d'une fonction $f$.
- en informatique, pour observer par exemple la répartition des niveaux de gris dans une image en noir et blanc.
- ...

Dans tous les cas, on utilisera la bibliothèque ```matplotlib``` qui offre tout un tas de possibilités pour faire un graphique.

!!! exemple "Niveau d'intensité"
    Expérience faite en première NSI. On prend une photo en noir et blanc (plus précisément en niveau de gris...), celle présentée ci-dessous(```puppy.png```), et on compte les pixels d'intensité 0(noir), d'intensité 1,... et d'intensité 255. On stocke les résultats dans une liste.
    <center>
    ![puppy](<img/puppy.png>)
    </center>
    Le code suivant génère l'histogramme.
    ```py
    # import des bibliothèques nécessaires
    import matplotlib.pyplot as plt # pour les graphiques
    import numpy as np # pour générer des listes (np.arange)
    #liste L obtenue en parcourant tous les pixels de l'image puppy.png 
    # il y a 1 pixel d'intensité 0(totalement noir), il y a 1 pixel d'intensité 1
    # il y a 4 pixel d'intensité 2, il y a 12 pixel d'intensité 3, ... et 366 pixels d'intensité 255(totalement blanc)
    L = [1, 1, 4, 12, 13, 25, 44, 48, 65, 60, 82, 111, 121, 137, 155, 148, 162, 220, 228, 264, 275, 290, 213, 283, 351, 343, 363, 394, 381, 333, 323, 394, 453, 422, 424, 397,
    404, 390, 368, 451, 369, 453, 469, 457, 454, 434, 428, 449, 447, 449, 433, 489, 449, 495, 467, 455, 501, 462, 499, 453, 480, 494, 547, 550, 662, 749, 930, 1119, 1453,
    1281, 1079, 952, 978, 869, 943, 770, 740, 674, 668, 667, 682, 734, 741, 753, 772, 783, 781, 858, 838, 843, 890, 840, 860, 915, 898, 937, 879, 892, 862, 921, 883, 931, 
    895, 944, 993, 996, 1006, 1013, 1071, 1077, 1105, 1056, 995, 961, 948, 958, 953, 930, 920, 950, 1034, 1023, 1108, 1036, 944, 940, 875, 836, 746, 729, 787, 668, 733, 737, 
    718, 721, 681, 644, 676, 642, 656, 589, 540, 596, 583, 596, 562, 532, 536, 560, 536, 505, 484, 465, 500, 469, 529, 602, 621, 675, 755, 789, 801, 1104, 1307, 1299, 1054,
    987, 1086, 1188, 1239, 1320, 1533, 1670, 1679, 1925, 1646, 1444, 1310, 1032, 868, 686, 615, 517, 501, 550, 549, 533, 518, 532, 446, 397, 391, 310, 269, 253, 244, 233,
    198, 205, 222, 209, 210, 308, 382, 336, 295, 264, 225, 215, 193, 177, 207, 198, 205, 222, 206, 261, 193, 224, 213, 238, 219, 219, 229, 251, 210, 181, 176, 207, 202, 
    260, 258, 284, 403, 431, 401, 435, 451, 443, 406, 425, 265, 221, 224, 216, 174, 107, 114, 130, 129, 128, 156, 202, 383, 366]
    

    fig, ax = plt.subplots() #une figure et des axes
    x = [i  for i in range(256)] #génération par compréhension de la liste x = [0,1,2,...,254,255]
    y = L #liste ci-dessus
    ax.bar(x, y, width = 1, color = 'magenta', edgecolor = "red", linewidth = 0.7)
    # fait un histogramme avec en abscisse les valeurs de x et en ordonnée les valeurs de y
    #x et y doivent être de même dimension!!!!
    ax.set(xlim=(0, 255), xticks = np.arange(0, 255, 50),
        ylim=(0, 2000), yticks=np.arange(0, 2000, 200))
    # options qui définissent les graduations des axes
    ax.set_ylabel('Nombre de pixels')
    ax.set_title(f"Histogramme de l'image puppy.png")
    ax.set_xlabel('Intensité de gris')

    plt.show()
    img.close()
    ```

On obtient le joli graphique:
<center>
![histogramme](<img/histo_puppy.png>)
</center>

!!! tip "À retenir"
    Pour tracer un graphique quelconque, il faut en général une liste pour les abscisses et une pour les ordonnées. Attention, ces deux listes doivent avoir le même nombre d'éléments!

!!! exemple "La courbe représentative d'une fonction mathématique"
    Rien de plus simple! Il faut:

    - une fonction $f$ définie sur un intervalle $I$
    - une liste en abscisse
    - une liste en ordonnée
    
    Puis on utilisera la méthode ```.plot``` à la place de ```.bar``` pour obtenir une courbe au lieu d'un histogramme...
        
Par exemple voici le code ```python``` pour construire la courbe représentative des fonctions $\cos$ et $\sin$ sur l'intervalle $I=[0, 2\pi]$.

!!! exemple "Fonctions trigonométriques"
    ```py
    ####### import bibliothèques ###############
    import numpy as np
    import math
    import matplotlib.pyplot as plt
    ####### une figure et des axes ############
    fig, ax = plt.subplots()
    ###### valeurs extrêmes en X et Y #########
    x_min = 0
    x_max = 2*np.pi
    y_min = -1 #valeur minimale du cos et sin
    y_max = 1 #valeur maximale du cos et sin
    ##### fonction cos et sin #################
    def lesinus(x):
        return np.sin(x)
    def lecosinus(x):
        return np.cos(x)
    ##### génération de la liste des abscisses
    X = np.arange(start = x_min, stop = x_max, step = 0.25)
    #### limite horizontale du graphique ######
    plt.xlim(x_min, x_max)
    #### limite verticale du graphique ########
    plt.ylim(y_min, y_max)
    ###### pour les grilles ###################
    grid_x_ticks = np.arange(x_min, x_max, 0.5)
    grid_y_ticks = np.arange(y_min, y_max, 0.25)
    ###### pour les graduations
    ax.set_xticks(grid_x_ticks, minor= False)
    ax.set_yticks(grid_y_ticks , minor= False)
    #### pour l'affichage de la grille ########
    ax.grid(which='both')
    ### construction des deux courbes
    # X est la première liste et lesinus(X) est la deuxième
    plt.plot(X, lesinus(X), color ='red', label ='cos')
    plt.plot(X, lecosinus(X), color = 'green', label ='sin')
    ##### pour la légende #####################
    plt.xlabel(r"$x$ ")#syntaxe latex
    plt.ylabel(r" $\sin(x)$ et $\cos(x)$")#syntaxe latex
    plt.legend()
    plt.title(r"Fonctions trigonométriques ")
    plt.show()
    ```

On obtient le graphique suivant:

<center>
![histogramme](<img/fct_trigo.png>)
</center>