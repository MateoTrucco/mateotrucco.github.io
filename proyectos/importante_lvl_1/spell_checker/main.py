# -------------------- IMPORTS --------------------
try:
    import sys, os, json, textwrap, re
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
    from base_functions import enable_high_dpi, make_screen, c

    enable_high_dpi()
except ImportError:
    print("Error: base_functions module not found. Please ensure it is in the correct directory.")
    sys.exit(1)

def load_idioms(archivo=None):
    if archivo is None:
        archivo = os.path.join(os.path.dirname(__file__), "json", "idioms.json")
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

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
    raw_text = input_text.get().strip()
    if not raw_text:
        output_label.config(text="Por favor ingresa un texto para corregir.")
        return

    input_text.config(state="disabled")
    action_button.config(state="disabled")
    output_label.config(text="")
    
    show_result(raw_text)

def show_result(text):
    corrected = basic_text_correction(text)
    output_label.config(text=corrected)
    input_text.config(state="normal")
    action_button.config(state="normal")

# -------------------- GUI SETUP --------------------
ui = make_screen(
    title="Argentinian to Spanish",
    button_command=correct_and_display_text,
    button_text="TRANSLATE",
    loading_steps=30
)

window = ui["window"]
input_text = ui["input_text"]
output_label = ui["output_label"]
action_button = ui["action_button"]

output_label.config(font=("Arial", 14))

# -------------------- MAIN LOOP --------------------
window.mainloop()