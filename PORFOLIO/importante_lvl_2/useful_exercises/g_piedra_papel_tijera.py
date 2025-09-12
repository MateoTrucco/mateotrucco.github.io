"""
============================
    PIEDRA PAPEL TIJERAS
============================

Es un clásico juego de mesa para dos jugadores.

Cada jugador elige una de las siguientes opciones:

1. Piedra (puño cerrado)
2. Papel (mano plana)
3. Tijeras (un puño con el dedo índice y
    el dedo medio extendidos, formando una V)

El jugador que gana obtiene un punto, y el
primer jugador en obtener tres puntos gana el
juego.
"""
from a_funciones_basicas import *
import random

score_user, score_pc = 0, 0

while True:
    user_ = str(wInput("""
    Elige una opcion (numero):
    1. PIEDRA 🪨
    2. PAPEL 📋
    3. TIJERA ✂️
    """))
    
    if user_ == "1": user = "🪨"
    elif user_ == "2": user = "📋"
    elif user_ == "3": user = "✂️"
    else:
        write("Opcion no valida")
        exit()

    pc = random.choice(["🪨","📋","✂️"])

    if user == pc:
        result = ("EMPATE")
    elif (user == "🪨" and pc == "✂️") or (user == "📋" and pc == "🪨") or (user == "✂️" and pc == "📋"):
        result = ("GANASTE")
        score_user += 1
    elif (user == "🪨" and pc == "📋") or (user == "📋" and pc == "✂️") or (user == "✂️" and pc == "🪨"):
        result = ("PERDISTE")
        score_pc += 1
    
    ancho_campo = 28
    ancho_total = 40
    write(encuadrar(f"""
{('RESULTADOS').center(ancho_total)}
{'─' * ancho_total}
User:     {user.rjust(ancho_campo)} 
Pc:       {pc.rjust(ancho_campo)} 
{'─' * ancho_total}
{result.center(ancho_total)}
{(f'USER {score_user} - {score_pc} PC').center(ancho_total)}
"""),0.01)
    
    if score_user == 5 or score_pc == 5: playAgain()