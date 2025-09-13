import tkinter as tk
import platform

if platform.system() == "Windows":
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
elif platform.system() in ["Darwin", "Linux"]:
    try:
        tk.Tk().call('tk', 'scaling', 2.0)
    except:
        pass

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

def translate_to_braille_board(text, max_chars=12):
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

bg_color = "#3c739f"

window = tk.Tk()
window.title("Braille Translator")
window.geometry("600x500")
window.minsize(400, 250)
window.configure(bg=bg_color)

canvas = tk.Canvas(window, bg=bg_color, highlightthickness=0)
scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=bg_color)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

label = tk.Label(scrollable_frame, text="Enter text (a-z, ñ, spaces):", font=("Arial", 16), bg=bg_color, fg="white")
label.pack(pady="10 0", fill="both")

input_text = tk.Entry(scrollable_frame, width=40, font=("Arial", 14), background="white", fg="black", borderwidth=3, relief="solid", cursor="xterm")
input_text.pack(pady=10, padx=20, fill="both")

translate_button = tk.Button(scrollable_frame, text="Translate", command=translate_text, font=("Arial", 14), bg="#409243", fg="white", borderwidth=3, relief="raised", cursor="hand2", activebackground="#6AB76D")
translate_button.pack()

output_label = tk.Label(scrollable_frame, text="", font=("Courier", 12), bg="white", anchor="nw", justify="left", borderwidth=3, relief="solid")
output_label.pack(padx=10, pady=10, fill="both", expand=True)

canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
scrollbar.pack(side="right", fill="y")

window.bind("<Configure>", update_board)

def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

window.bind_all("<MouseWheel>", on_mouse_wheel)

window.mainloop()