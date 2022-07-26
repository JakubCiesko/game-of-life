class Rules():
    def __init__(self, grid, threshold_values):
        """
        :param grid: parameter grid, na ktory sa budu aplikovat pravidla
        :param threshold_values: prahove hodnoty, ktore rozhoduju o tom, ktore pravidlo bude aplikovane.
        """
        self.grid = grid
        self.threshold_values = threshold_values

    def apply_rules(self):
        """
            Metoda apply_rules aplikuje pravidla Game-of-life na objekt triedy Grid, objekt je touto aplikaciou zmeneny.
            Pravidla sa aplikuju postupne na vsetky bunky (cell) obsiahnute v mriezke (grid).
            :param grid: Objekt triedy Grid

        """
        field = self.grid.field
        width, height = len(field[0]), len(field)
        for row in range(height):
            for column in range(width):
                cell = self.grid.get_value((row, column))
                live_neighbor_count, dead_neighbor_count = self.grid.get_number_of_live_dead_neighbors((row, column))

                if cell.state:
                    if live_neighbor_count < self.threshold_values['underpopulation']:
                        field[row][column].change_state()
                        continue
                    elif live_neighbor_count < self.threshold_values['survive']:
                        continue
                    elif live_neighbor_count > self.threshold_values['overpopulation']:
                        field[row][column].change_state()
                else:
                    if live_neighbor_count == self.threshold_values['revive']:
                        field[row][column].change_state()
        self.grid.cycle_number += 1
        return

class EndGameTester:
    def __init__(self, grid):
        """
        :param grid: objekt triedy Grid potrebny pre vyhodnotenie End Game Testu.
        """
        self.grid = grid

    def test_change(self, field_copy):
        """
        Metoda monitoruje zmenu hodnoty field objektu triedy Grid.
        Pouziva sa na porovnanie objektu triedy Grid pred a po aplikovani pravidiel Game-of-life pre ukoncenie cyklu.
        Navracia True, ak sa field zmeni, a False, ak sa nezmeni.
        :param field_copy: list
        :return: bool grid-pred-aplikovanim-pravidiel == grid-po-aplikovani pravidiel
        """
        field_values = [[cell.get_state() for cell in row] for row in self.grid.field]
        copied_field_values = [[cell_state for cell_state in row] for row in field_copy]
        return field_values != copied_field_values