def es_monticulo_maximo(arreglo: list, i: int, n: int) -> bool:
    """Verifica si un árbol binario es un montículo máximo.

    parámetros:
    -----------
    - arreglo: lista de elementos. A en el pseudocódigo.
    - i: índice del nodo raíz del subárbol.
         Equivale a i en el pseudocódigo.
    - n: tamaño del montículo.

    retorna:
    --------
    - bool: True si el árbol es un montículo máximo, False en caso contrario.
    """
    # recordemos el caso base: si el nodo i es una hoja, entonces es un montículo
    # Máximo
    if 2 * i + 2 > n:
        return True
    # ahora, verificamos si el nodo i cumple con la propiedad de montículo máximo
    # es decir, si el nodo i es mayor o igual a sus hijos, su hijo izquierdo
    # es el nodo 2*i+1 y el hijo derecho es el nodo 2*i+2
    izquierda_ok = arreglo[i] >= arreglo[2 * i + 1] and es_monticulo_maximo(
        arreglo, 2 * i + 1, n
    )

    derecha_ok = (2 * i + 2 == n) or (
        arreglo[i] >= arreglo[2 * i + 2]
        and es_monticulo_maximo(arreglo, 2 * i + 2, n)
    )

    return izquierda_ok and derecha_ok


def revisar_monticulo_maximo(arreglo: list) -> None:
    if es_monticulo_maximo(arreglo, 0, len(arreglo)):
        print("Sí, es un montículo máximo")
    else:
        print("No, no es un montículo máximo")


def izquierda(i: int) -> int:
    """Calcula el índice del hijo izquierdo de un nodo en un árbol binario.

    parámetros:
    ----------
    - i (int): Índice del nodo padre.

    retorna:
    --------
    - int: Índice del hijo izquierdo.
    """
    return 2 * i + 1


def derecha(i: int) -> int:
    """Calcula el índice del hijo derecho de un nodo en un árbol binario.

    parámetros:
    ----------
    - i (int): Índice del nodo padre.

    retorna:
    --------
    - int: Índice del hijo derecho.
    """
    return 2 * i + 2


def padre(i: int) -> int:
    """Calcula el índice del padre de un nodo en un árbol binario.

    parámetros:
    ----------
    - i (int): Índice del nodo hijo.

    retorna:
    --------
    - int: Índice del nodo padre.
    """
    return i // 2


def intercambiar(arreglo: list, i: int, j: int) -> None:
    """Intercambia dos elementos en un arreglo.

    parámetros:
    ----------
    - arreglo (list): Arreglo de elementos. A en el pseudocódigo.
    - i (int): Índice del primer elemento.
    - j (int): Índice del segundo elemento.
    """
    temp = arreglo[i]
    arreglo[i] = arreglo[j]
    arreglo[j] = temp


def monticularizar(arreglo: list, n: int) -> None:
    """Convierte un arreglo en un montículo máximo.

    parámetros:
    ----------
    - arreglo (list): Arreglo de elementos. A en el pseudocódigo.
    - n (int): Tamaño del arreglo.
    """
    tamanno_monticulo = n
    print("Arreglo original: ", arreglo)
    print()

    # Construir el montículo máximo desde la mitad del arreglo hacia abajo.
    for i in range((n // 2) - 1, -1, -1):
        corregir_cima(arreglo, i, tamanno_monticulo)
        print("Iteración ", n // 2 - i, ":\n", arreglo, "después de corregir cima\n")
        print()


def corregir_cima(arreglo: list, i: int, tamano_del_monticulo: int) -> None:
    """Restaura la propiedad de montículo máximo en un subárbol.

    parámetros:
    ----------
    - arreglo (list): Arreglo de elementos. A en el pseudocódigo.
    - i (int): Índice del nodo raíz del subárbol.
    - tamano_del_monticulo (int): Tamaño del montículo actual.
    """
    izquierdo = izquierda(i)
    derecho = derecha(i)
    maximo = i

    # Encontrar el nodo con el mayor valor entre el nodo actual y sus hijos.
    if izquierdo < tamano_del_monticulo and arreglo[izquierdo] > arreglo[maximo]:
        maximo = izquierdo
    if derecho < tamano_del_monticulo and arreglo[derecho] > arreglo[maximo]:
        maximo = derecho

    # Si el nodo actual no es el mayor, intercambiarlo con el mayor y
    # corregir recursivamente el subárbol correspondiente.
    if maximo != i:
        intercambiar(arreglo, i, maximo)
        corregir_cima(arreglo, maximo, tamano_del_monticulo)


def ordenamiento_por_monticulos(arreglo: list) -> list:
    """Ordena un arreglo usando el algoritmo de ordenamiento por montículos.

    parámetros:
    ----------
    - arreglo (list): Arreglo de elementos. A en el pseudocódigo.

    retorna:
    --------
        list: Arreglo ordenado.
    """
    n = len(arreglo)
    print("---Monticularizando---")
    monticularizar(arreglo, n)
    print("---Monticularizado---\n")

    # Ordenar el arreglo intercambiando el elemento raíz con el último
    # elemento y luego corrigiendo el montículo restante.
    print("---Ordenando---")
    for i in range(n - 1, 0, -1):
        intercambiar(arreglo, 0, i)
        corregir_cima(arreglo, 0, i)
        print(
            f"Iteración ordenamiento {n - i}:"
            f"\n{arreglo} después de corregir cima\n",
        )
    print("---Ordenado---")
    return arreglo


if __name__ == "__main__":
    arreglo = [8, 6, 2, 3, 9, 11, 7, 10, 12, 4]
    revisar_monticulo_maximo(arreglo)

    arreglo = [1, 6, 4, 12, 7, 10, 8, 13]
    print("Arreglo ordenado: ", ordenamiento_por_monticulos(arreglo))
