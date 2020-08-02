import sys
import numpy as np
from .transforms import *
from .Context import Context
from PyQt5 import QtCore, QtGui, QtWidgets

d_sens_step = 1
d_sens_rot = 20

class Ui_Worckbanch(object):

    def setupUi(self, Worckbanch):
        Worckbanch.setObjectName("Worckbanch")
        Worckbanch.resize(758, 227)
        Worckbanch.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(Worckbanch)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.buttons_frame = QtWidgets.QGroupBox(self.centralwidget)
        self.buttons_frame.setGeometry(QtCore.QRect(10, 10, 311, 171))
        self.buttons_frame.setObjectName("buttons_frame")
        self.translate_buttons = QtWidgets.QGroupBox(self.buttons_frame)
        self.translate_buttons.setGeometry(QtCore.QRect(10, 20, 141, 141))
        self.translate_buttons.setObjectName("translate_buttons")
        self.z_down = QtWidgets.QPushButton(self.translate_buttons)
        self.z_down.setGeometry(QtCore.QRect(10, 60, 41, 41))
        self.z_down.setStyleSheet("color:blue\n"
"")
        self.z_down.setObjectName("z_down")
        self.y_up = QtWidgets.QPushButton(self.translate_buttons)
        self.y_up.setGeometry(QtCore.QRect(50, 20, 41, 41))
        self.y_up.setStyleSheet("color:green\n"
"")
        self.y_up.setObjectName("y_up")
        self.z_up = QtWidgets.QPushButton(self.translate_buttons)
        self.z_up.setGeometry(QtCore.QRect(90, 60, 41, 41))
        self.z_up.setStyleSheet("color:blue\n"
"")
        self.z_up.setObjectName("z_up")
        self.x_up = QtWidgets.QPushButton(self.translate_buttons)
        self.x_up.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.x_up.setStyleSheet("color:red\n"
"")
        self.x_up.setObjectName("x_up")
        self.y_down = QtWidgets.QPushButton(self.translate_buttons)
        self.y_down.setGeometry(QtCore.QRect(50, 60, 41, 41))
        self.y_down.setStyleSheet("color:green\n"
"")
        self.y_down.setObjectName("y_down")
        self.x_down = QtWidgets.QPushButton(self.translate_buttons)
        self.x_down.setGeometry(QtCore.QRect(90, 20, 41, 41))
        self.x_down.setStyleSheet("color:red\n"
"")
        self.x_down.setObjectName("x_down")
        self.t_sens = QtWidgets.QLineEdit(self.translate_buttons)
        self.t_sens.setGeometry(QtCore.QRect(50, 110, 41, 20))
        self.t_sens.setObjectName("t_sens")
        self.step_l = QtWidgets.QLabel(self.translate_buttons)
        self.step_l.setGeometry(QtCore.QRect(10, 110, 41, 16))
        self.step_l.setAlignment(QtCore.Qt.AlignCenter)
        self.step_l.setObjectName("step_l")
        self.unit_l = QtWidgets.QLabel(self.translate_buttons)
        self.unit_l.setGeometry(QtCore.QRect(90, 110, 47, 16))
        self.unit_l.setAlignment(QtCore.Qt.AlignCenter)
        self.unit_l.setObjectName("unit_l")
        self.rotate_buttons = QtWidgets.QGroupBox(self.buttons_frame)
        self.rotate_buttons.setGeometry(QtCore.QRect(160, 20, 141, 141))
        self.rotate_buttons.setObjectName("rotate_buttons")
        self.yaw_down = QtWidgets.QPushButton(self.rotate_buttons)
        self.yaw_down.setGeometry(QtCore.QRect(10, 60, 41, 41))
        self.yaw_down.setStyleSheet("color:blue\n"
"")
        self.yaw_down.setObjectName("yaw_down")
        self.pitch_up = QtWidgets.QPushButton(self.rotate_buttons)
        self.pitch_up.setGeometry(QtCore.QRect(50, 20, 41, 41))
        self.pitch_up.setStyleSheet("color:red\n"
"")
        self.pitch_up.setObjectName("pitch_up")
        self.yaw_up = QtWidgets.QPushButton(self.rotate_buttons)
        self.yaw_up.setGeometry(QtCore.QRect(90, 60, 41, 41))
        self.yaw_up.setStyleSheet("color:blue\n"
"")
        self.yaw_up.setAutoDefault(False)
        self.yaw_up.setDefault(False)
        self.yaw_up.setFlat(False)
        self.yaw_up.setObjectName("yaw_up")
        self.pitch_down = QtWidgets.QPushButton(self.rotate_buttons)
        self.pitch_down.setGeometry(QtCore.QRect(50, 60, 41, 41))
        self.pitch_down.setStyleSheet("color:red\n"
"")
        self.pitch_down.setObjectName("pitch_down")
        self.r_sens = QtWidgets.QLineEdit(self.rotate_buttons)
        self.r_sens.setGeometry(QtCore.QRect(50, 110, 41, 20))
        self.r_sens.setObjectName("r_sens")
        self.step_ll = QtWidgets.QLabel(self.rotate_buttons)
        self.step_ll.setGeometry(QtCore.QRect(10, 110, 41, 16))
        self.step_ll.setAlignment(QtCore.Qt.AlignCenter)
        self.step_ll.setObjectName("step_ll")
        self.unit_ll = QtWidgets.QLabel(self.rotate_buttons)
        self.unit_ll.setGeometry(QtCore.QRect(90, 110, 47, 16))
        self.unit_ll.setAlignment(QtCore.Qt.AlignCenter)
        self.unit_ll.setObjectName("unit_ll")
        self.numeric_frame = QtWidgets.QGroupBox(self.centralwidget)
        self.numeric_frame.setGeometry(QtCore.QRect(330, 10, 411, 171))
        self.numeric_frame.setObjectName("numeric_frame")
        self.translate_numeric = QtWidgets.QGroupBox(self.numeric_frame)
        self.translate_numeric.setGeometry(QtCore.QRect(10, 20, 191, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.translate_numeric.sizePolicy().hasHeightForWidth())
        self.translate_numeric.setSizePolicy(sizePolicy)
        self.translate_numeric.setObjectName("translate_numeric")
        self.x_coord = QtWidgets.QLineEdit(self.translate_numeric)
        self.x_coord.setGeometry(QtCore.QRect(40, 30, 71, 20))
        self.x_coord.setObjectName("x_coord")
        self.y_coord = QtWidgets.QLineEdit(self.translate_numeric)
        self.y_coord.setGeometry(QtCore.QRect(40, 70, 71, 20))
        self.y_coord.setObjectName("y_coord")
        self.z_coord = QtWidgets.QLineEdit(self.translate_numeric)
        self.z_coord.setGeometry(QtCore.QRect(40, 110, 71, 20))
        self.z_coord.setObjectName("z_coord")
        self.x_l = QtWidgets.QLabel(self.translate_numeric)
        self.x_l.setGeometry(QtCore.QRect(10, 30, 31, 16))
        self.x_l.setStyleSheet("color:red\n"
"")
        self.x_l.setTextFormat(QtCore.Qt.AutoText)
        self.x_l.setAlignment(QtCore.Qt.AlignCenter)
        self.x_l.setObjectName("x_l")
        self.y_l = QtWidgets.QLabel(self.translate_numeric)
        self.y_l.setGeometry(QtCore.QRect(10, 70, 31, 16))
        self.y_l.setStyleSheet("color:green\n"
"")
        self.y_l.setTextFormat(QtCore.Qt.AutoText)
        self.y_l.setAlignment(QtCore.Qt.AlignCenter)
        self.y_l.setObjectName("y_l")
        self.z_l = QtWidgets.QLabel(self.translate_numeric)
        self.z_l.setGeometry(QtCore.QRect(10, 110, 31, 16))
        self.z_l.setStyleSheet("color:blue\n"
"")
        self.z_l.setTextFormat(QtCore.Qt.AutoText)
        self.z_l.setAlignment(QtCore.Qt.AlignCenter)
        self.z_l.setObjectName("z_l")
        self.t_update = QtWidgets.QPushButton(self.translate_numeric)
        self.t_update.setGeometry(QtCore.QRect(120, 50, 61, 23))
        self.t_update.setObjectName("t_update")
        self.t_reset = QtWidgets.QPushButton(self.translate_numeric)
        self.t_reset.setGeometry(QtCore.QRect(120, 70, 61, 23))
        self.t_reset.setObjectName("t_reset")
        self.t_move = QtWidgets.QPushButton(self.translate_numeric)
        self.t_move.setGeometry(QtCore.QRect(120, 90, 61, 23))
        self.t_move.setObjectName("t_move")
        self.rotate_numeric = QtWidgets.QGroupBox(self.numeric_frame)
        self.rotate_numeric.setGeometry(QtCore.QRect(210, 20, 191, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_numeric.sizePolicy().hasHeightForWidth())
        self.rotate_numeric.setSizePolicy(sizePolicy)
        self.rotate_numeric.setObjectName("rotate_numeric")
        self.p_angle = QtWidgets.QLineEdit(self.rotate_numeric)
        self.p_angle.setGeometry(QtCore.QRect(40, 30, 71, 20))
        self.p_angle.setObjectName("p_angle")
        self.y_angle = QtWidgets.QLineEdit(self.rotate_numeric)
        self.y_angle.setGeometry(QtCore.QRect(40, 70, 71, 20))
        self.y_angle.setObjectName("y_angle")
        self.r_angle = QtWidgets.QLineEdit(self.rotate_numeric)
        self.r_angle.setGeometry(QtCore.QRect(40, 110, 71, 20))
        self.r_angle.setObjectName("r_angle")
        self.pitch_l = QtWidgets.QLabel(self.rotate_numeric)
        self.pitch_l.setGeometry(QtCore.QRect(10, 30, 31, 16))
        self.pitch_l.setStyleSheet("color:red\n"
"")
        self.pitch_l.setTextFormat(QtCore.Qt.AutoText)
        self.pitch_l.setAlignment(QtCore.Qt.AlignCenter)
        self.pitch_l.setObjectName("pitch_l")
        self.yaw_l = QtWidgets.QLabel(self.rotate_numeric)
        self.yaw_l.setGeometry(QtCore.QRect(10, 70, 31, 16))
        self.yaw_l.setStyleSheet("color:blue\n"
"")
        self.yaw_l.setTextFormat(QtCore.Qt.AutoText)
        self.yaw_l.setAlignment(QtCore.Qt.AlignCenter)
        self.yaw_l.setObjectName("yaw_l")
        self.roll_l = QtWidgets.QLabel(self.rotate_numeric)
        self.roll_l.setGeometry(QtCore.QRect(10, 110, 31, 16))
        self.roll_l.setStyleSheet("color:green\n"
"")
        self.roll_l.setTextFormat(QtCore.Qt.AutoText)
        self.roll_l.setAlignment(QtCore.Qt.AlignCenter)
        self.roll_l.setObjectName("roll_l")
        self.r_update = QtWidgets.QPushButton(self.rotate_numeric)
        self.r_update.setGeometry(QtCore.QRect(120, 50, 61, 23))
        self.r_update.setObjectName("r_update")
        self.r_reset = QtWidgets.QPushButton(self.rotate_numeric)
        self.r_reset.setGeometry(QtCore.QRect(120, 70, 61, 23))
        self.r_reset.setObjectName("r_reset")
        self.r_rotate = QtWidgets.QPushButton(self.rotate_numeric)
        self.r_rotate.setGeometry(QtCore.QRect(120, 90, 61, 23))
        self.r_rotate.setObjectName("r_rotate")
        Worckbanch.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Worckbanch)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 21))
        self.menubar.setObjectName("menubar")
        Worckbanch.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Worckbanch)
        self.statusbar.setObjectName("statusbar")
        Worckbanch.setStatusBar(self.statusbar)

        self.retranslateUi(Worckbanch)
        QtCore.QMetaObject.connectSlotsByName(Worckbanch)

    def retranslateUi(self, Worckbanch):
        _translate = QtCore.QCoreApplication.translate
        Worckbanch.setWindowTitle(_translate("Worckbanch", "Worckbanch"))
        self.buttons_frame.setTitle(_translate("Worckbanch", "Buttons controlls"))
        self.translate_buttons.setTitle(_translate("Worckbanch", "Translate"))
        self.z_down.setText(_translate("Worckbanch", "←"))
        self.y_up.setText(_translate("Worckbanch", "↑"))
        self.z_up.setText(_translate("Worckbanch", "→"))
        self.x_up.setText(_translate("Worckbanch", "<"))
        self.y_down.setText(_translate("Worckbanch", "↓"))
        self.x_down.setText(_translate("Worckbanch", ">"))
        self.step_l.setText(_translate("Worckbanch", "Step:"))
        self.unit_l.setText(_translate("Worckbanch", "Units"))
        self.rotate_buttons.setTitle(_translate("Worckbanch", "Rotate"))
        self.yaw_down.setText(_translate("Worckbanch", "←"))
        self.pitch_up.setText(_translate("Worckbanch", "↑"))
        self.yaw_up.setText(_translate("Worckbanch", "→"))
        self.pitch_down.setText(_translate("Worckbanch", "↓"))
        self.step_ll.setText(_translate("Worckbanch", "Step:"))
        self.unit_ll.setText(_translate("Worckbanch", "Deg"))
        self.numeric_frame.setTitle(_translate("Worckbanch", "Numeric controlls"))
        self.translate_numeric.setTitle(_translate("Worckbanch", "Translate"))
        self.x_l.setText(_translate("Worckbanch", "X:"))
        self.y_l.setText(_translate("Worckbanch", "Y:"))
        self.z_l.setText(_translate("Worckbanch", "Z:"))
        self.t_update.setText(_translate("Worckbanch", "UPDATE"))
        self.t_reset.setText(_translate("Worckbanch", "RESET"))
        self.t_move.setText(_translate("Worckbanch", "MOVE TO"))
        self.rotate_numeric.setTitle(_translate("Worckbanch", "Rotate"))
        self.pitch_l.setText(_translate("Worckbanch", "Pitch:"))
        self.yaw_l.setText(_translate("Worckbanch", "Yaw:"))
        self.roll_l.setText(_translate("Worckbanch", "Roll:"))
        self.r_update.setText(_translate("Worckbanch", "UPDATE"))
        self.r_reset.setText(_translate("Worckbanch", "RESET"))
        self.r_rotate.setText(_translate("Worckbanch", "ROTATE"))

    def connectUI(self,  ctx):
        # connecting the context
        assert isinstance(ctx, Context)
        self.context = ctx

        self.t_sens.setText(str(d_sens_step))
        self.r_sens.setText(str(d_sens_rot))

        # doing bindings 
        self.x_down.clicked.connect(self.moveFwd)
        self.x_up.clicked.connect(self.moveBack)
        self.y_up.clicked.connect(self.moveUp)
        self.y_down.clicked.connect(self.moveDown)
        self.z_up.clicked.connect(self.moveRight)
        self.z_down.clicked.connect(self.moveLeft)

        self.pitch_up.clicked.connect(self.pitchUp)
        self.pitch_down.clicked.connect(self.pitchDown)
        self.yaw_up.clicked.connect(self.yawUp)
        self.yaw_down.clicked.connect(self.yawDown)

        self.t_update.clicked.connect(self.updateCoordinates)
        self.t_reset.clicked.connect(self.resetCoordinates)
        self.t_move.clicked.connect(self.moveToCoordinates)

        self.r_update.clicked.connect(self.updateAngles)
        self.r_reset.clicked.connect(self.resetAngles)
        self.r_rotate.clicked.connect(self.rotateByAngles)

    # Movement
    def moveUp(self):
        newpos = self.context.camera.position + np.array([0, float(self.t_sens.text()), 0])
        self.context.camera.setCameraPosition(newpos)

    def moveDown(self):
        newpos = self.context.camera.position + np.array([0, -float(self.t_sens.text()), 0])
        self.context.camera.setCameraPosition(newpos)

    def moveRight(self):
        newpos = self.context.camera.position + np.array([0, 0, float(self.t_sens.text())])
        self.context.camera.setCameraPosition(newpos)

    def moveLeft(self):
        newpos = self.context.camera.position + np.array([0, 0, -float(self.t_sens.text())])
        self.context.camera.setCameraPosition(newpos)

    def moveFwd(self):
        newpos = self.context.camera.position + np.array([float(self.t_sens.text()), 0, 0])
        self.context.camera.setCameraPosition(newpos)
        
    def moveBack(self):
        newpos = self.context.camera.position + np.array([-float(self.t_sens.text()), 0, 0])
        self.context.camera.setCameraPosition(newpos)

    # Rotation
    def pitchUp(self):
        newpitch = self.context.camera.pitch + deg_to_rad(float(self.r_sens.text()))
        self.context.camera.roateCamera(newpitch, self.context.camera.yaw)

    def pitchDown(self):
        newpitch = self.context.camera.pitch - deg_to_rad(float(self.r_sens.text()))
        self.context.camera.roateCamera(newpitch, self.context.camera.yaw)

    def yawUp(self):
        newyaw = self.context.camera.yaw + deg_to_rad(float(self.r_sens.text()))
        self.context.camera.roateCamera(self.context.camera.pitch, newyaw)

    def yawDown(self):
        newyaw = self.context.camera.yaw - deg_to_rad(float(self.r_sens.text()))
        self.context.camera.roateCamera(self.context.camera.pitch, newyaw)
    
    # Translate data
    def updateCoordinates(self, useless):
        current_position = self.context.camera.position
        self.x_coord.setText(str(current_position[0]))
        self.y_coord.setText(str(current_position[1]))
        self.z_coord.setText(str(current_position[2]))

    def resetCoordinates(self, useless):
        self.x_coord.setText('0')
        self.y_coord.setText('0')
        self.z_coord.setText('0')

    def moveToCoordinates(self, useless):
        newpos = [float(self.x_coord.text()), float(self.y_coord.text()), float(self.z_coord.text())]
        self.context.camera.setCameraPosition(newpos)

    # Rotation data
    def updateAngles(self, useless):
        self.p_angle.setText(str(int(rad_to_deg(self.context.camera.pitch))))
        self.y_angle.setText(str(int(rad_to_deg(self.context.camera.yaw))))

    def resetAngles(self, useless):
        self.p_angle.setText('0')
        self.y_angle.setText('0')

    def rotateByAngles(self, useless):
        newpitch = deg_to_rad(float(self.p_angle.text()))
        newyaw = deg_to_rad(float(self.y_angle.text()))
        self.context.camera.roateCamera(newpitch, newyaw)
