# -------------------- IMPORTS --------------------
try:
    import sys, os, math
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
    from base_functions import enable_high_dpi, make_screen, c

    enable_high_dpi()
except ImportError:
    print("Error: base_functions module not found. Please ensure it is in the correct directory.")
    sys.exit(1)

# -------------------- FUNCTIONS --------------------
def es_cuadrado_perfecto(n):
    """
    Check if a number is a perfect square.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if the number is a perfect square, False otherwise.
    """
    raiz = int(math.sqrt(n))
    return raiz * raiz == n

# --------------------------------------------------
def factorizar_raiz(n):
    """
    Simplify the square root of a number.
    
    Args:
        n (int): The number to simplify.
    
    Returns:
        str: The simplified square root or a message if it cannot be simplified.
    """
    if es_cuadrado_perfecto(n):
        return f"√{n} = {int(math.sqrt(n))}"
    
    factor = 1
    b = n
    for i in range(2, int(math.sqrt(n)) + 1):
        while b % (i * i) == 0:
            factor *= i
            b //= i * i
    
    if factor == 1:
        return f"√{n} it cannot be simplified"
    return f"{factor}√{b}"

# --------------------------------------------------
def calcular():
    """
    Calculate the simplified square root based on user input and update the GUI.
    """
    try:
        num = int(input_text.get())
        resultado = factorizar_raiz(num)
        output_label.config(text=resultado)
    except ValueError:
        output_label.config(text="Error: Enter a valid number.")
        window.after(3000, lambda: output_label.config(text=""))

# -------------------- GUI --------------------
ui = make_screen(
    title="Root and Factorization",
    button_text="CALCULATE",
    button_command=calcular,
    loading_steps=30,
)

window = ui["window"]
title_label = ui["title_label"]
input_text = ui["input_text"]
output_label = ui["output_label"]

# -------------------- MAIN LOOP --------------------
window.mainloop()