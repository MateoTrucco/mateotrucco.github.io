import re
import json
import textwrap
import tkinter as tk
import sys, os, time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from base_functions import enable_high_dpi, colors

enable_high_dpi()

bg_body = colors["++"]
bg_int = colors["-"]
fg_int = colors["b"]
bg_button = colors["+"]
fg_button = colors["b"]

def load_idioms(archivo=None):
    if archivo is None:
        archivo = os.path.join(os.path.dirname(__file__), "json", "idioms.json")
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def animate_loading_bar(label, callback, step=0, duration=2000):
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

def basic_text_correction(text):
    text = text.lower()
    text = re.sub(r'\s+([.,!?])', r'\1', text)
    text = re.sub(r'([.!?])([^\s])', r'\1 \2', text)
    text = re.sub(r'\s+', ' ', text).strip()

    text = re.sub(r'(^|[.!?]\s+)(\w)', lambda m: m.group(1) + m.group(2).upper(), text)

    idioms = load_idioms()
    for word, fix in idioms.items():
        text = re.sub(rf'\b{re.escape(word)}\b', fix, text, flags=re.IGNORECASE)

    text = re.sub(r'\b(y|pero|aunque|sino)\b', r'\1,', text)

    return textwrap.fill(text, width=80)

def correct_and_display_text():
    raw_text = input_entry.get().strip()
    if not raw_text:
        output_label.config(text="Por favor ingresa un texto para corregir.")
        return

    input_entry.config(state="disabled")
    action_button.config(state="disabled")
    output_label.config(text="")
    
    animate_loading_bar(loading_label, lambda: show_result(raw_text))

def show_result(text):
    corrected = basic_text_correction(text)
    output_label.config(text=corrected)
    input_entry.config(state="normal")
    action_button.config(state="normal")
    loading_label.config(text="")

window = tk.Tk()
window.title("Spanish Spell Checker")
window.geometry("600x500")
window.minsize(400, 250)
window.configure(bg=bg_body)

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=0)
window.rowconfigure(1, weight=0)
window.rowconfigure(2, weight=0)
window.rowconfigure(3, weight=0)
window.rowconfigure(4, weight=1)

label = tk.Label(window, text="Spanish Spell Checker", font=("Arial", 16, "bold"), bg=bg_int, fg=fg_int, borderwidth=3, relief="solid", anchor="center", justify="center")
label.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="ew")

input_entry = tk.Entry(window, width=40, font=("Arial", 14), bg=bg_int, fg=fg_int, borderwidth=3, relief="solid", cursor="xterm")
input_entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

action_button = tk.Button(window, text="CHECK", command=correct_and_display_text, font=("Arial", 14), bg=bg_button, fg=fg_button, borderwidth=3, relief="raised", cursor="hand2", activebackground=bg_int, activeforeground=fg_int)
action_button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

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

output_label = tk.Label(output_canvas, text="", font=("Arial", 14),
                        bg=bg_int, fg=fg_int, anchor="center", justify="center", wraplength=560)
output_canvas.create_window((0, 0), window=output_label, anchor="nw")

def configure_scroll_region(event):
    output_canvas.configure(scrollregion=output_canvas.bbox("all"))

output_label.bind("<Configure>", configure_scroll_region)

window.mainloop()

