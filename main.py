from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
)
from PySide6.QtCore import QDateTime

t = QDateTime.currentDateTimeUtc()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Daniel's Clock")
        label = QLabel(f"{t}")

        self.setCentralWidget(label)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
