import flet as ft
import asyncio

class PomodoroTimer:
    def __init__(self, page: ft.Page, default_duration: int = 25, snooze_duration: int = 5, on_finish_callback=None):
        self.page = page
        self.default_duration = default_duration * 60  
        self.snooze_duration = snooze_duration * 60    
        
        self.remaining_seconds = self.default_duration
        self.is_running = False
        self.current_mode = "pomodoro"  
        self.timer_task = None
        self.on_finish_callback = on_finish_callback  
        
        self.timer_text = ft.Text(
            value=self._format_time(self.remaining_seconds),
            font_family="Comic Sans MS",
            size=50,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.YELLOW_800,
        )

    def _format_time(self, seconds: int) -> str:
        mins = seconds // 60
        secs = seconds % 60
        return f"{mins:02d}:{secs:02d}"

    async def _countdown(self):
        '''Asynchronous countdown task'''
        while self.remaining_seconds > 0 and self.is_running:
            await asyncio.sleep(1)
            self.remaining_seconds -= 1
            self.timer_text.value = self._format_time(self.remaining_seconds)
            self.page.update()
        
        if self.remaining_seconds == 0 and self.is_running:
            self.timer_text.value = "00:00"
            self.page.update()
            self.stop()
            
            if self.on_finish_callback:
                self.on_finish_callback()

    def start(self) -> bool:
        if not self.is_running:
            self.is_running = True
            self.timer_task = asyncio.create_task(self._countdown())
            return True
        return False

    def pause(self) -> bool:
        if self.is_running:
            self.is_running = False
            if self.timer_task:
                self.timer_task.cancel()
            return True
        return False

    def toggle(self) -> bool:
        if self.is_running:
            self.pause()
            return False
        else:
            self.start()
            return True

    def reset(self):
        self.stop()
        self.current_mode = "pomodoro"
        self.remaining_seconds = self.default_duration
        self.timer_text.value = self._format_time(self.remaining_seconds)
        self.page.update()

    def set_snooze(self):
        self.stop()
        self.current_mode = "snooze"
        self.remaining_seconds = self.snooze_duration
        self.timer_text.value = self._format_time(self.remaining_seconds)
        self.page.update()

    def stop(self):
        self.is_running = False
        if self.timer_task:
            self.timer_task.cancel()

    def get_timer_text(self) -> ft.Text:
        return self.timer_text

    def get_status(self) -> bool:
        return self.is_running

    def get_mode(self) -> str:
        return self.current_mode

    def is_at_initial_time(self) -> bool:
        if self.current_mode == "pomodoro":
            return self.remaining_seconds == self.default_duration
        else:
            return self.remaining_seconds == self.snooze_duration
