import flet as ft
from timer import PomodoroTimer

def main(page: ft.Page):
    
    page.title = "Pomodoro Timer"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 300
    page.window.height = 280
    page.window.resizable = False
    
    
    current_view = "initial"  
    is_running = False
    
    
    title_label = ft.Text("POMODORO TIMER", font_family="Comic Sans MS", size=16, weight="bold")
    
   
    initial_content = ft.Column(
        ft.Container(
            content=title_label,
            alignment=ft.Alignment(0, 0), 
            padding=ft.Padding.only(top= 5)
        ),
        ft.ElevatedButton(
            content=ft.Text("Start", font_family="Comic Sans MS"),
            on_click=lambda e: start_focus_view()
        )
    ), 


if __name__ == "__main__":
    ft.app(target=main)