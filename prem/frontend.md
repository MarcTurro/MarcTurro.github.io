---
hide:
  - navigation
  - toc
  - footer
---


# Le WEB


## Quézaco???
Le WEB ou plus précisément le **WorldWideWeb** est un système hypertexte public fonctionnant sur l'**internet**. Il permet de consulter, avec un navigateur, des pages accessibles sur des sites.

 En 1989, **Tim Berners-Lee**  engagé au CERN de Genève, propose de développer un système organisé en toile, afin d'améliorer la diffusion des informations internes. En 1990, naît alors le premier serveur WEB: la première page existe toujours et vous pouvez la consulter [ici](http://info.cern.ch/hypertext/WWW/TheProject.html).

## Le premier langage du WEB: le HTML

Le premier langage utilisé pour décrire le contenu d'une page web est le langage HTML(HyperTextMarkupLanguage). Ce n'est donc pas un **langage de programmation** mais un **langage de description** comme Latex par exemple...

Il repose sur des **balises** et leurs **attributs** qui décrivent un contenu: titre, paragraphe, entête, images, liens,....
Ci-dessous un exemple relativement simple d'une page web:


!!! example "Un exemple très simple de page web"
    ``` HTML
    <!DOCTYPE html>
    <html>
    <head>
    <title>Le titre de ma première page </title>
    </head>
    <body>
    <h1>Cool! mon premier titre</h1>
    <p>Il s'agit ici d'un paragraphe( balises p). <br> Il faut savoir que les balises ont par défaut des attributs (qu'on peut changer ensuite...). <br>
    Par exemple, une balise H1 propose un titre plus grand qu'une balise H2 ou H3....</p>
    </body>
    </html> 
    ```

## Lire ou écrire? Il faut savoir!

On écrit du code HTML dans un **éditeur**( NotePad, visualCode, blocnote,...) et on le lit avec un **navigateur**. La manipulation habituelle est celle décrite dans l'exercice suivant:

!!!NOTE "À faire: éditer du code et le lire" 
    1. Choisir un éditeur de texte (Notepad ou Visual Studio Code  est idéal... mais le blocnote suffirait!)
    2. Recopier le code HTML précédent et sauvegardez ce fichier sous le nom **index** avec l'**extension HTML** . En général, les logiciels d'édition utilisés permettent de le faire assez facilement...
    3. Vous venez alors de créer le fichier **index.html** qui s'ouvre par **défaut** avec un navigateur. Double-cliquez sur ce fichier: un navigateur doit s'ouvrir et afficher le contenu de la page web.
    4. En observant le site sur le navigateur, à quoi sert la balise _br_?
    4. Fermez ensuite le logiciel que vous avez utilisé pour éditer le code HTML. 

Il arrive fréquemment de modifier un code existant. Par exemple, comment ajouter des élements au fichier **index.html** ? Comment **écrire** sur ce doument? 

C'est simple; faites un clic-droit et le menu contextuel qui s'ouvre vous permet de choisir  _ouvrir avec ..._ , le logiciel d'édition. Je vous rappelle que par défaut, un fichier html s'ouvre en **lecture** avec un navigateur...

!!!NOTE "À faire: modifier du code HTML" 
    1. Ajouter le code HTML suivant au fichier précédent entre les balises fermantes ```<\p>``` et ```<\body>```.
        ``` HTML
        <h2>C'est mon deuxième titre</h2>
        <p>Remarquez que le titre H2 est plus petit que celui de H1</p>
    
        ```
    2. Lire le nouveau document pour observer les changements effectués.

Pour actualiser une page dans un navigateur, il suffit d'appuyer sur la touche  <kbd>F5</kbd> .


## La W3C schools 

Le W3C est un consortium chargée de développer et maintenir les standards du WEB que sont les langages HTML,CSS,PHP, ... mais aussi le format d'image **png**(Portable Network Graphics) idéal pour les pages WEB. Il offre aussi la possibilité de valider votre code en vous indiquant si vous avez respecté les normes en vigueur.

<center>

![le W3C](img/W3C.png "Le consortium W3C")
</center>

Ce consortium propose une école d'apprentissage du code HTML et d'autres... c'est la **W3schools!** Vous trouverez le lien [ici](https://www.w3schools.com/html/default.asp).
Les exercices qui suivent ont été inspirés par les exemples proposés dans cette école.

# Apprentissage du HTML

Cette partie s'intéresse à la partie codage et vous donne au fur et à mesure de nouvelles fonctionnalités. Il faut donc à chaque étape **modifier** ou **compléter** son code HTML dans un logiciel d'édition et **visualiser** dans un navigateur, le résultat de vos modifications. N'oubliez pas d':

