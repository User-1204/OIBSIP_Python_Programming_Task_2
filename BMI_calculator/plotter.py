# plotter.py
# Draws BMI graph using matplotlib inside Tkinter frame

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_trend(frame, entries):
    for widget in frame.winfo_children():  # Clear previous plot
        widget.destroy()

    if not entries: return  # Skip if no data

    bmi_values = [e["bmi"] for e in entries]  # Extract BMI values
    timestamps = [e["time"].split(",")[0] for e in entries]  # Extract dates

    fig, ax = plt.subplots(figsize=(4.5, 2.5), dpi=100)  # Create figure
    ax.plot(timestamps, bmi_values, marker='o', color="#3D3C58")  # Plot line
    ax.set_title("BMI Trend", fontsize=10)  # Add title
    ax.set_ylabel("BMI")
    ax.set_xlabel("Date")
    ax.grid(True)
    plt.xticks(rotation=45, ha='right')

    canvas = FigureCanvasTkAgg(fig, master=frame)  # Embed graph
    canvas.draw()
    canvas.get_tk_widget().pack()
