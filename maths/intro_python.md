---
hide:
  - navigation
  - toc
  - footer
---

# Je fais du python et j'aime ça!

!!! info "Pour faire du python..."

    il faut faire du python! Pour progresser il faut manipuler!

Dans ce chapitre, vous trouverez des codes ```python``` que je vous demande de :

- manipuler et analyser
- modifier pour répondre à nos besoins

```Python``` est un langage de haut niveau, proche du langage humain. Sans être un expert, on peut facilement comprendre et analyser un **programme** python .
La création de code vient en dernier lieu, lorsque on s'est bien imprégné des routines pythonesque (grosso modo boucles et affectation...).

La notion de **fonction** n'est pas aussi simple qu'on pourrait le croire et nécessite une étude particulière à voir [ici]("fonctions.md")

## Un premier test
!!!NOTE "À faire" 
    1. Ouvrez un IDLE comme Edupython  ou Thonny et saisissez le code suivant dans la zone script:
    ``` py 
    test = 10 # affectation de la variable à 10
    for i in range(5):#une boucle permet de répéter une même (ou plusieurs) instruction: ici 5 fois
        test = test + 2 #incrementation de la variable test.
        print(test) #affichage dans la console
    ```
    Le résultat devrait s'afficher dans la **console**.
    2. Quelle différence avec le programme suivant?
    ``` py 
    test = 10 # affectation de la variable à 10
    for i in range(5):#une boucle permet de répéter une même (ou plusieurs) instruction: ici 5 fois
        test = test + 2 #incrementation de la variable test.
    print(test) #affichage dans la console
    ```


???TIP "À retenir!"
    Le code s'écrit dans la zone script ou en console. Vous remarquerez dans les exemples précédents, la présence d'```espace``` avant et après les signes d'opérations: il faudra respecter cette règle dorénavant.
    
    L'**indentation** permet de définir les blocs d'instructions dans les boucles ou les conditions.

## Générer du hasard

Dans de nombreux cas, nous aurons besoin de simuler le hasard: plus précisément, certaines variables devront être affectées avec une valeur aléatoire. On distingue en général, les valeurs **entières** des valeurs **décimales**.

Pour cela, il faut **importer** la bibliothèque qui génére les nombres aléatoires:

```py
from random import randint
```
Cette  instruction n'importe **que** la méthode ```randint``` : la bibliothèque ```random``` en contient d'autres que nous n'utiliserons pas ici!

On considère le programme suivant:

```py
n = randint(0, 100)
mon_choix = int(input("proposez un nombre"))
if n == mon_choix:
    print("C'est gagné")
else:
    if n > mon_choix
        print("C'est plus")
    else:
        print("C'est moins")
```

!!! note  "À faire : Utiliser le hasard"
    1. Que fait l'instruction ```randint(0, 100)```?
    2. Quelle est la différence entre les instructions ```n = mon_choix``` et ```n == mon_choix```?
    3. À quoi sert le ```int``` devant le ```input```?
    4. Commenter chaque instruction de ce code comme dans l'exemple test.



## Manipulations
 On donne le code suivant:

```py
#affecter des entiers
a = 15
#affecter des flottants
b = 10.8
#affecter des chaînes de caractères
c = "c'est cool"
d = "c'est génial"
e = "c'est nul"
f = "maths"
#affecter des listes
g = ["HG", "EPS", "LV1", "Philo"] #je suis une liste de chaînes de caractères , des string!
#affecter des autres trucs, inutiles dans notre contexte
```

!!!NOTE "À faire"
    Quels sont les types de variables utilisées ou déclarées dans le code précédent?

En général, on donne des noms explicites aux variables: ces noms dépendent bien entendu du contexte dans lequel elles sont utilisées.
Par exemple, on appelle jamais ``` f``` une variable de type ```list ```  mais plutôt ```l``` .

Aussi, pourrait-on procéder ainsi:

``` py 
note = 15
moyenne = 10.8
discipline_majeure = "maths"
autres_disciplines = ["HG", "EPS", "LV1", "Philo", "Musique", "Physique"]
commentaires = ["c'est cool", "c'est génial", "c'est nul", "c'est marrant"]
note = note + 2
print(note)
print(discipline_majeure[2])
print(autres_disciplines[3])
print(autres_disciplines[6])
```

!!!NOTE "À faire"
    1. Copiez et exécutez le code suivant. Un problème apparaît: pourquoi?
    2. Réglez le problème.

On peut améliorer l'affichage dans la console par des affichages dynamiques. Nous utilisons par exemple des ```f-strings```:

!!!NOTE "À faire"
    1. Ajouter un code précédent, les instructions suivantes:
    ``` py
    print(f"J'ai eu {note} en {discipline_majeure} ")
    listes_notes = [randint(0,20) for i in range(10)]
    print(f" J'ai eu {listes_notes[randint(0, 9)]} en {autres_disciplines[randint(0, 3)]} et {commentaires[randint(0,3)]}")
    ```
    2. Exécutez plusieurs fois le code pour comprendre comment il fonctionne.
    3. Construire une ```f-string```, qui donnerait par exemple:
    ```console
    J'aime la Philo parce que c'est marrant
    ```


## Répéter des instructions:

Il y a en général deux façons de répéter des instructions.

### La boucle bornée ```for```.

Avec la boucle ```for```, on peut choisir le nombre de fois où on répète l'instruction.

