import flet as ft
from Button import Button
from Tile import Tile

SIZE = 800
position = [(400, 400), (400, 500), (400, 600),
            (500, 400), (500, 500), (500, 600),
            (600, 400), (600, 500), (600, 600)]

class TileGame:
    def __init__(self):
        self.buttonlist = []
    
    def setup(self, page: ft.Page):
        page.title = "Boutons Flet"
        page.window_width = SIZE
        page.window_height = SIZE
        page.bgcolor = ft.colors.WHITE  # Définir la couleur de fond

        for i in range(8):
            x, y = position[i]
            tile = Tile(x, y)
            button = Button(i)
            self.buttonlist.append(button)
            page.controls.append(button)  # Ajouter le bouton à la page
        
        page.update()  # Mettre à jour l'affichage

def main(page: ft.Page):
    game = TileGame()
    game.setup(page)

ft.app(target=main)  # Démarrer l'application