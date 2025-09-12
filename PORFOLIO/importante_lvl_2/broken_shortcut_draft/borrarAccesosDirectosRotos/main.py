import os
import tkinter as tk
from tkinter import filedialog, messagebox
from win32com.client import Dispatch

def obtener_todos_los_accesos(directorio):
    accesos = []
    for root, _, files in os.walk(directorio):
        for file in files:
            if file.endswith(".lnk"):
                ruta_completa = os.path.join(root, file)
                accesos.append(ruta_completa)
    return accesos

class AccesosRotosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🗑️ Eliminar accesos directos rotos 🗑️")
        self.root.geometry("600x500")
        self.root.configure(bg="#2C3E50")
        
        self.frame = tk.Frame(root, bg="#2C3E50")
        self.frame.pack(pady=10)
        
        self.btn_seleccionar = tk.Button(self.frame, text="📂 Seleccionar Carpeta", command=self.seleccionar_carpeta, bg="#2980B9", fg="white", font=("Arial", 12, "bold"), relief="ridge", activebackground="#1F618D")
        self.btn_seleccionar.pack(pady=5)
        
        self.btn_revisar_todo = tk.Button(self.frame, text="🔍 Revisar Toda la PC", command=self.revisar_toda_pc, bg="#16A085", fg="white", font=("Arial", 12, "bold"), relief="ridge", activebackground="#138D75")
        self.btn_revisar_todo.pack(pady=5)
        
        self.lista_frame = tk.Frame(root, bg="#2C3E50")
        self.lista_frame.pack()
        
        self.canvas = tk.Canvas(self.lista_frame, bg="#34495E")
        self.scrollbar = tk.Scrollbar(self.lista_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#34495E")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        self.btn_marcar_todo = tk.Button(root, text="✔️ Marcar Todo", command=self.marcar_todo, bg="#E67E22", fg="white", font=("Arial", 12, "bold"), relief="ridge", activebackground="#D35400")
        self.btn_marcar_todo.pack(pady=5)
        
        self.btn_borrar = tk.Button(root, text="🗑️ Borrar Seleccionados", command=self.borrar_seleccionados, bg="#E74C3C", fg="white", font=("Arial", 12, "bold"), relief="ridge", activebackground="#C0392B")
        self.btn_borrar.pack(pady=5)
        
        self.archivos = []
        self.checkboxes = []
    
    def seleccionar_carpeta(self):
        carpeta = filedialog.askdirectory()
        if not carpeta:
            return
        
        self.listar_accesos(obtener_todos_los_accesos(carpeta))
    
    def revisar_toda_pc(self):
        self.listar_accesos(obtener_todos_los_accesos("C:\\"))
    
    def listar_accesos(self, accesos):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        self.archivos = []
        self.checkboxes = []
        
        for ruta_completa in accesos:
            if not self.es_acceso_valido(ruta_completa) and not self.es_microsoft_store(ruta_completa):
                var = tk.BooleanVar()
                chk = tk.Checkbutton(self.scrollable_frame, text=os.path.basename(ruta_completa), variable=var, bg="#34495E", fg="white", selectcolor="#2C3E50", font=("Arial", 10))
                chk.pack(anchor="w")
                self.archivos.append(ruta_completa)
                self.checkboxes.append((chk, var))
    
    def es_acceso_valido(self, ruta):
        try:
            shell = Dispatch("WScript.Shell")
            acceso = shell.CreateShortcut(ruta)
            return os.path.exists(acceso.TargetPath)
        except:
            return False
    
    def es_microsoft_store(self, ruta):
        return any(keyword in ruta.lower() for keyword in ["windowsapps", "microsoft", "gplay"])
    
    def marcar_todo(self):
        for _, var in self.checkboxes:
            var.set(True)
    
    def borrar_seleccionados(self):
        seleccionados = [i for i, (_, var) in enumerate(self.checkboxes) if var.get()]
        if not seleccionados:
            messagebox.showinfo("⚠️ Info", "No seleccionaste ningún acceso directo roto.")
            return
        
        for index in seleccionados[::-1]:  # Invertir para borrar sin afectar los índices
            try:
                os.remove(self.archivos[index])
                self.checkboxes[index][0].destroy()
                del self.archivos[index]
                del self.checkboxes[index]
            except Exception as e:
                messagebox.showerror("❌ Error", f"No se pudo borrar: {self.archivos[index]}\n{e}")
        
        messagebox.showinfo("✅ Éxito", "Accesos directos eliminados correctamente.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AccesosRotosApp(root)
    root.mainloop()
