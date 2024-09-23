import numpy as np
import math

NIL = np.inf


def modulo_hash(k: int, m: int) -> int:
    """
    Calculate the modulo hash of a key.

    Parameters
    ----------
    k : int
        The key to hash.
    m : int
        The size of the hash table.

    Returns
    -------
    int
        The hash value of the key.
    """
    return k % m


def modulo_hash_with_jump(k: int, m: int) -> int:
    """
    Calculate the modulo hash of a key with an added jump.

    Parameters
    ----------
    k : int
        The key to hash.
    m : int
        The size of the hash table.

    Returns
    -------
    int
        The hash value of the key with an added jump.
    """
    return 2 + (k % (m - 2))


def quadratic_probing_hash(i: int, k: int, m: int, c1: int, c2: int) -> int:
    """
    Calculate the hash value using quadratic probing.

    Parameters
    ----------
    i : int
        The current iteration.
    k : int
        The key to hash.
    m : int
        The size of the hash table.
    c1 : int
        The first constant used in the quadratic probing formula.
    c2 : int
        The second constant used in the quadratic probing formula.

    Returns
    -------
    int
        The hash value calculated using quadratic probing.
    """
    return (modulo_hash(k, m) + c1 * i + c2 * pow(i, 2)) % m


def double_hashing(i: int, k: int, m: int) -> int:
    """
    Calculate the hash value using double hashing.

    Parameters
    ----------
    i : int
        The current iteration.
    k : int
        The key to hash.
    m : int
        The size of the hash table.

    Returns
    -------
    int
        The hash value calculated using double hashing.
    """
    return (modulo_hash(k, m) + i * modulo_hash_with_jump(k, m)) % m


def hash_insert(table: np.ndarray, k: int, hash_method: str, verbose: bool) -> int:
    """
    Insert a key into the hash table using the specified hash method.

    Parameters
    ----------
    table : np.ndarray
        The hash table.
    k : int
        The key to insert.
    hash_method : str
        The hash method to use ('double hash' or 'quadratic hash').
    verbose: bool
        whether to print where the element is inserted in the table
    Returns
    -------
    int
        The position where the key was inserted, or -1 if the table is full.
    """
    m: int = table.size
    if hash_method == "double hash":
        return insert_using_double_hashing(table, k, m, verbose)
    elif hash_method == "quadratic hash":
        return insert_using_quadratic_probing(table, k, m, verbose)


def insert_using_quadratic_probing(
    table: np.ndarray, k: int, m: int, verbose: bool
) -> int:
    """
    Insert a key into the hash table using quadratic probing.

    Parameters
    ----------
    table : np.ndarray
        The hash table.
    k : int
        The key to insert.
    m : int
        The size of the hash table.
    verbose: bool
        whether to print where the element is inserted in the table

    Returns
    -------
    int
        The position where the key was inserted, or -1 if the table is full.
    """
    c1: int = 2
    c2: int = 3
    i: int = 0
    while i != m:
        position = quadratic_probing_hash(i, k, m, c1, c2)
        if table[position] == NIL:
            if verbose:
                print(f"qh: element {k} inserted at {position} (had {i} collisions)")
            table[position] = k
            return position
        i += 1
    return -1


def insert_using_double_hashing(
    table: np.ndarray, k: int, m: int, verbose: bool
) -> int:
    """
    Insert a key into the hash table using double hashing.

    Parameters
    ----------
    table : np.ndarray
        The hash table.
    k : int
        The key to insert.
    m : int
        The size of the hash table.
    verbose: bool
        whether to print where the element is inserted in the table

    Returns
    -------
    int
        The position where the key was inserted, or -1 if the table is full.
    """
    i: int = 0
    while i != m:
        position = double_hashing(i, k, m)
        if table[position] == NIL:
            if verbose:
                print(f"dh: element {k} inserted at {position} (had {i} collisions)")
            table[position] = k
            return position
        i += 1
    return -1


def print_hash_table(table: np.ndarray) -> None:
    """
    Print the hash table, printing the empty spaces of the table as nil.

    Parameters
    ----------
    table : np.ndarray
        The hash table.

    Returns
    -------
    None
    """
    print("[", end="")
    for index in range(table.size - 1):
        if table[index] == NIL:
            print("NIL, ", end="")
        else:
            print(f"{table[index]}, ", end="")

    if table[table.size - 1] == NIL:
        print("NIL]")
    else:
        print(f"{table[index]}]")


def main() -> None:

    elements = [37, 36, 33, 3, 15, 35, 10]
    hash_table_quadratic_hash = np.full(10, NIL)
    hash_table_double_hash = np.full(10, NIL)
    for element in elements:
        hash_insert(hash_table_double_hash, element, "double hash", verbose=True)

    print("hash table dh:")
    print_hash_table(table=hash_table_double_hash)
    # I put them in two different loops to see better the prints
    for element in elements:
        hash_insert(hash_table_quadratic_hash, element, "quadratic hash", verbose=True)
    print("hash table qh:")
    print_hash_table(table=hash_table_quadratic_hash)


if __name__ == "__main__":
    main()
