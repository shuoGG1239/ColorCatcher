from PyQt5.QtWidgets import QApplication

import ColorCatcher

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = ColorCatcher.ColorCatcher()
    mainWindow.show()
    sys.exit(app.exec_())