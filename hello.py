import random

# verification: une fonction lambda qui retourne le résultat associé à chaque cas
verification = lambda guess, i: 'Trop grand' if guess > secret else 'Trop petit' if guess < secret else 'Gagné en {essais} essais !'.format(essais=i + 1)
MAX_ATTEMPTS = 6
secret = random.randint(0, 100)
stop = False # Variable intérmédiaire qui sert à arrêter le jeu si le joueur gagne

for i in range(MAX_ATTEMPTS):
    if not stop:
        guess = int(input())
        # Si l'utilisateur a utilisé toutes ses essais alors on écrit qu'il a perdu au lieu d'appeler la fonction verification
        if i + 1 == MAX_ATTEMPTS and guess != secret: print('Perdu ! Le secret était ', secret)
        else: print(verification(guess, i))
        if guess == secret:
            stop = True



# import random
# NB_ESSAIS_MAX = 6
# secret = random.randint(0, 100)
# i = 0
# win = False
# while i < NB_ESSAIS_MAX and not win:
#     i += 1
#     guess = int(input())
#     if guess == secret:
#         print('Gagné en ', i, ' essais !' )
#         win = True
#     elif i == NB_ESSAIS_MAX:
#         print('Perdu ! Le secret était ', secret)
#     elif guess > secret:
#         print('Trop grand')
#     else: 
#         print('Trop petit')
