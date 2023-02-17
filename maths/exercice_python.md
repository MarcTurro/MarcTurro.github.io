---
hide:
  - navigation
  - toc
  - footer
---

Une série d'exercices à réaliser. Réflechissez à la structure algorithmique avant de passer au codage à proprement dit:

- de combien de variables ai-je besoin?
- de quel type de variable ai-je besoin?
- dois-je faire une boucle?
- y a t-il des conditions?


!!! note "À faire: Manipuler des listes"
    On considère une liste quelconque ```L```.

    1. Donner l'instruction qui permet d'afficher le premier élément de la liste, le deuxième, le dernier.
    2. Donner les instructions qui permettent d'ajouter 1 à tous les éléments de la liste.
    3. Donner les instructions qui permettent de décaler d'un rang tous les éléments de la liste (le dernier revenant alors à la première position)


!!! note "À faire: Manipulation de listes bis"
    1. Construire un programme qui calcule la somme des éléments d'une liste. Par exemple:
    ```py
    >>>ma_liste1 = [1, 5, 6]# la somme vaut 1+5+6=12
    >>>ma_liste2 = [i for i in range(100)]# la somme vaut 0+1+2+...+98+100=5050
    ```
    2. Construire un programme qui calcule la somme des nombres pairs d'une liste d'entiers. Par exemple:
    ```py
    >>>ma_liste1 = [1, 5, 6]# la somme vaut 6
    >>>ma_liste2 = [1, 2, 3, 4, 5, 6, 7, 8]# la somme vaut 2+4+6+8=20
    ```
  
!!! note "À faire: Simuler le lancer d'un dé"
    On souhaite simuler plusieurs lancers d'un même dé.

    1. Donner l'instruction qui permet d'affecter à une variable ```n```, un entier saisi au clavier.
    2. Donner l'instruction qui permet d'affecter à une variable ```de``` un nombre entier aléatoire entre 1 et 6.
    3. Donner les instructions ```python``` qui permettent de simuler ```n``` lancers d'un dé à six faces et de stocker les résultats dans une liste ```resultat```.
    4. Plus dur! Donner les instructions ```python``` qui permettent de calculer la fréquence de sortie de chaque face lorsque on jette ```n``` fois un dé.

!!! note "À faire: Course en folie!"
    Léon et Peppa font une drôle de course qui consiste à parcourir six cases consécutives. Léon lance un dé:

    - si le dé affiche 6, il avance de 6 cases et gagne la course
    - sinon Peppa avance d'une case.

    Le gagnant est celui qui arrive le premier sur la dernière case(la sixième...).

    1. Créer une série d'instructions qui permet de simuler cette course.
    2. Utiliser ces instructions pour déterminer la probabilité de gagner de chaque individu.


!!! note "À faire: descente dichotomique"
    Tout le monde connaît le jeu du juste prix qui consiste à trouver le bon prix par le jeu des questions réponses, ```c'est plus!```, ```c'est moins!```.

    1. Créer les instructions qui permettent:
        - de choisir un entier ```alea``` entre 1 et ```n```.
        - de proposer un entier ```choix```.
        - d'afficher la comparaison de ces deux entiers
        - et de recommencer jusqu'à la bonne réponse.
    2. Créer les mêmes instructions mais cette fois-ci, l'ordinateur joue tout seul (c'est lui qui propose un nouveau nombre à chaque fois !)
    3. Créer une nouvelle instruction qui compte le nombre de questions posées avant de trouver la bonne réponse
    4. Créer un graphique qui prend en abscisse le nombre ```n```(choix maxi de ```alea```) et le nombre minimum de questions posées pour retrouver l'entier ```alea```(comme précédemment...)


!!! note "À faire: redescente dichotomique"
    On considère la fonction $f$ définie pour tout $x$ dans $I = [0, 2]$ par $f(x)=x^2-2$.

    1. Justifier qu'il existe une valeur $\alpha$ dans $I$ telle que $f(\alpha) = 0$
    2. Proposer une suite d'instructions qui permet de donner une valeur approchée à $10^{-8}$ de $\alpha$.


