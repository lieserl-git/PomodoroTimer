class PomodoroTimer:
    def __init__(self, root, label):
        self.root = root
        self.label = label
        self.remaining = 0
        self.after_id = None
        self.active = False

    def start(self, seconds):
        self.remaining = seconds
        self.active = True
        self._tick()

    def _tick(self):
        if self.remaining > 0 and self.active:
            mins, secs = divmod(self.remaining, 60)
            self.label.config(text=f"{mins:02d}:{secs:02d}")
            self.remaining -= 1
            self.after_id = self.root.after(1000, self._tick)
        else:
            self.label.config(text="00:00")
            self.active = False

    def pause(self):
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None
        self.active = False

    def resume(self):
        if not self.active and self.remaining > 0:
            self.active = True
            self._tick()