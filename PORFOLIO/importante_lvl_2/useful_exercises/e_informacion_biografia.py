"""
===================================
    INFORMACION DE LA BIOGRAFIA
===================================

Pregunte a un usuario su información personal
en una sola ronda de preguntas. Luego hay que
verificar que la información que se ha ingresado
sea válida. Finalmente, se imprime un resumen
de toda la información que ha sido ingresada.
"""
from a_funciones_basicas import *

while True:
    nombre      =   wInput("Nombre completo: "); wait()
    edad        =   wInput("Edad: "); wait()
    mail        =   wInput("Mail: "); wait()
    telefono    =   wInput("Teléfono: "); wait()

    if not nombre or len(nombre.split()) <= 1:
        write("¡¡¡ Ingrese un nombre valido (nombre y apellido) !!!")
    elif not edad or not edad.isdigit():
        write("¡¡¡ Ingrese una edad valida (entero) !!!")
    elif not mail or "@" not in mail or "." not in mail:
        write("¡¡¡ Ingrese un mail valido (mail y dominio) !!!")
    elif not telefono or len(telefono) < 10:
        write("¡¡¡ Ingrese un teléfono valido (10 digitos) !!!")
    else:
        ancho_campo = 28
        ancho_total = 40
        write(encuadrar(f"""
{('RESUMEN INFORMACIÓN PERSONAL').center(ancho_total)}
{'─' * ancho_total}
Nombre:     {nombre.rjust(ancho_campo)}
Edad:       {edad.rjust(ancho_campo)}
Mail:       {mail.rjust(ancho_campo)}
Teléfono:   {telefono.rjust(ancho_campo)}
"""))
        
    playAgain()
