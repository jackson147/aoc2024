
class Guard:
    def __init__(self, pos, direction):
        self.pos = pos
        self.direction = direction
        
    def seralise(self) -> str:
        x,y = self.pos
        return f"{x}|{y}|{self.direction}"