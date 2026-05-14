import tkinter as tk
from timer import PomodoroTimer

window = tk.Tk()
window.geometry("300x200")
window.title("Pomodoro Timer")

frame_menu = tk.Frame(window)
frame_timer = tk.Frame(window)

# ------------------- Funções de controle -------------------
def abrir_timer():
    frame_menu.pack_forget()
    frame_timer.pack(fill="both", expand=True)
    timer.iniciar(5)   # 5 segundos para teste
    btn_pause.config(text="Pause", command=pausar)

def pausar():
    timer.pausar()
    btn_pause.config(text="Resume", command=continuar)

def continuar():
    timer.continuar()
    btn_pause.config(text="Pause", command=pausar)

def voltar_menu():
    timer.pausar()
    frame_timer.pack_forget()
    frame_menu.pack(fill="both", expand = True)

# ------------------- Tela inicial (menu) -------------------
titulo = tk.Label(frame_menu, text="POMODORO TIMER", font=('Comic Sans MS', 12))
titulo.pack(padx=20, pady=(20, 10))

start = tk.Button(frame_menu, text="Start", font=('Comic Sans MS', 10), command=abrir_timer)
start.pack(padx=10, pady=(0, 20))

# ------------------- Tela do timer -------------------
timer_label = tk.Label(frame_timer, text="25:00", font=("Helvetica", 32))
timer_label.pack(pady=20)

btn_pause = tk.Button(frame_timer, text="Pause", font=('Comic Sans MS', 10), command=pausar)
btn_pause.pack(pady=(0, 20), anchor='center')

btn_menu = tk.Button(frame_timer, text="Menu", font=('Comic Sans MS', 10), command=voltar_menu)
btn_menu.pack(side=tk.RIGHT, padx=5)




timer = PomodoroTimer(window, timer_label)


frame_menu.pack(fill="both", expand=True)

window.mainloop()