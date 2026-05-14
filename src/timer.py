class PomodoroTimer:
    def __init__(self, root, label):
        self.root = root
        self.label = label
        self.restante = 0
        self.after_id = None
        self.ativo = False

    def iniciar(self, segundos):
        self.restante = segundos
        self.ativo = True
        self._tick()

    def _tick(self):
        if self.restante > 0 and self.ativo:
            mins, secs = divmod(self.restante, 60)
            self.label.config(text=f"{mins:02d}:{secs:02d}")
            self.restante -= 1
            self.after_id = self.root.after(1000, self._tick)
        else:
            self.label.config(text="00:00")
            self.label.config(text="DONE")
            self.ativo = False

    def pausar(self):
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None
        self.ativo = False

    def continuar(self):
        if not self.ativo and self.restante > 0:
            self.ativo = True
            self._tick()