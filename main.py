import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRect

class SquareApp(QWidget):
    def __init__(self):
        super().__init__()

        # Инициализация переменных
        self.squares = []  # список квадратов с их координатами и цветами
        self.success_count = 0
        self.fail_count = 0

        # Настройка UI
        self.initUI()

    def initUI(self):
        # Создаем кнопки и метку статистики
        self.add_button = QPushButton("Добавить квадрат", self)
        self.add_button.clicked.connect(self.add_square)

        self.remove_button = QPushButton("Удалить квадрат", self)
        self.remove_button.clicked.connect(self.remove_square)

        self.stats_label = QLabel("Успешные попытки: 0, Неудачные попытки: 0", self)

        # Устанавливаем вертикальный лейаут
        layout = QVBoxLayout()
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.stats_label)

        self.setLayout(layout)
        self.setWindowTitle('Square Drawer')
        self.setGeometry(100, 100, 600, 600)

    def add_square(self):
        size = 50
        max_attempts = 10
        for _ in range(max_attempts):
            # Генерация случайной позиции
            x = random.randint(0, self.width() - size)
            y = random.randint(0, self.height() - size)
            new_square = QRect(x, y, size, size)
            
            # Проверка на пересечение
            if not any(new_square.intersects(square[0]) for square in self.squares):
                color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                self.squares.append((new_square, color))
                self.success_count += 1
                break
            else:
                for i, (square, color) in enumerate(self.squares):
                    self.squares[i] = (square, QColor(255, 0, 0))  # окраска в красный при пересечении
                self.fail_count += 1
        self.update_stats()
        self.update()

    def remove_square(self):
        if self.squares:
            self.squares.pop()
            self.reset_colors()
            self.update_stats()
            self.update()

    def reset_colors(self):
        # Восстанавливаем исходный цвет квадратов
        for i, (square, color) in enumerate(self.squares):
            self.squares[i] = (square, QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def update_stats(self):
        # Обновляем текст метки со статистикой
        self.stats_label.setText(f"Успешные попытки: {self.success_count}, Неудачные попытки: {self.fail_count}")

    def paintEvent(self, event):
        # Рисуем квадраты
        qp = QPainter()
        qp.begin(self)
        for square, color in self.squares:
            qp.setBrush(color)
            qp.drawRect(square)
        qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SquareApp()
    ex.show()
    sys.exit(app.exec_())
