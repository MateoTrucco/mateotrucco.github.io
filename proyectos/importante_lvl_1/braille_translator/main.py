import tkinter as tk
from tkinter import messagebox

def tabla_base(p1, p2, p3, p4, p5, p6):
    return [p1, p4, p2, p5, p3, p6]

ABECEDARIO = {
    ' ': tabla_base(0,0,0,0,0,0),
    'a': tabla_base(1,0,0,0,0,0),
    'b': tabla_base(1,0,1,0,0,0),
    'c': tabla_base(1,1,0,0,0,0),
    'd': tabla_base(1,1,0,1,0,0),
    'e': tabla_base(1,0,0,1,0,0),
    'f': tabla_base(1,1,1,0,0,0),
    'g': tabla_base(1,1,1,1,0,0),
    'h': tabla_base(1,0,1,1,0,0),
    'i': tabla_base(0,1,1,0,0,0),
    'j': tabla_base(0,1,1,1,0,0),
    'k': tabla_base(1,0,0,0,1,0),
    'l': tabla_base(1,0,1,0,1,0),
    'm': tabla_base(1,1,0,0,1,0),
    'n': tabla_base(1,1,0,1,1,0),
    'ñ': tabla_base(1,1,1,1,0,1),
    'o': tabla_base(1,0,0,1,1,0),
    'p': tabla_base(1,1,1,0,1,0),
    'q': tabla_base(1,1,1,1,1,0),
    'r': tabla_base(1,0,1,1,1,0),
    's': tabla_base(0,1,1,0,1,0),
    't': tabla_base(0,1,1,1,1,0),
    'u': tabla_base(1,0,0,0,1,1),
    'v': tabla_base(1,0,1,0,1,1),
    'w': tabla_base(0,1,1,1,0,1),
    'x': tabla_base(1,1,0,0,1,1),
    'y': tabla_base(1,1,0,1,1,1),
    'z': tabla_base(1,0,0,1,1,1),
}

def braille_visual(letra):
    letra = letra.lower()
    if letra not in ABECEDARIO:
        return [["?", "?"], ["?", "?"], ["?", "?"]]
    puntos = ABECEDARIO[letra]
    return [
        ['•' if puntos[0] else ' ', '•' if puntos[3] else ' '],
        ['•' if puntos[1] else ' ', '•' if puntos[4] else ' '],
        ['•' if puntos[2] else ' ', '•' if puntos[5] else ' ']
    ]

def traducir_horizontal_tablero(texto):
    if not texto:
        return ""

    letras = [braille_visual(l) for l in texto]
    filas = len(letras[0])

    linea_superior = "┌" + "┬".join(["──" for _ in texto]) + "┐"
    linea_inferior = "└" + "┴".join(["──" for _ in texto]) + "┘"

    resultado = [linea_superior]

    for fila in range(filas):
        linea = "│"
        for letra in letras:
            linea += letra[fila][0] + letra[fila][1] + "│"
        resultado.append(linea)

    resultado.append(linea_inferior)
    return "\n".join(resultado)

def traducir():
    texto = entrada_texto.get()
    if not texto:
        messagebox.showwarning("Aviso", "Ingrese al menos una letra")
        return
    resultado = traducir_horizontal_tablero(texto)
    salida_texto.config(state='normal')
    salida_texto.delete("1.0", tk.END)
    salida_texto.insert(tk.END, resultado)
    salida_texto.config(state='disabled')

ventana = tk.Tk()
ventana.title("Traductor a Braille")
ventana.geometry("800x300")
ventana.resizable(True, True)

tk.Label(ventana, text="Ingrese texto (a-z, ñ):").pack(pady=10)
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack()

tk.Button(ventana, text="Traducir", command=traducir).pack(pady=10)

salida_texto = tk.Text(ventana, width=120, height=10, state='disabled', font=("Courier", 12))
salida_texto.pack(padx=10, pady=10)

ventana.mainloop()
