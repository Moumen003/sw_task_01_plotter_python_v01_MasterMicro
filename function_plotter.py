import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLineEdit, QPushButton, QLabel, QMessageBox)
from PySide2.QtCore import Qt

class FunctionPlotter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Function Plotter')
        self.setGeometry(100, 100, 1000, 600)

        # Central Widget and Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Main Vertical Layout
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Title
        self.title_label = QLabel('Master Micro SW Engineering Internship GUI made by Moumen Ibrahim')
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.main_layout.addWidget(self.title_label)

        # Instructional Message
        self.instruction_label = QLabel(
            'Dear user, please note that the only supported operators are: "+ - / * ^ log10() sqrt()". '
            'If you would like more features, please contact Moumen at moumenibrahim506@gmail.com and be ready to pay for what you ask unless you are going to pay for food then I am totally ok with it.'
        )
        self.instruction_label.setWordWrap(True)
        self.instruction_label.setStyleSheet("font-size: 12px;")
        self.main_layout.addWidget(self.instruction_label)

        # Horizontal Layout for controls and plot
        self.horizontal_layout = QHBoxLayout()
        self.main_layout.addLayout(self.horizontal_layout)

        # Controls Layout
        self.controls_layout = QVBoxLayout()
        self.horizontal_layout.addLayout(self.controls_layout)

        # Input Fields
        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText('Enter function of x (e.g., 5*x**3 + 2*x)')
        self.controls_layout.addWidget(self.function_input)

        self.min_input = QLineEdit()
        self.min_input.setPlaceholderText('Enter min x value')
        self.controls_layout.addWidget(self.min_input)

        self.max_input = QLineEdit()
        self.max_input.setPlaceholderText('Enter max x value')
        self.controls_layout.addWidget(self.max_input)

        # Plot Button
        self.plot_button = QPushButton('Plot')
        self.plot_button.clicked.connect(self.plot_function)
        self.controls_layout.addWidget(self.plot_button)

        # Matplotlib Figure and Canvas
        self.figure, self.ax = plt.subplots()
        self.ax.set_title('Best Plot')
        self.ax.set_xlabel('x-axis')
        self.ax.set_ylabel('y-axis')
        self.canvas = FigureCanvas(self.figure)
        self.horizontal_layout.addWidget(self.canvas)

    def plot_function(self):
        function = self.function_input.text()
        min_x = self.min_input.text()
        max_x = self.max_input.text()

        # Check for empty inputs
        if not function or not min_x or not max_x:
            QMessageBox.critical(self, 'Input Error', 'Input fields cannot be empty.')
            return

        try:
            # Convert min_x and max_x to floats
            min_x = float(min_x)
            max_x = float(max_x)

            # Check if min_x is less than max_x
            if min_x >= max_x:
                raise ValueError('Min x value must be less than Max x value and not equal.')
        except ValueError as ve:
            QMessageBox.critical(self, 'Input Error', str(ve))
            return

        # Generate x values
        try:
            x = np.linspace(min_x, max_x, 400)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error generating x values: {str(e)}')
            return

        # Evaluate the function
        try:
            y = self.evaluate_function(function, x)
        except ValueError as ve:
            QMessageBox.critical(self, 'Function Error', str(ve))
            return
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error evaluating function: {str(e)}')
            return

        # Plot the function
        try:
            self.ax.clear()
            self.ax.plot(x, y)
            self.ax.set_title('Best Plot')
            self.ax.set_xlabel('x-axis')
            self.ax.set_ylabel('y-axis')
            self.canvas.draw()
        except Exception as e:
            QMessageBox.critical(self, 'Plotting Error', f'Error plotting function: {str(e)}')

    def evaluate_function(self, function, x):
        try:
        # Replace ^ with ** for exponentiation, log10 and sqrt with their numpy equivalents
            function = function.replace('^', '**').replace('log10', 'np.log10').replace('sqrt', 'np.sqrt')
        
        # Temporarily suppress warnings to handle overflow cases
            with np.errstate(over='ignore'):
                y = eval(function)
        
        # Additional checks
            if 'log10' in function and np.any(x <= 0):
                raise ValueError('Logarithm input must be positive.')
            if '1/x' in function and np.any(x == 0):
                raise ValueError('Division by zero encountered.')

            return y
        except Exception as e:
            raise ValueError(f'Invalid function or input: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FunctionPlotter()
    window.show()
    sys.exit(app.exec_())
