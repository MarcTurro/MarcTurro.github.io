---
hide:
  - navigation
  - toc
  - footer
---


# Structures de données linéaires


## Introduction


Le programme Python possède un ensemble de **types de base** et de **types structurés** rencontrés en classe de première: entier (`int`), flottants (`float`), chaîne de caractères, tuple, liste ou encore dictionnaires...

Nous allons dans ce chapitre définir de nouveaux **types abstraits** , à partir de son **interface**, qui rassemble l'ensemble des opérations qui permettent de définir, de lire ou de modifier ces nouveaux objets.

Dans la plus part des cas, on distinguera:

- les **constructeurs** qui crée la donnée
- les **_getters_** qui permettent d'obtenir des informations sur la structure
- les **_setters_** qui permettent de modifier les caractéristiques de ces données

On fera bien la distinction entre **interface** et **implémentation**: la première définit une opération, la seconde la code! Pour une même interface, il peut exister plusieurs implémentations comme nous allons le découvrir dans ce chapitre!

## Les listes

### Présentation !
!!! note "Le type abstrait Liste"
    Une **liste** est une séquence ordonnée d'éléments.

La liste suivante (🤣) donne une interface minimale de ce type:

<center>

| Primitives de l'interface | Commentaires |
|------------------------|--------------------------------------------------------------------------------|
| **creer_liste()** | crée une liste vide |
| **est_vide(L)** | retourne un booléen indiquant si la liste est vide |
| **inserer(L, e)** | insérer l'élément `e` dans la liste `L` |
| **affiche_tete(L)** | affiche le premier élément de la liste `L` |

</center>
Remarquez qu'on ne précise pas dans la dernière instruction où est inséré l'élément: à la fin? au début?

On peut **enrichir** cette interface par de nouvelles **primitives** comme **supprimer(L,e)**, **afficher_premier_elt(L)** ou simplement une opérations qui retourne le nombre d'éléments de cette liste...

Pour information, les interfaces Python sont en général très **riches**, ce qui fait aussi sa popularité!

### Comment implémenter une liste?

Deux choix principaux pour l'implémentation d'une liste:

- soit par un tableau (`array `) où les éléments sont consécutifs en mémoire: dans le langage C, la taille des tableaux est définie préalablement pour allouer la place en mémoire et faire en sorte que les éléments soient à des adresses voisines.
- soit par une liste chaînée: une liste est alors composée d'une tête et d'une queue! Les éléments d'une même liste peuvent être stockés n'importe où dans la mémoire...

Une différence importante entre ces deux choix : dans un tableau, l’**accès** à un élément par son indice est rapide
mais l’**insertion** est coûteuse et c’est le contraire pour les listes chaînées !

La cellule `(tete, queue)` permet de créer ces dernières listes!

<center>
![Un exemple de liste chaînée](../img/listechaine.png)
</center>


### Une première tentative...

Allez soyons fous! Faisons le choix d'implémenter une liste chaînée par des listes (précisément par des listes python...)!🤔

Reprenons le tableau enrichi de l'interface sur les listes: 

=== "Interface"


    | Primitives de l'interface | Commentaires |
    |------------------------|--------------------------------------------------------------------------------|
    | **creer_liste_vide()** | crée une liste vide |
    | **est_vide(L)** | retourne un booléen indiquant si la liste est vide |
    | **inserer(L, e)** | insérer l'élément `e` à la tête de la liste `L` |
    | **affiche_tete(L)** | affiche la tête de la liste `L` |
    | **affiche_queue(L)** | affiche la queue de la liste `L` |
    | **affiche_liste(L)** | affiche tous les éléments de la liste |

=== "Implémentation"
    ``` python
    def creer_liste_vide():
        return []

    def est_vide(L):
        return L == []
    
    def inserer(L, e):
        return [e, L]
    
    def affiche_tete(L):
        if not est_vide(L):
            return L[0]
    def affiche_queue(L):
        if not est_vide(L):
            return L[1]
    def affiche_liste(L):
        aff = []
        while not est_vide(L):
            aff.append(L[0])
            L = L[1]
        return aff
    ```



On peut alors créer des listes avec les interfaces précédentes:

=== "Le code suivant..."
    ```python
    l1 = creer_liste_vide()
    for i in range(4):
        l1 = inserer(l1, i)
    ``` 

=== "... produit la liste chaînée suivante!"
    ```
    [3, [2, [1, [0, []]]]]

    ```

Remarquez que la construction d'une liste chaînée est **récursive**!

