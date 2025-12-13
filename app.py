import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QTextEdit, QFileDialog
)
from PyQt5.QtCore import QTimer, QTime, Qt


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer(self)
        self.laps = []

        # --- UI elementi ---
        self.time_label = QLabel("00:00:00.00")
        self.start_button = QPushButton("▶ Start")
        self.stop_button = QPushButton("⏸ Stop")
        self.reset_button = QPushButton("⟳ Reset")
        self.lap_button = QPushButton("🏁 Lap")
        self.save_button = QPushButton("💾 Save Laps")
        self.laps_display = QTextEdit()
        self.laps_display.setReadOnly(True)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch Pro")
        self.setFixedSize(500, 600)

        # --- Glavni layout ---
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label, alignment=Qt.AlignCenter)

        hbox_buttons = QHBoxLayout()
        hbox_buttons.addWidget(self.start_button)
        hbox_buttons.addWidget(self.stop_button)
        hbox_buttons.addWidget(self.reset_button)
        vbox.addLayout(hbox_buttons)

        hbox_extra = QHBoxLayout()
        hbox_extra.addWidget(self.lap_button)
        hbox_extra.addWidget(self.save_button)
        vbox.addLayout(hbox_extra)

        vbox.addWidget(QLabel("Lap times:"))
        vbox.addWidget(self.laps_display)

        self.setLayout(vbox)

        # --- Stil ---
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f9ff;
            }
            QLabel {
                font-size: 100px;
                font-weight: bold;
                background-color: #cce5ff;
                border-radius: 20px;
                padding: 10px;
            }
            QPushButton {
                font-size: 24px;
                font-weight: bold;
                padding: 12px;
                border-radius: 12px;
                background-color: #0078d4;
                color: white;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
            QTextEdit {
                font-size: 18px;
                border-radius: 10px;
                background-color: white;
            }
        """)

        # --- Signali i slotovi ---
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.lap_button.clicked.connect(self.add_lap)
        self.save_button.clicked.connect(self.save_laps)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.laps.clear()
        self.laps_display.clear()
        self.time_label.setText("00:00:00.00")

    def add_lap(self):
        lap_time = self.format_time(self.time)
        self.laps.append(lap_time)
        self.laps_display.append(f"Lap {len(self.laps)}: {lap_time}")

    def save_laps(self):
        if not self.laps:
            return
        path, _ = QFileDialog.getSaveFileName(self, "Save Laps", "", "Text Files (*.txt)")
        if path:
            with open(path, "w") as f:
                for i, lap in enumerate(self.laps, start=1):
                    f.write(f"Lap {i}: {lap}\n")

    def format_time(self, time):
        return f"{time.hour():02}:{time.minute():02}:{time.second():02}.{time.msec() // 10:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Stopwatch()
    window.show()
    sys.exit(app.exec_())