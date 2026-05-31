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
    
    
    def on_timer_finish():
        if fab.icon != ft.Icons.START:
            fab.icon = ft.Icons.START
            page.update()
    
    pomodoro = PomodoroTimer(page, on_finish_callback=on_timer_finish)
    
    fab = ft.FloatingActionButton(
        icon=ft.Icons.START, 
        shape=ft.StadiumBorder(),
        on_click=lambda e: handle_fab_click(e, page, pomodoro, fab)
    )
    
    page.floating_action_button = fab
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.Colors.YELLOW_800,
        shape=ft.CircularRectangleNotchShape(),
        content=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.HOME, 
                    icon_color=ft.Colors.WHITE,
                    tooltip="Reset (25 min)",
                    on_click=lambda e: handle_home_click(e, page, pomodoro, fab)
                ),
                ft.Container(expand=True),
                
                ft.IconButton(
                    icon=ft.Icons.SNOOZE, 
                    icon_color=ft.Colors.WHITE,
                    tooltip="Snooze (5 min)",
                    on_click=lambda e: handle_snooze_click(e, page, pomodoro, fab)
                ),
            ]
        ),
    )

    page.add(
        ft.SafeArea(
            content=ft.Column(
                [
                    pomodoro.get_timer_text()
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
    )

    def handle_fab_click(e, page, timer_obj, btn):
        if timer_obj.timer_text.value == "00:00":
            if timer_obj.get_mode() == "snooze":
                timer_obj.reset() 
            timer_obj.start()
            btn.icon = ft.Icons.PAUSE
            page.update()
            return

        if timer_obj.get_status():
            timer_obj.pause()
            btn.icon = ft.Icons.PLAY_ARROW
        
        else:
            timer_obj.start()
            btn.icon = ft.Icons.PAUSE
            
        page.update()

    def handle_snooze_click(e, page, timer_obj, btn):
        timer_obj.set_snooze()
        btn.icon = ft.Icons.START
        page.update()

    def handle_home_click(e, page, timer_obj, btn):
        timer_obj.reset()
        btn.icon = ft.Icons.START
        page.update()

ft.run(main)