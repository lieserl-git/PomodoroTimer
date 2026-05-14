import tkinter as tk
from tkinter import ttk
from timer import PomodoroTimer

# ---------- Main window ----------
window = tk.Tk()
window.geometry("300x280")
window.title("Pomodoro Timer")

# ---------- Notebook (tabs) ----------
notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

# Tab containers
focus_tab = ttk.Frame(notebook)
break_tab = ttk.Frame(notebook)

notebook.add(focus_tab, text="Focus")
notebook.add(break_tab, text="Break")

# ================== FOCUS TAB ==================
initial_frame = ttk.Frame(focus_tab)
timer_frame = ttk.Frame(focus_tab)

# --- Initial screen ---
title_label = tk.Label(initial_frame, text="POMODORO TIMER", font=("Comic Sans MS", 12))
title_label.pack(padx=20, pady=(20, 10))

start_button = tk.Button(initial_frame, text="Start", font=("Comic Sans MS", 10),
                         command=lambda: show_timer())
start_button.pack(padx=10, pady=(0, 20))

initial_frame.pack(fill="both", expand=True)

# --- Timer screen ---
focus_timer_label = tk.Label(timer_frame, text="25:00", font=("Helvetica", 32))
focus_timer_label.pack(pady=20)

# Frame contêiner para centralizar os botões
focus_button_frame = ttk.Frame(timer_frame)
focus_button_frame.pack(pady=(0, 20))

focus_pause_button = tk.Button(focus_button_frame, text="Pause", font=("Comic Sans MS", 10))
focus_pause_button.pack(side=tk.LEFT, padx=5)

focus_menu_button = tk.Button(focus_button_frame, text="Menu", font=("Comic Sans MS", 10))
focus_menu_button.pack(side=tk.LEFT, padx=5)

# Instantiate focus timer
focus_timer = PomodoroTimer(window, focus_timer_label)

# --- Focus control functions ---
def show_timer():
    initial_frame.pack_forget()
    timer_frame.pack(fill="both", expand=True)
    focus_timer.start(5)  # test with 5 seconds
    focus_pause_button.config(text="Pause", command=pause_focus)

def pause_focus():
    focus_timer.pause()
    focus_pause_button.config(text="Resume", command=resume_focus)

def resume_focus():
    focus_timer.resume()
    focus_pause_button.config(text="Pause", command=pause_focus)

def back_to_menu():
    focus_timer.pause()
    timer_frame.pack_forget()
    initial_frame.pack(fill="both", expand=True)

focus_pause_button.config(command=pause_focus)
focus_menu_button.config(command=back_to_menu)

# ================== BREAK TAB ==================
break_timer_label = tk.Label(break_tab, text="05:00", font=("Helvetica", 32))
break_timer_label.pack(pady=20)

break_button_frame = ttk.Frame(break_tab)
break_button_frame.pack()

break_start_button = tk.Button(break_button_frame, text="Start", font=("Comic Sans MS", 10))
break_start_button.pack(side=tk.LEFT, padx=5)

break_pause_button = tk.Button(break_button_frame, text="Pause", font=("Comic Sans MS", 10))
break_pause_button.pack(side=tk.LEFT, padx=5)

break_timer = PomodoroTimer(window, break_timer_label)

def start_break():
    break_timer.start(5)  # test with 5 seconds
    break_pause_button.config(text="Pause", command=pause_break)

def pause_break():
    break_timer.pause()
    break_pause_button.config(text="Resume", command=resume_break)

def resume_break():
    break_timer.resume()
    break_pause_button.config(text="Pause", command=pause_break)

break_start_button.config(command=start_break)
break_pause_button.config(command=pause_break)

window.mainloop()