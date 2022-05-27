# One line to give the program's name and a brief description.
# Copyright © 2022 yourname

# This library is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, see <http://www.gnu.org/licenses/>.
from classFibonacci import Fibonacci


def main():
    """docstring for ma"""

    # Declaramos que funcion queremos usar para calcular
    funcion = Fibonacci.get_fibonacci_number_by_formula

    # Creamos la instancia y definimos sus parametros
    fibo = Fibonacci(func=funcion,          # Funcion que usaremos
                     file="fibonacci.txt",  # Archivo donde guardaremos
                     chunk=1)               # Uno por linea

    # Para efectos de prueba, calcular el millon, al 10% tenia un archivo
    # de 900 mb, usando get_fibonacci_number_by_iter_cached
    # fibo.fibonacci_escribir_sec(1000000)

    fibo.fibonacci_escribir_sec(600)

    # Ejemplo de como calcular con las funciones estaticas de la clase
    print(Fibonacci.get_fibonacci_number_by_iter(40))


if __name__ == "__main__":
    main()
