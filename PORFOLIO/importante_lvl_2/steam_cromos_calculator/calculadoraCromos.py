import tkinter as tk
from tkinter import messagebox

def calcular_ganancia():
    try:
        cromos_totales = float(entry_cromos_totales.get())
        cromos_posibles = cromos_totales * 0.6
        cromos_mas_barato = float(entry_cromos_mas_barato.get())
        precio_total_cromos = cromos_posibles * cromos_mas_barato
        precio_juego_S_impuestos = float(entry_precio_juego.get())
        precio_juego_C_impuestos = precio_juego_S_impuestos + (0.75 * precio_juego_S_impuestos)

        ganancia_sin_impuestos = precio_total_cromos - precio_juego_S_impuestos
        ganancia_con_impuestos = precio_total_cromos - precio_juego_C_impuestos

        resultado_cromos_posibles.config(text=f"Cromos Posibles: {cromos_posibles:.2f}", bg="#323232", fg="white")
        resultado_precio_total_cromos.config(text=f"Precio de Cromos: ${precio_total_cromos:.2f}", bg="#323232", fg="white")
        resultado_precio_con_impuestos.config(text=f"Con impuestos: ${precio_juego_C_impuestos:.2f}", bg="#323232", fg="white")
        resultado_label_sin_impuestos.config(text=f"Ganancia SIN impuestos: ${ganancia_sin_impuestos:.2f}", bg="#323232", fg="green" if ganancia_sin_impuestos > 0 else "red")
        resultado_label_con_impuestos.config(text=f"Ganancia CON impuestos: ${ganancia_con_impuestos:.2f}", bg="#323232", fg="green" if ganancia_con_impuestos > 0 else "red")
        
    except ValueError:
        messagebox.showerror("Error", "Valor no válido")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Calculadora de Cromos")
ventana.configure(bg="#121212")
fuente = ("Arial", 14)

# Obtener las dimensiones de la pantalla
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Establecer el tamaño de la ventana al 80% de las dimensiones de la pantalla
ventana_width = int(screen_width * 0.6)
ventana_height = int(screen_height * 0.3)

ventana.geometry(f"{ventana_width}x{ventana_height}")

# Etiqueta y entrada para la cantidad de cromos totales
cromos_totales_label = tk.Label(ventana, text="Cromos:", font=fuente, bg="#121212", fg="white")
cromos_totales_label.grid(row=0, column=0, padx=5, pady=10, sticky="w")
entry_cromos_totales = tk.Entry(ventana, font=fuente)
entry_cromos_totales.grid(row=0, column=1, padx=5, pady=10, sticky="w")
resultado_cromos_posibles = tk.Label(ventana, text="Cromos posibles: ", font=fuente, bg="#323232", fg="white")
resultado_cromos_posibles.grid(row=0, column=2, padx=5, pady=10, sticky="w")

# Etiqueta y entrada para el valor del cromo más barato
cromos_mas_barato_label = tk.Label(ventana, text="Más barato:", font=fuente, bg="#121212", fg="white")
cromos_mas_barato_label.grid(row=1, column=0, padx=5, pady=10, sticky="w")
entry_cromos_mas_barato = tk.Entry(ventana, font=fuente)
entry_cromos_mas_barato.grid(row=1, column=1, padx=5, pady=10, sticky="w")
resultado_precio_total_cromos = tk.Label(ventana, text="Precio de cromos: ", font=fuente, bg="#323232", fg="white")
resultado_precio_total_cromos.grid(row=1, column=2, padx=5, pady=10, sticky="w")

# Etiqueta y entrada para el valor del juego sin impuestos
precio_juego_label = tk.Label(ventana, text="Precio sin impuestos:", font=fuente, bg="#121212", fg="white")
precio_juego_label.grid(row=2, column=0, padx=5, pady=10, sticky="w")
entry_precio_juego = tk.Entry(ventana, font=fuente)
entry_precio_juego.grid(row=2, column=1, padx=5, pady=10, sticky="w")
resultado_precio_con_impuestos = tk.Label(ventana, text="Con impuestos: ", font=fuente, bg="#323232", fg="white")
resultado_precio_con_impuestos.grid(row=2, column=2, padx=5, pady=10, sticky="w")

# Botón para calcular la ganancia
calcular_button = tk.Button(ventana, text="Calcular Ganancia", font=fuente, command=calcular_ganancia, bg="#4CAF50", fg="white")
calcular_button.grid(row=3, column=0, columnspan=3, padx=5, pady=20, sticky="w")

# Resultados
resultado_label_sin_impuestos = tk.Label(ventana, text="Ganancia SIN impuestos:", font=fuente, bg="#323232", fg="white")
resultado_label_sin_impuestos.grid(row=3, column=1, padx=5, pady=10, sticky="w")

resultado_label_con_impuestos = tk.Label(ventana, text="Ganancia CON impuestos:", font=fuente, bg="#323232", fg="white")
resultado_label_con_impuestos.grid(row=3, column=2, padx=5, pady=10, sticky="w")

# Ajustar tamaño de ventana automáticamente
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_rowconfigure(2, weight=1)
ventana.grid_rowconfigure(3, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)
ventana.grid_columnconfigure(3, weight=1)

ventana.mainloop()


# while True:
#     try:
#         cromos_totales = float(input("Ingrese la cantidad de cromos totales: "))

#         cromos_posibles = cromos_totales * 0.6

#         cromos_mas_barato = float(input("Ingrese el valor del cromo mas barato: "))

#         precio_total_cromos = cromos_posibles * cromos_mas_barato

#         precio_juego_S_impuestos = float(input("Ingrese el valor del juego: "))

#         precio_juego_C_impuestos = precio_juego_S_impuestos + (0.75 * precio_juego_S_impuestos)

#         if precio_total_cromos > precio_juego_C_impuestos:
#             print(f"Al juego se le saca una ganancia de ${precio_total_cromos-precio_juego_C_impuestos}")
#         else:
#             print(f"No se le saca ganancia.\nSe pierde un valor de ${precio_juego_C_impuestos-precio_total_cromos}")
#     except ValueError: print("Caracter no válido")