from Tile import Tile
import flet as ft


class Button(Tile):
    def __init__(self, number) -> None:
        super.__init__()
        self.bgcolor = ft.Colors.WHITE
        self.color = ft.Colors.BLACK
        self.number = number
        self.position = Tile.x, Tile.y

    def draw(self, Page) -> None:
        '''dessine le bouton sur l'écran'''
        square = ft.Container(
        width=self._position[0],
        height=self._position[1],
        bgcolor=ft.colors.RED)

    
    





    
    

    
