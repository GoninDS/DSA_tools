#include <algorithm>
#include <chrono>
#include <csignal>
#include <iostream>
#include <random>
#include <stdexcept>

#include "Ordenador.hpp"

Ordenador ordenador;

/**
 * @brief Genera un arreglo de números aleatorios.
 *
 * @param arreglo una referencia al vector de enteros que se va a llenar con
 * números aleatorios.
 * @param min Valor mínimo del rango de números aleatorios.
 * @param max Valor máximo del rango de números aleatorios.
 */
void generarNumerosAleatorios(std::vector<int> &arreglo, int min, int max) {
  std::random_device dispositivoAleatorio;
  std::mt19937 generador(dispositivoAleatorio());
  std::uniform_int_distribution<> distribucion(min, max);
  auto n = arreglo.size();
  for (auto i = 0; i < n; i++) arreglo[i] = distribucion(generador);
}

/**
 * @brief prueba si el ordenamiento es correcto.
 *
 * @param ordenador Referencia al objeto Ordenador que contiene el método de
 * ordenamiento.
 * @param arreglo referencia constante al vector de enteros al cual se le genera
 * una copia y se ordena la copia.
 * @param funcionOrdenamiento Puntero a la función de ordenamiento miembro de
 * Ordenador.
 * @param nombreMetodo Nombre del método de ordenamiento, usado para imprimir
 * mensajes.
 */
void probarOrdenamiento(const Ordenador &ordenador,
                        const std::vector<int> &arreglo,
                        void (Ordenador::*funcionOrdenamiento)(int *, int)
                            const,
                        const std::string &nombreMetodo) {
  std::vector<int> copia(arreglo.begin(), arreglo.end());
  int tamano = arreglo.size();
  try {
    auto inicio = std::chrono::high_resolution_clock::now();
    (ordenador.*funcionOrdenamiento)(copia.data(), tamano);
    auto fin = std::chrono::high_resolution_clock::now();

    if (!std::is_sorted(copia.begin(), copia.end())) {
      std::cerr << "Error: El " << nombreMetodo << " falló." << std::endl;
      std::cerr << ordenador.datosDeTarea() << std::endl;
    }

    std::chrono::duration<double> duracion = fin - inicio;
    std::cout << "Tiempo de " << nombreMetodo << ": " << duracion.count()
              << " segundos" << std::endl;
  } catch (const std::exception &e) {
    std::cerr << "Error en " << nombreMetodo << ": " << e.what() << std::endl;
  }
}
/**
 * @brief Manejador de señales para errores críticos.
 *
 * Esta función maneja señales críticas como SIGABRT, SIGSEGV, SIGILL y SIGFPE.
 * Imprime un mensaje de error y los datos de la tarea del ordenador antes de
 * finalizar el programa.
 *
 * @param sennal La señal recibida.
 */
void manejarSennales(int sennal) {
  if (sennal == SIGABRT || sennal == SIGSEGV || sennal == SIGILL ||
      sennal == SIGFPE) {
    std::cerr
        << "Error crítico detectado durante el ordenamiento. Posible causa: ";

    switch (sennal) {
      case SIGABRT:
        std::cerr << "Llamada a abort()";
        break;
      case SIGSEGV:
        std::cerr << "Violación de segmento (acceso inválido a memoria)";
        break;
      case SIGILL:
        std::cerr << "Instrucción ilegal";
        break;
      case SIGFPE:
        std::cerr << "Error de punto flotante (división por cero, etc.)";
        break;
      default:
        std::cerr << "Señal desconocida";
    }

    std::cerr << std::endl;
    std::cerr << ordenador.datosDeTarea() << std::endl;
    exit(1);
  }
}

/**
 * @brief Función para realizar pruebas defensivas en métodos de ordenamiento.
 *
 * Esta función prueba un método de ordenamiento con varios casos inválidos para
 * asegurar que maneje adecuadamente las entradas incorrectas. Los casos
 * probados incluyen un tamaño negativo, un arreglo nulo, y un tamaño de arreglo
 * cero.
 *
 * @param ordenador Referencia constante al objeto Ordenador que contiene el
 * método de ordenamiento.
 * @param funcionOrdenamiento Puntero a la función de ordenamiento miembro de
 * Ordenador.
 * @param nombreMetodo Nombre del método de ordenamiento, usado para imprimir
 * mensajes.
 */
void probarProgramacionDefensiva(const Ordenador &ordenador,
                                 void (Ordenador::*funcionOrdenamiento)(int *,
                                                                        int)
                                     const,
                                 const std::string &nombreMetodo) {
  signal(SIGABRT, manejarSennales);
  signal(SIGSEGV, manejarSennales);
  signal(SIGILL, manejarSennales);
  signal(SIGFPE, manejarSennales);

  int arreglo[] = {0, 0, 0};
  int tamano = 3;
  std::cout << "----Realizando Pruebas defensivas sobre " << nombreMetodo
            << "----" << std::endl;

  std::cout << "- Probando con n negativo..." << std::endl;
  (ordenador.*funcionOrdenamiento)(arreglo, -5);
  std::cout << "✓ Pasa prueba de n negativo." << std::endl;

  std::cout << "- Probando con puntero nulo..." << std::endl;
  (ordenador.*funcionOrdenamiento)(nullptr, tamano);
  std::cout << "✓ Pasa prueba de A puntero nulo." << std::endl;

  std::cout << "- Probando con n cero..." << std::endl;
  (ordenador.*funcionOrdenamiento)(arreglo, 0);
  std::cout << "✓ Pasa prueba de n cero." << std::endl;

  std::cout << "---- ✓ Pruebas defensivas sobre " << nombreMetodo
            << " completadas sin errores.----" << std::endl;
}

int main() {
  constexpr int TAMANNO_ARREGLO = 10000;

  std::vector<int> arreglo(TAMANNO_ARREGLO, 0);
  generarNumerosAleatorios(arreglo, 1, 100000);

  std::cout << "-RESULTADOS DE PRUEBAS BÁSICA DE ORDENAMIENTO-" << std::endl;
  probarOrdenamiento(ordenador, arreglo, &Ordenador::ordenamientoPorInsercion,
                     "ORDENAMIENTO POR INSERCIÓN");
  probarOrdenamiento(ordenador, arreglo, &Ordenador::ordenamientoPorSeleccion,
                     "ORDENAMIENTO POR SELECCIÓN");
  probarOrdenamiento(ordenador, arreglo, &Ordenador::ordenamientoPorMezcla,
                     "ORDENAMIENTO POR MEZCLA");

  std::cout << std::endl;

  std::cout << "-RESULTADOS DE PRUEBAS DE PROGRAMACIÓN DEFENSIVA-" << std::endl;
  probarProgramacionDefensiva(ordenador, &Ordenador::ordenamientoPorInsercion,
                              "ORDENAMIENTO POR INSERCIÓN");
  probarProgramacionDefensiva(ordenador, &Ordenador::ordenamientoPorSeleccion,
                              "ORDENAMIENTO POR SELECCIÓN");
  probarProgramacionDefensiva(ordenador, &Ordenador::ordenamientoPorMezcla,
                              "ORDENAMIENTO POR MEZCLA");

  return 0;
}
