import tkinter as tk
from tkinter import messagebox

# Event listeners (handlers) for button clicks
def on_button1_click():
    messagebox.showinfo("Button 1", "You clicked Button 1!")

def on_button2_click():
    messagebox.showinfo("Button 2", "You clicked Button 2!")

def on_button3_click():
    messagebox.showinfo("Button 3", "You clicked Button 3!")

def on_button4_click():
    messagebox.showinfo("Button 4", "You clicked Button 4!")

# Create the main window
def create_gui():
    # Initialize the root window (main window)
    root = tk.Tk()
    root.title("Python GUI with Event Listeners")

    # Set window size
    root.geometry("300x300")

    # Create buttons and attach event listeners
    button1 = tk.Button(root, text="Button 1", command=on_button1_click)
    button1.pack(pady=10)

    button2 = tk.Button(root, text="Button 2", command=on_button2_click)
    button2.pack(pady=10)

    button3 = tk.Button(root, text="Button 3", command=on_button3_click)
    button3.pack(pady=10)

    button4 = tk.Button(root, text="Button 4", command=on_button4_click)
    button4.pack(pady=10)

    # Run the main event loop to display the window
    root.mainloop()

# Run the GUI application
if __name__ == "__main__":
    create_gui()




