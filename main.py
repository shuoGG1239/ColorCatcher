from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

import ColorCatcher

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = ColorCatcher.ColorCatcher()
    mainWindow.setWindowIcon(QIcon('./shuoGG_re.ico'))
    mainWindow.show()
    sys.exit(app.exec_())