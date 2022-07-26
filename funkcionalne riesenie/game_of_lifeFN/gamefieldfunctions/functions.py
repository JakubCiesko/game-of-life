import random
import cellfunctions.functions as cf
import os

def generate_game_field(width: int, height: int):
    values = (True, False)
    return [[random.choice(values) for _ in range(width)] for _ in range(height)]

def print_game_field(field, cycle_number):
    os.system('cls')
    print(f'\n\t\t\033[93m\033[96mGAME OF LIFE\n\tCycle: {cycle_number}\n')
    for row in field:
        row_string = '\t\033[92m'
        for col in row:
            if col:
                row_string += '■'
            else:
                row_string += ' '
        print(row_string)

def apply_rules(field):
    width, height = len(field[0]), len(field)
    for row in range(height):
        for column in range(width):
            cell = field[row][column]
            live_neighbor_count, dead_neighbor_count = cf.get_number_of_live_dead_neighbors(field, (row,column))
            if cell:
                if live_neighbor_count < 2:
                    field[row][column] = False
                    continue
                elif live_neighbor_count < 4:
                    continue
                elif live_neighbor_count > 3:
                    field[row][column] = False
            else:
                if live_neighbor_count == 3:
                    field[row][column] = True
    return field
