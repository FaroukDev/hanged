'''
'Etape 1 :
Importer une Liste de potence
Choisir le mot aléatoire
Definir la taille du mot
Nombre de lettre trouvé
Nombre d'echec = 0

Etape 2
Do Voulez vous jouer Y/N
  Tant que nbre echec < 5 OR Nombre de lettre à trouver
    Tant que l'utilisateur ne rentre pas un caractere
        Demander à l'utilisateur seulement un caractere,

    Convertir ce caractere
    Si la lettre existe dans le mot :
        afficher le mot caché mise à jour avec l'emplacement
    SiNo
        Afficher la potence corespendante
        incrementer nombre echec ++

  Si nombre tentative ==0
     écrire Perdu


 Class Pendu
    attribbut : mot à deviner,
    attribut nbre de tentative restantes
    attribut  nbre d'échec


    Définir les variables
    fonction recupérer le mot
    fonction vérifier si la lettre existe dans le mot
    fonction récuperer la lettre
    fonction (nbre d'eche)
        print potence
'''

from random_word import RandomWords

r = RandomWords()

r.get_random_word()

print(r.get_random_word())

nbr_letter_to_find = 5
nbr_fail = 0

my_try = input("Welcome to my game find my word ! ahaha : ")

while nbr_fail < 5 or len(nbr_letter_to_find):



