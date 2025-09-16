# -------------------- IMPORTS --------------------
try:
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
    from base_functions import enable_high_dpi, make_screen

    enable_high_dpi()
except ImportError:
    print("Error: base_functions module not found. Please ensure it is in the correct directory.")
    sys.exit(1)

# -------------------- VARIABLES --------------------
BRAILLE_ALPHABET = {
    ' ': (0,0,0,0,0,0),
    'a': (1,0,0,0,0,0),
    'b': (1,1,0,0,0,0),
    'c': (1,0,0,1,0,0),
    'd': (1,0,0,1,1,0),
    'e': (1,0,0,0,1,0),
    'f': (1,1,0,1,0,0),
    'g': (1,1,0,1,1,0),
    'h': (1,1,0,0,1,0),
    'i': (0,1,0,1,0,0),
    'j': (0,1,0,1,1,0),
    'k': (1,0,1,0,0,0),
    'l': (1,1,1,0,0,0),
    'm': (1,0,1,1,0,0),
    'n': (1,0,1,1,1,0),
    'ñ': (1,1,0,1,1,1),
    'o': (1,0,1,0,1,0),
    'p': (1,1,1,1,0,0),
    'q': (1,1,1,1,1,0),
    'r': (1,1,1,0,1,0),
    's': (0,1,1,1,0,0),
    't': (0,1,1,1,1,0),
    'u': (1,0,1,0,0,1),
    'v': (1,1,1,0,0,1),
    'w': (0,1,0,1,1,1),
    'x': (1,0,1,1,0,1),
    'y': (1,0,1,1,1,1),
    'z': (1,0,1,0,1,1),
    '1': (1,0,0,0,0,0),
    '2': (1,1,0,0,0,0),
    '3': (1,0,0,1,0,0),
    '4': (1,0,0,1,1,0),
    '5': (1,0,0,0,1,0),
    '6': (1,1,0,1,0,0),
    '7': (1,1,0,1,1,0),
    '8': (1,1,0,0,1,0),
    '9': (0,1,0,1,0,0),
    '0': (0,1,0,1,1,0),
    'á': (1,1,1,0,1,1),
    'é': (0,1,1,1,0,1),
    'í': (0,0,1,1,0,0),
    'ó': (0,0,1,1,0,1),
    'ú': (0,1,1,1,1,1),
    'ü': (1,1,0,0,1,1),
    ',': (0,1,0,0,0,0),
    ';': (0,1,1,0,0,0),
    ':': (0,1,0,0,1,0),
    '.': (0,1,0,0,1,1),
    '¡': (0,1,1,0,1,0),
    '!': (0,1,1,0,1,0),
    '(': (0,1,1,0,1,1),
    ')': (0,1,1,0,1,1),
    '¿': (0,0,1,0,1,1),
    '?': (0,1,1,0,0,1),
    '"': (0,1,1,0,0,1),
    '*': (0,0,1,0,1,0),
}

# -------------------- FUNCTIONS --------------------
def create_braille_pattern(p1, p2, p3, p4, p5, p6):
    """
    Creates a braille pattern from six dot positions.

    Args:
        p1, p2, p3, p4, p5, p6 (int): Binary values (0 or 1) for each dot in a braille cell.

    Returns:
        list: List of six binary values representing the braille pattern.
    """
    return (p1, p4, p2, p5, p3, p6)

# --------------------------------------------------
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

# --------------------------------------------------
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

# --------------------------------------------------
def translate_text():
    """Translates input text to braille and displays it in the GUI."""
    text = input_text.get().strip()
    result = translate_to_braille_board(text)
    output_label.config(text=result, wraplength=window.winfo_width() - 10)

# --------------------------------------------------
def update_board(event=None):
    """
    Updates the braille board when the window is resized.

    Args:
        event: Tkinter event object (optional).
    """
    text = input_text.get().strip()
    if text:
        result = translate_to_braille_board(text)
        output_label.config(text=result, wraplength=window.winfo_width() - 10)

# -------------------- GUI SETUP --------------------
ui = make_screen(
    title="Braille Translator",
    button_command=translate_text,
    button_text="TRANSLATE",
    loading_steps=30
)

window = ui["window"]
input_text = ui["input_text"]
output_label = ui["output_label"]

# -------------------- MAIN LOOP --------------------
window.mainloop()