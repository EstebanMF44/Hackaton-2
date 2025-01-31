from Tile import Tile
import flet as ft


class Button(Tile):
    def __init__(self, x, y, number):
        Tile.__init__(self, x, y)  # Initialiser Tile
        ft.Container.__init__(self)  # Initialiser ft.Container

        self.number = number
        self.left = x  # Position X
        self.top = y   # Position Y
        self.width = 50  # Taille du bouton
        self.height = 50
        self.bgcolor = ft.colors.RED  # Couleur de fond
        self.content = ft.Text(str(number), color=ft.colors.WHITE)  # Texte affiché


    def draw(self, Page) -> None:
        '''dessine le bouton sur l'écran'''
        square = ft.Container(
        width=self._position[0],
        height=self._position[1],
        bgcolor=ft.colors.RED)
        Page.add(square)

    
    





    
    

    
