#!/usr/bin/env python3

import tkinter as tk
import customtkinter as ctk
import time

class StreamRecorderApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Stream recorder")
        self.root.geometry("300x200")

        self.camera_connected = False
        self.timer_running = False
        self.start_time = 0

        self.create_widgets()

    def create_widgets(self):
        # Camera button
        self.camera_button = ctk.CTkButton(self.root, text="Connect", command=self.toggle_camera)
        self.camera_button.pack(pady=10)

        # Timer label
        self.timer_label = ctk.CTkLabel(self.root, text="Timer: 00h 00m 00s")
        self.timer_label.pack(pady=10)

        # Record button
        self.record_button = ctk.CTkButton(self.root, text="Start", command=self.toggle_record, state="disabled")
        self.record_button.pack(pady=10)

    def toggle_camera(self):
        if self.camera_button.cget("text") == "Connect":
            self.camera_button.configure(text="Disconnect")
            self.camera_connect()
            self.camera_connected = True
            self.record_button.configure(state="normal")  # Enable the Start button
        else:
            self.camera_button.configure(text="Connect")
            self.camera_disconnect()
            self.camera_connected = False
            self.record_button.configure(state="disabled")  # Disable the Start button

    def toggle_record(self):
        if self.record_button.cget("text") == "Start":
            self.record_button.configure(text="Stop")
            self.start_function()
            self.timer_running = True
            self.start_time = time.time()
            self.update_timer()
        else:
            self.record_button.configure(text="Start")
            self.stop_function()
            self.timer_running = False
            self.timer_label.configure(text="Timer: 00h 00m 00s")

    def update_timer(self):
        if self.timer_running:
            elapsed_time = int(time.time() - self.start_time)
            hours, remainder = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.timer_label.configure(text=f"Timer: {hours:02d}h {minutes:02d}m {seconds:02d}s")
            self.root.after(1000, self.update_timer)

    @staticmethod
    def camera_connect():
        print("Camera connected")

    @staticmethod
    def camera_disconnect():
        print("Camera disconnected")

    @staticmethod
    def start_function():
        print("Start function triggered")

    @staticmethod
    def stop_function():
        print("Stop function triggered")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    print("Starting GUI application...")
    app = StreamRecorderApp()
    app.run()