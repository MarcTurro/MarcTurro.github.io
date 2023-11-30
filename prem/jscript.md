---
hide:
  - navigation
  - toc
  - footer
---

<h1>
 Le javascript pour donner du tonus à notre code
 </h1>
<center>

![Js](img\js.jpg)

</center>

## Le principe!

Le cours précédent rappelle que le {== HTML ==} décrit le contenu des pages web que le {==CSS ==} vient par la suite formater. Il ne s'agit pas d'un **langage de programmation** et on ne peut donc pas interagir avec des événements comme le clic de la souris, l'appui sur une touche du clavier ou le chargement d'une page...

Le **javascript** est un **langage de programmation** créé en 1995 et intégré au navigateur **Netscape Navigator** afin de **dynamiser** les pages webs **statiques**. À une action d'un utilisateur, on peut par exemple associer un comportement comme le changement de couleur d'un texte, d'un paragraphe,...

## Le Document Object Model (D.O.M)

Le DOM est la représentation schématique et hiérarchique de votre page web permettant de visualiser l'ensemble des balises HTML qui la constituent.

Le javascript agit sur les objets du DOM. Il les repère soit par le nom de leur balise soit par leur idendifiant (**id**) ou bien leur classe (**class**).

## L'exemple de base...

Nous utiliserons le code HTML [index.html](fichier\index.html) et la feuille de style [style.css](fichier\style.css) qui va avec ...

!!!NOTE "À faire: Construire son arborescence"
    1. Créer un dossier ```WEBJS``` contenant les dossiers ```img, css``` et ```js```. Attention de bien respecter la **casse**!
    2. Téléchargez puis enregistrez le fichier ```index.html```(clic droit->code  source de la page) à la racine du dossier ```WEBJS``` et le fichier ```style.css``` dans le dossier ```css```.
    3. Visualiser alors le fichier ```index.html``` avec un navigateur et appelez le professeur pour validation.

Le DOM de ce code HTML, **volontairement incomplet**, pourrait ressembler à cela:
<center>

![DOM](img\DOM_site_crs.png)

</center>

# Et c'est parti!

Les exercices suivants n'ont rien d'original. Ils montrent seulement comment intégrer du code javascript dans un document HTML afin de répondre à des besoins spécifiques...

## Une manipulation simple!

!!!NOTE "À faire: Mon premier js..."
    1. Intégrer entre les balises ```<head>``` le code suivant:
      ``` javascript
      <script > alert("Le JavaScript fonctionne maintenant!")</script>
      ```
    2. Enregistrez votre fichier HTML et rafraîchissez le navigateur afin de voir apparaître l'effet attendu.
    

Ce code est exécuté suite à un événement: le chargement de la page web. Mais on peut modifier cela!

!!!NOTE "À faire: Mon deuxième js..."
    1. Effacer les balises ```<script>``` précédente.
    2. Insérer dans le corps du document HTML juste après la balise ```<body>```, le code suivant:
    ``` HTML
    <button onclick="alert('Ça marche aussi comme cela! ') ">Appuyez ici!</button>
    ```
    3. Enregistrez et rafraîchissez!

On a déjà exposé dans un cours précédent notre volonté de séparer les codes selon leur utilisation: le css dans un dossier ```css```, les images dans un dossier ```img```,... Continuons ce rangement efficace en enregistrant le code javascript dans son dossier de destination ```js```.

!!!NOTE "À faire: Mon troisième js..."

    1. Avec notepad, ouvrer un nouveau document (language = javascript) que vous enregistrez sous le nom ```monpremierjs.js``` dans le dossier ```js```.
    2. Copiez-y le code suivant:
      ``` javascript
      function ma_fonc_test(){
      window.alert("C'est encore mieux de faire ainsi!!");
      }
      ```
    
    3.Il faut maintenant indiquer au document courant où se situe le code javascript. Insérer alors le code suivant dans l'entête (balises ```<head>```) de la page HTML:
    ``` HTML
    <script src="js\monpremierjs.js"></script>
    ```
    4. Il faut aussi modifier notre bouton pour associer à sa fonction ```onclick``` l'exécution de la fonction ```ma_fonc_test```:
    ``` HTML
    <button onclick="ma_fonc_test()">Appuyez ici!</button>
    ```
    5. Enregistrez et rafraîchissez, tout doit fonctionner!

!!! danger "**Remarquez!**"
    1. Chaque instruction javascript se terminer par un ```;```. Son oubli est souvent une source d'erreur...
    2. Il y a une différence que l'on retrouve dans le langage ```python``` entre ```ma_fonc_test``` et ```ma_fonc_test()```: le premier invoque le nom d'une fonction le deuxième l'exécute !

## En mode debug...

Souvent, le code javascript est long et complet et disons-le ne fonctionne pas toujours comme on le voudrait... Aussi prenons-nous l'habitude d'imprimer dans la console javascript l'état de certaines variables pour savoir si elles évoluent dans le bon sens... On retrouve cette habitude dans d'autres langages de programmation, en ```python``` par exemple...

