import tkinter as tk
def buttonText(num, seg=3):
    calcularBtn.config(text=num)
    app.after((int(seg) * 1000), lambda: calcularBtn.config(text="Calcular"))

def entryText(num):
    exponenteEnt.insert(tk.END, num)

def entryDel():
    exponenteEnt.delete(0, tk.END)

def calculate_result():
    try:
        exp = int(exponenteEnt.get())
        mod = exp % 4

        if   mod == 0: buttonText("1")
        elif mod == 1: buttonText("i")
        elif mod == 2: buttonText("-1")
        elif mod == 3: buttonText("-i")
    except ValueError: buttonText("Error")

app = tk.Tk()
app.title("Calculadora de Exponente de i")
app.configure(bg="#F0F0F0")

exponenteEnt = tk.Entry(app, font=("Helvetica", 20), justify="center")
calcularBtn = tk.Button(app, text="Calcular", command=calculate_result, bg="#4CAF50", fg="white", font=("Helvetica", 15), relief="flat", borderwidth=2, padx=15, pady=5, cursor="hand2")

calcBtn1 = tk.Button(app, text="1", command=lambda:entryText("1"), bg="beige", fg="black", font=("Helvetica", 15))
calcBtn2 = tk.Button(app, text="2", command=lambda:entryText("2"), bg="beige", fg="black", font=("Helvetica", 15))
calcBtn3 = tk.Button(app, text="3", command=lambda:entryText("3"), bg="beige", fg="black", font=("Helvetica", 15))

calcBtn4 = tk.Button(app, text="4", command=lambda:entryText("4"), bg="beige", fg="black", font=("Helvetica", 15))
calcBtn5 = tk.Button(app, text="5", command=lambda:entryText("5"), bg="beige", fg="black", font=("Helvetica", 15))
calcBtn6 = tk.Button(app, text="6", command=lambda:entryText("6"), bg="beige", fg="black", font=("Helvetica", 15))

calcBtn7 = tk.Button(app, text="7", command=lambda:entryText("7"), bg="beige", fg="black", font=("Helvetica", 15))
calcBtn8 = tk.Button(app, text="8", command=lambda:entryText("8"), bg="beige", fg="black", font=("Helvetica", 15))
calcBtn9 = tk.Button(app, text="9", command=lambda:entryText("9"), bg="beige", fg="black", font=("Helvetica", 15))

calcBtn0 = tk.Button(app, text="0", command=lambda:entryText("0"), bg="beige", fg="black", font=("Helvetica", 15))
calcBtnDel = tk.Button(app, text="<<<", command=lambda:entryDel(), bg="pink", fg="black", font=("Helvetica", 15))

exponenteEnt.grid(row=0, column=0, padx=10, pady=5, columnspan=3, sticky="nsew")
calcularBtn.grid(row=1, column=0, padx=10, pady=5, columnspan=3, sticky="nsew")

calcBtn1.grid(row=2, column=0, padx=3, pady=3, sticky="nsew")
calcBtn2.grid(row=2, column=1, padx=3, pady=3, sticky="nsew")
calcBtn3.grid(row=2, column=2, padx=3, pady=3, sticky="nsew")

calcBtn4.grid(row=3, column=0, padx=3, pady=3, sticky="nsew")
calcBtn5.grid(row=3, column=1, padx=3, pady=3, sticky="nsew")
calcBtn6.grid(row=3, column=2, padx=3, pady=3, sticky="nsew")

calcBtn7.grid(row=4, column=0, padx=3, pady=3, sticky="nsew")
calcBtn8.grid(row=4, column=1, padx=3, pady=3, sticky="nsew")
calcBtn9.grid(row=4, column=2, padx=3, pady=3, sticky="nsew")

calcBtn0.grid(row=5, column=0, padx=3, pady=3, sticky="nsew")
calcBtnDel.grid(row=5, column=1, padx=3, pady=3, columnspan=2, sticky="nsew")

for row in range(6):
    app.grid_rowconfigure(row, weight=2)

for column in range(4):
    app.grid_columnconfigure(column, weight=2)

exponenteEnt.config(highlightthickness=2, highlightbackground="#4CAF50")

app.mainloop()