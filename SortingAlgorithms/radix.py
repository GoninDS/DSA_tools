def ordenamiento_por_conteo_digito(
    arreglo, longitud_arreglo, lugar_valor_posicional, base=10
):
    """
    Ordena un arreglo de enteros no negativos por el dígito en una posición específica, usando la base dada.
    parametros:
    ----------
    - arreglo: lista de enteros no negativos a ordenar.
    - longitud_arreglo: cantidad de elementos en el arreglo.
    - lugar_valor_posicional: valor posicional del dígito a considerar.
    - base: base del sistema numérico a utilizar. Por defecto es 10.
    """

    # Crear arreglos auxiliares
    arreglo_salida = [0] * longitud_arreglo
    conteo_digitos = [0] * base  # Tamaño basado en la base

    # Contar la frecuencia de cada dígito en la posición especificada
    for i in range(longitud_arreglo):
        digito = (arreglo[i] // lugar_valor_posicional) % base
        conteo_digitos[digito] += 1
    print(f"C = {conteo_digitos}")

    # Calcular las posiciones finales de cada dígito en el arreglo ordenado (frecuencia acumulada)
    for i in range(1, base):
        conteo_digitos[i] += conteo_digitos[i - 1]
    print(f"C' = {conteo_digitos}")

    # Construir el arreglo de salida
    for i in range(longitud_arreglo - 1, -1, -1):
        digito = (arreglo[i] // lugar_valor_posicional) % base
        arreglo_salida[conteo_digitos[digito] - 1] = arreglo[i]
        conteo_digitos[digito] -= 1

    print(f"C'' = {conteo_digitos}")

    # Copiar el arreglo de salida al arreglo original
    print("B -> A:")
    for i in range(longitud_arreglo):
        arreglo[i] = arreglo_salida[i]
        print(f"pos {i+1}: {arreglo_salida[i]} ")
    print("---------------------------------------------")


def ordenamiento_por_base(arreglo, numero_digitos, base=10):  # Base por defecto es 10
    """
    Ordena un arreglo de enteros no negativos utilizando el algoritmo de ordenamiento por base (radix sort).
    parametros:
    ----------
    - arreglo: lista de enteros no negativos a ordenar.
    - numero_digitos: cantidad de dígitos a considerar en el ordenamiento.
    - base: base del sistema numérico a utilizar. Por defecto es 10.
    """
    longitud_arreglo = len(arreglo)

    # Realizar ordenamiento por conteo para cada dígito, comenzando por el menos significativo (unidades)
    for posicion_digito in range(numero_digitos):
        lugar_valor_posicional = base**posicion_digito  # Usar la base correcta
        ordenamiento_por_conteo_digito(
            arreglo, longitud_arreglo, lugar_valor_posicional, base
        )


# Ejemplos de uso
A_1 = [int(str(num), 10) for num in [22, 34, 14, 3, 31, 3, 54, 3]]
print("Arreglo original (A_1):", A_1)
ordenamiento_por_base(A_1, 2, 10)  # Ordenar en base 6 (2 dígitos)
print("Arreglo ordenado:", A_1)

A_2 = [int(str(num), 10) for num in [11, 52, 42, 2, 51, 5, 2, 35]]
print("Arreglo original (A_2):", A_2)
ordenamiento_por_base(A_2, 3, 10)  # Ordenar en base 6 (2 dígitos)
print("Arreglo ordenado:", A_2)
