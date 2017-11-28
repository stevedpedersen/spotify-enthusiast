from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QAction, QLineEdit, QVBoxLayout, QHBoxLayout, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import *
import os

class SingleFrameWindow(QWidget):

    def __init__(self, screen_w, screen_h):
        super().__init__()
        self.screen_w = screen_w
        self.screen_h = screen_h

    def init_popup(self, x, y, window_title, object_title):
        self.x = x
        self.y = y
        self.window_title = window_title
        self.object_title = object_title
        self.setWindowTitle(self.window_title)
        self.setObjectName(self.object_title)
        
        self.setFocus()
        # A modal widget prevents widgets in all other windows from getting any input.
        # self.isModal()


    def add_frame(self, frame):
        for component in frame.get_popup_components():
            component.show()        

        self.w = frame.popup_text.width()        
        self.h = frame.popup_text.height() if frame.popup_text.height() < self.screen_h else self.screen_h-100

        # frame.popup_text.setAlignment(Qt.AlignTop)
        popup_scroll = QScrollArea()
        popup_scroll.setWidget(frame.popup_text)
        popup_scroll.setWidgetResizable(True)          
        popup_scroll.setFixedHeight(self.h)
        popup_scroll.setStyleSheet('background-color: #1D1D1D;')  
        popup_layout = QVBoxLayout(self)
        popup_layout.addWidget(popup_scroll)
       
        self.setGeometry(self.x, self.y, self.w, self.h)
        self.load_styles()

        frame.show()


    # Opens css stylesheet and apply it to Spotify Infosuite elements
    def load_styles(self):
        self.setStyleSheet('')
        style = ''
        # with open('./view/style.css') as f:
        with open(os.path.dirname(__file__) + '/style.css') as f:
            for line in f:
                style += line
                # print(line)
        self.setStyleSheet(style)

