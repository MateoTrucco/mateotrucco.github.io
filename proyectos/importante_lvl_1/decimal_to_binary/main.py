import tkinter as tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from base_functions import enable_high_dpi, colors

enable_high_dpi()

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
        label.config(text="", fg=fg_int)
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

bg_body = colors["++"]
bg_int = colors["-"]
fg_int = colors["b"]
bg_button = colors["+"]
fg_button = colors["b"]

window = tk.Tk()
window.title("Decimal to Binary Converter")
window.geometry("600x500")
window.minsize(400, 250)
window.configure(bg=bg_body)

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=0)
window.rowconfigure(1, weight=0)
window.rowconfigure(2, weight=0)
window.rowconfigure(3, weight=0)
window.rowconfigure(4, weight=1)

label = tk.Label(window, text="Decimal to Binary", font=("Arial", 16, "bold"), bg=bg_int, fg=fg_int, borderwidth=3, relief="solid", anchor="center", justify="center")
label.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="ew")

input_entry = tk.Entry(window, width=40, font=("Arial", 14), bg=bg_int, fg=fg_int, borderwidth=3, relief="solid", cursor="xterm")
input_entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

translate_button = tk.Button(window, text="CONVERT", command=convert_to_binary, font=("Arial", 14), bg=bg_button, fg=fg_button, borderwidth=3, relief="raised", cursor="hand2", activebackground=bg_int, activeforeground=fg_int)
translate_button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

loading_label = tk.Label(window, text="", font=("Arial", 12), bg=bg_body, fg=fg_int, anchor="center", justify="center")
loading_label.grid(row=3, column=0, padx=20, pady=5, sticky="ew")

output_frame = tk.Frame(window, bg=bg_int, borderwidth=3, relief="solid")
output_frame.grid(row=4, column=0, padx="10 0", pady=10, sticky="nsew")
output_frame.rowconfigure(0, weight=1)
output_frame.columnconfigure(0, weight=1)

output_canvas = tk.Canvas(output_frame, bg=bg_int, highlightthickness=0)
output_canvas.grid(row=0, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(output_frame, orient="vertical", command=output_canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

output_canvas.configure(yscrollcommand=scrollbar.set)

output_label = tk.Label(output_canvas, text="", font=("Arial", 20, "bold"), bg=bg_int, fg=fg_int, anchor="center", justify="center", wraplength=560)
output_canvas.create_window((0, 0), window=output_label, anchor="nw")

def configure_scroll_region(event):
    output_canvas.configure(scrollregion=output_canvas.bbox("all"))

output_label.bind("<Configure>", configure_scroll_region)

window.mainloop()