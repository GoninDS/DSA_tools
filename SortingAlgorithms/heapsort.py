def es_monticulo_maximo(A, i, n):
    """
    Verifica si un árbol binario es un montículo máximo.
    el árbol es representado por un arreglo A de tamaño n.
    """
    # recordemos el caso base: si el nodo i es una hoja, entonces es un montículo Máximo
    if 2 * i + 2 > n:
        return True
    # ahora, verificamos si el nodo i cumple con la propiedad de montículo máximo
    # es decir, si el nodo i es mayor o igual a sus hijos, su hijo izquierdo es el nodo 2*i+1 y el hijo derecho es el nodo 2*i+2
    izquierda_ok = A[i] >= A[2 * i + 1] and es_monticulo_maximo(A, 2 * i + 1, n)

    derecha_ok = (2 * i + 2 == n) or (
        A[i] >= A[2 * i + 2] and es_monticulo_maximo(A, 2 * i + 2, n)
    )

    return izquierda_ok and derecha_ok


def revisar_monticulo_maximo(A):
    if es_monticulo_maximo(A, 0, len(A)):
        print("Sí, es un montículo máximo")
    else:
        print("No, no es un montículo máximo")


def izquierda(i):
    """
    Calcula el índice del hijo izquierdo de un nodo en un árbol binario.

    Args:
        i (int): Índice del nodo padre.

    Returns:
        int: Índice del hijo izquierdo.
    """
    return 2 * i + 1


def derecha(i):
    """
    Calcula el índice del hijo derecho de un nodo en un árbol binario.

    Args:
        i (int): Índice del nodo padre.

    Returns:
        int: Índice del hijo derecho.
    """
    return 2 * i + 2


def padre(i):
    """
    Calcula el índice del padre de un nodo en un árbol binario.

    Args:
        i (int): Índice del nodo hijo.

    Returns:
        int: Índice del nodo padre.
    """
    return i // 2


def intercambiar(A, i, j):
    """
    Intercambia dos elementos en un arreglo.

    Args:
        A (list): Arreglo de elementos.
        i (int): Índice del primer elemento.
        j (int): Índice del segundo elemento.
    """
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def monticularizar(A, n):
    """
    Convierte un arreglo en un montículo máximo.

    Args:
        A (list): Arreglo de elementos.
        n (int): Tamaño del arreglo.
    """
    tamaño_del_monticulo = n
    print("Arreglo original: ", A)
    print()

    # Construir el montículo máximo desde la mitad del arreglo hacia abajo.
    for i in range((n // 2) - 1, -1, -1):
        corregir_cima(A, i, tamaño_del_monticulo)
        print("Iteración ", n // 2 - i, ":\n", A, "después de corregir cima\n")
        print()


def corregir_cima(A, i, tamano_del_monticulo):
    """
    Restaura la propiedad de montículo máximo en un subárbol.

    Args:
        A (list): Arreglo de elementos.
        i (int): Índice del nodo raíz del subárbol.
        tamano_del_monticulo (int): Tamaño del montículo actual.
    """
    izquierdo = izquierda(i)
    derecho = derecha(i)
    maximo = i

    # Encontrar el nodo con el mayor valor entre el nodo actual y sus hijos.
    if izquierdo < tamano_del_monticulo and A[izquierdo] > A[maximo]:
        maximo = izquierdo
    if derecho < tamano_del_monticulo and A[derecho] > A[maximo]:
        maximo = derecho

    # Si el nodo actual no es el mayor, intercambiarlo con el mayor y
    # corregir recursivamente el subárbol correspondiente.
    if maximo != i:
        intercambiar(A, i, maximo)
        corregir_cima(A, maximo, tamano_del_monticulo)


def ordenamiento_por_monticulos(A):
    """
    Ordena un arreglo usando el algoritmo de ordenamiento por montículos.

    Args:
        A (list): Arreglo de elementos.

    Returns:
        list: Arreglo ordenado.
    """
    n = len(A)
    monticularizar(A, n)

    # Ordenar el arreglo intercambiando el elemento raíz con el último
    # elemento y luego corrigiendo el montículo restante.
    for i in range(n - 1, 0, -1):
        intercambiar(A, 0, i)
        corregir_cima(A, 0, i)
        print("Iteración ordenamiento ", n - i, ":\n", A, "después de corregir cima\n")

    return A


if __name__ == "__main__":
    arreglo = [6, 4, 9, 1, 7, 9, 5, 8, 10, 2]
    arreglo_2 = [13, 12, 13, 11, 7, 5, 6, 4, 3, 5]
    revisar_monticulo_maximo(arreglo)
    revisar_monticulo_maximo(arreglo_2)

    arreglo = [12, 13, 5, 6, 14, 10, 2, 8]
    monticularizar(arreglo, len(arreglo))
    arreglo = [12, 13, 5, 6, 14, 10, 2, 8]
    print("Arreglo ordenado: ", ordenamiento_por_monticulos(arreglo))
    print("----------------------------------------")
    arreglo = [1, 6, 4, 12, 7, 10, 8, 13]
    monticularizar(arreglo, len(arreglo))
    arreglo = [1, 6, 4, 12, 7, 10, 8, 13]
    print("Arreglo ordenado: ", ordenamiento_por_monticulos(arreglo))
