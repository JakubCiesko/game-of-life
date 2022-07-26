class Cell:
    def __init__(self, state, position):
        """
        :param state: bool stav bunky: True - Ziva, False - Mrtva
        :param position: iterable (x,y) - pozicia bunky v hracom poli
        """
        self.state =  state
        self.position = position

    def get_state(self):
        """
        Navracia hodnotu state objektu triedy Cell
        :return:  state
        """
        return self.state

    def set_state(self, state_value):
        """
        Funkcia meni hodnotu state objektu triedy Cell na zadanu hodnotu state_value
        :param state_value: Zvolena hodnota, ktora ma byt nastavena
        :return:
        """
        self.state = state_value

    def change_state(self):
        """
        Funkcia meni hodnotu state objektu triedy Cell na jej negaciu:
        :return: True if self.state == False else False
        """
        self.set_state(not self.get_state())
