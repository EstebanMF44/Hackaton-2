import flet as ft

def main(page):
    # Créer un carré rouge de 100x100 px
    square = ft.Container(
        width=100,
        height=100,
        bgcolor=ft.colors.RED
    )
    
    # Ajouter le carré à la page
    page.add(square)

# Lancer l'application Flet
ft.app(target=main)