On appelle **débugger**, l'action de rechercher et corriger les erreurs d'un programme informatique. L'utilisation des ```print``` pour visualiser l'état des variables, permet souvent de débugger...


!!! tip "Mais où se trouve la console javascript???"
    Dans Firefox, tapez <kbd>F12</kbd> et vous verrez apparaître plusieurs onglets dont la console...

Pour imprimer dans la console, rien de plus simple!

!!! Note "À faire: print dans la console..."
    1. Ajouter à la fonction ```ma_fonc_test()```, l'instruction suivante:
    ``` javascript
    function ma_fonc_test(){
      window.alert("C'est encore mieux de faire ainsi!!");
      console.log("Ma javascript fonctionne");
      }
    ```
    2. Enregistrez, rafraîchissez et visulisez dans la console que tout va bien!
    3. Échangez les deux instructions et commentez ce qui se passe.

Remarquez la présence du ```;``` à la fin de chaque instruction et la position des accolades qui englobent les deux instructions: à l'appel de la fonction, les deux instructions sont alors exécutées!


## Bouton et événements

Dans la partie précédente, nous avons:

- créer un bouton: les balises HTML du même nom permettent de le faire
- associer un événement à l'appui sur ce bouton: le bouton a un attribut ```onclick``` auquel on peut asocier une **fonction javascript** à condition qu'elle soit bien entendu codée dans le fichier js.

On se propose ici de créer de nouvelles fonctionnalités pour montrer ce dont javascript est capable de faire.

### Un bouton plus stylé!

Notre bouton n'est pas très joli... modifions son style!

!!! Note "À faire: en mode stylé!"
    1. Dans le fichier ```style.css```, ajouter le code suivant:
    ``` HTML
    button {
        display: inline-block;
        background-color: #7b38d8;
        border-radius: 10px;
        border: 4px double #cccccc;
        color: #eeeeee;
        text-align: center;
        font-size: 28px;
        padding: 20px;
        width: 200px;
        transition: all 0.5s;
        cursor: pointer;
        margin: 5px;
      }
    
    button:hover {
        background-color: #f7c2f9;
      }
    
    ```
    2. Enregistrez, rafraîchissez et admirez!

Pour centrer le bouton, nous allons utiliser une astuce qui consiste à la positionner dans une zone, un conteneur que nous allons centrer. Nous utiliserons alors les balises ```<div></div>```.

!!! Note "À faire: utiliser un conteneur"
    1. Ajouter les balises ```<div></div>``` taggées par la classe ```b_haut``` autour des balises ```<button>```:
    ``` HTML
    <div class = "b_haut"><button onclick="ma_fonc_test()">Essai</button></div>
    ```
    2. Dans le css, on va indiquer que cette balise taggée ```<div>``` doit être centrée:
    ``` css
    div.b_haut{
    display: flex;
    justify-content: center;
    }
    ```
    3. Enregistrez et rafraîchissez.
    4. Enfin, taggez la balise ```<div>``` contenant les autres boutons pour uniformiser notre affichage.


### Changement d'apparence

Les paragraphes existants ont un ```background-color``` en ```rgb(20,100,100)``` défini dans la feuille de style. On souhaite ici modifier cette couleur en appuyant sur notre bouton de test...

L'algorithme est donc:

1. rechercher tous les éléments ```<p>``` dans le DOM
2. changer leur bg
3. associer l'étape 1 et 2 au clic du bouton.

