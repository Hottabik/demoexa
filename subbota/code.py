#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, # это то, что поддерживает работоспособность приложения Qt, выполняя его основной цикл событий
    QDialog # это базовый класс диалогового окна
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sys # взаимодействие с интерпретатором

from PyQt5.QtGui import QPixmap, QIcon # для работы с изображениями и загрузки иконок

# Окно приветствия
class Test(QDialog):
        def __init__(self):
            super(Test, self).__init__()
            loadUi("test.ui",self) # загружаем интерфейс

# запуcк приложения
app = QApplication(sys.argv)

# позволяте менять страницы в окне
welcome = Test()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)

# загружаем иконку
icon = QIcon()
icon.addPixmap(QPixmap("bober.jpg"), QIcon.Normal, QIcon.Off)
widget.setWindowIcon(icon)
widget.show()
widget.setFixedWidth(1000)
widget.setFixedHeight(500)

    # запускаем приложение
try:
    sys.exit(app.exec_())
except:

    print("You close application")