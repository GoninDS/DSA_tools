#include <iostream>
#include <chrono>
#include <random>
#include <algorithm>
#include "Ordenador.hpp" 

void generarNumerosAleatorios(int *arr, int n, int min, int max) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(min, max);

    for (int i = 0; i < n; ++i) {
        arr[i] = dis(gen);
    }
}

bool estaOrdenado(int *arr, int n) {
    return std::is_sorted(arr, arr + n);
}

int main() {
    const int TAMANNO_ARREGLO = 100000; 
    int arreglo[TAMANNO_ARREGLO];

    // Generar números aleatorios en el arreglo
    generarNumerosAleatorios(arreglo, TAMANNO_ARREGLO, 1, 100000);

    Ordenador ordenador;

    //--------------------Prueba de ordenamiento por inserción---------------------------
    int copiaInsercion[TAMANNO_ARREGLO];
    std::copy(std::begin(arreglo), std::end(arreglo), std::begin(copiaInsercion)); 

    auto inicioInsercion = std::chrono::high_resolution_clock::now();
    ordenador.ordenamientoPorInsercion(copiaInsercion, TAMANNO_ARREGLO);
    auto finInsercion = std::chrono::high_resolution_clock::now();

    if (!estaOrdenado(copiaInsercion, TAMANNO_ARREGLO)) {
        std::cout << ordenador.datosDeTarea() << std::endl;
    }

    std::chrono::duration<double> duracionInsercion = finInsercion - inicioInsercion;
    std::cout << "Tiempo de ordenamiento por inserción: " << duracionInsercion.count() << " segundos" << std::endl;

    //-------------------------Prueba de ordenamiento por selección------------------------
    int copiaSeleccion[TAMANNO_ARREGLO];
    std::copy(std::begin(arreglo), std::end(arreglo), std::begin(copiaSeleccion)); 

    auto inicioSeleccion = std::chrono::high_resolution_clock::now();
    ordenador.ordenamientoPorSeleccion(copiaSeleccion, TAMANNO_ARREGLO);
    auto finSeleccion = std::chrono::high_resolution_clock::now();

    if (!estaOrdenado(copiaSeleccion, TAMANNO_ARREGLO)) {
        std::cout << ordenador.datosDeTarea() << std::endl;
    }

    std::chrono::duration<double> duracionSeleccion = finSeleccion - inicioSeleccion;
    std::cout << "Tiempo de ordenamiento por selección: " << duracionSeleccion.count() << " segundos" << std::endl;

    // --------------------- Prueba de ordenamiento por mezcla---------------------------------
    int copiaMezcla[TAMANNO_ARREGLO];
    std::copy(std::begin(arreglo), std::end(arreglo), std::begin(copiaMezcla));

    auto inicioMezcla = std::chrono::high_resolution_clock::now();
    ordenador.ordenamientoPorMezcla(copiaMezcla, TAMANNO_ARREGLO);
    auto finMezcla = std::chrono::high_resolution_clock::now();

    if (!estaOrdenado(copiaMezcla, TAMANNO_ARREGLO)) {
        std::cout << ordenador.datosDeTarea() << std::endl;
    }

    std::chrono::duration<double> duracionMezcla = finMezcla - inicioMezcla;
    std::cout << "Tiempo de ordenamiento por mezcla: " << duracionMezcla.count() << " segundos" << std::endl;

    return 0;
}
