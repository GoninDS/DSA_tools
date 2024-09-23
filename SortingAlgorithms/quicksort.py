def intercambiar(
    arreglo: list, indice_primero: int, indice_segundo: int
) -> None:
    """Intercambia dos elementos en un arreglo.

    parametros:
    ----------
    - arreglo: lista de elementos en la que se realizará el intercambio.
    - indice_primero: índice del primer elemento a intercambiar.
    - indice_segundo: índice del segundo elemento a intercambiar.
    """
    temporal = arreglo[indice_primero]
    arreglo[indice_primero] = arreglo[indice_segundo]
    arreglo[indice_segundo] = temporal


def quicksort(
    arreglo: list,
    indice_inicio: int,
    indice_final: int,
    sangria: str = "",
    nivel: int = 1,
) -> None:
    """Ordena un arreglo utilizando quicksort sin selección de pivote aleatorio.

    parametros:
    ----------
    - arreglo: lista de elementos a ordenar. Equivale a A en el pseudocódigo.
    - indice_inicio: índice del primer elemento del subarreglo a ordenar.
      Equivale a p en el pseudocódigo.
    - indice_final: índice del último elemento del subarreglo a ordenar.
      Equivale a r en el pseudocódigo.
    - sangria: cadena de texto que se agrega al inicio de cada impresión.
      para mejorar la legibilidad de la recursión.
    """
    if indice_inicio < indice_final:
        print(
            sangria
            + f"N: {nivel}, p: {indice_inicio + 1}, r: {indice_final + 1}\n"
            + sangria
            + f"El pivote es {arreglo[indice_final]}"
            + f" (pos {indice_final + 1})\n" + sangria 
            + "trabaja sobre el Subarreglo: "
            + f"{arreglo[indice_inicio:indice_final + 1]}.",
        )
        indice_pivote = particionar(
            arreglo, indice_inicio, indice_final, sangria
        )
        quicksort(
            arreglo,
            indice_inicio,
            indice_pivote - 1,
            sangria + " " * 3,
            nivel + 1,
        )
        quicksort(
            arreglo,
            indice_pivote + 1,
            indice_final,
            sangria + " " * 3,
            nivel + 1,
        )


def particionar(
    arreglo: list,
    indice_inicio: int,
    indice_final: int,
    sangria: str = "",
) -> int:
    """Particiona un arreglo en dos, uno con elementos <= al pivote y otro con elementos >= al pivote.

    parametros:
    ----------
    - arreglo: lista de elementos a particionar.
               Equivale a A en el pseudocódigo.
    - indice_inicio: índice del primer elemento del subarreglo a particionar.
                     Equivale a p en el pseudocódigo.
    - indice_final: índice del último elemento del subarreglo a particionar.
                    Equivale a r en el pseudocódigo.
    retorna:
    --------
    - int: índice del pivote después de la partición.
           Equivale a q en el pseudocódigo.
    """
    valor_pivote = arreglo[indice_final]
    limite_elementos_menores = indice_inicio - 1
    for indice_actual in range(indice_inicio, indice_final):
        if arreglo[indice_actual] <= valor_pivote:
            limite_elementos_menores += 1
            intercambiar(arreglo, limite_elementos_menores, indice_actual)
    intercambiar(arreglo, limite_elementos_menores + 1, indice_final)
    print(sangria + f"Finalizó pos {limite_elementos_menores + 1 + 1}")
    print(
        sangria
        + f"Dejó el arreglo de trabajo como: {arreglo[indice_inicio:indice_final + 1]}"
    )
    return limite_elementos_menores + 1


arreglo = ["K", "V", "Y", "N", "T", "S", "D", "B", "J", "I", "G"]
print("Arreglo original:", arreglo)
quicksort(arreglo, 0, len(arreglo) - 1)
print("Arreglo ordenado:", arreglo)
print()
print("------------------------------------------------")
print()
