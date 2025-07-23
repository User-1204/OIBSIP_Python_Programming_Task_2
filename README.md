# BMI Calculator

## Overview

This project is a modular, GUI-based BMI (Body Mass Index) calculator built in Python. It allows users to enter their weight and height, calculates BMI, classifies it into health categories, and saves historical data to visualize trends over time. It demonstrates how to combine core programming logic, data storage, and graphical interface design.


## Features

* Calculates BMI from weight and height.
* Categorizes BMI as Underweight, Normal weight, Overweight, or Obese.
* User-friendly graphical interface using Tkinter.
* Stores BMI history per user in a JSON file.
* Displays the last few BMI entries.
* Plots BMI trends over time using Matplotlib.
* Exports BMI history to CSV.
* Input validation and user-friendly error handling.


## Theory and Concepts

### BMI Calculation

BMI is calculated with the formula:

```
BMI = weight (kg) / (height (m))^2
```


### Categorization

Based on BMI value:

* Underweight: BMI < 18.5
* Normal weight: 18.5 ≤ BMI < 24.9
* Overweight: 24.9 ≤ BMI < 29.9
* Obese: BMI ≥ 30


### GUI Design

Built using Tkinter, the app has:

* Input fields for name, weight, and height.
* Buttons for Calculate BMI, Export to CSV, and Reset.
* Areas to display results, recent history, and a BMI trend graph.


### Data Storage

Uses a local JSON file (`bmi_data.json`) to save historical BMI entries per user.
Data can also be exported to CSV format.


### Data Visualization

Uses Matplotlib to plot BMI trends, helping users see changes over time.


### Input Validation

* Weight: 10–300 kg
* Height: 0.5–2.5 m
* Name must not be empty
  Invalid inputs show clear error messages.


## How It Works

1. Users enter name, weight, and height.
2. Click “Calculate BMI”:

   * BMI is computed and categorized.
   * Entry is saved to JSON file.
   * Recent history and trend graph update.
3. Optionally export data to CSV.
4. “Reset” clears the form and results.


## Project Structure

```
bmi_calculator/
├── main.py              # Entry point
├── gui.py               # GUI layout and widgets
├── controller.py        # Connects logic and GUI, handles actions
├── logic.py             # BMI calculation and categorization
├── data_manager.py      # Data loading, saving, exporting
├── plotter.py           # Plots BMI trends
├── constants.py         # UI styling and config
└── bmi_data.json        # Auto-generated storage file
```


## Technologies Used

* Python 3.x
* Tkinter
* Matplotlib
* JSON and CSV (built-in modules)


## Running the Application

From the project directory, run:

```
python main.py
```

The GUI will open where you can enter your data and view results.


## Possible Enhancements

* Imperial units support.
* Dark mode or theme customization.
* More detailed health recommendations.
* User authentication.
* Desktop notifications.


## Demo Video




## Output Image

<img width="630" height="985" alt="Image" src="https://github.com/user-attachments/assets/80f0ccfd-1ad7-4151-8a15-db1d3f4b0ddf" />
