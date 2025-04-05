#!/usr/bin/env python3

import tkinter as tk
import customtkinter as ctk
import time

def start_function():
    print("Start function triggered")

def stop_function():
    print("Stop function triggered")

def main():
    # Initialize the main window
    root = ctk.CTk()
    root.title("Stream recorder")
    root.geometry("200x200")

    # Create a timer label
    timer_label = ctk.CTkLabel(root, text="Timer: 00h 00m 00s")
    timer_label.pack(pady=10)

    # Timer state
    timer_running = [False]  # Use a mutable object to allow modification in nested function
    start_time = [0]

    # Create a button with toggle functionality
    def toggle_button():
        if button.cget("text") == "Start":
            button.configure(text="Stop")
            start_function()
            timer_running[0] = True
            start_time[0] = time.time()
            update_timer()
        else:
            button.configure(text="Start")
            stop_function()
            timer_running[0] = False
            timer_label.configure(text="Timer: 0")

    # Update the timer
    def update_timer():
        if timer_running[0]:
            elapsed_time = int(time.time() - start_time[0])
            hours, remainder = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            timer_label.configure(text=f"Timer: {hours:02d}h {minutes:02d}m {seconds:02d}s")
            root.after(1000, update_timer)

    button = ctk.CTkButton(root, text="Start", command=toggle_button)
    button.pack(pady=10)

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    print("Starting GUI application...")
    main()