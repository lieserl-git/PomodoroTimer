import flet as ft

def main(page: ft.Page):
    page.title = "Pomodoro Timer"
    page.add(ft.Text(value="POMODORO", font_family = "Comic Sans MS"))
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 300        
    page.window.height = 280       
    page.window.resizable = False  
    page.update()
    




ft.app(target=main)
