from src.plugin_interface import PluginInterface
<<<<<<< HEAD
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QMessageBox
from src.models.model_apps import ModelApps
from .ui_main import Ui_Form
import cv2

# from moildev import Moildev
=======
from PyQt6.QtWidgets import QWidget
from .ui_main import Ui_Form
import cv2

>>>>>>> origin/rega

class Controller(QWidget):
    def __init__(self, model):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = model
<<<<<<< HEAD
        self.model_apps = ModelApps()
        # self.moildev = Moildev()
        self.image = None
        self.x = 0
=======
        self.image = None
>>>>>>> origin/rega
        self.set_stylesheet()

    def set_stylesheet(self):
        # This is set up style label on bonding box ui
<<<<<<< HEAD
        self.ui.label_7.setStyleSheet(self.model.style_label())
        self.ui.label_8.setStyleSheet(self.model.style_label())
        self.ui.label_10.setStyleSheet(self.model.style_label())
        self.ui.label_9.setStyleSheet(self.model.style_label())
        self.ui.label_13.setStyleSheet(self.model.style_label())
        self.ui.label_14.setStyleSheet(self.model.style_label())

        self.ui.vidio_fisheye.setStyleSheet(self.model.style_label())
        self.ui.vidio_pano.setStyleSheet(self.model.style_label())
        self.ui.Gate_In.setStyleSheet(self.model.style_label())
        self.ui.Gate_Out.setStyleSheet(self.model.style_label())
        # self.ui.img_plat.setStyleSheet(self.model.style_label())

        self.ui.btn_save.setStyleSheet(self.model.style_pushbutton())
        self.ui.btn_stop.setStyleSheet(self.model.style_pushbutton())
        self.ui.btn_start.setStyleSheet(self.model.style_pushbutton())

        self.ui.frame_4.setStyleSheet(self.model.style_frame_main())
        self.ui.frame_3.setStyleSheet(self.model.style_frame_main())

        self.ui.frame_12.setStyleSheet(self.model.style_frame_object())
        self.ui.frame_11.setStyleSheet(self.model.style_frame_object())
        self.ui.frame_10.setStyleSheet(self.model.style_frame_object())
        self.ui.frame_5.setStyleSheet(self.model.style_frame_object())
        self.ui.frame_7.setStyleSheet(self.model.style_frame_object())
        self.ui.frame_13.setStyleSheet(self.model.style_frame_object())
        self.ui.frame_15.setStyleSheet(self.model.style_frame_object())
        self.ui.frame_19.setStyleSheet(self.model.style_frame_object())

        self.ui.line.setStyleSheet(self.model.style_line())

        self.ui.frame_14.setMaximumSize(QtCore.QSize(16777215, 23))
        self.ui.frame_mode1.setMaximumSize(QtCore.QSize(16777215, 23))
        self.ui.frame_mode1_2.setMaximumSize(QtCore.QSize(16777215, 23))
        self.ui.frame_mode2.setMaximumSize(QtCore.QSize(16777215, 23))
        self.ui.frame_mode2_2.setMaximumSize(QtCore.QSize(16777215, 23))

        self.ui.frame_14.hide()
        self.ui.frame_mode1.hide()
        self.ui.frame_mode2.hide()
        self.ui.frame_mode1_2.hide()
        self.ui.frame_mode2_2.hide()

        self.ui.btn_radio_hidden.toggled.connect(self.change_mode)
        self.ui.btn_radio_mode1.toggled.connect(self.change_mode)
        self.ui.btn_radio_mode2.toggled.connect(self.change_mode)

        self.ui.spinBox_alpha_4.setRange(-999, 999)

        self.ui.btn_start.clicked.connect(self.start)

        # self.ui.spinBox_alpha_1.setStyleSheet(self.model.)

        self.ui.spinBox_alpha_1.valueChanged.connect(self.pano)
        # if self.ui.btn_radio_mode1.isChecked():
        #     QMessageBox.information(self, "tes,", f"aa")
        # else:
        #     QMessageBox.information(self, "tes,", f"bb")

    def pano(self):
        alpabeta_max = self.ui.spinBox_alpha_1.value()

        # self.moildev = self.model.connect_to_moildev(parameter_name)
        self.image = self.moildev.panorama_car(self.image, alpabeta_max, 80, 0, 0.25, 0.75, 0, 1)
        self.showImg()



    def change_mode(self):
        if self.ui.btn_radio_mode1.isChecked():
            mode = 1
            self.ui.frame_14.show()
            self.ui.frame_mode1.show()
            self.ui.frame_mode1_2.show()

            self.ui.frame_mode2.hide()
            self.ui.frame_mode2_2.hide()
        elif self.ui.btn_radio_mode2.isChecked():
            mode = 2
            self.ui.frame_14.show()
            self.ui.frame_mode2.show()
            self.ui.frame_mode2_2.show()

            self.ui.frame_mode1.hide()
            self.ui.frame_mode1_2.hide()
        else:
            mode = 0
            self.ui.frame_14.hide()
            self.ui.frame_mode1.hide()
            self.ui.frame_mode1_2.hide()
            self.ui.frame_mode2.hide()
            self.ui.frame_mode2_2.hide()

    def start(self):
        source_type, cam_type, source_media, parameter_name = self.model.select_media_source()
        self.image = cv2.imread(source_media)
        self.moildev = self.model.connect_to_moildev(parameter_name)
        # self.image = cv2.imread('/home/gritz/Documents/ftdc/moilapp/moilapp-pak-heru/src/fisheye.png')
        self.image = self.moildev.panorama_car(self.image, 180, 80, 0, 0.25, 0.75, 0, 1)
        self.showImg()

        # file = self.model.select_file()
        # if file:
        #     # if file:
        #     #     self.image=
        #     self.image = cv2.imread(source_media)
        #     self.showImg()

    def showImg(self):

        self.model.show_image_to_label(self.ui.vidio_pano, self.image, 820)
=======
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
>>>>>>> origin/rega

    def load_image(self):
        file = self.model.select_file()
        if file:
            if file:
                self.moildev = self.model.connect_to_moildev(parameter_name=file)
            self.image_original = cv2.imread(file)
            self.image = self.image_original.copy()
            # self.panorma_views()
            self.show_to_ui()



<<<<<<< HEAD
class ParkingGateSystem(PluginInterface):
=======
class CarParking(PluginInterface):
>>>>>>> origin/rega
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

