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

# -------------------- FUNCTIONS --------------------
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

# --------------------------------------------------
def convert_to_binary():
    """Converts the input decimal number to binary and updates the GUI."""
    text = input_entry.get().strip()
    if not text:
        output_label.config(text="Please enter a number.")
        output_label.after(3000, lambda: output_label.config(text=""))
        return
    if text.lower() == "salir":
        window.destroy()
        return

    try:
        num = int(text)
        if num < 0:
            raise ValueError
        output_label.config(text="")
        show_result(num)
    except ValueError:
        output_label.config(text="Please enter a valid non-negative integer.")
        output_label.after(3000, lambda: output_label.config(text=""))

# --------------------------------------------------
def show_result(num):
    """
    Displays the binary conversion result.

    Args:
        num (int): Decimal number to convert.
    """
    binary = decimal_to_binary(num)
    output_label.config(text=binary)

# -------------------- GUI SETUP --------------------
ui = make_screen(
    title="Decimal to Binary Converter",
    button_command=convert_to_binary,
    button_text="CONVERT",
    output_font=("Arial", 16, "bold"),
)

window = ui["window"]
input_entry = ui["input_text"]
output_label = ui["output_label"]

# -------------------- MAIN LOOP --------------------
window.mainloop()
