import pytest
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt
from PySide2.QtGui import QGuiApplication
from PySide2.QtWidgets import QMessageBox
from function_plotter import FunctionPlotter  # Make sure this matches your file name
import numpy as np


@pytest.fixture
def app(qtbot):
    window = FunctionPlotter()
    qtbot.addWidget(window)
    window.show()
    return qtbot, window

def test_initial_state(app):
    qtbot, window = app
    assert window.function_input.text() == ''
    assert window.min_input.text() == ''
    assert window.max_input.text() == ''
    assert window.ax.get_title() == 'Best Plot'
    assert window.ax.get_xlabel() == 'x-axis'
    assert window.ax.get_ylabel() == 'y-axis'


def test_plot_invalid_function(app, qtbot):
    qtbot, window = app
    window.function_input.setText('5*x**2 + 2*x +')
    window.min_input.setText('-10')
    window.max_input.setText('10')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    
    # Use waitUntil to wait for a condition with a timeout
    qtbot.waitUntil(lambda: window.isVisible(), timeout=5000)
    
    assert window.isVisible()


def test_min_equal_max(app, qtbot):
    qtbot, window = app
    window.function_input.setText('5*x**2 + 2*x')
    window.min_input.setText('10')
    window.max_input.setText('10')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    
    # Wait until the condition is met or timeout occurs
    qtbot.waitUntil(lambda: not window.isVisible(), timeout=5000)
    
    assert not window.isVisible()


def test_exponential_function(app):
    qtbot, window = app
    window.function_input.setText('2**x')
    window.min_input.setText('0')
    window.max_input.setText('5')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    assert len(window.ax.lines) == 1  # Ensure that a plot is drawn
    assert window.ax.get_title() == 'Best Plot'

def test_large_range(app):
    qtbot, window = app
    window.function_input.setText('x**2')
    window.min_input.setText('-1000')
    window.max_input.setText('1000')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    assert len(window.ax.lines) == 1  # Ensure that a plot is drawn
    assert window.ax.get_title() == 'Best Plot'



def test_function_with_spaces(app):
    qtbot, window = app
    window.function_input.setText('  5*x**2  +  2*x  ')
    window.min_input.setText('0')
    window.max_input.setText('10')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    assert len(window.ax.lines) == 1  # Ensure that a plot is drawn
    assert window.ax.get_title() == 'Best Plot'

def test_function_with_high_degree_polynomial(app):
    qtbot, window = app
    window.function_input.setText('x**10 - x**5 + x - 1')
    window.min_input.setText('-10')
    window.max_input.setText('10')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    assert len(window.ax.lines) == 1  # Ensure that a plot is drawn
    assert window.ax.get_title() == 'Best Plot'



def test_function_plot_title(app):
    qtbot, window = app
    window.function_input.setText('x**2')
    window.min_input.setText('-10')
    window.max_input.setText('10')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    assert window.ax.get_title() == 'Best Plot'



def test_plot_title_on_empty_function(app, qtbot):
    qtbot, window = app
    window.function_input.setText('')
    window.min_input.setText('0')
    window.max_input.setText('10')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    
    # Wait until the plot title is set to the expected value or timeout occurs
    qtbot.waitUntil(lambda: window.ax.get_title() == 'Best Plot', timeout=5000)
    
    assert window.ax.get_title() == 'Best Plot'

def test_min_greater_than_max(app, qtbot):
    qtbot, window = app
    window.function_input.setText('x**2')
    window.min_input.setText('10')
    window.max_input.setText('5')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    
    # Wait until a certain condition is met or timeout occurs
    qtbot.waitUntil(lambda: not window.isVisible(), timeout=5000)
    
    assert not window.isVisible()

def test_invalid_function_format(app, qtbot):
    qtbot, window = app
    window.function_input.setText('x**2 + log(x)')
    window.min_input.setText('0')
    window.max_input.setText('10')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    
    # Wait until the window is no longer visible or until the timeout occurs
    qtbot.waitUntil(lambda: not window.isVisible(), timeout=5000)
    
    assert not window.isVisible()

def test_invalid_characters_in_function(app, qtbot):
    qtbot, window = app
    window.function_input.setText('x**2 + abc')
    window.min_input.setText('0')
    window.max_input.setText('10')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    
    # Wait until the window is no longer visible or until the timeout occurs
    qtbot.waitUntil(lambda: not window.isVisible(), timeout=5000)
    
    assert not window.isVisible()


def test_empty_function_input(app, qtbot):
    qtbot, window = app
    window.function_input.setText('')
    window.min_input.setText('0')
    window.max_input.setText('10')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    
    # Wait until the window is no longer visible or until the timeout occurs
    qtbot.waitUntil(lambda: not window.isVisible(), timeout=5000)
    
    assert not window.isVisible()

def test_empty_min_max_input(app, qtbot):
    qtbot, window = app
    window.function_input.setText('x**2')
    window.min_input.setText('')
    window.max_input.setText('')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    
    # Wait until the window is no longer visible or until the timeout occurs
    qtbot.waitUntil(lambda: not window.isVisible(), timeout=5000)
    
    assert not window.isVisible()

def test_invalid_min_max_input(app, qtbot):
    qtbot, window = app
    window.function_input.setText('x**2')
    window.min_input.setText('ten')
    window.max_input.setText('fifteen')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    
    # Wait until the window is not visible or a timeout occurs
    qtbot.waitUntil(lambda: not window.isVisible(), timeout=5000)
    
    assert not window.isVisible()

def test_large_input_values(app):
    qtbot, window = app
    window.function_input.setText('x**2')
    window.min_input.setText('-1e+300')
    window.max_input.setText('1e+300')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    assert len(window.ax.lines) == 1  # Ensure that a plot is drawn
    assert window.ax.get_title() == 'Best Plot'

def test_function_with_missing_parentheses(app, qtbot):
    qtbot, window = app
    window.function_input.setText('np.log10x')
    window.min_input.setText('1')
    window.max_input.setText('10')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    
    # Wait until a condition is met or timeout occurs
    qtbot.waitUntil(lambda: not window.isVisible(), timeout=5000)
    
    assert not window.isVisible()

def test_function_with_unrecognized_functions(app, qtbot):
    qtbot, window = app
    window.function_input.setText('unknown_func(x)')
    window.min_input.setText('0')
    window.max_input.setText('10')
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)
    
    # Wait until a condition is met or timeout occurs
    qtbot.waitUntil(lambda: not window.isVisible(), timeout=5000)
    
    assert not window.isVisible()


if __name__ == '__main__':
    pytest.main()
