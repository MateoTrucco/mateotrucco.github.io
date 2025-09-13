import time

try:
    from colorama import Fore, Style
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False


def slip(taim):
    time.sleep(taim)

def barra_de_carga():
    if COLORAMA_AVAILABLE:
        print(Fore.MAGENTA + "Cargando:", end=" ")
        colores = [Fore.RED, Fore.RED, Fore.RED, Fore.RED, Fore.RED, Fore.RED, Fore.YELLOW, Fore.YELLOW, Fore.YELLOW, Fore.YELLOW, Fore.YELLOW, Fore.YELLOW, Fore.GREEN, Fore.GREEN, Fore.GREEN, Fore.GREEN, Fore.GREEN, Fore.GREEN, Fore.MAGENTA, Fore.MAGENTA]
    else:
        print("Cargando:", end=" ")
        colores = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    
    for i in range(20):
        time.sleep(0.1)
        print(colores[i] + "█" + (Style.RESET_ALL if COLORAMA_AVAILABLE else ""), end="", flush=True)
    print(Style.RESET_ALL if COLORAMA_AVAILABLE else "")

def decimal_a_binario(n):
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        residuo = n % 2
        binario = str(residuo) + binario
        n //= 2
    return binario

def main():
    try:
        entrada = input((Fore.CYAN if COLORAMA_AVAILABLE else "") + "Ingrese un número decimal (o 'salir' para terminar): \n--- " + (Style.RESET_ALL if COLORAMA_AVAILABLE else ""))
        if entrada.lower() == "salir":
            print((Fore.YELLOW if COLORAMA_AVAILABLE else "") + "Saliendo del programa..." + (Style.RESET_ALL if COLORAMA_AVAILABLE else ""))
            slip(1)
            return False  # Devuelve False para indicar que hay que terminar el loop
        num = int(entrada)
        slip(0.5)
        print((Fore.BLUE if COLORAMA_AVAILABLE else "") + "\nProcesando..." + (Style.RESET_ALL if COLORAMA_AVAILABLE else ""))
        barra_de_carga()
        binario = decimal_a_binario(num)
        print((Fore.GREEN if COLORAMA_AVAILABLE else "") + f"El número {num} en binario es: \n |||   {binario}   |||\n" + (Style.RESET_ALL if COLORAMA_AVAILABLE else ""))
        slip(0.5)
    except ValueError:
        print((Fore.RED if COLORAMA_AVAILABLE else "") + "Error: Ingrese un número ENTERO válido.\n" + (Style.RESET_ALL if COLORAMA_AVAILABLE else ""))
        slip(0.5)
    return True  # Devuelve True para seguir el loop

if __name__ == "__main__":
    while True:
        if not main():
            break  # Rompe el loop cuando `main()` devuelve False
