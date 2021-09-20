"""
Practice  2_1
Data Structures
"""

from pprint import pprint


# How we can store numbers?
# simple variables
num_1, num_2, num_3 = 123, 234, 678


# list of variables
list_of_variables = [num_1, num_2, num_3]  # what's this option pros and cons?


# what if I want to bond all this number scores with corresponding players?
player_1, player_2, player_3 = 'Ivan', 'Vasiliy', 'Petr'  # not effective to keep in mind relations
list_of_players = [player_1, player_2, player_3]  # relations are visible as indexes, what about order and support?

# add new player?
player_4, num_4 = 'Olga', 1000
list_of_players.append(player_4), list_of_variables.append(num_4)

print(f"""Players: {list_of_players}
Scores: {list_of_variables}""")  # all this data storage will be broken, when we will try to sort it

# need another more effective structure to store this info
# dictionary
table_score = dict()
for player_id in range(len(list_of_players)):
    table_score[list_of_players[player_id]] = list_of_variables[player_id]

pprint(table_score)
