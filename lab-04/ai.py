import random

class AI:
    def __init__(self, size=6):
        self.size = size
        self.tried = set()
        self.hunt_targets = []   # priority queue after a hit

    def notify_hit(self, pos):
        """Called by game when AI scores a hit — adds adjacent cells."""
        r, c = pos
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            candidate = (nr, nc)
            if (0 <= nr < self.size and 0 <= nc < self.size
                    and candidate not in self.tried
                    and candidate not in self.hunt_targets):
                self.hunt_targets.append(candidate)

    def choose(self):
        # Drain priority targets first
        while self.hunt_targets:
            pos = self.hunt_targets.pop(0)
            if pos not in self.tried:
                self.tried.add(pos)
                return pos

        options = [(r, c) for r in range(self.size)
                           for c in range(self.size)
                           if (r, c) not in self.tried]
        if not options:
            return None
        pos = random.choice(options)
        self.tried.add(pos)
        return pos