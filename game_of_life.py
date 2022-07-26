from grid.gridobject.grid import Grid
from grid.gridfunctions.gridfn  import generate_game_field
from cell.cellobject.cellobj import Cell
from functions.inputfunctions import get_input, replay_input
from functions.displayfunctions import final_screen_print
from rules.rulesobject.rules import Rules, EndGameTester
from time import sleep

#APP LOOP
game = True
while game:
    #PLAYER'S INPUT - INITIAL STATE SETTINGS
    width, height, time_delay, live_cell_symbol, dead_cell_symbol = get_input()

    #SETTINGS DICT
    game_of_life_settings = {
        'life_symbol': live_cell_symbol,
        'death_symbol': dead_cell_symbol,
        'replay_key': 'x',
        'time_delay': time_delay,
        'threshold_values': {'underpopulation': 2,
                            'survive': 4,
                            'overpopulation': 3,
                            'revive': 3
                            }
    }

    #GRID CREATION
    grid = generate_game_field(width,height,Cell)
    grid = Grid(grid,1,life_symbol = game_of_life_settings['life_symbol'],
                death_symbol = game_of_life_settings['death_symbol'])

    #RULES CREATION
    rules = Rules(grid,game_of_life_settings['threshold_values'])

    #CREATION OF CYCLE TESTER CONDITION OBJECT
    tester = EndGameTester(grid)

    # GAME OF LIFE LOOP
    condition = True
    while condition:
        print(grid)
        grid_field_values_copy = [[cell.get_state() for cell in row] for row in grid.field]
        #Applying rules on grid
        rules.apply_rules()
        sleep(game_of_life_settings['time_delay'])
        #Testing condition
        condition = tester.test_change(grid_field_values_copy)

    #FINAL SCREEN & REPLAY OPTION
    final_screen_print(grid)
    game = replay_input(game_of_life_settings['replay_key'])
