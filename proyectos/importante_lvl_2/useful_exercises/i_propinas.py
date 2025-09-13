"""
==============================
    CALCULADOR DE PROPINAS
==============================

En este programa, el objetivo es calcular la propina
que hay que pagar después de un servicio. Para hacerlo,
se necesita conocer la factura total. Con esta información,
se aplicarán diferentes tasas de propina: 18%, 20% y 25%.
"""
from ....base_functions import *

while True:
    factura = float(wInput("\n¿Cuál es el total de la factura?: "))

    propinas = {"18%": factura * 0.18, "20%": factura * 0.20, "25%": factura * 0.25}

    for propina, porcentaje in propinas.items():
        write(f"\n{propina} → ${porcentaje:.2f} = ${factura + porcentaje:.2f}")
        factura_total = factura + porcentaje
        
    personas = int(wInput("\n¿Cuántas personas van a pagar?: "))

    factura_dividida = round(factura_total / personas, 2)
    write(f"\nPor persona → ${factura_dividida}")

    playAgain()