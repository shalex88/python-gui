#!/usr/bin/env python3

import tkinter as tk
import customtkinter as ctk

def main():
    # Initialize the main window
    root = ctk.CTk()
    root.title("CustomTkinter GUI Application")
    root.geometry("400x300")

    # Create a label
    label = ctk.CTkLabel(root, text="Hello, CustomTkinter!")
    label.pack(pady=20)

    # Create a button
    button = ctk.CTkButton(root, text="Click Me", command=lambda: label.configure(text="Button Clicked!"))
    button.pack(pady=10)

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    print("Starting GUI application...")
    main()