## 简单的拾色器
* 最近遇到几次取屏幕某处颜色的场景, 用ps去取色又觉得有点麻烦(步骤太多我懒), 索性自己做一个简单的拾色器
* 功能极简单就是取屏幕某处的色号, 按下空格把颜色记录下来...



## 效果
![colorcatcher.gif](https://i.loli.net/2019/06/09/5cfc9e5a216b517905.gif)



## 思路

* 定时截取屏幕然后取下鼠标位置的像素颜色

```python
def catch(self):
    x = QCursor.pos().x()
    y = QCursor.pos().y()
    pixmap = QGuiApplication.primaryScreen().grabWindow(QApplication.desktop().winId(), x, y, 1, 1)
    if not pixmap.isNull():
        image = pixmap.toImage()
        if not image.isNull():
            if (image.valid(0, 0)):
                color = QColor(image.pixel(0, 0))
                r, g, b, _ = color.getRgb()
                self.nowColor = color
                self.ui.lineEditMove.setText('(%d, %d, %d) %s' % (r, g, b, color.name().upper()))
                self.ui.lineEditMove.setStyleSheet('QLineEdit{border:2px solid %s;}' % (color.name()))

```





## 依赖
* PyQt5



## 代码

* [https://github.com/shuoGG1239/ColorCatcher](https://github.com/shuoGG1239/ColorCatcher)