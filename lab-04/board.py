class Board:
    SIZE = 6

    def __init__(self):
        self.ships = []      # list of sets, one per ship
        self.shots = set()

    def place_ship(self, cells):
        self.ships.append(set(cells))

    @property
    def all_cells(self):
        return {cell for ship in self.ships for cell in ship}

    def fire(self, pos):
        self.shots.add(pos)
        return pos in self.all_cells

    def ship_sunk(self, pos):
        """Return the ship set if pos just sank it, else None."""
        for ship in self.ships:
            if pos in ship and ship <= self.shots:
                return ship
        return None

    def all_sunk(self):
        return self.all_cells <= self.shots