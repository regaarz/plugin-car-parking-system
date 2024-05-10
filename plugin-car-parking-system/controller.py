from src.plugin_interface import PluginInterface
from PyQt6 import QtCore
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox
from src.models.model_apps import ModelApps
from .ui_main import Ui_Form
import cv2

# from moildev import Moildev

class Controller(QWidget):
    def __init__(self, model):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = model
        self.model_apps = ModelApps()
        # self.moildev = Moildev()
        self.panorama = None
        self.gate_in = None
        self.gate_out = None
        self.moildev = None
        self.x = 0
        self.set_stylesheet()

    def set_stylesheet(self):
        # This is set up style label on bonding box ui
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

        self.ui.spinBox_alpha_5.setRange(-999,999)
        self.ui.spinBox_beta_4.setRange(-999, 999)
        self.ui.spinBox_x_5.setRange(-999,999)
        self.ui.spinBox_x_6.setRange(-999,999)
        self.ui.btn_start.clicked.connect(self.start)

        # self.ui.spinBox_alpha_1.setStyleSheet(self.model.)
        #Spinbox mode 2 Gate_In
        self.ui.spinBox_alpha_5.valueChanged.connect(self.anypoint_mode_2)
        self.ui.spinBox_beta_4.valueChanged.connect(self.anypoint_mode_2)
        self.ui.spinBox_x_5.valueChanged.connect(self.anypoint_mode_2)
        self.ui.spinBox_x_6.valueChanged.connect(self.anypoint_mode_2)

        #Spinbox mode 2 Gate_out
        self.ui.spinBox_alpha_6.valueChanged.connect(self.anypoint_mode_2)
        self.ui.spinBox_beta_5.valueChanged.connect(self.anypoint_mode_2)
        self.ui.spinBox_x_7.valueChanged.connect(self.anypoint_mode_2)
        self.ui.spinBox_x_8.valueChanged.connect(self.anypoint_mode_2)



    def start(self):
        source_type, cam_type, source_media, parameter_name = self.model.select_media_source()
        self.gate_in = cv2.imread(source_media)
        self.gate_out = cv2.imread(source_media)
        self.moildev = self.model.connect_to_moildev(parameter_name)
        # self.image = cv2.imread('/home/gritz/Documents/ftdc/moilapp/moilapp-pak-heru/src/fisheye.png')
      #self.image = self.moildev.panorama_car(self.panorama, 180, 80, 0, 0.25, 0.75, 0, 1)
        self.image_1 = self.moildev.anypoint_mode2(self.gate_in, -90, 0, 0, 1)
        self.image_2 = self.moildev.anypoint_mode2(self.gate_in, -90, 0, 0, 1)
        self.showImg()

#  def pano(self):
        #lpabeta_max = self.ui.spinBox_alpha_1.value()

        # self.moildev = self.model.connect_to_moildev(parameter_name)
      # self.panorama = self.moildev.panorama_car(self.panorama, alpabeta_max, 80, 0, 0.25, 0.75, 0, 1)
       #self.showImg()###

    def anypoint_mode_2(self):
        pitch = self.ui.spinBox_alpha_5.value()
        yaw = self.ui.spinBox_beta_4.value()
        roll = self.ui.spinBox_x_5.value()
        zoom = self.ui.spinBox_x_6.value()
        print(f'{pitch, yaw, roll, zoom = }')
        self.image_1 = self.moildev.anypoint_mode2(self.gate_in, pitch, yaw, roll, zoom)

        pitch_2 = self.ui.spinBox_alpha_6.value()
        yaw_2 = self.ui.spinBox_beta_5.value()
        roll_2 = self.ui.spinBox_x_7.value()
        zoom_2 = self.ui.spinBox_x_8.value()
        print(f'{pitch_2, yaw_2, roll_2, zoom_2 = }')
        self.image_2 = self.moildev.anypoint_mode2(self.gate_out, pitch_2, yaw_2, roll_2, zoom_2)



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


        # file = self.model.select_file()
        # if file:
      #     # if file:
        #     #     self.image=
        #     self.image = cv2.imread(source_media)
        #     self.showImg()

    def showImg(self):
        height, width, channel = self.image_1.shape
        bytesPerLine = 3 * width
        qImg_1 = QImage(self.image_1.data, width, height, bytesPerLine, QImage.Format.Format_BGR888)
        scaled_qImg_1 = qImg_1.scaled(self.ui.Gate_In.width(), self.ui.Gate_In.height())
        self.ui.Gate_In.setPixmap(QPixmap.fromImage(scaled_qImg_1))

        # Menyiapkan gambar untuk Gate_Out
        height, width, channel = self.image_2.shape
        bytesPerLine = 3 * width
        qImg_2 = QImage(self.image_2.data, width, height, bytesPerLine, QImage.Format.Format_BGR888)
        scaled_qImg_2 = qImg_2.scaled(self.ui.Gate_Out.width(), self.ui.Gate_Out.height())
        self.ui.Gate_Out.setPixmap(QPixmap.fromImage(scaled_qImg_2))

    def load_image(self):
        file = self.model.select_file()
        if file:
            if file:
                self.moildev = self.model.connect_to_moildev(parameter_name=file)
            self.image_original = cv2.imread(file)
            self.image = self.image_original.copy()
         # self.panorma_views()
            self.show_to_ui()



class ParkingGateSystem(PluginInterface):
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