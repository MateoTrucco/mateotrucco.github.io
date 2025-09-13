import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def seleccionar_archivo():
    # Abrir cuadro de diálogo para seleccionar archivo .py
    archivo = filedialog.askopenfilename(filetypes=[("Archivos Python", "*.py")])
    if archivo:
        entry_archivo.delete(0, tk.END)  # Limpiar entrada
        entry_archivo.insert(0, archivo)  # Colocar ruta en la entrada

def seleccionar_destino():
    # Abrir cuadro de diálogo para elegir carpeta de destino
    destino = filedialog.askdirectory()
    if destino:
        entry_destino.delete(0, tk.END)  # Limpiar entrada
        entry_destino.insert(0, destino)  # Colocar ruta en la entrada

def convertir_a_exe():
    archivo_py = entry_archivo.get()
    destino = entry_destino.get()

    # Verificar si se han seleccionado archivo y destino
    if not archivo_py or not destino:
        messagebox.showerror("Error", "Debes seleccionar un archivo y una carpeta de destino.")
        return

    # Ruta de salida para el archivo .exe
    salida = os.path.join(destino, os.path.basename(archivo_py).replace(".py", ".exe"))

    # Comando para ejecutar PyInstaller
    comando = f'pyinstaller --onefile --noconsole --distpath "{destino}" --workpath "{destino}/build" "{archivo_py}"'
    
    try:
        # Ejecutar PyInstaller
        subprocess.run(comando, check=True, shell=True)

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", f"El archivo se ha convertido exitosamente en: {salida}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Ocurrió un error al convertir el archivo: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Convertir Python a EXE")

# Crear widgets
label_archivo = tk.Label(ventana, text="Selecciona el archivo .py:")
label_archivo.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_archivo = tk.Entry(ventana, width=40)
entry_archivo.grid(row=0, column=1, padx=10, pady=10)

boton_archivo = tk.Button(ventana, text="Seleccionar archivo", command=seleccionar_archivo)
boton_archivo.grid(row=0, column=2, padx=10, pady=10)

label_destino = tk.Label(ventana, text="Selecciona la carpeta de destino:")
label_destino.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_destino = tk.Entry(ventana, width=40)
entry_destino.grid(row=1, column=1, padx=10, pady=10)

boton_destino = tk.Button(ventana, text="Seleccionar carpeta", command=seleccionar_destino)
boton_destino.grid(row=1, column=2, padx=10, pady=10)

boton_convertir = tk.Button(ventana, text="Convertir a EXE", command=convertir_a_exe)
boton_convertir.grid(row=2, column=0, columnspan=3, padx=10, pady=20)

# Iniciar la interfaz gráfica
ventana.mainloop()
