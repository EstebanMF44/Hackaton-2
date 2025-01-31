from .Tile import Tile
import felt as ft

class Button(Tile):
    def __init__(self, number):
        super.__init__()
        self.bgcolor = ft.Colors.WHITE
        self.color = ft.Colors.BLACK
        self.number = number

def __repr__(self):
    
