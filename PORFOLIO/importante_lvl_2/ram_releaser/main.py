import psutil
import tkinter as tk
from tkinter import messagebox
import ctypes
from ctypes import wintypes

# Configuración para llamar a funciones de la API de Windows
psapi = ctypes.WinDLL('psapi.dll')
kernel32 = ctypes.WinDLL('kernel32.dll')

# Configurar función EmptyWorkingSet
EmptyWorkingSet = psapi.EmptyWorkingSet
EmptyWorkingSet.argtypes = [wintypes.HANDLE]
EmptyWorkingSet.restype = wintypes.BOOL

# Función para liberar memoria de un proceso
def free_process_memory(pid):
    PROCESS_QUERY_INFORMATION = 0x0400
    PROCESS_SET_INFORMATION = 0x0200
    handle = kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_SET_INFORMATION, False, pid)
    if handle:
        result = EmptyWorkingSet(handle)
        kernel32.CloseHandle(handle)
        return result
    return False

# Función para liberar memoria del sistema
def free_system_memory():
    success_count = 0
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if free_process_memory(proc.info['pid']):
                success_count += 1
        except Exception:
            pass
    return success_count

# Función para obtener el uso de memoria actual
def get_memory_usage():
    memory = psutil.virtual_memory()
    used_memory = memory.used // (1024 * 1024)
    total_memory = memory.total // (1024 * 1024)
    return f"Usada: {used_memory} MB / Total: {total_memory} MB"

# Acción del botón "Liberar Memoria"
def free_memory():
    freed_processes = free_system_memory()
    messagebox.showinfo("Memoria Liberada", f"Memoria optimizada en {freed_processes} procesos.")
    memory_label.config(text=get_memory_usage())

# Crear la ventana principal
root = tk.Tk()
root.title("Monitor de Memoria")
root.geometry("300x200")

# Etiqueta para mostrar el uso de memoria
memory_label = tk.Label(root, text=get_memory_usage(), font=("Arial", 14))
memory_label.pack(pady=10)

# Botón para liberar memoria
free_memory_button = tk.Button(root, text="Liberar Memoria", font=("Arial", 12),
                                bg="#0078d4", fg="white", command=free_memory)
free_memory_button.pack(pady=10)

# Iniciar el bucle principal
root.mainloop()
