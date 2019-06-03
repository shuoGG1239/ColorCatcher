from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QGuiApplication, QColor, QCursor
from PyQt5.QtWidgets import QWidget, QApplication

import ui_colorcatcher


class ColorCatcher(QWidget):
    load_pixmap = None
    signal_complete_capture = pyqtSignal(QPixmap)

    def __init__(self):
        QWidget.__init__(self)
        self.ui = ui_colorcatcher.Ui_ColorCatcher()
        self.ui.setupUi(self)
        # self.load_background_pixmap()
        # self.setCursor(Qt.CrossCursor)
        self.show()
        self.printColor()

    def printColor(self):
        x = QCursor.pos().x()
        y = QCursor.pos().y()

        pixmap = QGuiApplication.primaryScreen().grabWindow(QApplication.desktop().winId())
        if not pixmap.isNull():
            image = pixmap.toImage()
            if not image.isNull():
                if (image.valid(0, 0)):
                    color = image.pixel(0, 0)
                    print(QColor(color).getRgb())
                    # r, g, b = color.red(), color.green(), color.blue()
                    # print(r, g, b)
                    self.ui.labelActive.setText("")

    def load_background_pixmap(self):
        # 截下当前屏幕的图像
        self.load_pixmap = QGuiApplication.primaryScreen().grabWindow(QApplication.desktop().winId())
        self.screen_width = self.load_pixmap.width()
        self.screen_height = self.load_pixmap.height()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.signal_complete_capture.emit(self.capture_pixmap)
            self.close()
