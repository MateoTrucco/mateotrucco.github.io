import winreg
import os

# Lista de programas que suelen volver a agregarse solos
programas_pesados = {
    "Discord": "💬 Suele volver si no lo desactivás desde su config.",
    "Spotify": "🎵 Puede autoinstalarse en inicio otra vez.",
    "MicrosoftEdgeAutoLaunch": "🌐 Microsoft empuja esto fuerte.",
    "Canva": "🎨 Algunas versiones lo reactivan solas.",
}

def listar_autoinicio():
    ubicaciones = [
        (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
        (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run")
    ]
    
    entradas = []

    for raiz, ruta in ubicaciones:
        try:
            clave = winreg.OpenKey(raiz, ruta)
            i = 0
            while True:
                nombre, valor, _ = winreg.EnumValue(clave, i)
                entradas.append((raiz, ruta, nombre, valor))
                i += 1
        except OSError:
            pass

    return entradas

def mostrar_entradas(entradas):
    print("\n🔍 Lista de programas al inicio:\n")
    for idx, (raiz, ruta, nombre, valor) in enumerate(entradas):
        nota = ""
        for sospechoso in programas_pesados:
            if sospechoso.lower() in nombre.lower():
                nota = f" ⚠️  {programas_pesados[sospechoso]}"
                break
        print(f"[{idx}] {nombre} -> {valor}{nota}")

def eliminar_entrada(entrada, bloquear=False):
    raiz, ruta, nombre, _ = entrada
    try:
        clave = winreg.OpenKey(raiz, ruta, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(clave, nombre)
        print(f"✅ Entrada '{nombre}' eliminada correctamente.")

        if bloquear:
            # Bloquear creando una clave vacía
            winreg.SetValueEx(clave, nombre, 0, winreg.REG_SZ, "")
            print(f"🚫 '{nombre}' bloqueado para que no se reactive solo.")
    except Exception as e:
        print(f"❌ Error al eliminar la entrada '{nombre}': {e}")

def main():
    entradas = listar_autoinicio()
    if not entradas:
        print("✅ No hay programas configurados para iniciar con Windows.")
        return

    mostrar_entradas(entradas)

    while True:
        opcion = input("\n¿Querés eliminar alguna entrada? (s para sí, n para salir): ").strip().lower()
        if opcion == 'n':
            break
        elif opcion == 's':
            try:
                idx = int(input("Número de la entrada a eliminar: "))
                if 0 <= idx < len(entradas):
                    bloquear = input("¿Querés bloquear que se vuelva a agregar? (s/n): ").strip().lower() == 's'
                    eliminar_entrada(entradas[idx], bloquear)
                else:
                    print("⚠️ Índice fuera de rango.")
            except ValueError:
                print("⚠️ Tenés que poner un número.")
        else:
            print("❓ Opción inválida.")

if __name__ == "__main__":
    main()
