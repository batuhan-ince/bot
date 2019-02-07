import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class Emojis(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        poop_label = QLabel(self)
        self.show()

        input_str = input("Please Input the Name of the Emoji you want to see:)) \n To Finish Process type 'finish' ")
        while not input_str == "finish":
            input_str = input("Please Input the Name of the Emoji you want to see:))")

            if input_str == "poop":
                poop = QPixmap('poop.png')
                poop_label.setPixmap(poop)
                self.resize(poop.width(), poop.height())
                self.update()
            elif input_str == "smiley":
                smiley = QPixmap('smiley.png')
                poop_label.setPixmap(smiley)
                self.resize(smiley.width(), smiley.height())
                self.update()
            elif input_str == "smirk":
                smirk = QPixmap('smirk.png')
                poop_label.setPixmap(smirk)
                self.resize(smirk.width(), smirk.height())
                self.update()

            elif input_str == "surprised":
                surprised = QPixmap('surprised.png')
                poop_label.setPixmap(surprised)
                self.resize(surprised.width(), surprised.height())
                self.update()
            elif input_str == "heart_eyes":
                heart_eyes = QPixmap('heart_eyes.png')
                poop_label.setPixmap(heart_eyes)
                self.resize(heart_eyes.width(), heart_eyes.height())
                self.update()
            elif input_str == "crying":
                crying = QPixmap('crying.png')
                poop_label.setPixmap(crying)
                self.resize(crying.width(), crying.height())
                self.update()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Emojis()
    sys.exit(app.exec_())