**Assalam alaykom**
*****very very very important****
the code was tested with Pyside6 and python 3.12
although the requirement was for Pyside 2 I had to work with python 3.12 which is not compatible with pyside2 hence upgraded to pyside6
however upon finishing the project I changed every naming of pyside6 to pyside2 in both the function plotter file and test file
and in the main function i changed app.exec to app.exec_ to be pyside2 comptaible
if any error triggers then please change every pyside2 to pyside6 and return app.exec_ back to app.exec

# Function Plotter

This is a Python GUI program that plots an arbitrary user-entered function. The GUI is built using PySide2 and Matplotlib.
*******Credits: GeeksforGeeks, Stack Overflow, ChatGPT********

## Features

- Plot any mathematical function of x.
- Input validation and error messages for invalid inputs.
- Supports operators: +, -, *, /, ^, log10(), sqrt().

## Requirements

- Python 3.7+
- PySide2
- Matplotlib
- pytest
- pytest-qt

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd function_plotter
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application:
```bash
py function_plotter.py
```
and for the test:
```bash
pytest test_function_plotter.py
```

***************************************function_plotter.py************************************

Overview:

    FunctionPlotter.py is a Python application designed to offer a graphical user interface (GUI) for plotting mathematical functions. Leveraging PySide2 for the GUI and Matplotlib for visualization, this application allows users to input mathematical functions, define the range for the x-axis, and view the resulting plots.

Programming Concepts:

    Object-Oriented Programming (OOP): Utilizes OOP principles with the FunctionPlotter class inheriting from QMainWindow, encapsulating the application's functionality.
    Event-Driven Programming: Implements event handling to respond to user interactions, such as button clicks.
    Libraries Used
    PySide2: For GUI components:
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
    Matplotlib: For plotting:
    plt.subplots(), FigureCanvasQTAgg
    NumPy: For numerical operations:
    np.linspace(), np.log10(), np.sqrt()
    Methods
    The FunctionPlotter class contains the following methods:

*__init__*

    Purpose: Initializes the main window, sets up the layout, and creates GUI elements.
    Details: Configures the title, instructional message, input fields, and plot button. Sets up Matplotlib for plotting.


*plot_function*

    Purpose: Manages the plotting of the mathematical function based on user input.
    Details: Validates inputs, generates x-values, evaluates the function, and updates the plot. Displays error messages for invalid inputs or plotting issues.


*evaluate_function*

Purpose: Evaluates the mathematical function provided by the user.
Details: Converts the function string to Python expressions, performs the evaluation, and handles errors related to invalid functions or mathematical operations.


****Key Functionalities****

GUI Layout:

    Utilizes vertical and horizontal layouts to organize widgets for a user-friendly interface.


Input Handling:
Users can input a function and specify the x-axis range. Input validation ensures correctness and usability.


Function Evaluation and Plotting:
Processes the input, evaluates the function, and updates the plot accordingly.


Error Handling:
Employs QMessageBox to notify users of input errors, evaluation problems, or plotting issues.
Error Handling
Validation Errors: Handles empty inputs, invalid function formats, and range-related issues.
Evaluation Errors: Manages exceptions that occur during function evaluation.
Plotting Errors: Provides feedback if issues arise during the plotting process.




***************************************test_function_plotter.py************************************


test_function_plotter.py test file uses pytest and pytest-qt to ensure the functionality of the FunctionPlotter GUI application. It includes tests for various input scenarios and checks the application's behavior and error handling.

it also looks for and tests Attribution, Assertion, Runtime, Type errors, and Logical Errors

1)Attribution Errors
These errors occur when there is an issue with assigning values or properties.

test_initial_state: Checks initial state values and default settings to ensure they are correctly set up.
test_plot_title_on_empty_function: Verifies that the plot title is correctly set, even with an empty function.


2)Assertion Errors
These errors occur when the expected outcome does not match the actual result.