Comprenez que Python a sa propre interface pour les listes, celle que vous connaissez habituellement.

### Une deuxième tentative!

Puisque nous créeons de nouveaux objets définis par leur propriété et leur méthode, la **programmation orientée objet** semble prendre toute sa place ici.  L'objet nécessaire à la construcion de telles listes est définie par la classe ```Cellule``` proposée ci-dessous:

``` python
"""
Implantation de la classe “Cellule”
Elle sera utilisée pour les listes, les piles et les files.
"""
class Cellule() :
    def __init__(self, valeur = None, suivant = None) :
        """
        Paramètres
        ----------
        valeur : type quelconque
        Description : Une valeur stockée dans la cellule
        suivant : Un autre objet de type “Cellule”
        Description : La cellule qui “suit” cette cellule selon l’ordre
        défini par la structure.
        ----------
        Crée une cellule avec une valeur et l’adresse de la cellule qui la suit.
        """
        self.valeur = valeur
        self.suivant = suivant
```
Les attributs sont optionnels par défaut. Voici maintenant une implémentation possible de listes chaînées avec ce constructeur:

``` python


from Cellule import Cellule
class Liste() :
    def __init__(self) :
        """
        Crée une liste vide.
        L’attribut “head” est un objet Cellule qui définit la cellule
        en tête de la liste (premier élément de la liste)
        """        
        self.head = None

    def estVide(self) :
        """
        Renvoie True si la liste est vide et False sinon.
        """
        return self.head == None

    def insererEnTete(self, element) :
        """
        Paramètres
        ----------
        element : N’importe quel type
        Description : L’élément à ajouter en tête de la liste
        -------
        Ajoute un élément en tête de liste.
        """
        nouvelle_cellule = Cellule(element, self.head)
        self.head = nouvelle_cellule

    def tete(self) :
        """
        Renvoie la valeur de l’élément en tête de liste.
        """
        if not(self.estVide()) :
            return self.head.valeur

    def queue(self) :
        """
        Renvoie la liste privée de son premier élément (queue de la liste)
        """
        subList = None
        if not(self.estVide()) :
            subList = Liste()
            subList.head = self.head.suivant
        return subList
    
    def __str__(self):
        l = "|"
        c = self.head
        while c != None :
            l = l + str(c.valeur) + "|"
            c = c.suivant
        return l


```
On peut alors créer de nouvelles listes avec cette nouvelle implémentation.

!!! note "À faire"
    1. Créer la liste ordonnée  ```3,2,1,0``` avec la classe précédente.
    2. Créer une liste de 20 nombres aléatoires compris entre 0 et 100.
    2. Afficher sa tête puis sa queue.


On veut enrichir la structure par de nouvelles méthodes.

!!! note "À faire"
    1. Définir la méthode ```__len__(self)``` qui retourne la longueur de la liste.
    2. Définir la méthode ```__getitem__(self, position)``` qui permet d'accéder à l'élément situé à la position ```position``` de la liste si celui-ci existe!
    3. Définir la méthode ```__ajouter_fin__(self, elt)``` qui permet d'ajouter un élément à la liste...


On peut envisager une multitude d'implémentation selon le choix du développeur même si les primitives de l'interface ```liste``` ne changent pas vraiment... Nous retrouverons cette idée dans la partie exercice...

!!! note "À faire"
    Implémenter la fonction qui permet d'insérer dans la liste chaînée ci-dessus, un élément à une position quelconque...
    
## Les piles
<center>
![une pile](../img/pile.jpg)
</center>
### Présentation
La pile, comme la liste, permet de stocker des données et y accéder. La différence se situe au niveau de l'ajout et de la suppression d'un élément!

On parle de mode **LIFO** (Last In, First Out, donc, dernier arrivé, premier sorti), c’est-
à-dire que le dernier élément ajouté à la structure sera le prochain élément auquel
on accèdera. Les premiers éléments ayant été ajoutés devront « attendre » que tous
les éléments qui ont été ajoutés après eux soient sortis de la pile. Contrairement
aux listes, on ne peut donc pas accéder à n’importe quelle valeur de la structure
(pas d’index). Pour gérer cette contrainte, on définit alors le sommet de la pile qui
caractérise l’emplacement pour ajouter ou retirer des éléments.

On peut s’imaginer une pile d’assiettes pour mieux se représenter mentalement cette
structure. On ajoute des nouvelles assiettes au sommet de la pile, et quand on veut en
retirer une, on est obligé de prendre celle située au sommet.

