# MGA_802_Jeu_du_pendu
Ce dépôt contient 3 fichiers :
- ce fichier readme qui explique comment utiliser les autres fichiers
- un fichier 'mots_pendu.txt' qui contient une liste de mots servant de base de donnée au fichier python ('.py)
- un fichier python 'Jeu-du-pendu' qui contient le code permettant de jouer au jeu du pendu à partir du fichier '.txt' inclu dans ce dépôt.

Afin de jouer au jeu du pendu, il faut télécharger les 2 fichiers, puis 'run' le fichier python (avec pycharms par exemple) 
Le code vous demande d'entrer des lettres une à une afin de trouver le mot qui a été tiré aléatoirement parmi la liste.
Vous avez 6 chances pour deviner le mot.

Si la lettre entrée fait partie du mot recherché, alors elle est ajoutée et vous ne perdez pas de chance.
Si la lettre entrée ne fait pas partie du mot recherché, alors vous perdez une chance.

Si vous trouvez toutes les lettres, vous avez gagné. En revanche si vous chances restantes atteignent 0 alors vous perdez.

Le jeu fonctionne seulement avec des mots ne comportant pas d'accents. De plus, le jeu se joue seulement avec les lettres minuscules.
Il est possible d'ajouter des mots au fichier texte en utilisant le même format.
