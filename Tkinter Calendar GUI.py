import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

# Function to update calendar display
def show_calendar(year, month):
    cal_content = calendar.month(year, month)
    cal_label.config(text=cal_content)

# Callback function to handle month/year changes
def update_calendar(*args):
    try:
        selected_year = int(year_var.get())
        selected_month = months.index(month_var.get()) + 1
        show_calendar(selected_year, selected_month)
    except:
        pass

# Set up the main window
root = tk.Tk()
root.title("YouTube Style Calendar")

# Initialize current month and year
current_year = datetime.now().year
current_month = datetime.now().month

# Set up Year and Month drop-downs
year_var = tk.StringVar(value=current_year)
month_var = tk.StringVar(value=calendar.month_name[current_month])

year_label = tk.Label(root, text="Year:")
year_label.pack(padx=10, pady=5)

year_entry = tk.Entry(root, textvariable=year_var)
year_entry.pack(padx=10, pady=5)

month_label = tk.Label(root, text="Month:")
month_label.pack(padx=10, pady=5)

months = list(calendar.month_name)[1:]  # Get month names (Jan-Dec)
month_menu = ttk.Combobox(root, textvariable=month_var, values=months, state="readonly")
month_menu.pack(padx=10, pady=5)

# Set up the calendar display area
cal_label = tk.Label(root, text="", font=("Consolas", 10), justify=tk.LEFT)
cal_label.pack(padx=10, pady=10)

# Set up event listeners
year_var.trace("w", update_calendar)
month_var.trace("w", update_calendar)

# Initialize calendar display
show_calendar(current_year, current_month)

# Run the application
root.mainloop()
