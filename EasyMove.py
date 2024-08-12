import os

from PyQt5 import QtCore, QtGui, QtWidgets
import shutil
class functions:
	def __init__(self):
		pass
class Ui_MainWindow(functions):
	def __init__(self):
		self.val = ''

	def JPG_Func(self):
		format = '.JPG'
		self.val=format
		print("JPG button clicked.")
	def jpeg_Func(self):
		format = '.jpeg'
		self.val=format
		print("jpeg function called.")
	def JPEG_Func(self):
		format = '.JPEG'
		self.val=format
		print("JPEG button clicked.")
	def jpg_Func(self):
		format = '.jpg'
		self.val=format
		print("jpg button clicked.")
	def MP4_Func(self):
		format = '.MP4'
		self.val=format
		print("MP4 button clicked.")
	def mp4_Func(self):
		format = '.srt'
		self.val=format
		print("srt_Func button clicked.")
	def PNG_Func(self):
		format = '.PNG'
		self.val=format
		print("PNG button clicked.")
	def png_Func(self):
		format = '.png'
		self.val=format
		print("png button clicked.")
	def MOV_Func(self):
		format = '.MOV'
		self.val=format
		print("MPV button clicked.")
	def mov_Func(self):
		format = '.mov'
		self.val=format
		print("mov button clicked.")
	def InFunc(self):
		self.infile=QtWidgets.QFileDialog.getExistingDirectory()
		print("IN button clicked.")
	def OutFunc(self):
		self.out = QtWidgets.QFileDialog.getExistingDirectory()
		print("Out button clicked.")
	def Gobtn(self):
		print(self.val)
		ls = os.listdir(self.infile)
		print(ls)
		for i in ls:
			if f"{i}".startswith('.'):
				continue
			if i.endswith(f'{self.val}'.upper()) or i.endswith(f'{self.val}'.lower()):
				print(i)
				if os.path.exists(f"{self.out}/{i}"):
					print("File Exist.")
				else:
					shutil.move(src=f"{self.infile}/{i}", dst=self.out)
		# print("Go button clicked.")
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(448, 300)
		MainWindow.setMaximumSize(QtCore.QSize(448, 300))
		MainWindow.setAutoFillBackground(False)
		MainWindow.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		self.widget = QtWidgets.QWidget(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
		self.widget.setSizePolicy(sizePolicy)
		self.widget.setStyleSheet("background:black;border-radius:10px;")
		self.widget.setObjectName("widget")
		self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
		self.gridLayout_2.setContentsMargins(4, 4, 4, 4)
		self.gridLayout_2.setVerticalSpacing(4)
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.label = QtWidgets.QLabel(self.widget)
		self.label.setStyleSheet("color:white;")
		self.label.setObjectName("label")
		self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
		self.label_2 = QtWidgets.QLabel(self.widget)
		self.label_2.setStyleSheet("color:white;")
		self.label_2.setObjectName("label_2")
		self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
		self.inputBtn = QtWidgets.QPushButton(self.widget)
		self.inputBtn.setStyleSheet("background:grey;border-radius:5px;")
		self.inputBtn.setObjectName("inputBtn")
		self.gridLayout_2.addWidget(self.inputBtn, 0, 1, 1, 1)
		self.inputBtn.clicked.connect(self.InFunc)
		self.outputBtn = QtWidgets.QPushButton(self.widget)
		self.outputBtn.setStyleSheet("background:grey;border-radius:5px;")
		self.outputBtn.setObjectName("outputBtn")
		self.gridLayout_2.addWidget(self.outputBtn, 1, 1, 1, 1)
		self.outputBtn.clicked.connect(self.OutFunc)
		self.gridLayout.addWidget(self.widget, 0, 0, 1, 1, QtCore.Qt.AlignTop)
		self.widget_2 = QtWidgets.QWidget(self.centralwidget)
		self.widget_2.setStyleSheet("background:black;border-radius:10px;")
		self.widget_2.setObjectName("widget_2")
		self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
		self.gridLayout_3.setContentsMargins(4, 4, 4, 4)
		self.gridLayout_3.setVerticalSpacing(4)
		self.gridLayout_3.setObjectName("gridLayout_3")
		self.jpeg = QtWidgets.QPushButton(self.widget_2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.jpeg.sizePolicy().hasHeightForWidth())
		self.jpeg.setSizePolicy(sizePolicy)
		self.jpeg.setStyleSheet("background:white;color:black;border-radius:5px")
		self.jpeg.setObjectName("jpeg")
		self.gridLayout_3.addWidget(self.jpeg, 1, 1, 1, 1)
		self.jpeg.clicked.connect(self.jpeg_Func)
		self.FileFormatLabel = QtWidgets.QLabel(self.widget_2)
		self.FileFormatLabel.setStyleSheet("color:white;")
		self.FileFormatLabel.setObjectName("FileFormatLabel")
		self.gridLayout_3.addWidget(self.FileFormatLabel, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
		self.mp4 = QtWidgets.QPushButton(self.widget_2)
		self.mp4.setStyleSheet("background:white;color:black;border-radius:5px;")
		self.mp4.setObjectName("mp4")
		self.gridLayout_3.addWidget(self.mp4, 5, 1, 1, 1)
		self.mp4.clicked.connect(self.mp4_Func)
		self.png = QtWidgets.QPushButton(self.widget_2)
		self.png.setStyleSheet("background:white;color:black;border-radius:5px;")
		self.png.setObjectName("png")
		self.gridLayout_3.addWidget(self.png, 7, 1, 1, 1)
		self.png.clicked.connect(self.png_Func)
		self.MP4 = QtWidgets.QPushButton(self.widget_2)
		self.MP4.setStyleSheet("background:white;color:black;border-radius:5px;")
		self.MP4.setObjectName("MP4")
		self.gridLayout_3.addWidget(self.MP4, 4, 1, 1, 1)
		self.MP4.clicked.connect(self.MP4_Func)
		self.JPEG = QtWidgets.QPushButton(self.widget_2)
		self.JPEG.setStyleSheet("background:white;color:black;border-radius:5px;")
		self.JPEG.setObjectName("JPEG")
		self.gridLayout_3.addWidget(self.JPEG, 2, 1, 1, 1)
		self.JPEG.clicked.connect(self.JPEG_Func)
		self.PNG = QtWidgets.QPushButton(self.widget_2)
		self.PNG.setStyleSheet("background:white;color:black;border-radius:5px;")
		self.PNG.setObjectName("PNG")
		self.gridLayout_3.addWidget(self.PNG, 6, 1, 1, 1)
		self.PNG.clicked.connect(self.PNG_Func)
		self.jpg = QtWidgets.QPushButton(self.widget_2)
		self.jpg.setStyleSheet("background:white;color:black;border-radius:5px;")
		self.jpg.setObjectName("jpg")
		self.gridLayout_3.addWidget(self.jpg, 3, 1, 1, 1)
		self.jpg.clicked.connect(self.jpg_Func)
		self.JPG = QtWidgets.QPushButton(self.widget_2)
		self.JPG.setStyleSheet("background:white;color:black;border-radius:5px;")
		self.JPG.setObjectName("JPG")
		self.gridLayout_3.addWidget(self.JPG, 0, 1, 1, 1)
		self.JPG.clicked.connect(self.JPG_Func)
		self.MOV = QtWidgets.QPushButton(self.widget_2)
		self.MOV.setStyleSheet("background:white;color:black;border-radius:5px;")
		self.MOV.setObjectName("MOV")
		self.gridLayout_3.addWidget(self.MOV, 8, 1, 1, 1)
		self.MOV.clicked.connect(self.MOV_Func)
		self.mov = QtWidgets.QPushButton(self.widget_2)
		self.mov.setStyleSheet("background:white;color:black;border-radius:5px;")
		self.mov.setObjectName("mov")
		self.gridLayout_3.addWidget(self.mov, 9, 1, 1, 1)
		self.mov.clicked.connect(self.mov_Func)
		self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1, QtCore.Qt.AlignTop)
		self.GoBtn = QtWidgets.QPushButton(self.centralwidget)
		self.GoBtn.setStyleSheet("background:white;color:black")
		self.GoBtn.setObjectName("GoBtn")
		self.gridLayout.addWidget(self.GoBtn, 1, 0, 1, 2)
		self.GoBtn.clicked.connect(self.Gobtn)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 22))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.toolBar = QtWidgets.QToolBar(MainWindow)
		self.toolBar.setObjectName("toolBar")
		MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "Input Directory"))
		self.label_2.setText(_translate("MainWindow", "Output Directory"))
		self.inputBtn.setText(_translate("MainWindow", "In"))
		self.outputBtn.setText(_translate("MainWindow", "Out"))
		self.jpeg.setText(_translate("MainWindow", ".jpeg"))
		self.FileFormatLabel.setText(_translate("MainWindow", "File Format"))
		self.mp4.setText(_translate("MainWindow", ".srt"))
		self.png.setText(_translate("MainWindow", ".png"))
		self.MP4.setText(_translate("MainWindow", ".MP4"))
		self.JPEG.setText(_translate("MainWindow", ".JPEG"))
		self.PNG.setText(_translate("MainWindow", ".PNG"))
		self.jpg.setText(_translate("MainWindow", ".jpg"))
		self.JPG.setText(_translate("MainWindow", ".JPG"))
		self.MOV.setText(_translate("MainWindow", ".MOV"))
		self.mov.setText(_translate("MainWindow", ".mov"))
		self.GoBtn.setText(_translate("MainWindow", "Go->"))
		self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
