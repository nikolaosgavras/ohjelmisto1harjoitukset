class Player:
    def __init__(self, name, itemsList, location):
        self.player_name = str(name)
        self.player_items = itemsList
        self.player_location = location # tämänhetkinen Room olio
    def move(self, direction):
        self.move_diretion = direction
    def take_item(self, item):
        self.player_items.append(item)
        self.player_location.remove_item(item)
    def move_to_room(self, room):
        self.player_location = room

