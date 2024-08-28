import random
import time
import os

# --------------- Players  --------------- #
print()

while True:  
    try: 
        players = int(input("Combien y-a-t'il de joueurs ? "))
        break
    except:
        print("Ce n'est pas un chiffre.")

nb_player = int(players)
player_names =[]
for i in range(0, nb_player):
    name = input(f"\nJoueur {i+1}, quel est votre nom: ")
    player_names.append(name)

# --------------- Des  --------------- #

print()

while True:  
    try: 
        des = int(input("Combien de dés utilisez-vous? "))
        break
    except:
        print("Ce n'est pas un chiffre.")

nb_des = int(des)

# --------------- Script  --------------- #

nb_lancer = 0

try:
    while True:
        nb_lancer += 1
        print(f"\n  Tour n° {nb_lancer}")
        for p in range(0, nb_player):
            input(f"\n{player_names[p]}, à vous de lancer les dés ")
            print("")
            total = 0
            for v in range(0, nb_des):
                val = 7
                for i in range(0, 6):
                    val -= 1
                    print(val, end='\r', flush=True)
                    time.sleep(.15)
                value = random.randint(1, 6)
                total += value
                print(f"Dés {v+1}: {value}")
                time.sleep(1)
            #print(f"\nTotal: {total}")
            print(f"\n{player_names[p]}, avancez de {total} cases.")
            time.sleep(5)
except KeyboardInterrupt:
    os.system('cls')
    print("\n\n### Le jeu est terminé. ###\n")
    time.sleep(5)
    os.system('cls')