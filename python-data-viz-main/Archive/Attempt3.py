import tkinter as tk
from tkinter import messagebox
import csv
import os

def get_total_infections():
    # Use a relative path to point to the CSV file within your application's directory
    file_path = os.path.join(os.path.dirname(__file__), 'commercial-backyard-flocks.csv')

    total_infections = 0
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                try:
                    total_infections += int(row[-1])
                except ValueError:
                    continue

        messagebox.showinfo("Total Infections", f"Total bird flu infections: {total_infections}")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found. Please ensure the file exists in the application's directory.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("Bird Flu Infections Calculator")

calculate_button = tk.Button(root, text="Calculate Total Infections", command=get_total_infections)
calculate_button.pack(pady=20)

root.mainloop()