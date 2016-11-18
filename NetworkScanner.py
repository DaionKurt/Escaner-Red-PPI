# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NetworkScanner.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import FTPServer,HTTPServer,IPScanner,PortScanner,TelnetServer,MACScanner
import threading,re,subprocess,socket
import subprocess,ipaddress,re,socket,MACScanner


HTTP_PORT = 80
FTP_PORT = 20
TELNET_PORT = 23

ip_actual = None
actives = None

info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

class Net:
    def __init__(self, ip, mac, classification, name):
        self.ip = ip
        self.mac = mac
        self.classification = classification
        self.name = name

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, " destruido")

    def displayCount(self):
        print()

class Ui_principal(object):

    def setupUi(self, principal):
        principal.setObjectName("principal")
        principal.resize(800, 416)
        self.centralwidget = QtWidgets.QWidget(principal)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setObjectName("tabs")
        self.tab_escaneo = QtWidgets.QWidget()
        self.tab_escaneo.setObjectName("tab_escaneo")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.tab_escaneo)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.titulo_escaneo = QtWidgets.QLabel(self.tab_escaneo)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.titulo_escaneo.setFont(font)
        self.titulo_escaneo.setObjectName("titulo_escaneo")
        self.verticalLayout_13.addWidget(self.titulo_escaneo)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_tipo_an = QtWidgets.QLabel(self.tab_escaneo)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_tipo_an.setFont(font)
        self.label_tipo_an.setObjectName("label_tipo_an")
        self.horizontalLayout_12.addWidget(self.label_tipo_an)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.boton_an_rapido = QtWidgets.QPushButton(self.tab_escaneo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_an_rapido.sizePolicy().hasHeightForWidth())
        self.boton_an_rapido.setSizePolicy(sizePolicy)
        self.boton_an_rapido.setMinimumSize(QtCore.QSize(100, 0))
        self.boton_an_rapido.setObjectName("boton_an_rapido")
        self.boton_an_rapido.clicked.connect(self.inicia_escaneo_rapido)
        self.horizontalLayout_8.addWidget(self.boton_an_rapido)
        self.descr_an_rapido = QtWidgets.QLabel(self.tab_escaneo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.descr_an_rapido.sizePolicy().hasHeightForWidth())
        self.descr_an_rapido.setSizePolicy(sizePolicy)
        self.descr_an_rapido.setMaximumSize(QtCore.QSize(150, 16777215))
        self.descr_an_rapido.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.descr_an_rapido.setWordWrap(True)
        self.descr_an_rapido.setObjectName("descr_an_rapido")
        self.horizontalLayout_8.addWidget(self.descr_an_rapido)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.boton_an_normal = QtWidgets.QPushButton(self.tab_escaneo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_an_normal.sizePolicy().hasHeightForWidth())
        self.boton_an_normal.setSizePolicy(sizePolicy)
        self.boton_an_normal.setMinimumSize(QtCore.QSize(100, 0))
        self.boton_an_normal.setObjectName("boton_an_normal")
        self.boton_an_normal.clicked.connect(self.inicia_escaneo_normal)
        self.horizontalLayout_9.addWidget(self.boton_an_normal)
        self.desc_an_normal = QtWidgets.QLabel(self.tab_escaneo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.desc_an_normal.sizePolicy().hasHeightForWidth())
        self.desc_an_normal.setSizePolicy(sizePolicy)
        self.desc_an_normal.setMaximumSize(QtCore.QSize(150, 16777215))
        self.desc_an_normal.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.desc_an_normal.setWordWrap(True)
        self.desc_an_normal.setObjectName("desc_an_normal")
        self.horizontalLayout_9.addWidget(self.desc_an_normal)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.boton_an_profundo = QtWidgets.QPushButton(self.tab_escaneo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_an_profundo.sizePolicy().hasHeightForWidth())
        self.boton_an_profundo.setSizePolicy(sizePolicy)
        self.boton_an_profundo.setMinimumSize(QtCore.QSize(100, 0))
        self.boton_an_profundo.setObjectName("boton_an_profundo")
        self.boton_an_profundo.clicked.connect(self.inicia_escaneo_profundo)
        self.horizontalLayout_10.addWidget(self.boton_an_profundo)
        self.desc_an_profundo = QtWidgets.QLabel(self.tab_escaneo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.desc_an_profundo.sizePolicy().hasHeightForWidth())
        self.desc_an_profundo.setSizePolicy(sizePolicy)
        self.desc_an_profundo.setMaximumSize(QtCore.QSize(150, 16777215))
        self.desc_an_profundo.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.desc_an_profundo.setWordWrap(True)
        self.desc_an_profundo.setObjectName("desc_an_profundo")
        self.horizontalLayout_10.addWidget(self.desc_an_profundo)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_14.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_ip_disponibles = QtWidgets.QLabel(self.tab_escaneo)
        self.label_ip_disponibles.setObjectName("label_ip_disponibles")
        self.verticalLayout_7.addWidget(self.label_ip_disponibles)
        self.lista_ips = QtWidgets.QTableWidget(self.tab_escaneo)
        self.lista_ips.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lista_ips.setObjectName("lista_ips")
        self.verticalLayout_7.addWidget(self.lista_ips)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.boton_seleccionar = QtWidgets.QPushButton(self.tab_escaneo)
        self.boton_seleccionar.setObjectName("boton_seleccionar")
        self.boton_seleccionar.clicked.connect(self.selecciona_red)
        self.boton_seleccionar.setMaximumWidth(120)
        self.horizontalLayout_11.addWidget(self.boton_seleccionar)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_14.addLayout(self.verticalLayout_7)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_ip_trabajo = QtWidgets.QLabel(self.tab_escaneo)
        self.label_ip_trabajo.setObjectName("label_ip_trabajo")
        self.verticalLayout_10.addWidget(self.label_ip_trabajo)
        self.panel_info_ip = QtWidgets.QTextEdit(self.tab_escaneo)
        self.panel_info_ip.setObjectName("panel_info_ip")
        self.verticalLayout_10.addWidget(self.panel_info_ip)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_puertos = QtWidgets.QLabel(self.tab_escaneo)
        self.label_puertos.setObjectName("label_puertos")
        self.horizontalLayout_13.addWidget(self.label_puertos)


        self.boton_puertos = QtWidgets.QPushButton(self.tab_escaneo)
        self.boton_puertos.setObjectName("boton_puertos")
        self.boton_puertos.clicked.connect(self.escanea_puertos)
        self.horizontalLayout_13.addWidget(self.boton_puertos)
        self.verticalLayout_11.addLayout(self.horizontalLayout_13)


        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_puertos_abiertos = QtWidgets.QLabel(self.tab_escaneo)
        self.label_puertos_abiertos.setObjectName("label_puertos_abiertos")
        self.verticalLayout_9.addWidget(self.label_puertos_abiertos)
        self.panel_puertos = QtWidgets.QTextEdit(self.tab_escaneo)
        self.panel_puertos.setObjectName("panel_puertos")
        self.verticalLayout_9.addWidget(self.panel_puertos)
        self.verticalLayout_11.addLayout(self.verticalLayout_9)
        self.horizontalLayout_14.addLayout(self.verticalLayout_11)
        self.verticalLayout_12.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        #self.label_progreso = QtWidgets.QLabel(self.tab_escaneo)
        #self.label_progreso.setObjectName("label_progreso")
        #self.horizontalLayout_7.addWidget(self.label_progreso)
        #self.barra_progreso = QtWidgets.QProgressBar(self.tab_escaneo)
        #self.barra_progreso.setProperty("value", 0)
        #self.barra_progreso.setObjectName("barra_progreso")
        #self.horizontalLayout_7.addWidget(self.barra_progreso)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        self.horizontalLayout_15.addLayout(self.verticalLayout_13)
        self.tabs.addTab(self.tab_escaneo, "")
        self.tab_servicios = QtWidgets.QWidget()
        self.tab_servicios.setObjectName("tab_servicios")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_servicios)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.titulo_servicios = QtWidgets.QLabel(self.tab_servicios)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.titulo_servicios.setFont(font)
        self.titulo_servicios.setObjectName("titulo_servicios")
        self.verticalLayout_4.addWidget(self.titulo_servicios)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem1)
        self.desc_servicios = QtWidgets.QLabel(self.tab_servicios)
        self.desc_servicios.setObjectName("desc_servicios")
        self.verticalLayout_4.addWidget(self.desc_servicios)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_http = QtWidgets.QLabel(self.tab_servicios)
        self.label_http.setObjectName("label_http")
        self.horizontalLayout_2.addWidget(self.label_http)
        self.boton_in_http = QtWidgets.QPushButton(self.tab_servicios)
        self.boton_in_http.setObjectName("boton_in_http")
        self.boton_in_http.clicked.connect(self.inicia_http)
        self.horizontalLayout_2.addWidget(self.boton_in_http)
        self.boton_off_http = QtWidgets.QPushButton(self.tab_servicios)
        self.boton_off_http.setObjectName("boton_off_http")
        self.boton_off_http.clicked.connect(self.apaga_servicio_http)
        self.boton_off_http.setVisible(False)
        self.horizontalLayout_2.addWidget(self.boton_off_http)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_ftp = QtWidgets.QLabel(self.tab_servicios)
        self.label_ftp.setObjectName("label_ftp")
        self.horizontalLayout_3.addWidget(self.label_ftp)
        self.boton_in_ftp = QtWidgets.QPushButton(self.tab_servicios)
        self.boton_in_ftp.setObjectName("boton_in_ftp")
        self.boton_in_ftp.clicked.connect(self.inicia_ftp)
        self.horizontalLayout_3.addWidget(self.boton_in_ftp)
        self.boton_off_ftp = QtWidgets.QPushButton(self.tab_servicios)
        self.boton_off_ftp.setObjectName("boton_off_ftp")
        self.boton_off_ftp.clicked.connect(self.apaga_servicio_ftp)
        self.boton_off_ftp.setVisible(False)
        self.horizontalLayout_3.addWidget(self.boton_off_ftp)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_telnet = QtWidgets.QLabel(self.tab_servicios)
        self.label_telnet.setObjectName("label_telnet")
        self.horizontalLayout_4.addWidget(self.label_telnet)
        self.boton_in_telnet = QtWidgets.QPushButton(self.tab_servicios)
        self.boton_in_telnet.setObjectName("boton_in_telnet")
        self.boton_in_telnet.clicked.connect(self.inicia_telnet)
        self.horizontalLayout_4.addWidget(self.boton_in_telnet)
        self.boton_off_telnet = QtWidgets.QPushButton(self.tab_servicios)
        self.boton_off_telnet.setObjectName("boton_off_telnet")
        self.boton_off_telnet.clicked.connect(self.apaga_servicio_telnet)
        self.boton_off_telnet.setVisible(False)
        self.horizontalLayout_4.addWidget(self.boton_off_telnet)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_estado = QtWidgets.QLabel(self.tab_servicios)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_estado.sizePolicy().hasHeightForWidth())
        self.label_estado.setSizePolicy(sizePolicy)
        self.label_estado.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_estado.setFont(font)
        self.label_estado.setAlignment(QtCore.Qt.AlignCenter)
        self.label_estado.setObjectName("label_estado")
        self.verticalLayout.addWidget(self.label_estado)
        self.estado_http = QtWidgets.QLabel(self.tab_servicios)
        self.estado_http.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.estado_http.setObjectName("estado_http")
        self.verticalLayout.addWidget(self.estado_http)
        self.estado_ftp = QtWidgets.QLabel(self.tab_servicios)
        self.estado_ftp.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.estado_ftp.setObjectName("estado_ftp")
        self.verticalLayout.addWidget(self.estado_ftp)
        self.estado_telnet = QtWidgets.QLabel(self.tab_servicios)
        self.estado_telnet.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.estado_telnet.setObjectName("estado_telnet")
        self.verticalLayout.addWidget(self.estado_telnet)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_detalles_serv = QtWidgets.QLabel(self.tab_servicios)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_detalles_serv.setFont(font)
        self.label_detalles_serv.setObjectName("label_detalles_serv")
        self.verticalLayout_2.addWidget(self.label_detalles_serv)
        self.panel_servicios = QtWidgets.QTextEdit(self.tab_servicios)
        self.panel_servicios.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panel_servicios.sizePolicy().hasHeightForWidth())
        self.panel_servicios.setSizePolicy(sizePolicy)
        self.panel_servicios.setMinimumSize(QtCore.QSize(400, 0))
        self.panel_servicios.setObjectName("panel_servicios")
        self.verticalLayout_2.addWidget(self.panel_servicios)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.tabs.addTab(self.tab_servicios, "")
        self.verticalLayout_6.addWidget(self.tabs)
        principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 729, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuAcerca_de = QtWidgets.QMenu(self.menubar)
        self.menuAcerca_de.setObjectName("menuAcerca_de")
        principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(principal)
        self.statusbar.setObjectName("statusbar")
        principal.setStatusBar(self.statusbar)
        self.actionEncender_todos_los_servidores = QtWidgets.QAction(principal)
        self.actionEncender_todos_los_servidores.setObjectName("actionEncender_todos_los_servidores")
        self.actionApagar_todos_los_servidores = QtWidgets.QAction(principal)
        self.actionApagar_todos_los_servidores.setObjectName("actionApagar_todos_los_servidores")
        self.actionSalir = QtWidgets.QAction(principal)
        self.actionSalir.setObjectName("actionSalir")
        self.actionSalir_2 = QtWidgets.QAction(principal)
        self.actionSalir_2.setObjectName("actionSalir_2")
        self.menuArchivo.addAction(self.actionEncender_todos_los_servidores)
        self.menuArchivo.addAction(self.actionApagar_todos_los_servidores)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir_2)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAcerca_de.menuAction())
        self.retranslateUi(principal)
        self.tabs.setCurrentIndex(0)
        self.lista_ips.setColumnCount(3)
        menu = ["IP","MAC","Nombre"]
        self.lista_ips.setHorizontalHeaderLabels(menu)
        self.lista_ips.setColumnWidth(0,80)
        self.lista_ips.setColumnWidth(1,130)
        self.lista_ips.setColumnWidth(2,100)
        self.boton_seleccionar.setEnabled(False)
        self.boton_puertos.setEnabled(False)
        self.panel_puertos.setReadOnly(True)
        QtCore.QMetaObject.connectSlotsByName(principal)

    def retranslateUi(self, principal):
        _translate = QtCore.QCoreApplication.translate
        principal.setWindowTitle(_translate("principal", "Herramienta de análisis y servicios en red"))
        self.titulo_escaneo.setText(_translate("principal", "Escaneo de la red actual"))
        self.label_tipo_an.setText(_translate("principal", "Tipo de análisis"))
        self.boton_an_rapido.setText(_translate("principal", "Análisis rápido"))
        self.descr_an_rapido.setText(_translate("principal", "No garantiza la detección de todos los dispositivos."))
        self.boton_an_normal.setText(_translate("principal", "Análisis normal"))
        self.desc_an_normal.setText(_translate("principal", "Detecta más dispositivos en la red que el rápido."))
        self.boton_an_profundo.setText(_translate("principal", "Análisis profundo"))
        self.desc_an_profundo.setText(_translate("principal", "Obtiene la mayor cantidad de dispositivos conectados"))
        self.label_ip_disponibles.setText(_translate("principal", "IP\'s disponibles en la red"))
        self.boton_seleccionar.setText(_translate("principal", "Seleccionar"))
        self.label_ip_trabajo.setText(_translate("principal", "IP de trabajo:"))
        self.label_puertos.setText(_translate("principal", "Escaneo de puertos"))
        self.boton_puertos.setText(_translate("principal", "Iniciar escaneo"))
        self.label_puertos_abiertos.setText(_translate("principal", "Puertos abiertos"))
        #self.label_progreso.setText(_translate("principal", "Progreso del análisis"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_escaneo), _translate("principal", "Escaneo de red"))
        self.titulo_servicios.setText(_translate("principal", "Servicios y Servidores"))
        self.desc_servicios.setText(_translate("principal", "Los servidores de los que disponemos "))
        self.label_http.setText(_translate("principal", "Servidor HTTP"))
        self.boton_in_http.setText(_translate("principal", "Iniciar"))
        self.boton_off_http.setText(_translate("principal", "Apagar"))
        self.label_ftp.setText(_translate("principal", "Servidor FTP"))
        self.boton_in_ftp.setText(_translate("principal", "Iniciar"))
        self.boton_off_ftp.setText(_translate("principal", "Apagar"))
        self.label_telnet.setText(_translate("principal", "Servidor Telnet"))
        self.boton_in_telnet.setText(_translate("principal", "Iniciar"))
        self.boton_off_telnet.setText(_translate("principal", "Apagar"))
        self.label_estado.setText(_translate("principal", "Estado"))
        self.estado_http.setText(_translate("principal", "O"))
        self.estado_ftp.setText(_translate("principal", "O"))
        self.estado_telnet.setText(_translate("principal", "O"))
        self.label_detalles_serv.setText(_translate("principal", "Detalles de los servidores"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_servicios), _translate("principal", "Inicio de servicios"))
        self.menuArchivo.setTitle(_translate("principal", "Sistema"))
        self.menuAcerca_de.setTitle(_translate("principal", "Acerca de"))
        self.actionEncender_todos_los_servidores.setText(_translate("principal", "Encender todos los servidores"))
        self.actionApagar_todos_los_servidores.setText(_translate("principal", "Apagar todos los servidores"))
        self.actionSalir.setText(_translate("principal", "Salir"))
        self.actionSalir_2.setText(_translate("principal", "Salir"))

    def getMyIpAddress(self):
        return socket.gethostbyname(socket.gethostname())

    def getNetIpAddress(self,ip):
        split_ip = ip.split('.', 3)
        net_address = ""
        for e in range(len(split_ip) - 1):
            net_address += split_ip[e]
            net_address += '.'
        net_address += '0'
        net_address += '/'
        net_address += '24'
        return net_address

    def get_ip_net(self):
        return ipaddress.ip_network(self.getNetIpAddress(self.getMyIpAddress()))

    def get_all_hosts(self,hosts):
        return list(hosts)

    def selecciona_red(self):
        try:
            global ip_actual
            global actives
            self.panel_info_ip.clear()
            ip_actual = actives[self.lista_ips.currentRow()]
            self.panel_info_ip.append(ip_actual.ip)
            self.panel_info_ip.append(str(ip_actual.mac))
            self.panel_info_ip.append(str(ip_actual.name))
            self.panel_info_ip.append(str(ip_actual.classification))
        except Exception as e:
            print(e)
    def escanea_puertos(self):
        server_thread_http = threading.Thread(target=self.muestra_puertos)
        server_thread_http.start()

    def muestra_puertos(self):
        global ip_actual
        print(ip_actual.ip)
        puertos_abiertos,tiempo = PortScanner.scan_ports(ip_actual.ip,0,250)
        self.panel_info_ip.append("Puertos abiertos: "+str(puertos_abiertos))
        for n in range(len(puertos_abiertos)):
            self.panel_puertos.append("Puerto abierto: "+str(puertos_abiertos[n]))
        self.panel_puertos.append("Tiempo de escaneo"+str(tiempo))

    def get_active_hosts(self,z, t):
        ip_net = self.get_ip_net()
        all_hosts = list(ip_net.hosts())
        global actives
        actives = []
        n = 1
        QtGui.QGuiApplication.processEvents()
        for i in range(len(all_hosts)):
            output = subprocess.Popen(['ping', '-n', z, '-w', t, str(all_hosts[i])], stdout=subprocess.PIPE,startupinfo=info, ).communicate()[0]
            IP = str(all_hosts[i])
            print("Escaneando actualmente a: ", IP)
            #self.statusbar.showMessage("Escaneando actualmente a: "+str(IP))
            if "Respuesta desde " in output.decode('ISO-8859-1') and "TTL=" in output.decode('ISO-8859-1'):
                from subprocess import Popen, PIPE
                pid = Popen(["arp", "-n", IP], stdout=PIPE)
                s = pid.communicate()[0]
                comando = "arp -a " + IP
                resultado = subprocess.check_output(comando, shell=True)
                MAC_addr = str(resultado).replace('-', ':')
                p = re.compile(r'([0-9a-f]{2}(?::[0-9a-f]{2}){5})', re.IGNORECASE)
                mac = re.findall(p, MAC_addr)
                nombre = socket.getfqdn(IP)
                n += 1
                if nombre.startswith("192.") and not nombre.endswith(".1") and not nombre.endswith(".254"):
                    clasificaciones = "[Dispositivo móvil]"
                elif nombre.endswith(".254") or nombre.endswith(".1"):
                    clasificaciones = "[Módem raiz]"
                else:
                    clasificaciones = "[Laptop/Desktop]"
                if len(mac) <= 0:
                    mac = MACScanner.get_MAC_addr()
                current = Net(IP, mac, clasificaciones, nombre)
                actives.append(current)

    def print_actives(self):
        print("Conexiones activas en esta red:")
        global actives
        for i in range(len(actives)):
            rowPosition = self.lista_ips.rowCount()
            self.lista_ips.insertRow(rowPosition)
            self.lista_ips.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(actives[i].ip)))
            self.lista_ips.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(actives[i].mac)))
            self.lista_ips.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(actives[i].name)))

    def __initial__(self):
        self.statusbar.showMessage("Se ha completado el escaneo de la red")
        self.habilita_red()
        self.print_actives()

    def inicia_escaneo_rapido(self):
        hilo_escaneo_rapido = threading.Thread(target=self.escaneo_rapido)
        hilo_escaneo_rapido.start()

    def inicia_escaneo_normal(self):
        hilo_escaneo_normal = threading.Thread(target=self.escaneo_normal)
        hilo_escaneo_normal.start()

    def inicia_escaneo_profundo(self):
        hilo_escaneo_profundo = threading.Thread(target=self.escaneo_profundo)
        hilo_escaneo_profundo.start()

    def habilita_red(self):
        self.boton_an_normal.setEnabled(True)
        self.boton_an_rapido.setEnabled(True)
        self.boton_an_profundo.setEnabled(True)
        self.boton_seleccionar.setEnabled(True)
        self.boton_puertos.setEnabled(True)

    def bloquea_botones_an(self):
        self.statusbar.showMessage("Se ha iniciado el escaneo")
        self.boton_an_normal.setEnabled(False)
        self.boton_an_rapido.setEnabled(False)
        self.boton_an_profundo.setEnabled(False)
        self.boton_seleccionar.setEnabled(False)
        self.boton_puertos.setEnabled(False)

    def escaneo_rapido(self):
        self.bloquea_botones_an()
        self.get_active_hosts('1', '50')
        self.__initial__()

    def escaneo_normal(self):
        self.bloquea_botones_an()
        self.get_active_hosts('2', '50')
        self.__initial__()

    def escaneo_profundo(self):
        self.bloquea_botones_an()
        self.get_active_hosts('3', '200')
        self.__initial__()

    def inicia_http(self):
        self.panel_servicios.append("Servidor HTTP iniciado en "+IPScanner.getMyIpAddress()+" en el puerto "+str(HTTP_PORT))
        server_thread_http = threading.Thread(target=self.inicia_servicio_http)
        server_thread_http.start()

    def inicia_ftp(self):
        self.panel_servicios.append("Servidor FTP iniciado en "+IPScanner.getMyIpAddress()+" en el puerto "+str(FTP_PORT))
        server_thread_ftp = threading.Thread(target=self.inicia_servicio_ftp)
        server_thread_ftp.start()

    def inicia_telnet(self):
        self.panel_servicios.append("Servidor Telnet en "+IPScanner.getMyIpAddress()+" iniciado en el puerto "+str(TELNET_PORT))
        server_thread_tel = threading.Thread(target=self.inicia_servicio_telnet)
        server_thread_tel.start()

    def inicia_servicio_http(self):
        self.boton_in_http.setVisible(False)
        self.boton_off_http.setVisible(True)
        HTTPServer.start_http_server(IPScanner.getMyIpAddress(), HTTP_PORT, False)

    def apaga_servicio_http(self):
        self.panel_servicios.append("Servidor HTTP apagado")
        self.boton_in_http.setVisible(True)
        self.boton_off_http.setVisible(False)
        print("Server turned off")
        try:
            HTTPServer.apaga_servidor()
        except:
            pass

    def inicia_servicio_ftp(self):
        self.boton_in_ftp.setVisible(False)
        self.boton_off_ftp.setVisible(True)
        FTPServer.start_ftp_server(IPScanner.getMyIpAddress(), FTP_PORT)

    def apaga_servicio_ftp(self):
        self.panel_servicios.append("Servidor FTP apagado")
        self.boton_in_ftp.setVisible(True)
        self.boton_off_ftp.setVisible(False)
        print("Server turned off")
        try:
            FTPServer.apaga_servidor()
        except:
            pass

    def inicia_servicio_telnet(self):
        self.boton_in_telnet.setVisible(False)
        self.boton_off_telnet.setVisible(True)
        TelnetServer.start_telnet_server(IPScanner.getMyIpAddress(), TELNET_PORT)

    def apaga_servicio_telnet(self):
        self.panel_servicios.append("Servidor Telnet apagado")
        self.boton_in_telnet.setVisible(True)
        self.boton_off_telnet.setVisible(False)
        print("Server turned off")
        try:
            TelnetServer.apaga_servidor()
        except:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    principal = QtWidgets.QMainWindow()
    ui = Ui_principal()
    ui.setupUi(principal)
    principal.show()
    app.aboutToQuit.connect(principal.closeEvent)
    sys.exit(app.exec_())