test_plot_invalid_function: Asserts that the application is visible if an invalid function is entered, and the condition is checked.
test_min_greater_than_max: Asserts that the appropriate error message is shown when the minimum x-value is greater than the maximum x-value.
test_min_equal_max: Asserts that the application hides the plot when the minimum and maximum x-values are equal.
test_empty_function: Asserts that no plot is generated for an empty function input.
test_exponential_function: Asserts that a plot is drawn for an exponential function and checks the plot title.
test_large_range: Asserts that a plot is drawn and the title is correct for large input ranges.
test_function_with_spaces: Asserts that spaces in the function input are handled correctly.
test_function_with_high_degree_polynomial: Asserts that a high-degree polynomial function is plotted correctly.
test_function_plot_title: Asserts that the plot title is correctly set for a valid function.
test_invalid_function_format: Asserts that the application handles invalid function formats and hides appropriately.
test_invalid_characters_in_function: Asserts that invalid characters in the function input are handled properly.
test_empty_function_input: Asserts that the plot is hidden for empty function input.
test_empty_min_max_input: Asserts that the plot is hidden for empty min and max inputs.
test_invalid_min_max_input: Asserts that the plot is hidden for non-numeric min and max values.
test_large_input_values: Asserts that the application can handle large input values and plots correctly.
test_function_with_missing_parentheses: Asserts that the plot is hidden when parentheses are missing in the function.
test_function_with_unrecognized_functions: Asserts that unrecognized functions are handled correctly and the plot is hidden.


3)Runtime Errors
These errors occur during the execution of the program, usually due to invalid operations or unexpected situations.

test_plot_invalid_function: May encounter runtime errors if the function format is incorrect and results in plotting errors.
test_min_greater_than_max: May encounter runtime errors related to plotting or error messages if min and max values are incorrect.
test_min_equal_max: May involve runtime errors if the application fails to handle equal min and max values properly.
test_empty_function: Could involve runtime errors related to plotting when the function input is empty.
test_exponential_function: May encounter runtime errors if the function format for exponentiation is not handled correctly.
test_large_range: Could involve runtime errors if large input values cause issues in plotting or calculations.
test_function_with_spaces: May involve runtime errors if extra spaces affect function evaluation.
test_function_with_high_degree_polynomial: Could involve runtime errors with high-degree polynomials if not handled properly.
test_function_plot_title: May involve runtime errors if the title setting fails under normal conditions.
test_invalid_function_format: May encounter runtime errors if the function format leads to unexpected results.
test_invalid_characters_in_function: Could involve runtime errors if the function contains characters that are not processed correctly.
test_empty_function_input: May involve runtime errors if the function input is empty but the application still tries to plot.
test_empty_min_max_input: May involve runtime errors if the min and max inputs are empty and affect plotting.
test_invalid_min_max_input: Could involve runtime errors if non-numeric values cause issues in calculations.
test_large_input_values: May involve runtime errors with very large input values affecting plotting or calculations.
test_function_with_missing_parentheses: May involve runtime errors if missing parentheses cause function evaluation issues.
test_function_with_unrecognized_functions: Could involve runtime errors if unrecognized functions are processed incorrectly.


Logic Errors
These errors occur when the code logic does not produce the correct result.

test_initial_state: Ensures that initial values and settings are correctly applied.
test_plot_invalid_function: Ensures the application handles invalid functions by remaining visible, which might indicate logical handling.
test_min_greater_than_max: Checks the logical handling of error conditions where min is greater than max.
test_min_equal_max: Validates the logical handling of equal min and max values.
test_empty_function: Checks the logical handling when the function input is empty.
test_exponential_function: Ensures that the exponential function is plotted logically and correctly.
test_large_range: Validates that large input ranges are logically handled.
test_function_with_spaces: Ensures that spaces in the function input are logically managed.
test_function_with_high_degree_polynomial: Checks the logical handling of high-degree polynomial functions.
test_function_plot_title: Ensures the title is set correctly based on the function input.
test_invalid_function_format: Validates that invalid function formats are handled logically.
test_invalid_characters_in_function: Checks logical handling of invalid characters in function input.
test_empty_function_input: Ensures that an empty function input is logically managed.
test_empty_min_max_input: Checks the logical handling of empty min and max inputs.
test_invalid_min_max_input: Validates logical handling of non-numeric min and max inputs.
test_large_input_values: Ensures that large input values are logically handled.
test_function_with_missing_parentheses: Validates logical handling of missing parentheses in the function.
test_function_with_unrecognized_functions: Ensures that unrecognized functions are logically handled.


*******THATS IT!*******
