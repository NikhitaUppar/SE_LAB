from board import Board
from ai import AI

class Battleship:
    def __init__(self):
        self.player = Board()
        self.enemy = Board()
        self.ai = AI()
        self._setup()

    def _setup(self):
        # Player has 2 ships
        self.player.place_ship({(0,0),(0,1),(0,2)})
        self.player.place_ship({(3,3),(3,4)})
        # Enemy has 2 ships
        self.enemy.place_ship({(1,1),(1,2),(1,3)})
        self.enemy.place_ship({(4,4),(4,5)})

    def show(self):
        remaining = len(self.enemy.all_cells - self.enemy.shots)
        print(f"\nEnemy ship cells remaining: {remaining}")
        print("Enter row,col (1-6) or 'q' to quit.")

    def run(self):
        print("=== Battleship ===")
        while True:
            self.show()
            raw = input("> ").strip().lower()
            if raw == "q":
                return

            # --- Player shot ---
            try:
                r, c = map(int, raw.split(","))
                pos = (r - 1, c - 1)
            except ValueError:
                print("Use row,col like 2,3.")
                continue

            if not (0 <= pos[0] < Board.SIZE and 0 <= pos[1] < Board.SIZE):
                print("Outside board (1-6 for both row and col).")
                continue

            if pos in self.enemy.shots:
                print("Already fired there.")
                continue

            hit = self.enemy.fire(pos)
            if hit:
                sunk = self.enemy.ship_sunk(pos)
                if sunk:
                    print("HIT! You sank a ship!")
                else:
                    print("HIT!")
            else:
                print("MISS.")

            if self.enemy.all_sunk():
                print("You sank the entire fleet. You win!")
                return

            # --- AI shot ---
            ai_pos = self.ai.choose()
            if ai_pos is None:
                print("AI has no moves left.")
                return

            print(f"AI fired at {ai_pos[0]+1},{ai_pos[1]+1}")
            ai_hit = self.player.fire(ai_pos)
            if ai_hit:
                sunk = self.player.ship_sunk(ai_pos)
                if sunk:
                    print("AI scored a hit and sank your ship!")
                else:
                    print("AI scored a hit!")
                self.ai.notify_hit(ai_pos)
            else:
                print("AI missed.")

            if self.player.all_sunk():
                print("AI sank your entire fleet. You lose.")
                return