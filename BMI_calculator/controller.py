# controller.py
# Handles calculate, reset, and export actions, and connects GUI to logic and data

from tkinter import messagebox
from logic import calculate_bmi, categorize_bmi
from data_manager import load_data, save_data, export_to_csv
from plotter import plot_trend
from datetime import datetime

class BMIController:
    def __init__(self):
        self.app = None  # GUI reference to set later

    def bind(self, app):
        #Attach GUI instance to controller
        self.app = app

    def calculate(self):
        name = self.app.name_entry.get().strip()
        try:
            weight = float(self.app.weight_entry.get())
            height = float(self.app.height_entry.get())

            if not name:
                messagebox.showwarning("Missing Name", "Please enter your name.")
                return
            if not (10 <= weight <= 300 and 0.5 <= height <= 2.5):
                raise ValueError

            bmi = calculate_bmi(weight, height)
            category, advice = categorize_bmi(bmi)

            # Update result label
            self.app.result_label.config(
                text=f"Name: {name}\nBMI: {bmi:.2f}\nCategory: {category}\n\n{advice}")

            # Save data
            data = load_data()
            timestamp = datetime.now().strftime("%b %d, %I:%M %p")
            entry = {"time": timestamp, "bmi": bmi, "category": category, "weight": weight, "height": height}
            data.setdefault(name, []).append(entry)
            save_data(data)

            # Update history and graph
            self.show_history(data[name])
            plot_trend(self.app.graph_frame, data[name])
            
            # this is for thr pop up message 
            #messagebox.showinfo("BMI Calculated", f"{name}, your BMI is {bmi:.2f} ({category})")

        except ValueError:
            messagebox.showerror("Invalid Input", "Enter valid numbers for weight (10–300) and height (0.5–2.5).")

    def show_history(self, entries):
        #Show last 3 BMI records
        recent = entries[-3:]
        lines = [f"{e['time']}: BMI {e['bmi']} ({e['category']})" for e in recent]
        self.app.history_label.config(text="Recent Entries:\n" + "\n".join(lines))

    def export(self):
        name = self.app.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Missing Name", "Please enter your name.")
            return

        data = load_data()
        if name not in data or not data[name]:
            messagebox.showinfo("No Data", f"No records found for {name}.")
            return

        filename = export_to_csv(name, data[name])
        messagebox.showinfo("Export Complete", f"Exported to {filename}")

    def reset(self):
        #Clear input fields and results
        self.app.name_entry.delete(0, "end")
        self.app.weight_entry.delete(0, "end")
        self.app.height_entry.delete(0, "end")
        self.app.result_label.config(text="")
        self.app.history_label.config(text="")
        for widget in self.app.graph_frame.winfo_children():
            widget.destroy()
        self.app.name_entry.focus()
