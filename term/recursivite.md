---
hide:
  - navigation
  - toc
  - footer
---


# Fonctions récursives

## Un exemple: comment calculer la somme des n premiers entiers consécutifs?

Il s'agit de calculer la somme (dite de Gauss...)  

$$ S = 1 + 2 + 3 + 4 + ... +  n-1 + n $$



!!!NOTE "À faire"      
    1. Copier et coller le code Python ci-dessous
    2. Testez pour plusieurs valeurs simples de $n$
  
``` py
n = int(input("Donner un entier positif"))
S = 0
for i in range(n + 1):
    S = S + i
print("La somme des {} premiers entiers est {}".format(n, S))
```
Le code ci-dessus est **impératif** au sens où nous donnons des ordres que l'ordinateur exécute ligne par ligne.



!!!NOTE "À faire" 
    1. Transformer le code ci-dessus en une fonction ``` somme_entier ``` qui prend en paramètre le seul entier $n$ et qui retourne la somme recherchée.
    2. Ajouter des assertions à la fonction.
    3. Effectuer des tests unitaires (voir le cours...)


Posons la notation $S_n$ pour indiquer la somme $1 + 2 + 3 + 4 + ... +  n-1 + n$. Remarquons alors ceci:

$$S_n=1 + 2 + 3 + 4 + ... +  n-1 + n =S_{n -1} + n$$

Autrement dit, le calcul de $S_n$ est récurrent et la traduction python de cette relation donne:

``` py
somme_rect(n) = somme_rect(n - 1) + n
```

!!! warning "Mais attention!"
    La relation précédente n'est valable que pour $n\geq 1$ et à la condition qu'elle soit aussi **initialisée**: si on déclare que ``` somme_rec(0) = 0 ```, on peut alors calculer ``` somme_rec(1),somme_rec(2),...  ```
Au final, nous obtenons la version **récursive** de la fonction précédente:

``` py
def somme_rec(n):
    if n == 0:
        return 0
    else:
        return somme_rec(n-1) + n

```

## Visualiser la pile d'exécution d'un appel récursif


!!!NOTE "À faire" 
    1. Allez sur le site [python tutor](https://pythontutor.com/render.html#mode=edit) et recopier le code de la fonction récursive dans la zone d'édition.
    2. Exécutez ``` somme_rec(5) ``` et visualisez les différents appels.
    3. Même consigne avec ``` somme_rec(50) ```.
    3. Quel pourrait être le problème des fonctions récursives? 

Il existe de nombreuses situations algorithmiques qui justifient l'appel d'une fonction récursive. Cependant le nombre d'appel dans la pile est souvent limitée pour des raisons évidentes de sécurité puisque la zone mémoire qui stocke tous les appels peut très vite augmentée...

Dans Thonny, on peut connaître le nombre maximum d'appel:

``` py
import sys
print(sys.getrecursionlimit())

```

!!! tldr "À retenir"
    Lors de l’exécution d’un algorithme récursif, les appels successifs de la fonction sont stockés dans une pile, c’est **la pile d’exécution**.
    Plus précisément, la pile d’exécution est un emplacement mémoire destiné à stocker les paramètres, les variables locales ainsi que les adresses mémoires de retour des fonctions en cours d’exécution. 

# Vocabulaire

!!! info "À savoir"
    Une fonction **récursive** est une fonction qui s'appelle elle-même dans son exécution. Elle présente toujours:

      - un **cas d'arrêt** correspondant au cas de base, l'équivalent de l'initialisation en mathématiques...
      - un appel récursif **décrémenté**: ainsi après plusieurs appels, on se ramène au cas de base!





# Exercices

!!!NOTE "À faire"
    La factorielle d'un entier n, notée $n!$ est égale à : $n!=1\times 2 \times 3 \times...\times (n-1) \times n$ si $n>0$ et égal à 1 si $n=0$.

    1. Écrire la fonction **facto_simple(n)** qui prend en paramètre un entier $n$ et qui renvoie la factorielle de $n$.
    2. Écrire la fonction **récursive** facto_recu(n) qui prend en paramètre un entier $n$ et qui renvoie la factorielle de $n$.

    On posera des assertions puis des tests dans ces fonctions pour vérifier leur comportement.
    

!!!NOTE "À faire"
    On rappelle que $x^n=x\times x \times x....\times x$, $n$ fois où $x$ est un réel quelconque et $n$ un entier.

    1. Écrire la fonction **puissance_recu(n,x)** qui prend en paramètres l'entier $n$ et le réel $x$.
    2. On peut améliorer cette dernière fonction en considérant la définition ci-dessous:

    $$\textrm{puissance}(x , n) = 
    \left\{
          \begin{array}{c c}
            x & \textrm{si } n = 1 \\
            \textrm{puissance}(x^2 , n/2) & \textrm{si } n \textrm{ est pair}\\
            x \times \textrm{puissance}(x^2 , (n - 1)/2) & \textrm{si } n \textrm{ est impair}\\
          \end{array}
    \right.$$

    Écrire la fonction **puissance_mieux(n, x)** avec cette définition et comparer le temps d'exécution de ces deux fonctions. On utilisera le module ``` timeit ``` pour cela...

!!!NOTE "À faire"
    1. Écrire une fonction nommée ```  reverse(phrase) ```qui prend en paramètre la chaîne de caractère ``` phrase```  et qui la renvoie à l'envers...
    2. Écrire la version récursive de cette fonction.
    
!!!NOTE "À faire"
    Que dessine la fonction récursive suivante dans ``` turtle ``` (essayez de deviner au lieu de recopier le code....)?
    ``` py
    from turtle import *
    def carre(c):
        for k in range(4):
            forward(c)
            right(90)

    def base(c):
        carre(c)
        forward(c/2)
        right(45)

    def trace(c):
        if c < 5 :
            return None
        else :
            base(c)
            return trace(c/(2**0.5))
        
    trace(200)

    ```
