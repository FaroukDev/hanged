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

#from random_word import RandomWords

#r = RandomWords()

#r.get_random_word()
'''
nbr_letter_to_find = 5
nbr_fail = 0
word_to_find = "Farouk"
my_caracter = ""

my_try = input("Welcome to my game find my word ! please enter a caracter : ")
while nbr_fail < 5 or len(nbr_letter_to_find) != len(word_to_find):
    while my_try == "":
        my_try = input("Enter one caracter :")
        my_try.isalpha()
        print(my_try)
    for my_try in list(word_to_find):
        if my_try == word_to_find:
            print("yes")
        else:
            print("no")
        break

'''
f = open("hang.py","r")
content = f.read()
print(content)


guesses = []
count = 1
word_to_find = 'python'
word = []

while count < 10:
    guess = input('guess a letter: ')
    guesses.append(guess)
    if ''.join(word) == word_to_find:
        print('you win')
        break
    elif len(guess) > 1 and word_to_find == guess:
        print(word_to_find)
        print('you win')
        break
    else:
        for char in word_to_find:
            if char in guesses and len(stages) - 1:
                word.append(char)
                print(char)
            else:
                print('_')
        count += 1
else:
    print('\nyou lose')