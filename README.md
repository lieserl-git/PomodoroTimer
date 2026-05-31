# 🍅 Pomodoro Timer
[![Flet](https://img.shields.io/badge/Flet-0.85.2-orange)](https://flet.dev)
[![Python](https://img.shields.io/badge/Python-3.10%2B-yellow)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

## 🌟 About
This Pomodoro was built as a personal learning exercise to improve my Python skills and gain experience with **Flet**

## 🚧 Upcoming Features
- Customizable Focus/Break durations
- Short vs Long break options
- Improved UI/Visual design
- Always on Top mode
- Sound effects

## 📥 Download

### Option 1: Pre-built Executable
Go to the **[Releases](https://github.com/lieserl-git/PomodoroTimer/releases)** section.

## Option 2: Run from Source
1. Clone the repository:
```bash
git clone https://github.com/lieserl-git/PomodoroTimer.git
cd PomodoroTimer
```
2. Install Dependencies
```bash
pip install flet pyinstaller
```
3. Build command: This command creates a standalone executable in the dist folder.
```bash
pyinstaller --onefile --windowed --name "PomodoroTimer" src/main.py
```

