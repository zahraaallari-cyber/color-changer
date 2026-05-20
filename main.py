import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout, QSlider
)
from PySide6.QtCore import Qt


class ColorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Color Changer App")
        self.setGeometry(100, 100, 400, 350)

        
        self.title = QLabel("Color Changer App")
        self.title.setStyleSheet("font-size: 20px; font-weight: bold;")

        
        self.description = QLabel("Use sliders or buttons to change the color.")

        
        self.color_label = QLabel("RGB(255,255,255)")

        
        self.r_slider = QSlider(Qt.Horizontal)
        self.g_slider = QSlider(Qt.Horizontal)
        self.b_slider = QSlider(Qt.Horizontal)

        for slider in [self.r_slider, self.g_slider, self.b_slider]:
            slider.setRange(0, 255)
            slider.setValue(255)
            slider.valueChanged.connect(self.update_color)

        
        self.red_btn = QPushButton("Red")
        self.green_btn = QPushButton("Green")
        self.blue_btn = QPushButton("Blue")
        self.reset_btn = QPushButton("Reset")

        self.red_btn.clicked.connect(lambda: self.set_color(255, 0, 0))
        self.green_btn.clicked.connect(lambda: self.set_color(0, 255, 0))
        self.blue_btn.clicked.connect(lambda: self.set_color(0, 0, 255))
        self.reset_btn.clicked.connect(lambda: self.set_color(255, 255, 255))

        
        layout = QVBoxLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.description)
        layout.addWidget(self.color_label)

        layout.addWidget(QLabel("Red"))
        layout.addWidget(self.r_slider)

        layout.addWidget(QLabel("Green"))
        layout.addWidget(self.g_slider)

        layout.addWidget(QLabel("Blue"))
        layout.addWidget(self.b_slider)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.red_btn)
        button_layout.addWidget(self.green_btn)
        button_layout.addWidget(self.blue_btn)

        layout.addLayout(button_layout)
        layout.addWidget(self.reset_btn)

        self.setLayout(layout)

        self.update_color()

    
    def update_color(self):
        r = self.r_slider.value()
        g = self.g_slider.value()
        b = self.b_slider.value()

        self.setStyleSheet(f"background-color: rgb({r},{g},{b});")
        self.color_label.setText(f"RGB({r},{g},{b})")

    
    def set_color(self, r, g, b):
        self.r_slider.setValue(r)
        self.g_slider.setValue(g)
        self.b_slider.setValue(b)



app = QApplication(sys.argv)
window = ColorApp()
window.show()
app.exec()