### Interface d'une pile


On peut définir au moins 6 primitives de cette struture de données:
<center>

| Primitives de l'interface | Commentaires |
    |------------------------|--------------------------------------------------------------------------------|
    | **creer_pile_vide()** | crée une pile vide |
    | **est_vide(P)** | retourne un booléen indiquant si la pile P est vide |
    | **taille_pile(P)** | retourne la taille de la pile P |
    | **empiler(P, e)** | ajoute l'élément  `e`  au sommet de la pile|
    | **depiler(P)** | retire l'élémént situé au sommet de la pile P |
    | **affiche_sommet(P)** | affiche le sommet de la pile P **sans** le retirer|

</center>

!!! danger "Attention aux effets de bords!"
    Les méthodes d'affichage en particulier ne doivent pas modifier l'état de la pile. En effet, pour afficher tous les éléments de la liste, l'idée naturelle serait de la dépiler entièrement et d'afficher chaque élément. Mais à la fin, la pile serait vide!
    On appelle cela **un effet de bord**!

Les fonctions javascript en particulier créent de nombreux effet de bords de par leur nature mais c'est voulu!
!!! cite "ce que dit Wikipédia..."
    En informatique, une fonction est dite à effet de bord (traduction mot à mot de l'anglais side effect, dont le sens est plus proche d'effet secondaire) si elle modifie un état en dehors de son environnement local, c'est-à-dire a une interaction observable avec le monde extérieur autre que retourner une valeur.

La struture **Pile** est utilisée pour:

- conserver l'historique de navigation
- stocker des actions et les annuler (++ctrl+z++ et ++ctrl+y++)
- programmer une calculatrice en notation polonaise inversée
- ...

### Implémenter une pile

On peut à peu près tout imaginer pour implémenter la struture de pile... je vous en propose deux ici!

=== "paradigme fonctionnel"
    ``` python
    def creer_pile_vide() :
        """
        Crée une pile vide en s’appuyant sur les listes Python
        """
        return []
    def taille_pile(pile):
        """
        Paramètres
        ----------
        pile : Une pile, telle que créée dans ce module (utilisant une list Python)
        Description : La pile dont on veut connaître le nombre d’éléments
        -------
        Renvoie le nombre d’éléments contenus dans la pile.
        """
        return len(pile)
    def est_vide(pile) :
        """
        Paramètres
        ----------
        pile : Une pile, telle que créée dans ce module (utilisant une list Python)
        Description : La pile dont on souhaite déterminer si elle est vide.
        -------
        Renvoie ``True`` si la pile est vide, et ``False`` sinon
        """
        return taille_pile(pile) == 0
    def empiler(pile, element) :
        """
        Paramètres
        ----------
        pile : Une pile, telle que créée dans ce module (utilisant une list Python)
        Description : La pile sur laquelle on souhaite empiler un élément
        element : N’importe quel type de données.
        Description : L’élément à empiler dans la pile.
        -------
        Empile un élément dans la pile passée en paramètres.
        """
        pile.append(element)

    def depiler(pile) :
        """
        Paramètres
        ----------
        pile : Une pile, telle que créée dans ce module (utilisant une list Python)
        Description : La pile sur laquelle on souhaite dépiler un élément
        -------
        Dépile (supprime de la pile) l’élément au sommet de la pile et le renvoie.
        """
        if est_vide(pile) :
            return None
        else :
            return pile.pop()
    def affiche_sommet(pile) :
        """
        Paramètres
        ----------
        pile : Une pile, telle que créée dans ce module (utilisant une list Python)
        Description : La pile dont on veut connaître le sommet.
        -------
        Renvoie le sommet de la pile (mais ne le dépile pas).
        """
        if est_vide(pile) :
            return None
        else :
            return pile[len(pile) - 1]
    ```
=== "paradigme orienté objet"
    ``` python
    from Cellule import Cellule
    class Pile :
        def __init__(self) :
            """
            Crée une pile vide.
            L’attribut “top” est un objet Cellule qui définit la cellule
            constituant le “sommet” de la pile.
            """
            self.top = None
        def estVide(self) :
            """
            Renvoie True si la pile est vide et False sinon.
            """
            return self.top == None
        def sommet(self) :
            """
            Renvoie la valeur de l’élément au sommet de la pile.
            """
            if not(self.estVide()) :
                return self.top.valeur
            else :
                return None
        def empiler(self, element) :
            """
            Paramètres
            ----------
            element : est de n’importe quel type
            Description : L’élément à empiler sur la pile.
            -------
            Ajoute un élément au sommet de la pile.
            """
            nouvelleCellule = Cellule(element, self.top)
            self.top = nouvelleCellule
        def depiler(self) :
            """
            Dépile et renvoie l’élément situé au sommet de la pile.
            """
            if not(self.estVide()) :
                valeur = self.top.valeur
                self.top = self.top.suivant
                return valeur
            else :
                return None
        def __len__(self) :
            """
            Renvoie le nombre d’éléments de la pile.
            """
            taille = 0
            celluleCourante = self.top
            while(celluleCourante != None) :
                celluleCourante = celluleCourante.suivant
                taille += 1
                return taille
    ```

