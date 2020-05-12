import random
from termcolor import colored
amount_of_players = int(input("Number of players:"))
amount_of_game_rules = int(input("amount of game rules per game:"))
players = []
game_rule = ['Knifed = drink','zeused = drink','killed by lesser players = drink','aced = drink','round loss = drink','Killed = Drink','negev killed = drink']
round_rule = ['Knife only','Negev Only','No gravity','Third Person','Infinity Ammo','No recoil','Slow-mo','Grenades Only','Shotgun Only','Pistol only','Deg Only','Snipers only','no-scope only','shift walk only','crouch only','T head start 30s','CT head start 30s']
x = 0
# Game Rules


def games():
    for i in range(amount_of_game_rules):
        game_picker = random.randint(0, len(game_rule) - 1)
        print(colored("Game Rule:", 'red'), game_rule[game_picker])
games()
for i in range(amount_of_players):
    players.append(i+1)


for x in range(amount_of_players):
    players[x] = input("Players Name:")
print("Start Your Game")


# Rounds
def rounds():
    round_picker = random.randint(0, len(round_rule)-1)
    print(colored("Round Rule:", 'yellow'), round_rule[round_picker])
    drink_picker = random.randint(1, 100)
    if drink_picker <= 50:
        player_picker = random.randint(0, amount_of_players-1)
        print(colored("Sorry:", 'blue'), players[player_picker])
    elif drink_picker <= 90:
        print(colored('No-one drink', 'green'))
    elif drink_picker <= 100:
        print(colored('Everyone drink', 'red'))
    main()


def main():
    new_round = input("New Round:(Y/N)")
    if new_round == "Y" or new_round == "y":
        random_event = random.randint(0, 100)
        if random_event <= 33:
            random_player1 = players[random.randint(0, len(players)-1)]
            random_player2 = players[random.randint(0, len(players) - 1)]
            event = random_player1, "and", random_player2, "fight to the death"
            print(colored(event, 'red'))
        print("##################################")
        rounds()
    if new_round == "N" or new_round == "n":
        new_game = input("New Game:(Y/N)")
        if new_game == "Y" or new_game == "y":
            games()
        else:
            print("Beta.")
            exit()


main()
