# Première NSI

## Programme de la classe



## Project layout
!!! note "Normalement ça marche!"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! question "Est-ce aussi simple que cela?"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
    
    
Code pour faire des annotations, (1) consectetur adipiscing elit.
    { .annotate }

    1.  :man_raising_hand: I'm an annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be expressed in Markdown.
	
	
=== "Tab 1"

    C'est trop cool, (1) consectetur adipiscing elit.
    { .annotate }

    1.  :man_raising_hand: I'm an annotation!

=== "Tab 2"

   J'ai compris! (1){.annotate }

    1.  :woman_raising_hand: I'm an annotation as well!

``` py title="bubble_sort.py"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```
# terminale NSI
!!!NOTE 
	Information the user should notice even if skimming.

???TIP
	Optional information to help a user be more successful.

!!!IMPORTANT
	Essential information required for user success.

!!!CAUTION
	Negative potential consequences of an action.

!!!WARNING
	Dangerous certain consequences of an action.
## Programme de la classe
``` py
import tensorflow as tf
```
The `#!python range()` function is used to generate a sequence of numbers.


## Project layout

    