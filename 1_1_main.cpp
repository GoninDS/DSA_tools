#include <iostream>
#include <chrono>
#include <random>
#include <algorithm>
#include <stdexcept>
#include "Ordenador.hpp" 

/**
 * @brief Genera un arreglo de números aleatorios.
 *
 * @param arr Puntero al arreglo de enteros que se va a llenar con números aleatorios.
 * @param n Tamaño del arreglo.
 * @param min Valor mínimo del rango de números aleatorios.
 * @param max Valor máximo del rango de números aleatorios.
 */
void generarNumerosAleatorios(int *arr, int n, int min, int max) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(min, max);

    for (int i = 0; i < n; ++i) {
        arr[i] = dis(gen);
    }
}

/**
 * @brief Verifica si un arreglo está ordenado.
 *
 * @param arr Puntero al arreglo de enteros que se va a verificar.
 * @param n Tamaño del arreglo.
 * @return true si el arreglo está ordenado, false en caso contrario.
 */
bool estaOrdenado(int *arr, int n) {
    return std::is_sorted(arr, arr + n);
}


/**
 * @brief prueba si el ordenamiento es correcto.
 *
 * Esta función toma un objeto Ordenador, un arreglo de enteros, su tamaño, 
 * un puntero a una función de ordenamiento miembro de Ordenador, y el nombre del método de ordenamiento.
 * Realiza una copia del arreglo, ejecuta el método de ordenamiento y mide el tiempo de ejecución.
 * Luego verifica si el arreglo está ordenado correctamente.
 *
 * @param ordenador Referencia al objeto Ordenador que contiene el método de ordenamiento.
 * @param arreglo Puntero al arreglo de enteros que se va a ordenar.
 * @param tamano Tamaño del arreglo.
 * @param funcionOrdenamiento Puntero a la función de ordenamiento miembro de Ordenador.
 * @param nombreMetodo Nombre del método de ordenamiento, usado para imprimir mensajes.
 */
void probarOrdenamiento(Ordenador& ordenador, int* arreglo, int tamano, 
                        void (Ordenador::*funcionOrdenamiento)(int*, int) const, const std::string& nombreMetodo) {
    int* copia = nullptr;
    try {
        copia = new int[tamano];
        std::copy(arreglo, arreglo + tamano, copia);

        auto inicio = std::chrono::high_resolution_clock::now();
        (ordenador.*funcionOrdenamiento)(copia, tamano); 
        auto fin = std::chrono::high_resolution_clock::now();

        if (!estaOrdenado(copia, tamano)) {
            std::cout << "Error: El " << nombreMetodo << " falló." << std::endl;
            std::cout << ordenador.datosDeTarea() << std::endl;
        } else {
            std::chrono::duration<double> duracion = fin - inicio;
            std::cout << "Tiempo de " << nombreMetodo << ": " << duracion.count() << " segundos" << std::endl;
        }
        delete[] copia;
    } catch (const std::exception& e) {
        std::cout << "Error en " << nombreMetodo << ": " << e.what() << std::endl;
        delete[] copia;
    }
}

/**
 * @brief realiza pruebas de básicas de programación defensivas en métodos de ordenamiento.
 *
 * Esta función prueba un método de ordenamiento con varios casos inválidos para asegurar que maneje
 * adecuadamente las entradas incorrectas. Los casos probados incluyen un tamaño negativo, un arreglo nulo,
 * y un tamaño de arreglo cero.
 *
 * @param ordenador Referencia al objeto Ordenador que contiene el método de ordenamiento.
 * @param funcionOrdenamiento Puntero a la función de ordenamiento miembro de Ordenador.
 * @param nombreMetodo Nombre del método de ordenamiento, usado para imprimir mensajes.
 */
void probarProgramacionDefensiva(Ordenador& ordenador, void (Ordenador::*funcionOrdenamiento)(int*, int) const, const std::string& nombreMetodo) {
    try {
        int arreglo[] = {0,0,0};
        int tamano = 3;
        try { // Prueba con n inválido (negativo)
            (ordenador.*funcionOrdenamiento)(arreglo, -5);
        } catch (const std::exception& e) {
            std::cout << "Error en " << nombreMetodo << " (n inválido): " << e.what() << std::endl;
            std::cout << ordenador.datosDeTarea() << std::endl;
        }

        try { // Prueba con arreglo nulo
            (ordenador.*funcionOrdenamiento)(nullptr, tamano);
        } catch (const std::exception& e) {
            std::cout << "Error en " << nombreMetodo << " (arreglo nulo): " << e.what() << std::endl;
            std::cout << ordenador.datosDeTarea() << std::endl;
        }

        try { // Prueba con tamaño cero
            (ordenador.*funcionOrdenamiento)(arreglo, 0);
        } catch (const std::exception& e) {
            std::cout << "Error en " << nombreMetodo << " (tamaño cero): " << e.what() << std::endl;
            std::cout << ordenador.datosDeTarea() << std::endl;
        }

    } catch (const std::exception& e) { // otra excepción inesperada
        std::cout << "Error inesperado en pruebas defensivas de " << nombreMetodo << ": " << e.what() << std::endl;
    }
}

int main() {
    constexpr int TAMANNO_ARREGLO = 10;

    int* arreglo = new int[TAMANNO_ARREGLO];
    generarNumerosAleatorios(arreglo, TAMANNO_ARREGLO, 1, 100000);

    Ordenador ordenador;
    std::cout << "-RESULTADOS DE PRUEBAS BÁSICA DE ORDENAMIENTO-" << std::endl;
    probarOrdenamiento(ordenador, arreglo, TAMANNO_ARREGLO, &Ordenador::ordenamientoPorInsercion, "ordenamiento por inserción");
    probarOrdenamiento(ordenador, arreglo, TAMANNO_ARREGLO, &Ordenador::ordenamientoPorSeleccion, "ordenamiento por selección");
    probarOrdenamiento(ordenador, arreglo, TAMANNO_ARREGLO, &Ordenador::ordenamientoPorMezcla, "ordenamiento por mezcla");

    std::cout << "-RESULTADOS DE PRUEBAS DE PROGRAMACIÓN DEFENSIVA-" << std::endl;
    probarProgramacionDefensiva(ordenador, &Ordenador::ordenamientoPorInsercion, "ordenamiento por inserción");
    probarProgramacionDefensiva(ordenador, &Ordenador::ordenamientoPorSeleccion, "ordenamiento por selección");
    probarProgramacionDefensiva(ordenador, &Ordenador::ordenamientoPorMezcla, "ordenamiento por mezcla");

    delete[] arreglo;

    return 0;
}
