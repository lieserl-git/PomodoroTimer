import asyncio
class PomodoroTimer:
    def __init__(self,update_callback):
        self.update_callback = update_callback
        self.remaining = 0
        self.active = False
        self.task = None

    def start(self, seconds):
        self.remaining = seconds
        self.active = True
        if self.task:
            self.task.cancel()
        self.taks = asyncio.create_task(self._tick_loop())
    
    async def _tick_loop(self):
        while self.remaining > 0 and self.active:
            await asyncio.sleep(1)
            if self.active:
                self.remaining -= 1
                mins, secs = divmod(self.remaining, 60)
                self.update_callback(f"{mins:02d}:{secs:02d}")
        if self.remaining == 0 and self.active:
            self.active = False
            self.update_callback("00:00")

    def pause(self):
        self.active = False
        if self.task:
            self.task.cancel()
    
    def resume(self):
        if not self.active and self.remaining > 0:
            self.active = True
            self.taks = asyncio.create_task(self._tick_loop())