import flet as ft

import flet as ft

def main(page):
    # Créer un carré rouge de 100x100 px
    square = ft.Container(
        width=100,
        height=100,
        bgcolor=ft.colors.RED,
    )
    
    # Créer une colonne (Column) et ajouter le carré
    column_1 = ft.Column(
        controls=[square],  # Ajouter le carré à la colonne
        alignment=ft.alignment.center  # Centrer le carré dans la colonne
    )
    
    
    
    
    
    # Créer une colonne (Column) et ajouter le carré
    row1 = ft.Row(
        controls=[square],  # Ajouter le carré à la colonne
        alignment=ft.alignment.center_right  # Centrer le carré dans la colonne
    )
    # Ajouter la colonne à la page
    page.add(row1,column_1)

# Lancer l'application Flet
ft.app(target=main)



