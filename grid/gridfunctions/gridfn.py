import random


def generate_game_field(width: int, height: int, obj):
    """
    Funkcia generuje 2Dpole objektov (obj). Objekty su iniciovane pomocou pozicie (x,y) a nahodne zvolenej bool hodnoty
    True alebo False: obj(bool, (x,y))
    :param width: int sirka hracieho pola
    :param height: int vyska hracieho pola
    :param obj: objekt, ktory obsadi vsetky pozicie na hracom poli
    :return: list: list listov zaplneny zvolenymi objektami
    """
    values = (True, False)
    return [[obj(random.choice(values), (y,x))  for x in range(width)] for y in range(height)]