## Les files
<center>
![une file](../img/file.jpg)
</center>

### Présentation
La file, comme la pile ou la liste, permet de stocker des données et d’y accéder. La différence se
situe au niveau de l’ajout et du retrait d’éléments.
On parle de mode **FIFO** (First in, First out, donc, premier arrivé, premier sorti), c’est-à-
dire que le premier élément ayant été ajouté à la structure sera le prochain élément
auquel on accèdera. Les derniers éléments ajoutés devront « attendre » que tous les
éléments ayant été ajoutés avant eux soient sortis de la file. Contrairement aux listes,
on ne peut donc pas accéder à n’importe quelle valeur de la structure (pas d’index).
Pour gérer cette contrainte, la pile est caractérisée par deux « emplacements » :

- la tête de file, sortie de la file (début de la structure), où les éléments sont retirés ;
- le bout de file, entrée de la file (fin de la structure), où les éléments sont ajoutés.

On peut s’imaginer une file d’attente, dans un cinéma par exemple. Les premières
personnes à pouvoir acheter leur place sont les premières arrivées, et les nouveaux
arrivants se placent au bout de la file.

### Interface d'une pile

Une file est une collection de données. On appelle **tête** de file le premier élément de
la structure et **queue** de la file le dernier élément. Quand un élément est ajouté à la file,
on l’ajoute en queue de file et il devient la nouvelle queue de la file. Quand un élément est retiré
de la file, on le sélectionne à la tête de la file et la nouvelle tête est l’élément qui
suivait l’ancienne tête. Lorsqu’on ajoute un élément à une file vide, celui-ci est donc à
la fois la tête et le bout de la file.

On peut définir au moins 6 primitives de cette struture de données:
<center>

| Primitives de l'interface | Commentaires |
    |------------------------|--------------------------------------------------------------------------------|
    | **creer_file_vide()** | crée une file vide |
    | **est_vide(F)** | retourne un booléen indiquant si la file F est vide |
    | **taille_file(F)** | retourne la taille de la file F |
    | **enfiler(F, e)** | ajoute l'élément  `e`  à la queue de F|
    | **defiler(F)** | retire l'élémént situé à la tête de la file F |
    | **affiche_tete(F)** | affiche la tête de la file F **sans** la retirer|

</center>


La struture **File** est utilisée pour:

- une imprimante dans sa gestion des documents à imprimer
- modéliser un jeu de bataille
- modéliser une file d'attente dan sun cas plus général...

### Implémenter une file
Toujours deux implémentations possibles même si on en découvrira bien d'autres...


??? example "La classe File..."
    ``` python
    class Cellule:
    
        def __init__(self, element, succ):
            self.element = element
            self.succ = succ
            
        def get_element(self):
            return self.element
        
        def get_succ(self):
            return self.succ
        
        def set_succ(self, cell):
            self.succ = cell
        
        def __repr__(self):
            return str(self.element) + '|'
    
    class File:
    
        def __init__(self):
            self.tete = None
            self.dernier = None
            
        def est_vide(self):
            return self.tete == None
            
        def enfiler(self, element):
            if not self.est_vide():
                self.dernier.set_succ(Cellule(element, None))
                self.dernier = self.dernier.get_succ()
            else:
                self.dernier = Cellule(element, None)
                self.tete = self.dernier
            
            
        def premier(self):
            assert not self.est_vide()
            return self.tete.get_element()
        
        def defiler(self):
            assert not self.est_vide()
            self.tete = self.tete.get_succ()
            
        def __repr__(self):
            c = self.tete
            s = ''
            while not c is None:
                s = s + c.__repr__()
                c = c.get_succ()
            return 'entree|' + s[:] + 'sortie'   

    ```

!!! note "À faire"
    En vous inspirant de l'implémentation des piles, proposez une implémentation des files en fonctionnelle avec des listes python.