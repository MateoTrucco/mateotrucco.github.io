import tkinter as tk
from tkinter import messagebox
import math
import platform

def es_cuadrado_perfecto(n):
    raiz = int(math.sqrt(n))
    return raiz * raiz == n

def factorizar_raiz(n):
    if es_cuadrado_perfecto(n):
        return f"√{n} = {int(math.sqrt(n))}"
    
    factor = 1
    b = n
    for i in range(2, int(math.sqrt(n)) + 1):
        while b % (i * i) == 0:
            factor *= i
            b //= i * i
    
    if factor == 1:
        return f"√{n} no puede simplificarse"
    return f"√{n} = {factor}√{b}"

def calcular():
    try:
        num = int(entry.get())
        resultado = factorizar_raiz(num)
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Ingresá un número válido.")

def adaptar_interfaz():
    sistema = platform.system()
    if sistema == "Android":
        root.geometry("400x600")
        label.config(font=("Arial", 20))
        entry.config(font=("Arial", 18))
        boton.config(font=("Arial", 18))
    else:
        root.geometry("300x200")
        label.config(font=("Arial", 14))
        entry.config(font=("Arial", 12))
        boton.config(font=("Arial", 12))

root = tk.Tk()
root.title("Raíz y Factorización")

label = tk.Label(root, text="Ingresá un número:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

boton = tk.Button(root, text="Calcular", command=calcular)
boton.pack(pady=10)

adaptar_interfaz()
root.mainloop()
