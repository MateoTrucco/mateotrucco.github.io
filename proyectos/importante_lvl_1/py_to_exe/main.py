import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from base_functions import enable_high_dpi

enable_high_dpi()

def select_file():
    """
    Opens a file dialog to select a Python (.py) file and updates the entry field.
    """
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def select_destination():
    """
    Opens a directory dialog to select the destination folder and updates the entry field.
    """
    folder_path = filedialog.askdirectory()
    if folder_path:
        destination_entry.delete(0, tk.END)
        destination_entry.insert(0, folder_path)

def convert_to_exe():
    """
    Converts the selected Python file to an executable and saves it in a named subfolder.

    Creates a subfolder named after the Python file (without .py) in the destination folder,
    and saves the .exe and build files there.
    """
    file_path = file_entry.get()
    destination_folder = destination_entry.get()

    if not file_path or not destination_folder:
        messagebox.showerror("Error", "Please select a Python file and a destination folder.")
        return

    file_name = os.path.basename(file_path).replace(".py", "")
    output_folder = os.path.join(destination_folder, file_name)
    os.makedirs(output_folder, exist_ok=True)

    output_exe = os.path.join(output_folder, f"{file_name}.exe")

    command = f'pyinstaller --onefile --noconsole --distpath "{output_folder}" --workpath "{output_folder}/build" "{file_path}"'

    try:
        subprocess.run(command, check=True, shell=True)
        messagebox.showinfo("Success", f"The file was successfully converted to:\n{output_exe}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while converting the file:\n{e}")

ventana = tk.Tk()
ventana.title("Convertir Python a EXE")

file_label = tk.Label(ventana, text="Selecciona el archivo .py:")
file_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

file_entry = tk.Entry(ventana, width=40)
file_entry.grid(row=0, column=1, padx=10, pady=10)

file_button = tk.Button(ventana, text="Seleccionar archivo", command=select_file)
file_button.grid(row=0, column=2, padx=10, pady=10)

destination_label = tk.Label(ventana, text="Selecciona la carpeta de destino:")
destination_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

destination_entry = tk.Entry(ventana, width=40)
destination_entry.grid(row=1, column=1, padx=10, pady=10)

destination_button = tk.Button(ventana, text="Seleccionar carpeta", command=select_destination)
destination_button.grid(row=1, column=2, padx=10, pady=10)

convert_button = tk.Button(ventana, text="Convertir a EXE", command=convert_to_exe)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=20)

ventana.mainloop()
