def is_position_possible(field_dimensions, position):
    width, height = field_dimensions
    if 0 <= position[0] < height and 0 <= position[1] < width:
        return True
    return False

def get_cell_value(field, cell_position):
    row, column = cell_position
    return field[row][column]

def get_neighbors_positions(cell_position, field_dimensions):
    row, column = cell_position
    neighbors_positions = [(nrow, ncol) for nrow in range(row - 1, row + 2) for ncol in range(column - 1, column + 2)]
    neighbors_positions.remove((row, column))
    neighbors_positions = [position for position in neighbors_positions if is_position_possible(field_dimensions,position)]
    return neighbors_positions

def get_number_of_live_dead_neighbors(field, cell_position):
    width, height = len(field[0]), len(field)
    neighbors_positions = get_neighbors_positions(cell_position, (width,height))
    neighbors = [get_cell_value(field,cell_position) for cell_position in neighbors_positions]
    number_of_dead_neighbors = neighbors.count(False)
    number_of_live_neighbors = neighbors.count(True)
    return number_of_live_neighbors,number_of_dead_neighbors



