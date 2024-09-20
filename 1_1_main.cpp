#include <iostream>
#include <chrono>
#include <random>
#include <algorithm>
#include <stdexcept>
#include "Ordenador.hpp" 

/**
 * @brief Genera un arreglo de números aleatorios.
 *
 * @param arreglo una referencia al vector de enteros que se va a llenar con números aleatorios.
 * @param min Valor mínimo del rango de números aleatorios.
 * @param max Valor máximo del rango de números aleatorios.
 */
void generarNumerosAleatorios(std::vector<int>& arreglo, int min, int max) {
    std::random_device randomDevice;
    std::mt19937 generator(randomDevice());
    std::uniform_int_distribution<> distribution(min, max);
    auto n = arreglo.size(); 
    for (auto i = 0; i < n; i++)
        arreglo[i] = distribution(generator);
}

/**
 * @brief prueba si el ordenamiento es correcto.
 *
 * @param ordenador Referencia al objeto Ordenador que contiene el método de ordenamiento.
 * @param arreglo referencia constante al vector de enteros al cual se le genera una copia y se ordena la copia.
 * @param funcionOrdenamiento Puntero a la función de ordenamiento miembro de Ordenador.
 * @param nombreMetodo Nombre del método de ordenamiento, usado para imprimir mensajes.
 */
void probarOrdenamiento(const Ordenador& ordenador, 
                        const std::vector<int>& arreglo,
                        void (Ordenador::*funcionOrdenamiento)(int*, int) const, 
                        const std::string& nombreMetodo) {
    std::vector<int> copia(arreglo.begin(), arreglo.end());
    int tamano = arreglo.size();
    try {

        auto inicio = std::chrono::high_resolution_clock::now();
        (ordenador.*funcionOrdenamiento)(copia.data(), tamano); 
        auto fin = std::chrono::high_resolution_clock::now();

        if (!std::is_sorted(copia.begin(),copia.end())) {
            std::cerr << "Error: El " << nombreMetodo << " falló." << std::endl;
            std::cerr << ordenador.datosDeTarea() << std::endl;
        } 

        std::chrono::duration<double> duracion = fin - inicio;
        std::cout << "Tiempo de " << nombreMetodo << ": " << duracion.count() << " segundos" << std::endl;
    
    } catch (const std::exception& e) {
        std::cerr << "Error en " << nombreMetodo << ": " << e.what() << std::endl;
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
void probarProgramacionDefensiva(const Ordenador& ordenador, void (Ordenador::*funcionOrdenamiento)(int*, int) const, const std::string& nombreMetodo) {
    try {
        int arreglo[] = {0,0,0};
        int tamano = 3;
        try { // Prueba con n inválido (negativo)
            (ordenador.*funcionOrdenamiento)(arreglo, -5);
        } catch (const std::exception& e) {
            std::cerr << "Error en " << nombreMetodo << " (n inválido): " << e.what() << std::endl;
            std::cerr << ordenador.datosDeTarea() << std::endl;
        }

        try { // Prueba con arreglo nulo
            (ordenador.*funcionOrdenamiento)(nullptr, tamano);
        } catch (const std::exception& e) {
            std::cerr << "Error en " << nombreMetodo << " (arreglo nulo): " << e.what() << std::endl;
            std::cerr << ordenador.datosDeTarea() << std::endl;
        }

        try { // Prueba con tamaño cero
            (ordenador.*funcionOrdenamiento)(arreglo, 0);
        } catch (const std::exception& e) {
            std::cerr << "Error en " << nombreMetodo << " (tamaño cero): " << e.what() << std::endl;
            std::cerr << ordenador.datosDeTarea() << std::endl;
        }

    } catch (const std::exception& e) { // otra excepción inesperada
        std::cerr << "Error inesperado en pruebas defensivas de " << nombreMetodo << ": " << e.what() << std::endl;
    }
}

int main() {
    constexpr int TAMANNO_ARREGLO = 10000;

    std::vector<int> arreglo(TAMANNO_ARREGLO, 0);
    generarNumerosAleatorios(arreglo, 1, 100000);

    Ordenador ordenador;
    std::cout << "-RESULTADOS DE PRUEBAS BÁSICA DE ORDENAMIENTO-" << std::endl;
    probarOrdenamiento(ordenador, arreglo, &Ordenador::ordenamientoPorInsercion, "ordenamiento por inserción");
    probarOrdenamiento(ordenador, arreglo, &Ordenador::ordenamientoPorSeleccion, "ordenamiento por selección");
    probarOrdenamiento(ordenador, arreglo, &Ordenador::ordenamientoPorMezcla, "ordenamiento por mezcla");

    std::cout << "-RESULTADOS DE PRUEBAS DE PROGRAMACIÓN DEFENSIVA-" << std::endl;
    probarProgramacionDefensiva(ordenador, &Ordenador::ordenamientoPorInsercion, "ordenamiento por inserción");
    probarProgramacionDefensiva(ordenador, &Ordenador::ordenamientoPorSeleccion, "ordenamiento por selección");
    probarProgramacionDefensiva(ordenador, &Ordenador::ordenamientoPorMezcla, "ordenamiento por mezcla");


    return 0;
}
