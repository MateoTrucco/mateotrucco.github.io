INICIO

    DEFINIR FUNCION UltimoDigito(x)
        RETORNAR x MOD 10
    FIN FUNCION

    DEFINIR FUNCION ContarDigitos(x)
        RETORNAR LONGITUD(CONVERTIR_A_CADENA(x))
    FIN FUNCION

    DEFINIR FUNCION ContarParesImpares(x)
        DEFINIR pares, impares COMO ENTERO
        pares ← 0
        impares ← 0
        PARA CADA digito EN CONVERTIR_A_CADENA(x) HACER
            SI CONVERTIR_A_ENTERO(digito) MOD 2 = 0 ENTONCES
                pares ← pares + 1
            SINO
                impares ← impares + 1
            FIN SI
        FIN PARA
        RETORNAR (pares, impares)
    FIN FUNCION

    DEFINIR FUNCION SumaDigitos(x)
        DEFINIR suma COMO ENTERO
        suma ← 0
        PARA CADA digito EN CONVERTIR_A_CADENA(x) HACER
            suma ← suma + CONVERTIR_A_ENTERO(digito)
        FIN PARA
        RETORNAR suma
    FIN FUNCION

    // Programa principal
    DEFINIR x COMO ENTERO
    ESCRIBIR "Ingrese un número natural: "
    LEER x

    ESCRIBIR "Último dígito: ", UltimoDigito(x)
    ESCRIBIR "Cantidad de dígitos: ", ContarDigitos(x)

    DEFINIR pares, impares COMO ENTERO
    (pares, impares) ← ContarParesImpares(x)
    ESCRIBIR "Cantidad de dígitos pares: ", pares, " impares: ", impares

    ESCRIBIR "Suma de los dígitos: ", SumaDigitos(x)

FIN
