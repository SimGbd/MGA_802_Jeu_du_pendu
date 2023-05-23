import random
#tirage du mot aléatoire parmi la liste du fichier texte
def tirage_mot():
    with open("mots_pendu.txt", 'r') as f:
        ensemble_mots = f.readlines()
        mot_tire = random.choice(ensemble_mots).strip()
        return mot_tire
#afficher le nombre de lettre du mot tiré sous forme "_____"
def afficher_mot(mot):
    return "_" * len(mot)
#afficher le schéma du pendu suivant l'évolution du nombre de chances restantes
def afficher_pendu(chances_restantes):
    if chances_restantes < 6:
        print(" ==========Y= ")
    if chances_restantes < 5:
        print(" ||/       |  ")
    if chances_restantes < 4:
        print(" ||        O  ")
    if chances_restantes < 3:
        print(" ||       /|\\ ")
    if chances_restantes < 2:
        print(" ||        |  ")
    if chances_restantes < 1:
        print(" ||       / \\ ")
        print("==============\n")

#vérifie si une lettre en entrée a déjà été proposée ou non
def verifier_lettre_proposee(lettre, lettres_proposees):
    if lettre in lettres_proposees:
        print(f"La lettre '{lettre}' a déjà été proposée pour ce mot.")
        return False
    return True

#ajoute la lettre au mot à trouver à la bonne place
def ajouter_lettre_mot_cache(mot_a_deviner, mot_cache, lettre):
    nouveau_mot_cache = ""
    for i in range(len(mot_a_deviner)):
        if mot_a_deviner[i] == lettre:
            nouveau_mot_cache += lettre
        else:
            nouveau_mot_cache += mot_cache[i]
    return nouveau_mot_cache

#fonction utilisée dans le cas où la lettre n'appartient pas au mot à trouver
def enlever_chance(nouvelle_lettre, chances_restantes) :
    # on baisse le nombre de chance (perte d'une vie)
    chances_restantes = chances_restantes - 1
    # affichage pour l'utilisateur de l'état de la partie en cours
    print(f"La lettre {nouvelle_lettre} n'appartient pas au mot recherché, vous perdez une chance. il vous reste {chances_restantes} chances")
    return chances_restantes

#fonction principale permettant de jouer au jeu du pendu à partir de la liste de mot du fichier texte
def jouer_jeu_pendu():
    mot_a_deviner = tirage_mot()
    mot_cache = afficher_mot(mot_a_deviner)
    chances_restantes = 6
    lettres_incorrectes = []
    lettres_proposees = []
    print("Bienvenue au jeu du pendu, le jeu ne prend en entrée que des lettres minuscules et sans accent.")
    print(f"Vous avez {chances_restantes} chance(s) pour trouver le mot.")
    while chances_restantes > 0 and mot_cache != mot_a_deviner:
        nouvelle_lettre = input("Choisissez une lettre qui pourrait faire partie du mot : ")
        if not verifier_lettre_proposee(nouvelle_lettre, lettres_proposees):
            continue
        if nouvelle_lettre in mot_a_deviner:
            mot_cache = ajouter_lettre_mot_cache(mot_a_deviner, mot_cache, nouvelle_lettre)
            print(f"La lettre est présente dans le mot recherché, il vous reste encore {chances_restantes} chance(s).")
            print(f"Mot à deviner : {mot_cache}")
        else:
            chances_restantes = enlever_chance(nouvelle_lettre,chances_restantes)
            afficher_pendu(chances_restantes)
            # ajout de la lettre entrée dans la liste de lettres incorrectes
            lettres_incorrectes += [nouvelle_lettre]
            print(f"Liste des lettres ne faisant pas partie du mot : {lettres_incorrectes}")
            if chances_restantes > 0 :
                print(f"Mot cherché : {mot_cache}")

        lettres_proposees +=[nouvelle_lettre]
    #affiche en cas de victoire
    if mot_cache == mot_a_deviner:
        print(f"Victoire ! Le mot à deviner était {mot_a_deviner}, il vous restait {chances_restantes} chance(s).")
    #affichage en cas de défaite
    else:
        print(f"Dommage, vous avez perdu... Le mot à deviner était {mot_a_deviner}.")

#lancement du jeu
jouer_jeu_pendu()