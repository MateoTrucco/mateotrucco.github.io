import tkinter as tk
from tkinter import messagebox
import platform
import time

def sleep(seconds):
    """
    Pauses execution for the specified number of seconds.

    Args:
        seconds (float): Number of seconds to pause.
    """
    time.sleep(seconds)

def decimal_to_binary(n):
    """
    Converts a decimal number to its binary representation.

    Args:
        n (int): Decimal number to convert.

    Returns:
        str: Binary representation of the number, or '0' if input is 0.
    """
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2
    return binary

def animate_loading_bar(label, callback, step=0, duration=2000):
    """
    Animates a loading bar in the GUI with color changes based on percentage.

    Args:
        label (tk.Label): Label to display the loading bar.
        callback (function): Function to call after animation completes.
        step (int): Current step in the animation.
        duration (int): Total duration of the animation in milliseconds.
    """
    total_steps = 40
    interval = duration // total_steps
    percentage = (step / total_steps) * 100

    if percentage <= 30:
        color = "#FF0000"
    elif percentage <= 60:
        color = "#FFFF00"
    elif percentage <= 90:
        color = "#00FF00"
    else:
        color = "#FF00FF"

    if step < total_steps:
        label.config(text=label.cget("text") + "█", fg=color)
        label.after(interval, animate_loading_bar, label, callback, step + 1, duration)
    else:
        label.config(text="", fg="white")
        callback()

def convert_to_binary():
    """
    Converts the input decimal number to binary and updates the GUI.

    Retrieves the input, validates it, shows a loading animation, and displays the result.
    """
    text = input_entry.get().strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter a number.")
        return
    if text.lower() == "salir":
        window.destroy()
        return

    try:
        num = int(text)
        if num < 0:
            raise ValueError
        input_entry.config(state="disabled")
        translate_button.config(state="disabled")
        output_label.config(text="")
        animate_loading_bar(loading_label, lambda: show_result(num))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid non-negative integer.")
        input_entry.config(state="normal")
        translate_button.config(state="normal")

def show_result(num):
    """
    Displays the binary conversion result.

    Args:
        num (int): Decimal number to convert.
    """
    binary = decimal_to_binary(num)
    output_label.config(text=binary)
    loading_label.config(text="")
    input_entry.config(state="normal")
    translate_button.config(state="normal")

bg_color = "#3c739f"

window = tk.Tk()
window.title("Decimal to Binary Converter")
window.geometry("600x500")
window.minsize(400, 250)
window.configure(bg=bg_color)

label = tk.Label(window, text="Decimal to Binary converter", font=("Arial", 16), bg=bg_color, fg="white")
label.pack(pady="10 0", fill="both")

input_entry = tk.Entry(window, width=40, font=("Arial", 14), background="white", fg="black", borderwidth=3, relief="solid", cursor="xterm")
input_entry.pack(pady=10, padx=20, fill="both")

translate_button = tk.Button(window, text="CONVERT", command=convert_to_binary, font=("Arial", 14), bg="#409243", fg="white", borderwidth=3, relief="raised", cursor="hand2", activebackground="#6AB76D")
translate_button.pack()

loading_label = tk.Label(window, text="", font=("Arial", 12), bg=bg_color, fg="white", anchor="center", justify="center")
loading_label.pack(pady=5)

output_label = tk.Label(window, text="", font=("Arial", 20), bg="white", fg="black", anchor="center", justify="center", borderwidth=3, relief="solid", wraplength=560)
output_label.pack(padx=10, pady=10, fill="both", expand=True)

window.mainloop()