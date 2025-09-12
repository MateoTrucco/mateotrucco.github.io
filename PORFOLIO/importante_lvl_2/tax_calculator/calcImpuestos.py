import tkinter as tk
from tkinter import simpledialog

class CalculadoraImpuestos:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Impuestos")
        self.root.geometry("300x150")
        self.root.configure(bg="#f0f0f0")

        self.precio_original_entry = tk.Entry(root)
        self.precio_original_entry.pack(pady=10, padx=20, fill=tk.X)

        self.botones_frame = tk.Frame(root, bg="#f0f0f0")
        self.botones_frame.pack(pady=5)

        self.calcular_button = tk.Button(self.botones_frame, text="Calcular", command=self.calcular_precio_final, bg="#4caf50", fg="white")
        self.calcular_button.pack(side=tk.LEFT, padx=5)

        self.configurar_button = tk.Button(self.botones_frame, text="Configurar", command=self.abrir_configuracion, bg="#2196f3", fg="white")
        self.configurar_button.pack(side=tk.LEFT, padx=5)

        self.precio_final_label = tk.Label(root, text="Precio Final", bg="#f0f0f0", font=("Arial", 12, "bold"))
        self.precio_final_label.pack(pady=5, padx=20, fill=tk.X)

    def calcular_precio_final(self):
        try:
            precio_original = float(self.precio_original_entry.get())
            impuesto_porcentaje = self.obtener_porcentaje_impuestos()
            precio_final = precio_original * (1 + impuesto_porcentaje / 100)
            self.precio_final_label.config(text=f"{precio_final:.2f} ARS")
        except ValueError:
            self.precio_final_label.config(text="Ingrese un valor válido")

    def abrir_configuracion(self):
        porcentaje_impuestos = simpledialog.askfloat("Configuración", "Porcentaje de impuestos:")
        if porcentaje_impuestos is not None:
            self.guardar_porcentaje_impuestos(porcentaje_impuestos)

    def obtener_porcentaje_impuestos(self):
        try:
            return float(self.root.getvar('porcentaje_impuestos'))
        except (tk.TclError, ValueError):
            return 0

    def guardar_porcentaje_impuestos(self, porcentaje_impuestos):
        self.root.setvar('porcentaje_impuestos', porcentaje_impuestos)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraImpuestos(root)
    root.mainloop()
