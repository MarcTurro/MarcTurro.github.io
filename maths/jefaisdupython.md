# Je fais du python et j'aime ça!

!!! info "Pour faire du python..."

    il faut faire du python! Inutile de potasser tous les bons cours trouvés sur le web , pour progresser il faut manipuler!

Dans ce chapitre, vous trouverez des codes ```python``` que je vous demande de :

- manipuler et analyser
- modifier pour répondre à nos besoins

La création de code vient en dernier lieu, lorsque on s'est bien imprégné des routines pythonesque (grosso modo boucles et affectation...).

La notion de **fonction** n'est pas aussi simple qu'on pourrait le croire et nécessite une étude particulière à voir [ici]("fonctions.md")

## Générer du hasard

Dans de nombreux cas, nous aurons besoin de simuler le hasard:plus précisément, certaines variables devront être affectées avec une valeur aléatoire. On distingue en général, les valeurs **entières** des valeurs **décimales**.

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
    1. Quelle est la différence entre les instructions ```n = mon_choix``` et ```n == mon_choix```?
    2. À quoi sert le ```int``` devant le ```imput```?
    3.