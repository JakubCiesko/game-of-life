import gamefieldfunctions.functions as gff
import time



width = int(input('zadaj sirku: '))
height = int(input('zadaj vysku: '))
game_field = gff.generate_game_field(width,height)
cycle_number = 0


while True:
    cycle_number+=1
    game_field = gff.apply_rules(game_field)
    time.sleep(0.025)
    gff.print_game_field(game_field, cycle_number)

