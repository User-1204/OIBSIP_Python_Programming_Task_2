# main.py
# Entry point: builds GUI and connects to controller

import tkinter as tk
from gui import BMICalculatorApp
from controller import BMIController
import os

# Clear console on start
os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    root = tk.Tk()

    # Build GUI first (controller=None for now)
    app = BMICalculatorApp(root, controller=None)

    # Create controller, bind to app, then attach controller back to GUI
    controller = BMIController()
    controller.bind(app)
    app.set_controller(controller)

    root.mainloop()
    os.system('cls' if os.name == 'nt' else 'clear')

