import psutil
import os
import webbrowser

def listar_procesos():
    procesos = []
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            procesos.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return procesos

def mostrar_procesos(procesos):
    print("\n🔍 Procesos en ejecución:\n")
    for idx, proc in enumerate(procesos):
        nombre = proc.get("name", "??")
        exe = proc.get("exe", "Ruta desconocida")
        print(f"[{idx}] {nombre} -> {exe}")
    print(f"\nTotal: {len(procesos)} procesos")

def buscar_en_google(nombre):
    query = nombre.replace(" ", "+")
    webbrowser.open(f"https://www.google.com/search?q={query}+proceso+Windows")

def terminar_proceso(proc):
    try:
        p = psutil.Process(proc['pid'])
        p.terminate()
        print(f"✅ Proceso '{proc['name']}' terminado.")
    except Exception as e:
        print(f"❌ No se pudo terminar el proceso: {e}")

def main():
    procesos = listar_procesos()
    mostrar_procesos(procesos)

    while True:
        opcion = input("\n¿Querés buscar info de un proceso o terminarlo? (b = buscar / t = terminar / n = salir): ").strip().lower()
        if opcion == 'n':
            break
        elif opcion in ['b', 't']:
            try:
                idx = int(input("Número del proceso: "))
                if 0 <= idx < len(procesos):
                    if opcion == 'b':
                        buscar_en_google(procesos[idx]['name'])
                    elif opcion == 't':
                        confirmar = input("¿Seguro que querés matarlo? (s/n): ").strip().lower()
                        if confirmar == 's':
                            terminar_proceso(procesos[idx])
                else:
                    print("⚠️ Índice fuera de rango.")
            except ValueError:
                print("⚠️ Tenés que poner un número.")
        else:
            print("❓ Opción inválida.")

if __name__ == "__main__":
    main()
