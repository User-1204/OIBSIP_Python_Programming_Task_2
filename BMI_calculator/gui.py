# gui.py
# Builds the GUI layout & widgets only

import tkinter as tk
from constants import *

class BMICalculatorApp:
    def __init__(self, root, controller=None):
        self.root = root
        self.controller = controller
        self.root.title("BMI Calculator")
        self.root.configure(bg=BACKGROUND_COLOR)

        # Set window size and disable resizing
        self.root.geometry("500x750")
        self.root.resizable(False, False)

        self.build_ui()

    def build_ui(self):
        # Title
        tk.Label(self.root, text="BMI Calculator", font=TITLE_FONT,
                 bg=BACKGROUND_COLOR, fg=TEXT_DARK).pack(pady=(20, 10))

        # Input fields frame
        input_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        input_frame.pack(pady=10)

        # Name
        tk.Label(input_frame, text="Name:", font=LABEL_FONT,
                 bg=BACKGROUND_COLOR, fg=TEXT_DARK).grid(row=0, column=0, sticky="e", padx=12, pady=8)
        self.name_entry = tk.Entry(input_frame, font=ENTRY_FONT, bg=FIELD_BG)
        self.name_entry.grid(row=0, column=1, padx=12)

        # Weight
        tk.Label(input_frame, text="Weight (kg):", font=LABEL_FONT,
                 bg=BACKGROUND_COLOR, fg=TEXT_DARK).grid(row=1, column=0, sticky="e", padx=12, pady=8)
        self.weight_entry = tk.Entry(input_frame, font=ENTRY_FONT, bg=FIELD_BG)
        self.weight_entry.grid(row=1, column=1, padx=12)

        # Height
        tk.Label(input_frame, text="Height (m):", font=LABEL_FONT,
                 bg=BACKGROUND_COLOR, fg=TEXT_DARK).grid(row=2, column=0, sticky="e", padx=12, pady=8)
        self.height_entry = tk.Entry(input_frame, font=ENTRY_FONT, bg=FIELD_BG)
        self.height_entry.grid(row=2, column=1, padx=12)

        # Buttons frame
        button_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        button_frame.pack(pady=20)

        # Create buttons without commands first
        self.calc_button = tk.Button(button_frame, text="Calculate BMI", font=BUTTON_FONT, bg="#AED9C8", width=14)
        self.calc_button.pack(side="left", padx=8)

        self.export_button = tk.Button(button_frame, text="Export to CSV", font=BUTTON_FONT, bg="#AED9C8", width=14)
        self.export_button.pack(side="left", padx=8)

        self.reset_button = tk.Button(button_frame, text="Reset", font=BUTTON_FONT, bg="#AED9C8", width=10)
        self.reset_button.pack(side="left", padx=8)

        # Result label
        self.result_label = tk.Label(self.root, text="", font=RESULT_FONT,
                                     bg=BACKGROUND_COLOR, fg=RESULT_COLOR, justify="left", wraplength=440)
        self.result_label.pack(pady=(10, 5))

        # History label
        self.history_label = tk.Label(self.root, text="", font=FOOTER_FONT,
                                      bg=BACKGROUND_COLOR, fg="#7D8884", justify="left", wraplength=440)
        self.history_label.pack(pady=(5, 10))

        # Graph area frame
        self.graph_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        self.graph_frame.pack(pady=10)

        # Footer
        tk.Label(self.root, text="Made by Sakshi | 2025", font=FOOTER_FONT,
                 fg="#999999", bg=BACKGROUND_COLOR).pack(side="bottom", pady=10)

        # Add Enter key bindings:
        # name → Enter → weight, weight → Enter → height, height → Enter → calculate
        self.name_entry.bind("<Return>", lambda e: self.weight_entry.focus())
        self.weight_entry.bind("<Return>", lambda e: self.height_entry.focus())
        self.height_entry.bind("<Return>", lambda e: self.controller.calculate())

        # Start focus at name entry
        self.name_entry.focus()

    def set_controller(self, controller):
        #Attach controller methods to buttons
        self.controller = controller
        self.calc_button.config(command=self.controller.calculate)
        self.export_button.config(command=self.controller.export)
        self.reset_button.config(command=self.controller.reset)
