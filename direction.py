import flet as ft

class Direction():

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