!!!NOTE "À faire"
    Ajoutez au code précédent les instructions suivantes et exécutez ce programme:
    ``` py
    autant_de_fois_que_tu_veux = 10
    for i in range(autant_de_fois_que_tu_veux):
        print(f" J'ai eu {listes_notes[randint(0, 9)]} en {autres_disciplines[randint(0, 3)]}")
    ```

La variable ```i``` est appelée **variable de boucle**. L'instruction ```for i in range(10)``` affecte à ```i``` les valeurs 0 puis 1 puis 2,... jusqu'à 9: il y a bien alors 10 affectations, donc 10 répétitions. En fait à chaque que fois que la variable ```i``` prend une valeur, l'instruction de la boucle est exécutée...

!!!NOTE "À faire"
    Pour visualiser comme évolue la variable ```i```, compléter le code précédent comme indiqué ci-après:
    ``` py
    autant_de_fois_que_tu_veux = 10
    for i in range(autant_de_fois_que_tu_veux):
        print(f"Note{i + 1}: J'ai eu {listes_notes[randint(0, 9)]} en {autres_disciplines[randint(0, 3)]}")
    ```

### La boucle non bornée ```while```.

Souvent, on ne sait pas _a priori_ combien de boucles sont nécessaires pour obtenir un résultat. On utilise alors une boucle ```while``` qui permet de répéter des instructions **tant que** une condition est vérifiée.

!!! example "Un exemple"
    ```py
    s = 0 
    cpt = 0 #pour compter le nombre d'actions
    while s < 100:# la condition s < 100 est vrai au départ: on rentre alors dans la boucle.
        s = s + 6 # s est incrémenté de 6
        cpt = cpt + 1 #incrémentation de la variable cpt
    ```

??? warning "Boucle infinie!"
    Une erreur classique consiste à créer des boucles infinies. Si la condition du ```while``` ne devient pas fausse dans l'exécution du programme, la boucle tourne à l'infini!

## Les listes ou les tableaux...

Les variables de type ```int``` servent à conserver en mémoire des entiers alors que les ```flottants``` sont utilisés pour les nombres décimaux. Mais parfois, il faut garder en mémoire toute une série de valeur. On utilise pour cela des **listes**.

### Générer des listes

Pour construire des listes, on peut procéder de plusieurs façons, décrites dans l'exercice suivant.

!!! note "À faire"
    1. Copiez le code suivant et exécutez-le:
    ``` py
    ma_liste_1 = [] # creation d'une liste vide
    for i in range(10):
        ma_liste_1.append(i**2)# à chaque tour de boucle on ajoute à la fin de la liste le carré de i
    ```
    Faites affichez la liste obtenue dans la console.
    2. Copiez et exécutez le code suivant:
    ```py
    from random import randint
    ma_liste_2 = [randint(0, 100) for i range(500)]# construction par compréhension de 500 entiers aléatoires entre 0 et 100
    ```
    3. Bien entendu, on peut construire une liste à la main mais c'est plus long et... peu cohérent avec les pratiques scientifiques et informatiques!
    ```py
    ma_liste_3 = [5, 89, 21, -1, 0]
    ```
    Faites affichez la liste dans la console.
    

### Accéder aux éléments d'une liste

Une liste étant définie, on accède à ces éléments grâce à son **indice**: le premier est d'indice ```0``` et le dernier d'indice ```len(ma_liste_1) - 1``` où l'instruction ```len(ma_liste_1)``` retourne le nombre d'éléments de la liste. Le décalage entre le nombre d'éléments d'une liste et l'indice d'un élément est courant en mathématique et dû au fait que les indices commençent à 0!

!!! example "Routines habituelles"
    ```py
    ma_liste_3 = [5, 89, 21, -1, 0]
    print(ma_liste_3[0])# affiche le premier élément de la liste (5 ici)
    print(ma_liste_3[3])# affiche l'élément situé au rang 3 soit -1
    print(ma_liste_3[5])# erreur! il n'y a pas d'élément au rang 5.
    ```
    Ces routines permettent l'accès à un élément de la liste. Mais on peut aussi utiliser une boucle pour afficher les éléments un par un...
    ```py
    for i in range(len(ma_liste_3)):
        print(ma_liste_3[i])
    ```

Une liste est un objet **mutable**: on peut modifier son contenu.

!!! example "Modification d'un élément"
    ```py
    ma_liste_2[10] = 56 #re-affectation de l'élément d'indice 10 de la liste ma_liste_2
    ```

Mieux encore! On peut modifier tous les éléments d'une liste en combinant les routines précédentes.

!!! example "Modifier tous les éléments d'une liste"
    ```py
    ma_liste = [randint(0, 10) for i in range(50)]# liste de 50 entiers choisis au hasard
    for i in range(len(ma_liste)):
        ma_liste[i] = 2*ma_liste[i] - 1 # re-affectation de tous les éléments de la liste
    ```



# Conclusion 

!!! tip " À retenir"
    Un langage informatique manipule des **variables** qui ont des **types** différents et des **valeurs** correspondantes : ```int```, ```float```, ```str```, ```list``` sont les types que nous avons découverts dans ce travail. Sachez qu'il en existe bien d'autres.

    À chaque type correspond une façon (parfois plusieurs...) de les créer, les modifier ou les afficher. Il faut connaître ses routines dont les principales ont été présentées ci-dessus!