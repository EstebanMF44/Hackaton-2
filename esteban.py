import numpy as np
import flet as ft



class GameObject():
    pass

class Tile(GameObject):
    def __init__(self, x, y, number) -> None:
        self._x = x # Line index
        self._y = y # Column index
        
    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        if value < 0 or value > 2:
            raise ValueError("Invalid value for x")
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        if value < 0 or value > 2:
            raise ValueError("Invalid value for y")
        self._y = value
    
    def draw(self) -> None:
        pass
        

class Move(Tile):
    def __init__(self, number, x, y):
        super().__init__(number, x, y)

    def droite(self):
        self.x += 1

    def gauche(self):
        self.x -= 1
    
    def haut(self):
        self.y -= 1

    def bas(self): 
        self.y += 1

class Choose(Tile):
    def __init__(self, number, x, y):
        super().__init__(number, x, y)

    def choose(self):
        pass



class Background(GameObject):


    def on_key_press(self, event, modifiers):
        if event.key == "ArrowRight":
            for tile in self.tilelist:
                tile.droite()
        elif event.key == "ArrowLeft":
            for tile in self.tilelist:
                tile.gauche()
        elif event.key == "ArrowUp":
            for tile in self.tilelist:
                tile.haut()
        elif event.key == "ArrowDown":
            for tile in self.tilelist:
                tile.bas()
    