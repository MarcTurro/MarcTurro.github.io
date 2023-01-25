# Des variables pour comprendre

!!! info "De quoi s'agit-il?"

    Un ordinateur est une grande commode composée de millions de tiroirs dans lesquels on peut stocker des chaussettes... ou plutôt des données!

Je fais référence aux espaces de stockages des ordinateurs de la plus grande (le disque dur) à la plus petite (le registre), en passant par les mémoires vives par lesquelles transitent les informations.
En informatique , tout est **donnée numérique**: les pages web, les images, les sons, les mels ,... et même les programmes sont des données stockées dans des variables contenant des valeurs de différents types. D'où notre obsession sur les **variables**...

On verra comment des _algorithmes_ puis des _programmes_ peuvent changer l'état de ces variables...

<figure markdown>
  ![Image title](../img/commode.png){ width="200" }
  <figcaption> En informatique, tout est nombre!!</figcaption>
</figure>

# Affectation de variables

`#!python Python` est un langage informatique qui permet de donner des instructions. Par exemple, le code suivant:

``` py
a = 2
b = 10
c = a + b
```
crée de façon manuelle (puisqu'on a les tapées...), _trois variables_  ` a,b` et ` c`. Sans trop de détails, vous venez simplement de réserver trois tiroirs de votre gigantesque commode, en leur donnant des noms et des valeurs.

!!! info " Vocabulaire"
    Lorsqu'on crée des variables et qu'on leur attribue des valeurs, on dit qu'on **affecte** une variable ou simplement que l'on a fait une  **affectation** de variables. On peut aussi parler d'**initialisation** de la variable quand pour la première fois, on affecte une valeur à une variable.

En ` Python`, chaque variable a un **type** qui peut-être, un nombre entier ou à virgule (en `python`, on dit un `int` ou un `float`), un texte (en `python`, on dit un `string`) , une liste (en `python`, on dit une ... `list`) ou tout autre chose dont on ne parlera pas pour le moment...

!!! faq "Pourquoi stocker dans des variables???"
    Tout simplement pour garder en mémoire(celle de l'ordi), les résultats obtenus ou calculés par un programme. Il suffit d'invoquer le nom de la variable pour retourver son contenu!

Un exemple! Le programme suivant calcule le prix ```TTC``` d'un article à partir du prix ```HT``` et de la valeur du taux d'imposition lié à la ```TVA```. Vous remarquerez que les variables utilisées sont ```implicites```: une variable qui désigne un prix sera appelée ```prix``` ou ```p```, mais pas ```x``` !!

``` py
prix_HT = 200
taux = 1.196 #pour une TVA a 19.6%
print(prix_HT * taux)
```

Le programme calcule puis **affiche** le prix ```TTC``` dans la console ```python```. Mais le résultat **ne sera pas conservé** en mémoire! On peut (doit?) remédier à cela en créant la variable ```prix_TTC``` et l'affecter comme suit:
``` py
prix_TTC = prix_HT * taux
```
et faire ensuite afficher le contenu de cette varaible:
``` py
print(prix_TTC)
```





# Les opérateurs sur les différentes variables

Il existe des **opérateurs** qui peuvent modifier l'état de ces variables. Outre les opérations mathématiques usuelles $(+, -, \times, \div)$, on aura l'occasion d'en découvrir d'autres.

!!! NOTE "Exercice n°1: Donner la valeur des variables ` a,b` et ` c` à la suite de ces affectations."

        === "Code"

            ``` py
            a = 2
            b = 10
            c = a + b
            b = b + 1
            a = a - 2
            c = c**2
            ```


        === "Solution"

            ``` py
            a = 2
            b = 10
            c = a + b # c vaut alors 12
            b = b + 1 # b vaut 11
            a = a - 2 # a vaut 0
            c = c**2  # c vaut le carré de 12 soit 144
            ```


Il faut lire l'instruction `b = b + 1` ainsi : la nouvelle valeur de la variable `b` est égale à la valeur de l'ancienne à laquelle j'ajoute 1. Cette opération porte même un joli nom:

!!! info " Vocabulaire"
    L' opération qui consiste à faire évoluer une variable en lui ajoutant 1 s'appelle une **incrémentation**.

Cette opération d'incrémentation est très utilisée en _info_. 

!!! NOTE "Exercice n°2:"
    
        === "Questions"

            1. Quelle instruction Python fait diminuer de 1 une variable `a` ?
            2. Cherchez le nom de cette instruction.
            3. Donnez le code qui incrémente une variable ```compteur``` de 5. 

        === "Réponses"

            1. `a = a - 1 #attention dans ce cas il faut que `a ` est été initialisée!`
            2. C'est la **décrémentation**!
            3. ```compteur = compteur + 5```

Il existe d'autres opérations que nous ne citerons pas pour le moment sauf celle du **modulo** car elle est très utilisée en informatique et est nouvelle pour la plupart des personnes qui lisent ces quelques lignes!

!!! info "le modulo ..."
    Nous vivons tous les jours **modulo 24** : toutes les 24 heures, nous remettons les compteurs à zéro! 
    Travaillez avec des entiers **modulo n** où **n** est aussi un entier, consiste à compter à partir de zéro en remettant le compteur à zéro à partir du rang ```n```.

Par exemple,

- en modulo 5: 0,1,2,3,4,0,1,2,3,...
- en modulo 2: 0,1,0,1,0,1,0,1,....

Dans la première liste, à l'entier ```7``` correspond l'entier ```2``` lorsqu'on compte ```modulo 5```: on dit alors que ```7``` est égal à ```2 ``` si on compte ```modulo 5``` et on écrit:

- en maths : ```7 = 2 modulo 5``` ou mieux ,$7 \equiv 2 \pmod 5$
- en ```python```: ```7%5``` qui donne comme valeur ```2```

On peut alors écrire les résultats suivants:

!!! example "des exemples de modulo..."
    ```7%5 = 2, 10%3 = 1, 100%20 = 0, 17%3 = 2```

Remarquez enfin qu'on nombre entier est pair si son ```modulo 2``` est... (à vous de finir la phrase!)
 
On peut aussi jouer avec des lettres ou du texte, ce que nous appelons des variables de type ```chaînes de caractères``` ou simplement `string` en python.

``` py
nom = "Alfred" 
club = "Madrid"
age = "30"
but = 26
```
Les variables de type `string` se déclare avec des **quotes**, doubles `" "` ou simples ` ' ' ` (la tradition veut que l'on utilise les simples pour un seul caractère...): les variables `nom, club` et `age` sont ainsi des chaînes de caractères. La variable `but` est en revanche un entier de type `int`.

!!! warning "Attention!"
    Une variable a un **type**, défini dans la façon dont la variable a été déclarée! Des **opérations** existent selon le type de la variable.

On peut pour illustrer mes propos, utiliser les **opérations** mathématiques classiques sur les variables de type nombres (```int``` ou ```float```) mais pas sur les chaînes de caractères!

La variable `age` n'est donc pas une variable de type `int` mais bien `string` car déclarée avec des _quotes_!

??? tip "Que peut-on faire avec des chaînes de caractères?"

    Les opérateurs sur ces objets sont des opérateurs de **lecture** et de **concaténation**. Mais il n'existe pas d'opérateur d'écriture qui modifierait la chaîne de caractères.

Cela signifie qu'une fois déclarée, une variable de type `string` ne peut plus être **modifiée**.

``` py
nom = "Alfred" 
club = "Madrid"
age = "30"
but = 26
print(nom[0]) #affiche le premier caractère de la variable nom
print(club[2]) #affiche le caractère situé au rang 2 de la variable club
phrase_du_jour = nom + " a marqué " + str(but) + " buts avec le club de " + club + " à l âge de " + age + "ans."
```
L'instruction `print` affiche la valeur de la variable. La variable `phrase_du_jour` est obtenue par la **concaténation** de plusieurs chaînes de caractètes. L'opérateur de concaténation est aussi le $+$ mais ne s'applique qu'aux chaînes de caractères! La variable `but` est **transtypée** pour passer d'un `int` à un `string`!
On obtient alors:

``` py
>>> print(phrase_du_jour)
Alfred a marqué 26 buts avec le club de Madrid à l âge de 30 ans.
```

Attention en revanche, on ne peut pas concaténer une chaîne de caractères et un entier:

``` py
>>> print("buts marqués" + but)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

# Le coin des exercices

!!! note "À faire"
    1. Donner les instructions ```python``` qui permettent:

        - de créer une variable ```h``` et de lui affecter la valeur ```10```.
        - de créer une variable ```p``` et de lui affecter le texte ```bonjour```.
        - de créer une variable ```prix``` et de lui affecter la valeur ```12.5```
    2. Tapez ces instructions dans la console ci-dessous puis pour chaque variable faites affichez son type par l'instruction ```print(type(var))``` où ```var``` doit être remplacé par les noms des variables créés précédemment.
    3. Donner les instructions ```python``` qui:
        - ajoute 10 à la variable ```h``` et socke le résultat dans ```h```.
        - concatène la variable ```p``` avec votre prénom stocke le résultat dans la variable ```phrase```.
        - multiplie la variable ```prix``` par ```1.1``` et stocke le résultat dans ```prix```


{{terminal() }}












