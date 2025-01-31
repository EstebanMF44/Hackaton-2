from .Tile import Tile
import felt as ft
'''cette classe représente un bouton dans le jeu avec felt comme librairie graphique, elle dessine aussi le bouton le rectangle du bouton et le chiffre'''
class Button(Tile):
    def __init__(self, number) -> None:
        super.__init__()
        self.bgcolor = ft.Colors.WHITE
        self.color = ft.Colors.BLACK
        self.number = number
        self.position = Tile.x, Tile.y

    def draw(self, screen) -> None:
        '''dessine le bouton sur l'écran'''
        screen.draw_rect(self.position, self.size, self.bgcolor)
        screen.draw_text(str(self.number), self.position, self.color)

    def draw_rect(self, screen) -> None:
        '''dessine le rectangle du bouton'''
        screen.draw_rect(self.position, self.size, self.color)
    

    
