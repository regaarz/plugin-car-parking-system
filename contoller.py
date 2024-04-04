from src.plugin_interface import PluginInterface
from PyQt6.QtWidgets import QWidget
from .ui_main import Ui_Form
from PyQt6 import QtCore, QtGui, QtWidgets

class Controller(QWidget):
    def __init__(self, model):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = model
        self.set_stylesheet()


        self.ui.pushButton_2.clicked.connect(self.show_fishEye)
        self.ui.pushButton.clicked.connect(self.show_normal)


    def show_fishEye(self):
        self.ui.label.setPixmap(QtGui.QPixmap("./plugins/moilapp-plugin-hello-world/fisheye.jpeg"))

    def show_normal(self):
        self.ui.label.setPixmap(QtGui.QPixmap("./plugins/moilapp-plugin-hello-world/normal.jpeg"))


    def set_stylesheet(self):
        self.ui.label.setStyleSheet("font-size:64px;")

        self.ui.label.setStyleSheet("font-size:64px;\n"
                                 "background-color: rgb(153, 193, 241);")
        self.ui.pushButton.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.ui.pushButton_2.setStyleSheet("background-color: rgb(53, 132, 228);")



class HelloWorld(PluginInterface):
    def __init__(self):
        super().__init__()
        self.widget = None
        self.description = "This is a plugins application"

    def set_plugin_widget(self, model):
        self.widget = Controller(model)
        return self.widget

    def set_icon_apps(self):
        return "icon.png"

    def change_stylesheet(self):
        self.widget.set_stylesheet()

