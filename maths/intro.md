# De bonnes pratiques
Il existe de nombreux **langages informatiques** dont le rôle est de proposer une interface de communication entre l'homme et la machine.
Python est un langage de haut niveau (c'est-à-dire que sa syntaxe est proche du langage humain 😀) qui possède ses régles d'écriture décrites dans la [PEP-8](https://peps.python.org/pep-0008/).

En particulier, on respectera les règles suivantes:

 - On entoure d'espaces le signe `=` lors de l'affectation de variables
 - On entoure d'espaces tous les signes d'opérations `+,-,*,...`



!!! example "À faire ou ne pas faire"

        === "BIEN"

            ``` py
            a = 1
            b = 2
            nom = "Hector"
            if x > 2:
                x = x + 2
            ```

        === "PAS BIEN"

            ``` py
            a=1
            b=2
            nom="Hector"
            if x>2:
                x=x+2
            ```

Le langage ```python``` possède sa syntaxe propre mais n'est finalement qu'une traduction des idées qui font de l'être humain, un individu qui réfléchit!

Avant tout, il est donc nécessaire de réfléchir à la façon dont un programme va nous permettre de **résoudre un problème**: sa structure **algorithmique** est prioritaire sur l'écriture à proprement dit du code.

Pour écrire du code ```python```, le bloc-note( éditeur de texte élémentaire de Windows...) suffirait. Il faudrait alors sauvegarder son code dans un fichier dont l'extension serait ```.py``` et utiliser l'exécutable de ```python```(s'il est installé :wink: ) pour lancer le script ainsi créé! Comme l'opération n'est pas évidente, on préférera utiliser un logiciel dédié qui permet de tout faire en cachant la complexité des opérations d'exécution à l'utilisateur...


Principalement, et quelque soit le logiciel utilisé, il existe:

- la zone d'édition ou de script qui permet d'écrire et de l'éxecuter par la suite. Avantage: on peut conserver son code dans un fichier dont l'extension sera `.py`.
- la console ou le terminal qui permet de donner directement des ordres

Ci-dessous, l'environnement proposé par le logiciel _Thonny_:

<figure markdown>
  ![Image title](../img/presentation_thonny.png)
  <figcaption> Tous les environnements présentent les mêmes zones</figcaption>
</figure>











