"""
=================
    INFO MAIL
=================

Recopile una dirección de correo electrónico 
del usuario y luego averigüe si el usuario tiene
un nombre de dominio personalizado o un nombre
de dominio popular.

Recopilamos una dirección de correo electrónico
del usuario y luego vamos a averiguar si ese 
email tiene nombre de dominio personalizado o 
un nombre de un dominio popular. Por ejemplo:

Entrada: mary.jane@gmail.com
Salida: Hola Mary, estoy viendo que tu email 
está registrado con Google. ¡Eso es genial!.
Entrada: peter.pan@myfantasy.com
Salida: Hola Peter, estoy observando que estás 
utilizando un dominio personalizado de myfantasy
"""
from ....base_functions import *

dominios_populares = ["gmail", "yahoo", "hotmail", "outlook"]
while True:
    mail = wInput("\nIntroduce tu correo electrónico: ")

    if not mail or "@" not in mail or "." not in mail:
        write("\nIngrese un mal válido\n")
    elif mail.split("@")[1].split(".")[0] in dominios_populares:
        write(f"\nHola {mail.split('@')[0]}, estoy viendo que usas un email POPULAR de {mail.split('@')[1].split('.')[0]}.")
    else:
        write(f"\nHola {mail.split('@')[0]}, estoy viendo que usas un email PERSONALIZADO con {mail.split('@')[1].split('.')[0]}.")
    
    playAgain()