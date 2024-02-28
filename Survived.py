# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'survived.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(918, 834)
        Form.setStyleSheet("QWidget#Form{\n"
"background-color: qlineargradient(spread:pad, x1:0.323, y1:0.374682, x2:1, y2:0.858, stop:0 rgba(0, 255, 234, 255), stop:0.988636 rgba(225, 225, 225, 255));}")
        self.pclassBox = QtWidgets.QLineEdit(Form)
        self.pclassBox.setGeometry(QtCore.QRect(290, 290, 171, 41))
        self.pclassBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pclassBox.setObjectName("pclassBox")
        self.parchBox = QtWidgets.QLineEdit(Form)
        self.parchBox.setGeometry(QtCore.QRect(290, 360, 171, 41))
        self.parchBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.parchBox.setObjectName("parchBox")
        self.pred_btn = QtWidgets.QPushButton(Form)
        self.pred_btn.setGeometry(QtCore.QRect(570, 650, 171, 51))
        self.pred_btn.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"background-color: qlineargradient(spread:pad, x1:0.323, y1:0.374682, x2:1, y2:0.858, stop:0 rgba(0, 18, 255, 255), stop:0.988636 rgba(225, 225, 225, 255));")
        self.pred_btn.setObjectName("pred_btn")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(100, 650, 431, 41))
        self.label_8.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.fare = QtWidgets.QLabel(Form)
        self.fare.setGeometry(QtCore.QRect(100, 430, 91, 41))
        self.fare.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.fare.setObjectName("fare")
        self.age = QtWidgets.QLabel(Form)
        self.age.setGeometry(QtCore.QRect(100, 150, 91, 41))
        self.age.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.age.setObjectName("age")
        self.parch = QtWidgets.QLabel(Form)
        self.parch.setGeometry(QtCore.QRect(100, 360, 101, 41))
        self.parch.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.parch.setObjectName("parch")
        self.embarked = QtWidgets.QLabel(Form)
        self.embarked.setGeometry(QtCore.QRect(100, 570, 151, 41))
        self.embarked.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.embarked.setObjectName("embarked")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(100, 730, 321, 31))
        self.label_9.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.sibsp = QtWidgets.QLabel(Form)
        self.sibsp.setGeometry(QtCore.QRect(100, 500, 111, 41))
        self.sibsp.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.sibsp.setObjectName("sibsp")
        self.resultBox = QtWidgets.QLabel(Form)
        self.resultBox.setGeometry(QtCore.QRect(580, 730, 161, 51))
        self.resultBox.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.resultBox.setText("")
        self.resultBox.setObjectName("resultBox")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 0, 741, 101))
        self.label.setStyleSheet("font: 75 25pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.fareBox = QtWidgets.QLineEdit(Form)
        self.fareBox.setGeometry(QtCore.QRect(290, 430, 171, 41))
        self.fareBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.fareBox.setObjectName("fareBox")
        self.sibspBox = QtWidgets.QLineEdit(Form)
        self.sibspBox.setGeometry(QtCore.QRect(290, 500, 171, 41))
        self.sibspBox.setObjectName("sibspBox")
        self.pclass = QtWidgets.QLabel(Form)
        self.pclass.setGeometry(QtCore.QRect(100, 290, 111, 41))
        self.pclass.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.pclass.setObjectName("pclass")
        self.ageBox = QtWidgets.QLineEdit(Form)
        self.ageBox.setGeometry(QtCore.QRect(290, 150, 171, 41))
        self.ageBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.ageBox.setObjectName("ageBox")
        self.embarkedBox = QtWidgets.QLineEdit(Form)
        self.embarkedBox.setGeometry(QtCore.QRect(290, 570, 171, 41))
        self.embarkedBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.embarkedBox.setObjectName("embarkedBox")
        self.sexBox = QtWidgets.QLineEdit(Form)
        self.sexBox.setGeometry(QtCore.QRect(290, 220, 171, 41))
        self.sexBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.sexBox.setObjectName("sexBox")
        self.sex = QtWidgets.QLabel(Form)
        self.sex.setGeometry(QtCore.QRect(100, 220, 81, 41))
        self.sex.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.sex.setObjectName("sex")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pred_btn.setText(_translate("Form", "Predict"))
        self.label_8.setText(_translate("Form", "Click Here To Get The Result"))
        self.fare.setText(_translate("Form", "Fare"))
        self.age.setText(_translate("Form", "Age"))
        self.parch.setText(_translate("Form", "PArch"))
        self.embarked.setText(_translate("Form", "Embarked"))
        self.label_9.setText(_translate("Form", "HERE IS THE RESULT"))
        self.sibsp.setText(_translate("Form", "SibSp"))
        self.label.setText(_translate("Form", "Predict Whether Person Survived Or Not \n"
"During Titanic"))
        self.pclass.setText(_translate("Form", "PClass"))
        self.sex.setText(_translate("Form", "Sex"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
