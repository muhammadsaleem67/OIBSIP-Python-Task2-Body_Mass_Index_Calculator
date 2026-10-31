# Command-Line BMI Calculator

A clean, robust **Python command-line application** that calculates a user's Body Mass Index (BMI) and determines their health category based on standard medical ranges. 

This project features robust input validation to handle user errors gracefully (such as negative numbers or non-numeric inputs).

## Features
* **Input Validation:** Prevents crashes by rejecting strings, negative numbers, and zeroes.
* **Standard Medical Categorization:** Sorts results into standard brackets: Underweight, Normal, Overweight, or Obese.
* **Clean Formatting:** Displays the calculated BMI rounded strictly to two decimal places.

## Code Structure
* `get_valid_input(prompt)`: Handles user input loops and catches `ValueError` exceptions.
* `classify_bmi(bmi)`: Processes conditional logic (`if`/`elif`/`else`) to evaluate health categories.
* `main()`: Controls the program execution flow.

## Getting Started

### Prerequisites
* **Python 3.x** installed on your system.

### How to Run
1. Clone this repository or download the source code file.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the following command:

```bash
python bmi_calculator.py
```

## Example Usage
```text
--- Command Line BMI Calculator ---
Enter your weight in kg: seventy
Error: Invalid input. Please enter numeric values only.
Enter your weight in kg: 70
Enter your height in meters (e.g., 1.75): 1.75

Result: Your BMI is 22.86
Health Category: Normal
```
