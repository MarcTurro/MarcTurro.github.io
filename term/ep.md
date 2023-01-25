---
hide:
  - navigation
  - toc
  - footer
---


Exercices à réaliser ou à compléter sous Thonny ou Edupython

!!! example "Exercice n°1:"
    Écrire une fonction `recherche` qui prend en paramètres `elt` un nombre entier et `tab`
    un tableau de nombres entiers, et qui renvoie l’indice de la première occurrence de `elt`
    dans `tab` si `elt` est dans `tab` et `-1` sinon.

    Exemples :
    ```python
    >>> recherche(1, [2, 3, 4])
    -1
    >>> recherche(1, [10, 12, 1, 56])
    2
    >>> recherche(50, [1, 50, 1])
    1
    >>> recherche(15, [8, 9, 10, 15])
    3
    ```

!!! example "Exercice n°2:"
    L’occurrence d’un caractère dans un phrase est le nombre de fois où ce caractère est
    présent.

    Exemples :

    - l’occurrence du caractère ‘o’ dans ‘bonjour’ est 2 ;
    - l’occurrence du caractère ‘b’ dans ‘Bébé’ est 1 ;
    - l’occurrence du caractère ‘B’ dans ‘Bébé’ est 1 ;
    - l’occurrence du caractère ‘ ‘ dans ‘Hello world !’ est 2.

    On cherche les occurrences des caractères dans une phrase. On souhaite stocker ces
    occurrences dans un dictionnaire dont les clefs seraient les caractères de la phrase et
    les valeurs l’occurrence de ces caractères.

    Par exemple : avec la phrase 'Hello world !' le dictionnaire est le suivant :

    `{'H': 1,'e': 1,'l': 3,'o': 2,' ': 2,'w': 1,'r': 1,'d': 1,'!': 1}`

    Écrire une fonction `occurrence_lettres` prenant comme paramètre une variable
    `phrase` de type `str`. Cette fonction doit renvoyer un dictionnaire de type constitué des
    occurrences des caractères présents dans la phrase.

!!! example "Exercice n°3:"
    On considère un tableau d'entiers `tab` (type `list` dont les éléments sont des `0` ou des `1`). On se propose de trier ce tableau selon l'algorithme suivant : à chaque étape du tri,le tableau est constitué de trois zones consécutives, la première ne contenant que des `0`,
    la seconde n'étant pas triée et la dernière ne contenant que des `1`.

    <table>
    <tr>
    <td>Zone de 0</td><td>Zone non triée</td><td>Zone de 1</td>
    </tr>
    </table>

    Tant que la zone non triée n'est pas réduite à un seul élément, on regarde son premier
    élément :

    - si cet élément vaut 0, on considère qu'il appartient désormais à la zone ne contenant
    que des 0 ;
    - si cet élément vaut 1, il est échangé avec le dernier élément de la zone non triée et on
    considère alors qu’il appartient à la zone ne contenant que des 1.

    Dans tous les cas, la longueur de la zone non triée diminue de 1.

    Recopier sous Python en la complétant la fonction `tri` suivante :

    ```python linenums='1'
    def tri(tab):
        #i est le premier indice de la zone non triee, j le dernier indice.
        #Au debut, la zone non triee est le tableau entier.
        i = ...
        j = ...
        while i != j :
            if tab[i]== 0:
                i = ...
            else :
                valeur = tab[j]
                tab[j] = ...
                ...
                j = ...
        ...

    Exemple :

    >>> tri([0,1,0,1,0,1,0,1,0])
    [0, 0, 0, 0, 0, 1, 1, 1, 1]       

    ``` 

!!! example "Exercice n°4:"
    On veut écrire une classe pour gérer une file à l’aide d’une liste chaînée. On dispose d’une
    classe ```Maillon``` permettant la création d’un maillon de la chaîne, celui-ci étant constitué
    d’une valeur et d’une référence au maillon suivant de la chaîne :

    ```python linenums='1'
    class Maillon :
        def __init__(self,v) :
            self.valeur = v
            self.suivant = None
    ```
    Compléter la classe ```File``` suivante où l'attribut ```dernier_file``` contient le maillon correspondant à l'élément arrivé en dernier dans la file:
    ``` python 
    class File :
        def __init__(self) :
            self.dernier_file = None

        def enfile(self,element) :
            nouveau_maillon = Maillon(...)
            nouveau_maillon.suivant = self.dernier_file
            self.dernier_file = ...

        def est_vide(self) :
            return self.dernier_file == None

        def affiche(self) :
            maillon = self.dernier_file
            while maillon != ... :
                print(maillon.valeur)
                maillon = ...

        def defile(self) :
            if not self.est_vide() :
                if self.dernier_file.suivant == None :
                    resultat = self.dernier_file.valeur
                    self.dernier_file = None
                    return resultat
                maillon = ...
                while maillon.suivant.suivant != None :
                    maillon = maillon.suivant
                resultat = ...
                maillon.suivant = None
                return resultat
            return None
    ```

!!! example "Exercice n°5:"
    Écrire une fonction python appelée `nb_repetitions` qui prend en paramètres un
    élément `elt` et une liste `tab` et renvoie le nombre de fois où l’élément apparaît dans la
    liste.

    Exemples :
    ```python
    >>> nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5])
    3
    >>> nb_repetitions('A', ['B', 'A', 'B', 'A', 'R'])
    2
    >>> nb_repetitions(12, [1, '!', 7, 21, 36, 44])
    0
    ```

!!! example "Exercice n°6:"

    Cet exercice utilise des piles qui seront représentées en Python par des listes (type `list`).
    On rappelle que l’expression `T1 = list(T)` fait une copie de `T `indépendante de `T`, que
    l’expression `x = T.pop()` enlève le sommet de la pile `T` et le place dans la variable `x` et,
    enfin, que l’expression `T.append(v)` place la valeur `v` au sommet de la pile `T`.

    Compléter le code Python de la fonction `positif` ci-dessous qui prend une pile `T` de
    nombres entiers en paramètre et qui renvoie la pile des entiers positifs dans le même
    ordre, sans modifier la variable `T`.

    ```python linenums='1'
    def positif(T):
        T2 = ...(T)
        T3 = ...
        while T2 != []:
            x = ...
            if ... >= 0:
                T3.append(...)
        T2 = []
        while T3 != ...:
            x = T3.pop()
            ...
        print('T = ',T)
        return T2
    ```
    Exemple :
    ```
    >>> positif([-1, 0, 5, -3, 4, -6, 10, 9, -8])
    T = [-1, 0, 5, -3, 4, -6, 10, 9, -8]
    [0, 5, 4, 10, 9]

    ``` 