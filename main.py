import sys 
import random 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRect


class SquareApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("square drawer")
        self.setGeometry(100, 100, 600, 400)
        
        self.squares = []
        self.square_size = 50
        
        # Основной виджет и макет
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        
        layout = QVBoxLayout(main_widget)
        
        # Кнопки добавления и удаления квадратов
        self.add_button = QPushButton("Добавить квадрат")
        self.add_button.clicked.connect(self.add_square)
        
        self.remove_button = QPushButton("Удалить квадрат")
        self.remove_button.clicked.connect(self.remove_square)
        
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)

    def add_square(self):
        # Пытаемся найти случайное место для нового квадрата
        for _ in range(100):  # Попробуем 100 раз найти место без пересечения
            x = random.randint(0, self.width() - self.square_size)
            y = random.randint(0, self.height() - self.square_size)
            new_square = QRect(x, y, self.square_size, self.square_size)
            
            # Проверка на пересечение
            if not any(new_square.intersects(square) for square in self.squares):
                self.squares.append(new_square)
                self.update()
                break

    def remove_square(self):
        if self.squares:
            self.squares.pop()
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(0, 128, 255))  # Синий цвет квадратов
        
        for square in self.squares:
            painter.drawRect(square)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SquareApp()
    window.show()
    sys.exit(app.exec_())
