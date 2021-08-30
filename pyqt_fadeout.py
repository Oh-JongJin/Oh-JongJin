import sys
import time
import pyqtgraph.opengl as gl

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsOpacityEffect, QPushButton, QVBoxLayout


class Window(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.opacity_effect = QGraphicsOpacityEffect()
        print(self.opacity_effect.opacity())

        self._heightMask = self.height()
        self.animation = QPropertyAnimation(self, b"heightPercentage")
        self.animation.setDuration(1000)
        self.animation.setStartValue(self.opacity_effect.opacity())
        self.animation.setEndValue(-0.01)
        self.animation.finished.connect(self.close)
        self.isStarted = False

    @pyqtProperty(int)
    def heightMask(self):
        return self._heightMask

    @heightMask.setter
    def heightPercentage(self, value):
        self._heightMask = value
        rect = QRect(0, 0, self.width(), self.heightMask)
        self.setMask(QRegion(rect))

    def closeEvent(self, event):
        if not self.isStarted:
            self.animation.start()
            self.isStarted = True
            event.ignore()
        else:
            QWidget.closeEvent(self, event)


class FadeWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        button = QPushButton(self)
        button.setText("Close")

        button.resize(200, 200)
        button.clicked.connect(self.fade)

        layout = QVBoxLayout(self)
        layout.addWidget(button)

        self.resize(300, 300)

    def fade(self):
        for i in range(100):
            i = i / 100
            self.setWindowOpacity(1 - i)
            time.sleep(0.005)
        self.close()

    def close(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FadeWindow()
    window.show()
    sys.exit(app.exec_())
