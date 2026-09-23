import random
from .item import Item


class Room:
    def __init__(self, name, description=""):
        self.room_name = name
        self.description = description
        self.items = []

        if random.randint(1, 2) == 1: # 50 prosentin mahdollisuus generoida esine
            self.generate_item()

    def generate_item(self):
        tavara_lista = [
            Item("Avain", 0.1),
            Item("Kolikko", 0.01),
            Item("Kartta", 0.2),
            Item("Taskulamppu", 0.3),
            Item("Jakoavain", 0.8),
            Item("Vasara", 1.2),
            Item("Ruuvimeisseli", 0.4),
            Item("Köysi", 1.0),
            Item("Juomapullo", 0.5),
            Item("Ensiapupakkaus", 0.3),
        ]
        self.items.append(random.choice(tavara_lista))
