from colorama import Fore, Style, init
from tqdm import tqdm
import time

init(autoreset=True)

def calcular_promedio():
    numeros = []
    print(Fore.CYAN + "Ingresá números (deja vacío para calcular el promedio):")
    
    while True:
        entrada = input(Fore.YELLOW + "→ ")
        if entrada == "":
            break
        try:
            numeros.append(float(entrada))
        except ValueError:
            print(Fore.RED + "⚠ Entrada no válida. Ingresá un número.")
    
    if numeros:
        print(Fore.MAGENTA + "Calculando el promedio...\n")
        for _ in tqdm(range(50), desc=Fore.GREEN + "Procesando", ncols=80, ascii=" █", colour="green"):
            time.sleep(0.05)
        promedio = sum(numeros) / len(numeros)
        print(Fore.BLUE + f"\nEl promedio de los números ingresados es: {Fore.GREEN}{promedio:.2f}")
    else:
        print(Fore.RED + "No ingresaste ningún número válido.")

if __name__ == "__main__":
    calcular_promedio()
    a = input("")
