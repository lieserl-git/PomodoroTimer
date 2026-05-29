import flet as ft
from timer import PomodoroTimer

def main(page: ft.Page):
    page.title = "Pomodoro Timer"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 300
    page.window.height = 300
    page.window.resizable = False
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.YELLOW)
    
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.START, 
        shape=ft.StadiumBorder(),
    
    )
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.Colors.YELLOW_800,
        shape=ft.CircularRectangleNotchShape(),
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.PAUSE, icon_color=ft.Colors.WHITE),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.Icons.SNOOZE, icon_color=ft.Colors.WHITE),
                
            ]
        ),
    )

    page.add(
    ft.SafeArea(
        content=ft.Column(
            [
                ft.Text(
                    value="25:00",
                    font_family="Comic Sans MS",
                    size=50,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.YELLOW_800,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
)

ft.run(main)    
    
    
   


