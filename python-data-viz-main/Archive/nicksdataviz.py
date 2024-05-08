import tkinter as tk
from tkinter import messagebox
import csv
import os

def get_total_infections():
    # Construct the path to your csv file, modify this path according to your actual path
    file_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'commercial-backyard-flocks.csv')
    
    # Initialize total_infections
    total_infections = 0
    
    try:
        # Open the csv file and calculate the total infections
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                try:
                    total_infections += int(row[-1])  # Assuming the flock size is the last column
                except ValueError:
                    continue  # Skips rows where conversion to int fails (e.g., missing or invalid data)
        
        # Display the result
        messagebox.showinfo("Total Infections", f"Total bird flu infections: {total_infections}")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found. Please ensure the file exists in the specified path.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Setting up the GUI
root = tk.Tk()
root.title("Bird Flu Infections Calculator")

# Button to calculate total infections
calculate_button = tk.Button(root, text="Calculate Total Infections", command=get_total_infections)
calculate_button.pack(pady=20)

root.mainloop()