# Pomodoro Timer
[![Flet](https://img.shields.io/badge/Flet-0.85.2-orange)](https://flet.dev)
[![Python](https://img.shields.io/badge/Python-3.10%2B-yellow)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)
This Pomodoro was built as a personal learning exercise to improve my Python skills and gain experience with **Flet**

<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
  <img src="./images/focus.png" width="300">
  <img src="./images/break.png" width="300">
</div>

## Upcoming Features
- Customizable Focus/Break durations
- Short vs Long break options
- Improved UI/Visual design
- Always on Top mode
- Sound effects

## Run from Source
1. Clone the repository:
```bash
git clone https://github.com/lieserl-git/PomodoroTimer.git
cd PomodoroTimer
```
2. Install Dependencies:
```bash
pip install flet pyinstaller
```
3. Build command: This command creates a standalone executable in the dist folder
```bash
pyinstaller --onefile --windowed --name "PomodoroTimer" src/main.py
```