!!! Note "À faire: changer le bg"
    1. Compléter le fichier ```monpremierjs.js```(inutile d'effacer son contenu existant) comme suit:
    ``` javascript
    function new_bg(){
      const elt = document.getElementsByTagName("p");
	    console.log(elt);
	    elt[0].style.backgroundColor = "rgb(200,200,0)";
	    elt[1].style.backgroundColor = "#00FF00";
	    elt[2].style.backgroundColor = "white";
    }
    ```
    2. Changer le nom de la fonction javascript dans l'attribut ```onclick```:
    ``` HTML
    <button onclick="new_bg()">
    ```

L'affichage de la constante ```elt``` permet de connaître son type et son contenu. En fouillant un peu, on voit qu'il y a quatre paragraphes trouvés et on peut aussi explorer leurs attributs...

Même si cela fonctionne, on peut faire beaucoup mieux en utilisant les classes ou les identificateurs.

!!! Note "À faire: taguage général!"
    1. Taguer les balises ```<p>``` selon le principe suivant: la premier balise est ```<p id ="p1">```, la deuxième ```<p id ="p2">```, etc...
    2. Modifier la fonction js précédente:

    ``` javascript
    function new_bg(){
      document.getElementById("p1").style.backgroundColor ="red";
      document.getElementById("p2").style.backgroundColor ="yellow";
      document.getElementById("p3").style.backgroundColor ="purple";
      }
    ```
    3. Enregistrez et rafraîchissez.
 On peut aussi changer d'autres styles que celui du background. Essayez par exemple les changements suivants:

!!! Note "À faire: quelques changements sympas!"
    À ajouter dans le corps de la fonction précédente (entre les accolades sinon cela ne fonctionnera pas...)
    ``` javascript
    document.getElementById("p1").style.visibility='hidden';
    document.getElementById("p2").style.border = "dashed red";
    document.getElementById("p3").style.fontSize ="500%";
    document.getElementById("p3").style.fontFamily = "Brush Script MT";
    
    ```

!!! tldr "En résumé!"
    On tague les différents éléments du DOM afin de pouvoir y accéder par un programme javascript:

    - si on tague par un ```id``` alors la recherche se fait par l'instruction ```document.getElementById(nom_id)```
    - si on tague par une ```classe``` alors la recherche se fait par l'instruction ```document.getElementByClassName(nom_class)```

!!! Note "Exercice de synthèse"
    Supprimez le premier bouton du document HTML puis:

    - en appuyant sur le bouton de gauche, le style des paragraphes changent : vous changerez les couleurs, les fontes, les tailles, ... et chaque paragraphe aura son propre style.
    - en appuyant sur le bouton de droite, le style revient dans sa configuration originale...
    - pour les meilleurs d'entre vous, changez aussi le style des listes (balises ```<ul>```)!
    

### Création de nouveaux objets dans le DOM

Le javascript permet aussi de modifier ou créer du contenant dans le document HTML himself!

!!! Note "À faire: modifier un fils..."
    1. Insérer après la balise ```<body>```, le code HTML suivant:
    ``` HTML
    <div class = "b_haut"><button onclick="ma_fonc_bonjour()">Essai</button></div>
    <p id="demo"></p>
    ```
    Cela crée le bouton que nous avions effacé à l'exercice précédent et un paragraphe vide...
    2. Créer un nouveau fichier javascript avec notepad, nommé  ```monscript.js ``` que vous enregistrez dans le dossier  ```js ```.
    3. Ajoutez-y le code suivant:
    ``` javascript
    function ma_fonc_bonjour(){
    document.getElementById("demo").innerHTML = "Bonjour, nous sommes le " + Date();
    }
    ```
    4. Enfin, n'oubliez pas de changer le chemin de la source js dans les balises ```<script>``` pour pointer vers le bon fichier js...
    5. Enregistrez, rafraîchissez et visualisez...

!!! tldr "En résumé!"
    La méthode ```.innerTHML``` permet de modifier le contenu d'une balise HTML

!!! Note "À faire:Utiliser la méthode ```.innerTHML```"
    1. Taguer le premier titre ```<h1>``` par ```id = premiertitre```.
    2. Compléter la fonction précédente pour que ce titre change en ```Qu'est ce que le Javascript?```

L'affichage de l'heure est dynamique mais invariant: quiconque appuie sur le bouton verra le même message. Ne peut-on pas personnaliser cet affichage?

!!! Note "À faire: ouvrir une fenêtre de saisie"
    1. Dans le fichier ```monscript.js ```, ajoutez le code suivant:
    ``` javascript
    function debut(){
	nom =  window.prompt("Donner votre nom avant de commencer!");
	document.getElementById("nom").innerHTML = "C'est parti!, "+ nom;
    }
    ```
    2. Changer l' ```id``` du paragraphe ```<p>``` de ```demo``` en ```nom```.
    3. Enfin, associer au clic de bouton la bonne fonction:
    ``` HTML
    <button onclick="debut()">
    ```


Autre possibilité: insérer une zone de saisie au sein du document HTML. 

!!! Note "À faire: insérer une zone de saisie"
    1. Ajouter le code HTML suivant sous le premier paragraphe(celui où ```id = nom```):
    ``` HTML
    <h1 > Donner votre âge  </h1>
    <div id="zone_saisie">
	<input id="choix_age" pattern ="[0-9]{2}" value= 16>
    <button  type="button" onclick="affiche_age()" >Valider</button>
    </div>
    <p id ="age"></p>
    ```
    2. Ajouter la fonction javascript suivante dans le fichier ```monscript.js ```.
    ``` javascript
    function affiche_age(){
        let choix = document.getElementById("choix_age").value;
		const d = new Date();
		const an = d.getFullYear()- choix
        document.getElementById("age").innerHTML = "Vous êtes né en " + an ;
    }
    ```
    3. Et si vous voulez centrer tout cela, ajouter à la feuille de style, les instructions suivantes:
    ``` css
    #zone_saisie {
	display: flex;
    justify-content: center;
    }
    ```
Les exemples précédents montrent des usages répandus du javascript: modification du DOM, interaction avec l'utilisateur, ... Bien entendu les possibilités sont vastes mais on peut déjà faire beaucoup de chose...

!!! Note "Exercice de synthèse"
    1. Construire une page web qui permet de saisir deux nombres et d'afficher leur somme.
    2. Même exercice mais les nombres saisis sont binaires!
    

<!--------    
### Des exemples sympas!


<figure markdown>
  ![Image title](img/travaux.jpg){ width="200" }
  <figcaption> Bientôt...</figcaption>
</figure>

--->