- **enregistrer** votre fichier modifié (touches <kbd>ctrl</kbd>+<kbd>S</kbd>)
- **actualiser** votre page dans le navigateur (touche <kbd>F5</kbd>)

On utilisera comme point de départ, le code de la page web donné dans la partie précédente:

!!! example "Code simple que nous allons compléter"
    ``` HTML
    <!DOCTYPE html>
    <html>
    <head>
    <title>Le titre de ma première page </title>
    </head>
    <body>
    <h1>Cool! mon premier titre</h1>
    <p>Il s'agit ici d'un paragraphe( balises p). <br> Il faut savoir que les balises ont par défaut des attributs (qu'on peut changer ensuite...). <br>
    Par exemple, une balise H1 propose un titre plus grand qu'une balise H2 ou H3....</p>
    <h2>C'est mon deuxième titre</h2>
    <p>Remarquez que le titre H2 est plus petit que celui de H1</p>
    </body>
    </html> 
    ```

## Des attributs pour formater à volonté...

Toutes les balises ont par **défaut**, des attributs de couleur, de grosseur, de positionnement qui peuvent être modifiés. Quelques exemples sont proposés ici.

!!!NOTE "À faire: ajouter des attributs aux balises" 
    1. Modifier la balise _body_ comme ceci:
    ``` HTML
    <body style="background-color:powderblue;" >
    
    ```
    2. Modifier la balise _H1_:
    ``` HTML
    <h1 style="color:Tomato; font-size:300%;text-align:center;"  >
    
    ```
    3. Modifier la balise _H2_ afin qu'elle soit aussi alignée au centre avec la couleur ```MediumSeaGreen```.
    4. Enfin faites en sorte que les paragraphes soient centrés avec un fond de couleur que vous pouvez choisir parmi les possibilités offertes [ici](https://www.w3schools.com/html/html_colors.asp)

!!! tldr "À retenir!"
    Tous les éléments HTML ont un style que vous pouvez définir ou redéfinir à souhait... Certains sont simples d'autres plus avancés.

!!!NOTE "À faire: un style balaise!"
    Essayez ce style sur les balise p:
    ``` HTML
    <p style="background: linear-gradient(to right,#ffbe02a1 0px,#fd606aba 100%);
    padding: 10px;
    border-radius: 10px;" >
    ```
    C'est joli, non?

## Des commentaires pour comprendre

Dans tout langage informatique, on peut (doit?) ajouter des commentaires qui permettent d'amener quelques explications aux choix effectués: ces lignes **ne sont pas interprétées** par le navigateur.

!!! example "Code simple que nous allons ccommenter"
    ``` HTML
    <!DOCTYPE html>
    <html>
    <head>
    <!-- Les commentaires sont intégrés au code par ces balises-->
    <title>Le titre de ma première page </title>
    </head>
    <body>
    <h1>Cool! mon premier titre</h1>
    <!-- bg en degradé vers la droite d'une couleur vers une autre-->
    <!-- le padding est le rembourrage dans l'élément mère-->
    <!-- le rayon du coin de la pordure est de 10px-->
    <p style="background: linear-gradient(to right,#ffbe02a1 0px,#fd606aba 100%);
    padding: 10px;
    border-radius: 10px;" >
    Il s'agit ici d'un paragraphe( balises p). <br> Il faut savoir que les balises ont par défauts des attributs (qu'on peut changer ensuite...). <br>
    Par exemple, une balise H1 propose un titre plus grand qu'une balise H2 ou H3....</p>
    </body>
    </html> 
    ```

On peut aussi utiliser des balises de commentaires pour isoler une partie du code afin qu'elle ne soit pas lues par le navigateur.

## Insérer des liens et des images

Une page web contient souvent des images. Le code ci-dessous permet d'intégrer l'image du logo de la nsi du lycée à récuperer [ici](img/logoNSI.png).

``` HTML
    <img src="img/logoNSI.png" alt="le logo de la NSI"> 
```
Si vous souhaitez insérer un lien vers un autre site sur un mot, une image, ... il faudra alors intégrer l'instruction suivante à votre code:

``` HTML
    <a href="https://lyceedebaudre.net/">Le lycée</a> 
```
Le lien se trouve sur la phrase _le lycée_: en cliquant dessus vous êtes dirigé vers le site dont l'**URL** est passé en paramètre.
!!!NOTE "À faire: insérer une image et un lien vers un autre site"
    1. Créer un dossier _img_ situé au même niveau d'arborescence que votre fichier _index.html_ et placez-y l'image du logo.
    2. Insérer l'image dans votre code et visualisez que tout fonctionne bien dans le navigateur.
    3. Le chemin de la source est-il absolu? relatif?
    3. Insérer un lien vers ce [site](https://www.w3schools.com/) dans votre code où vous le souhaitez !

Vous voulez en savoir davantage? Aucun soucis, cliquez [ici](https://www.w3schools.com/html/html_images.asp)

!!!NOTE "À faire:"
    À quoi sert la balise ```map```?

## Un tableau?

Vous coulez insérer un tableau à votre code? Rien de plus simple (ou presque...).

!!!NOTE "À faire: un simple tableau!"
    1. Insérer ce code au vôtre
    ``` HTML
    <table>
    <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
    </tr>
    <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
    </tr>
    <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
    </tr>
    <tr>
    <td>Ernst Handel</td>
    <td>Roland Mendel</td>
    <td>Austria</td>
    </tr>
    <tr>
    <td>Island Trading</td>
    <td>Helen Bennett</td>
    <td>UK</td>
    </tr>
    <tr>
    <td>Laughing Bacchus Winecellars</td>
    <td>Yoshi Tannamuri</td>
    <td>Canada</td>
    </tr>
    <tr>
    <td>Magazzini Alimentari Riuniti</td>
    <td>Giovanni Rovelli</td>
    <td>Italy</td>
    </tr>
    </table>
    ```
    2. Vous souhaitez le rendre plus joli encore? Insérer les styles suivants aux balises concernées...
    ``` HTML
    <table style="font-family: arial, sans-serif;  border-collapse: collapse;  width: 100%;">
    <tr style = "border: 1px solid #d80d0d; text-align: left;  padding: 8px; ">
    ```

Remarquez comment il est pénible d'ajouter les attributs de style à toutes les balises concernées. Le paragraphe suivant permet de contourner ce problème!

## Stylée la balise!!

Définir le style de chaque balise peut s'avérer fastidieux. Dans le tableau précédent il a fallu compléter toutes les balises ```<tr>```, une par une... ce qui n'est pas très productif. Il existe une balise qui permet de rassembler tous les styles.

!!! tldr "À retenir!"
    La balise ```<style>``` dans l'entête du fichier recense l'ensemble des styles imposés sur les différentes balises.
Ainsi tous les styles sont-ils définis au départ: le code s'en trouve largement simplifié...

!!! Note "À faire: regrouper les styles"
    Recopier le code suivant entre les balises ```head``` et supprimer les tyles dans les balises.
    ``` HTML
    <!DOCTYPE html>
    <html>
    <head>
    <title>Le titre de ma première page </title>
    <style>
      body {background-color:powderblue;}
      h1,h2 {color:Tomato; font-size:300%;text-align:center;}
      p {background: linear-gradient(to right,#ffbe02a1 0px,#fd606aba 100%);
    padding: 10px;border-radius: 10px; }
      table {font-family: arial, sans-serif;  border-collapse: collapse;  width: 100%;}
      tr {border: 1px solid #d80d0d; text-align: left;  padding: 8px;}
    </style>
    </head>
    <body >
    <h1 >Cool! mon premier titre</h1>
    <p >Il s'agit ici d'un paragraphe( balises p). <br> Il faut savoir que les balises ont par défauts des attributs (qu'on peut changer ensuite...). <br>
    Par exemple, une balise H1 propose un titre plus grand qu'une balise H2 ou H3....</p>
    <h2>C'est mon deuxième titre</h2>
    ...
    ...
    ```

Seul problème: les mêmes éléments ont le même style! Mais on peut contourner le problème en _taggant_ certaines balises...

## Les identifiants n'ont pas la classe!

Comment faire si on veut distinguer le style de deux paragraphes par exemple? Le regroupement des styles entre les balises du même nom ne permet plus de personnaliser ces affichages. 

Pas de panique! Tout est prévu, il suffit de **tagger** les balises par des classes(**class**) ou des idendificateurs (**id**).

Imaginons que nous souhaitions que les paragraphes définis pas le code précédent n'aient pas les mêmes couleurs. On va alors:

- tagger chaque balise ```<p>``` par une classe
- définir le style de la classe à l'intérieur de la balise ```<style>```

Le code suivant devient alors...


``` HTML
<!DOCTYPE html>
<html>
<head>
<title>Le titre de ma première page </title>
<style>
        body {background-color:powderblue;}
        h1,h2 {color:Tomato; font-size:300%;text-align:center;}
        p {padding: 10px;border-radius: 10px; }
        <!-- premiere classe -->
        .choix1 {
        background: linear-gradient(to right,#ffbe02a1 0px,#fd606aba 100%);
        }
        <!-- deuxieme classe: inversion du sens de degrade -->
        .choix2 {
        background: linear-gradient(to left,#ffbe02a1 0px,#fd606aba 100%);
        }
        table {font-family: arial, sans-serif;  border-collapse: collapse;  width: 100%;}
        tr {border: 1px solid #d80d0d; text-align: left;  padding: 8px;background-color: #dddddd;}
</style>
</head>
<body >
<h1  >Cool! mon premier titre</h1>
<!--tag du premier paragraphe-->
<p class = "choix1" >Il s'agit ici d'un paragraphe( balises p). <br> Il faut savoir que les balises ont par défauts des attributs (qu'on peut changer ensuite...). <br>
Par exemple, une balise H1 propose un titre plus grand qu'une balise H2 ou H3....</p>
<h2>C'est mon deuxième titre</h2>
<!-- tag du deuxième paragraphe -->
<p class = "choix2" >Remarquez que le titre H2 est plus petit que celui de H1</p>
<table >
    <tr >
        <th>Company</th>
        <th>Contact</th>
        <th>Country</th>
    </tr>
    <tr >
        <td >Alfreds Futterkiste</td>
        <td >Maria Anders</td>
        <td >Germany</td>
    </tr>
    <tr >
        <td>Centro comercial Moctezuma</td>
        <td>Francisco Chang</td>
        <td>Mexico</td>
    </tr>
    <tr >
        <td>Ernst Handel</td>
        <td>Roland Mendel</td>
        <td>Austria</td>
    </tr>
    <tr >
        <td>Island Trading</td>
        <td>Helen Bennett</td>
        <td>UK</td>
    </tr>
    <tr >
        <td>Laughing Bacchus Winecellars</td>
        <td>Yoshi Tannamuri</td>
        <td>Canada</td>
    </tr>
    <tr >
        <td>Magazzini Alimentari Riuniti</td>
        <td>Giovanni Rovelli</td>
        <td>Italy</td>
    </tr>
    </table>
</body>
</html> 
```

Ainsi, les paragraphes ont-ils:

- un style commun( ```padding``` et ```border-radius```)
- un style différent (le sens du dégradé)

!!! Note "À faire: créer des classes"
    On peut ajouter un ```background-color``` aux balises ```<tr>```. Je voudrais que les lignes de rang pair est une couleur d'arrière plan de ```#777777``` et celles de rang impair une couleur ```#dddddd```. Pour cela:

    1. Créer deux classes ```bg1``` et ```bg2``` dans les balises ```<style>```
    2. tagger les balises ```<tr>``` pour répondre à ma volonté

Les classes ont une autre fonction: celle de pouvoir identifier des éléments et d'agir sur eux (vois cours sur le CSS et JS).

On peut aussi utiliser un identifiant (```id```) pour désigner un et un seul élément(une balise quoi..) dans le DOM (Document Objet Model). C'est la différence entre les deux ``` tags ```: 

!!! tldr "À retenir!"
    Les ``` class ``` permettent d'identifier plusieurs éléments mais l'``` id ``` seulement un!

Alors que les noms de classes se déclarent dans les balises ```<style>``` avec des  ```.nom_de_la_classe```, les identifiants sont définis aux mêmes endroits par ```#nom_du_id```.

!!! Note "À faire: créer un identifiant"
    On va tagger la balise ```<h2>``` par un idendifiant. Pour cela suivre les instructions suivantes:
    
    1. Ajouter entre les balises ```<style>```:
    ``` HTML
    #montitre {
    background-color: lightblue;
    color: black;
    padding: 40px;
    text-align: center;
    }
    ```
    2. Ajouter à la balise ```<h2>``` l'identifiant ```id = "montitre"```:
    ``` HTML
    <h2 id = "montitre">
    ```
    3. Proposez une nouvelle couleur pour cet identifiant.

C'est cool, non?

## En mode professionnel!

Jusqu'à présent, les styles de toutes les balises sont regroupés entre les balises éponymes. En programmation comme en langage de description, on préfère séparer le contenu(le fond!) de son apparence(la forme!). Aussi va t-on créer un fichier particulier, appelé **feuille de style** qui permettra de formater le contenu html. Ce fichier porte l'extension **.css** et regroupe tous les styles.

!!! Note "À faire: créer une feuille de style"
    Suivez les instrutions suivantes:

    1. Créer au même niveau d'arborescence que le fichier ```index.html``` le dossier ```CSS``` à côté de clui des images ```img```.
    2. Ouvrez le blocnote et créez un nouveau fichier.
    3. Copier dans ce dernier fichier, l'ensemble des styles entre les balises ```<style>```(sans les balises) et supprimer ce contenu du fichier ```html``` (y compris les balises ```<style>``` et ```<\style>``` )
    4. Sauvegarder le fichier sous le nom ```monstyle.css``` dans le dossier ```CSS``` en sélectionnant ```Tous les fichiers``` à l'endroit indiqué...

Félicitations! Vous venez de créer votre première feuille de style!

Maintenant il faut indiquer au document ```index.html``` où se trouve la feuille de style chargée de le formater: c'est ce que nous appelons **attacher la feuille de style**!

!!! Note "À faire: attacher une feuille de style"
    Suivez les instrutions suivantes:
    
    1. Ajouter la balise ```<link rel="stylesheet" href="CSS/monstyle.css">``` entre les balises ```<head>``` dans le fichier ```index.html```.
    2. Enregistrez et vérifier que le chemin relatif ci-dessus est correct avant d'appeler votre professeur!

# Des trucs originaux maintenant!
Quelques manipulations supplémentaires qui vous donneront une petite idée des possibilités offertes par le HTML, le CSS ou le Javascript...


On peut par ce biais insérer des cartes OSM même si des problèmes de sécurité peuvent surgir...
## Du code pour dynamiser tout cela...
 Le code HTML formaté par le CSS est **statique**: il n'y a pas d'événements qui surviennent quelque soit l'action de l'utilisateur. On donne ici du code ```javascript``` qui va donner du **dynamisme** à notre code. Il s'agit ici d'exemples et nous aurons bientôt l'occasion d'étudier plus précisément ce langage de programmation!

!!! Note "À faire: insertion de code javascript"

    1. Insérer le code suivant en dessous du premier titre  ```<h1>```.
    2. Enregistrez puis cliquez sur le bouton: la date du jour doit apparaître.
    ``` HTML
    <button type="button" onclick="document.getElementById('tag_para').innerHTML = Date()">
    Tu veux connaître l'heure?</button>
    <p id="tag_para"></p>
    ```
    3. À quoi sert la méthode ```getElementById```
    

## Insérer une vidéo ou de l'audio

Beaucoup de sites proposent des vidéos à lire sur leur page d'accueil. À nous!

!!! Note "À faire: insertion de vidéo"

    1. Récupérer la vidéo [ici](img/fleur.mp4)
    2. Créer un dossier video(sans accent 😉 ) à un endroit judicieux...
    3. Insérer la balise:
    ``` HTML
    <video width="400" controls>
    <source src="video/fleur.mp4" type="video/mp4">
    Your browser does not support HTML video.
    </video>
    ```
    


## T'es où?

La géolocalisation est devenue une habitude pour les sites commarciaux. Intégrée au code HTML par des scripts ```javascript```, le principe est simple.

!!! Note "À faire: insertion de géolocalisation"

    1. Insérer la balise dans le corps du document HTML:
    ``` HTML
    <p>Obtenir sa position par sa latitude et longitude</p>
    <button onclick="getLocation()">Geolocalisez-moi!</button>
    <p id="test"></p>
    ```
    2. Insérer les balises suivantes dans les balises d'entête ```<head>```:
    ``` HTML
    <script>
    var x = document.getElementById("test");

    function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
    }

    function showPosition(position) {
    x.innerHTML = "Latitude: " + position.coords.latitude + 
    "<br>Longitude: " + position.coords.longitude;
    }
    </script>
    ```

## Prenons de l'altitude:

La géolocalisation vous permet de vous situer sur une carte. Je vous propose ici une application amusante de ces dernières techniques. Nous utilisons des cartes gratuites open source [leaflet](https://leafletjs.com/).

!!! Note "À faire: récupérer du code"
    
    1. Télécharger le fichier ```index_is.html``` à cet [endroit](fichier/index_iss.html).
    2. Ouvrez-le en lecture puis en écriture en essayant d'analyser le code utilisé.


## Cherchez son style!

Les **feuilles de style** façonnent votre site web. Vous trouverez de nombreux exemples sur le WEB. Vous trouverez [ici](https://www.w3schools.com/w3css/default.asp) les types développés par le W3C.

!!! Note "À faire: récupérer du code et le personnaliser"

    1. Récupérer le code du template ``` Portfolio Template``` du site précédent.
    3. Modifier le code pour faire quelque chose qui vous ressemble.


