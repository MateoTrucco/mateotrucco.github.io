import tkinter as tk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from base_functions import enable_high_dpi, colors

enable_high_dpi()

BRAILLE_ALPHABET = {
    ' ': [0, 0, 0, 0, 0, 0],
    'a': [1, 0, 0, 0, 0, 0],
    'b': [1, 0, 1, 0, 0, 0],
    'c': [1, 1, 0, 0, 0, 0],
    'd': [1, 1, 0, 1, 0, 0],
    'e': [1, 0, 0, 1, 0, 0],
    'f': [1, 1, 1, 0, 0, 0],
    'g': [1, 1, 1, 1, 0, 0],
    'h': [1, 0, 1, 1, 0, 0],
    'i': [0, 1, 1, 0, 0, 0],
    'j': [0, 1, 1, 1, 0, 0],
    'k': [1, 0, 0, 0, 1, 0],
    'l': [1, 0, 1, 0, 1, 0],
    'm': [1, 1, 0, 0, 1, 0],
    'n': [1, 1, 0, 1, 1, 0],
    'ñ': [1, 1, 1, 1, 0, 1],
    'o': [1, 0, 0, 1, 1, 0],
    'p': [1, 1, 1, 0, 1, 0],
    'q': [1, 1, 1, 1, 1, 0],
    'r': [1, 0, 1, 1, 1, 0],
    's': [0, 1, 1, 0, 1, 0],
    't': [0, 1, 1, 1, 1, 0],
    'u': [1, 0, 0, 0, 1, 1],
    'v': [1, 0, 1, 0, 1, 1],
    'w': [0, 1, 1, 1, 0, 1],
    'x': [1, 1, 0, 0, 1, 1],
    'y': [1, 1, 0, 1, 1, 1],
    'z': [1, 0, 0, 1, 1, 1],
}

def create_braille_pattern(p1, p2, p3, p4, p5, p6):
    """
    Creates a braille pattern from six dot positions.

    Args:
        p1, p2, p3, p4, p5, p6 (int): Binary values (0 or 1) for each dot in a braille cell.

    Returns:
        list: List of six binary values representing the braille pattern.
    """
    return [p1, p4, p2, p5, p3, p6]

def render_braille_char(char):
    """
    Renders a single character as a 3x2 braille cell.

    Args:
        char (str): Single character to convert to braille.

    Returns:
        list: 3x2 matrix representing the braille cell, with '•' for dots and ' ' for empty spaces.
    """
    char = char.lower()
    if char not in BRAILLE_ALPHABET:
        return [[char, char], [char, char], [char, char]]
    dots = BRAILLE_ALPHABET[char]
    return [
        ['•' if dots[0] else ' ', '•' if dots[3] else ' '],
        ['•' if dots[1] else ' ', '•' if dots[4] else ' '],
        ['•' if dots[2] else ' ', '•' if dots[5] else ' ']
    ]

def translate_to_braille_board(text, max_chars=10):
    """
    Translates text to a horizontal braille board with dynamic line breaks.

    Splits text into chunks based on window width or a maximum of 12 characters.

    Args:
        text (str): Text to translate into braille.
        max_chars (int): Maximum characters per board line (default 12).

    Returns:
        str: Formatted string with braille boards, separated by blank lines.
    """
    if not text:
        return ""

    window_width = window.winfo_width()
    char_width = 5
    max_chars = min(max_chars, max(1, (window_width - 10) // (char_width * 15)))

    chunks = [text[i:i + max_chars] for i in range(0, len(text), max_chars)]
    boards = []

    for chunk in chunks:
        chars = [render_braille_char(c) for c in chunk]
        rows = len(chars[0])

        top_border = "┌" + "┬".join(["─────" for _ in chunk]) + "┐"
        bottom_border = "└" + "┴".join(["─────" for _ in chunk]) + "┘"

        board = [top_border]
        for row in range(rows):
            line = "│"
            for char in chars:
                line += f" {char[row][0]} {char[row][1]} │"
            board.append(line)
        board.append(bottom_border)
        boards.append("\n".join(board))

    return "\n\n".join(boards)

def translate_text():
    """Translates input text to braille and displays it in the GUI.

    Retrieves text from the input field, translates it, and updates the output label.
    """
    text = input_text.get().strip()
    result = translate_to_braille_board(text)
    output_label.config(text=result, wraplength=window.winfo_width() - 10)

def update_board(event=None):
    """Updates the braille board when the window is resized.

    Args:
        event: Tkinter event object (optional).
    """
    text = input_text.get().strip()
    if text:
        result = translate_to_braille_board(text)
        output_label.config(text=result, wraplength=window.winfo_width() - 10)

bg_body = colors["++"]
bg_int = colors["-"]
fg_int = colors["b"]
bg_button = colors["+"]
fg_button = colors["b"]

window = tk.Tk()
window.title("Braille Translator")
window.geometry("580x450")
window.minsize(400, 250)
window.configure(bg=bg_body)

window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=0)  
window.rowconfigure(2, weight=0)  
window.rowconfigure(3, weight=1)  

label = tk.Label(
    window, text="Braille Translator", font=("Arial", 16, "bold"), bg=bg_int, fg=fg_int,
    borderwidth=3, relief="solid"
)
label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

input_text = tk.Entry(
    window, font=("Arial", 14), bg=bg_int, fg=fg_int, borderwidth=3, relief="solid", cursor="xterm"
)
input_text.grid(row=1, column=0, padx=20, pady=5, sticky="ew", ipady=5)

translate_button = tk.Button(
    window, text="TRANSLATE", command=translate_text, font=("Arial", 14), bg=bg_button, fg=fg_button,
    borderwidth=3, relief="raised", cursor="hand2", activebackground=bg_int, activeforeground=fg_int
)
translate_button.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

output_frame = tk.Frame(window, bg=bg_body)
output_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
output_frame.columnconfigure(0, weight=1)
output_frame.rowconfigure(0, weight=1)

output_canvas = tk.Canvas(output_frame, bg=bg_int, highlightthickness=0)
output_scrollbar = tk.Scrollbar(output_frame, orient="vertical", command=output_canvas.yview)
output_scrollable_frame = tk.Frame(output_canvas, bg=bg_int)

output_scrollable_frame.bind(
    "<Configure>",
    lambda e: output_canvas.configure(scrollregion=output_canvas.bbox("all"))
)

output_canvas.create_window((0, 0), window=output_scrollable_frame, anchor="n")
output_canvas.configure(yscrollcommand=output_scrollbar.set)

output_canvas.grid(row=0, column=0, sticky="nsew")
output_scrollbar.grid(row=0, column=1, sticky="ns")

output_label = tk.Label(
    output_scrollable_frame, text="", font=("Courier", 12, "bold"), bg=bg_int, fg=fg_int,
    anchor="center", justify="center", wraplength=window.winfo_width() - 20
)
output_label.pack(fill="both", expand=True)

def update_output_wraplength(event=None):
    """Update the wraplength of the output_label dynamically."""
    max_width = 800
    current_width = min(window.winfo_width() - 20, max_width)
    output_label.config(wraplength=current_width)

window.bind("<Configure>", lambda event: (update_board(), update_output_wraplength()))

window.mainloop()
