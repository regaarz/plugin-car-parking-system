from src.plugin_interface import PluginInterface
from PyQt6.QtWidgets import QWidget
from .ui_main import Ui_Form
import cv2


class Controller(QWidget):
    def __init__(self, model):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = model
        self.image = None
        self.set_stylesheet()

    def set_stylesheet(self):
        # This is set up style label on bonding box ui
        self.ui.label_6.setStyleSheet(self.model.style_label())
        self.ui.label_8.setStyleSheet(self.model.style_label())
        self.ui.label_9.setStyleSheet(self.model.style_label())
        self.ui.label_10.setStyleSheet(self.model.style_label())
        self.ui.label_11.setStyleSheet(self.model.style_label())
        self.ui.label_12.setStyleSheet(self.model.style_label())
        self.ui.label_13.setStyleSheet(self.model.style_label())

        self.ui.cam_fisheye.setStyleSheet(self.model.style_label())
        self.ui.cam_panorama.setStyleSheet(self.model.style_label())
        self.ui.cam_gate_in.setStyleSheet(self.model.style_label())
        self.ui.cam_gate_out.setStyleSheet(self.model.style_label())
        self.ui.img_plate.setStyleSheet(self.model.style_label())
        self.ui.zoom.setStyleSheet(self.model.style_label())

        self.ui.btn_load.setStyleSheet(self.model.style_pushbutton())
        self.ui.btn_clear.setStyleSheet(self.model.style_pushbutton())

        self.ui.btn_load.clicked.connect(self.load_img)

    def load_img(self):
        file = self.model.select_file()
        if file:
            # if file:
            #     self.image=
            self.image = cv2.imread(file)
            self.showImg()

    def showImg(self):
        self.model.show_image_to_label(self.ui.cam_fisheye, self.image, 250)

    def load_image(self):
        file = self.model.select_file()
        if file:
            if file:
                self.moildev = self.model.connect_to_moildev(parameter_name=file)
            self.image_original = cv2.imread(file)
            self.image = self.image_original.copy()
            # self.panorma_views()
            self.show_to_ui()



class CarParking(PluginInterface):
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

