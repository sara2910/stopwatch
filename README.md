# Stopwatch Pro – Precision Timer in PyQt5

A sleek and functional desktop stopwatch application developed in Python using PyQt5. It offers precise time measurement with start, stop, reset, lap recording, and lap saving functionality.

---

## Features

- **Start, pause, and reset** the stopwatch  
- **Lap time recording** displayed in a clean, read-only text area  
- **Save laps** to a `.txt` file via a standard save dialog  
- **High precision** with updates every 10 milliseconds  
- **Modern and intuitive user interface** featuring a large time display and styled controls  

---

## Installation

Make sure you have Python 3 installed. Then install the PyQt5 library:

```bash
pip install PyQt5
```
## Usage

Run the application with:

```bash
python stopwatch.py
```
## Controls

- **▶ Start** — Starts the stopwatch  
- **⏸ Stop** — Pauses the stopwatch  
- **⟳ Reset** — Resets the timer and clears all recorded laps  
- **🏁 Lap** — Records the current time as a lap  
- **💾 Save Laps** — Saves all recorded laps to a text file

 ## Technical Details

- Time displayed in `HH:MM:SS.ms` format with a large, clear font  
- Timer implemented using PyQt5’s `QTimer` class with 10 millisecond intervals  
- Laps stored in a list and displayed in a read-only text box  
- Saving laps allows easy review and analysis outside the app  
  


