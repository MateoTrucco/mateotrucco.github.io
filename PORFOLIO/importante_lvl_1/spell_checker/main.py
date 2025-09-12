import re
import language_tool_python
import json
import textwrap
import time
from colorama import Fore, Back, Style, init

# Inicializamos colorama para los colores
init(autoreset=True)

def cargar_modismos(archivo="modismos.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def barra_de_carga():
    # Barra de carga para darle más facha al proceso
    barra = ["[                    ]", "[=                   ]", "[==                  ]", "[===                 ]",
             "[====                ]", "[=====               ]", "[======              ]", "[=======             ]",
             "[========            ]", "[=========           ]", "[==========          ]", "[===========         ]",
             "[============        ]", "[=============       ]", "[==============      ]", "[===============     ]",
             "[================    ]", "[=================   ]", "[==================  ]", "[=================== ]",
             "[====================]"]
    
    # Primer 2/3 de la barra
    for i in range(14):
        print(Fore.YELLOW + Style.BRIGHT + barra[i], end='\r')
        time.sleep(0.2)
    
    # Simulamos que está "pensando" o procesando el texto
    print(Fore.CYAN + Style.BRIGHT + "[====================] Pensando... 🧠", end='\r')
    time.sleep(2)  # Tiempo de "pensado"

    # Completa la barra
    print(Fore.GREEN + Style.BRIGHT + "[====================] ¡Listo! Procesado con éxito!")

def corregir_texto(texto):
    tool = language_tool_python.LanguageTool('es')  # Español
    
    # Corrección ortográfica y gramatical
    texto_corregido = tool.correct(texto)
    
    # Normalización de espacios y signos de puntuación
    texto_corregido = re.sub(r'\s+([.,!?])', r'\1', texto_corregido)  # Elimina espacios antes de signos
    texto_corregido = re.sub(r'([.!?])([^\s])', r'\1 \2', texto_corregido)  # Añade espacio después de signos
    texto_corregido = re.sub(r'\s+', ' ', texto_corregido).strip()  # Elimina espacios innecesarios
    
    # Corrección de mayúsculas en inicios de oración
    texto_corregido = re.sub(r'(^|[.!?]\s+)(\w)', lambda m: m.group(1) + m.group(2).upper(), texto_corregido)
    
    # Corrección de modismos y jergas desde archivo externo
    modismos = cargar_modismos()
    for palabra, correccion in modismos.items():
        texto_corregido = re.sub(rf'\b{re.escape(palabra)}\b', correccion, texto_corregido, flags=re.IGNORECASE)
    
    # Agregar comas donde corresponda (ejemplo: antes de "pero", "y", "aunque", etc.)
    texto_corregido = re.sub(r'\b(y|pero|aunque|sino)\b', r'\1,', texto_corregido)
    
    # Ajuste de saltos de línea para mejor legibilidad
    texto_corregido = textwrap.fill(texto_corregido, width=80)
    
    # Estilo y color para la salida
    return f"{Fore.GREEN}{Style.BRIGHT}✅ Texto Corregido:\n\n{Fore.CYAN}{Style.BRIGHT}{texto_corregido}\n"

if __name__ == "__main__":
    # Presentación inicial, para ponerle más onda
    print(Fore.MAGENTA + Style.BRIGHT + "\n¡Bienvenido al Corrector Ultra Fachero!\n")
    print(Fore.CYAN + Style.BRIGHT + "✨ Este proceso será épico... ¡No te vayas a distraer!\n")
    time.sleep(1)
    
    texto = input(Fore.YELLOW + Style.BRIGHT + "Ingrese un texto a corregir: ")
    print(Fore.GREEN + Style.BRIGHT + "\nIniciando corrección...\n")
    
    # Barra de carga que va a mostrar progreso
    barra_de_carga()
    
    # Mostrar el texto corregido
    print(corregir_texto(texto))
    
    # Finaliza el proceso
    print(Fore.GREEN + Style.BRIGHT + "✨ Proceso Finalizado con Éxito ✨\n")
    print(Fore.RED + Style.BRIGHT + "Gracias por usar el corrector de textos más fachero del universo.\n")
