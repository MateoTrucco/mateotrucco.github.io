# -------------------- IMPORTS --------------------
try:
    import sys, os, subprocess
    import tkinter as tk
    from tkinter import filedialog
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
    from base_functions import enable_high_dpi, make_screen

    enable_high_dpi()
except ImportError:
    print("Error: base_functions module not found. Please ensure it is in the correct directory.")
    sys.exit(1)

# -------------------- FUNCTIONS --------------------
def select_file():
    """Open a file dialog to select a Python file."""
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

# --------------------------------------------------
def select_destination():
    """Open a directory dialog to select a destination folder."""
    folder_path = filedialog.askdirectory()
    if folder_path:
        destination_entry.delete(0, tk.END)
        destination_entry.insert(0, folder_path)

# --------------------------------------------------
def convert_to_exe():
    """Convert the selected Python file to an EXE using PyInstaller."""
    file_path = file_entry.get()
    destination_folder = destination_entry.get()
    if not file_path or not destination_folder:
        return

    file_name = os.path.basename(file_path).replace(".py", "")
    output_folder = os.path.join(destination_folder, file_name)
    os.makedirs(output_folder, exist_ok=True)

    command = f'pyinstaller --onefile --noconsole --distpath "{output_folder}" --workpath "{output_folder}/build" "{file_path}"'
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError:
        pass

# -------------------- GUI SETUP --------------------
ui = make_screen(
    title="Python to EXE Converter",
    winsize="650x200",
    use_title=False, use_input=False, use_button=False,
    use_loading_bar=False, use_output=False,
)

window = ui["window"]

# -------------------- UI ELEMENTS --------------------
file_label = ui["add_element"](
    "label", text="Select Python File:", row=0, col=0, padx=10, pady=10
)
destination_label = ui["add_element"](
    "label", text="Select Destination Folder:", row=1, col=0, padx=10, pady=10
)

file_entry = ui["add_element"](
    "entry", width=60, row=0, col=1, padx=10, pady=10, weight=1
)
destination_entry = ui["add_element"](
    "entry", width=60, row=1, col=1, padx=10, pady=10, weight=1
)

file_button = ui["add_element"](
    "button", text="Select File", command=select_file, row=0, col=2, padx=10, pady=10
)
destination_button = ui["add_element"](
    "button", text="Select Folder", command=select_destination, row=1, col=2, padx=10, pady=10
)

convert_button = ui["add_element"](
    "button", text="Convert to EXE", command=convert_to_exe,
    row=2, col=0, padx=10, pady=10, colspan="all"
)

# -------------------- MAIN LOOP --------------------
window.mainloop()
