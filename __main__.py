import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi('login/login.ui', self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password) #hide the password
        self.creataccbtn.clicked.connect(self.gotocreat)

    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        print(f'Succesfully logged In with Email:{email} and Password:{password}')

    def gotocreat(self):
        creatacc =CreatAcc()
        widget.addWidget(creatacc)
        widget.setCurrentIndex(widget.currentIndex()+1)


class CreatAcc(QDialog):
    def __init__(self):
        super(CreatAcc, self).__init__()
        loadUi('login/creatacc.ui', self)
        self.signupbtn.clicked.connect(self.creatacc_fun)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def creatacc_fun(self):
        email = self.email.text()
        if self.password.text()== self.confirmpass.text():
            password = self.password.text()
            print(f'Succesfully logged In with Email:{email} and Password:{password}')
        else:
            print('Passwords do not match')
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)


#sys.argv-->There are a bunch of arguments that you can pass like styles, debugging stuff and so on
app = QApplication([])  
mainwindow = Login()
widget=QtWidgets.QStackedWidget() #stck contain several mainwindow if i want to switch between them

widget.addWidget(mainwindow)
widget.setFixedWidth(380)
widget.setFixedHeight(520)
widget.setWindowTitle('Logging App')

widget.show()
app.exec_()


