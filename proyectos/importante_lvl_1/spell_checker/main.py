import re
import json
import textwrap
import time
from colorama import Fore, Style, init

init(autoreset=True)

def cargar_modismos(archivo="js/modismos.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def barra_de_carga():
    barra = ["[                    ]", "[=                   ]", "[==                  ]", "[===                 ]",
             "[====                ]", "[=====               ]", "[======              ]", "[=======             ]",
             "[========            ]", "[=========           ]", "[==========          ]", "[===========         ]",
             "[============        ]", "[=============       ]", "[==============      ]", "[===============     ]",
             "[================    ]", "[=================   ]", "[==================  ]", "[=================== ]",
             "[====================]"]
    
    for i in range(14):
        print(Fore.YELLOW + Style.BRIGHT + barra[i], end='\r')
        time.sleep(0.2)
    
    print(Fore.CYAN + Style.BRIGHT + "[====================] Pensando... 🧠", end='\r')
    time.sleep(2)
    print(Fore.GREEN + Style.BRIGHT + "[====================] ¡Listo! Procesado con éxito!")

def corregir_texto(texto):
    # Corrección básica de espacios y puntuación
    texto_corregido = texto.lower()
    texto_corregido = re.sub(r'\s+([.,!?;:])', r'\1', texto_corregido)  # Elimina espacios antes de puntuación
    texto_corregido = re.sub(r'([.!?])([^\s])', r'\1 \2', texto_corregido)  # Asegura espacio después de puntuación
    texto_corregido = re.sub(r'\s+', ' ', texto_corregido).strip()  # Elimina espacios múltiples

    # Capitaliza la primera letra de cada oración
    texto_corregido = re.sub(r'(^|[.!?]\s+)(\w)', lambda m: m.group(1) + m.group(2).upper(), texto_corregido)

    # Reemplazo de modismos
    modismos = cargar_modismos()
    for palabra, correccion in modismos.items():
        texto_corregido = re.sub(rf'\b{re.escape(palabra)}\b', correccion, texto_corregido, flags=re.IGNORECASE)

    # Agrega coma después de ciertas conjunciones
    texto_corregido = re.sub(r'\b(y|pero|aunque|sino)\b', r'\1,', texto_corregido)

    # Ajuste de formato
    texto_corregido = textwrap.fill(texto_corregido, width=80)

    return f"{Fore.GREEN}{Style.BRIGHT}✅ Texto Corregido:\n\n{Fore.CYAN}{Style.BRIGHT}{texto_corregido}\n"

if __name__ == "__main__":
    print(Fore.MAGENTA + Style.BRIGHT + "\n¡Bienvenido al Corrector Ultra Fachero!\n")
    print(Fore.CYAN + Style.BRIGHT + "✨ Este proceso será épico... ¡No te vayas a distraer!\n")
    time.sleep(1)

    texto = input(Fore.YELLOW + Style.BRIGHT + "Ingrese un texto a corregir: ")
    print(Fore.GREEN + Style.BRIGHT + "\nIniciando corrección...\n")

    barra_de_carga()

    print(corregir_texto(texto))

    print(Fore.GREEN + Style.BRIGHT + "✨ Proceso Finalizado con Éxito ✨\n")
    print(Fore.RED + Style.BRIGHT + "Gracias por usar el corrector de textos más fachero del universo.\n")

