# One line to give the program's name and a brief description.
# Copyright © 2022 TrinityXel

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

from sys import stdout
import asyncio
from functools import cache
from typing import Generator


class Fibonacci(object):
    """
    File: classFibonacci.py
    Author: TrinityXel
    Email: halrinachs@gmail.com
    Github: https://github.com/TrinityXel
    Description:
    """

    def __init__(self, func, chunk: int = 80, file: str = "stdout"):
        """Description

        @param func:    Función interna o externa para calcular el número
                        de Fibonacci. Internamente  hay 3:
                            get_fibonacci_number_by_formula
                            get_fibonacci_number_by_iter
                            get_fibonacci_number_by_iter_cached
                        Se debe definir en la construcción.

        @param chunk:   Tamaño máximo del buffer antes de imprimirlo
        @type  int      Opcional, default = 80

        @param file:    Archivo en el cual se imprimirá la salida,
                        dejar sin modificar o poner stdout para imprimirlo
                        en la terminal
                        Opcional, default = stdout
        """
        self._filept: str = file
        self._chunk: int = chunk
        self.function_get_number = func

    @staticmethod
    def get_fibonacci_number_by_formula(numero: int) -> int:
        """
        Primera función para generar el número de Fibonacci
        Esta limitada al tamaño maximo del tipo int, en mi caso no
        calculará mas del número 600, se puede mejorar con modulos externos
        pero para fin demostrativo cumple

        Formula: Fn = ( (1 + √5)^n - (1 - √5)^n ) / (2^n × √5)

        TODO: simplificarla a Fn = [( (1 + √5)^n ) / (2^n × √5)]

        Rápida evaluación

        @param numero:  Número a calcular
        @type  int:

        @return:  Regresa el número de Fibonacci convertido de float a int
        @rtype :  int

        @raise e: Debe generar el error al sobrepasar el tamaño limite
        """

        fibonacci = ((1 + 5**(0.5))**numero - (1 - 5**(0.5))
                     ** numero) / (2**numero * 5**(0.5))
        return int(fibonacci)

    @staticmethod
    def get_fibonacci_number_by_iter(numero: int) -> int:
        """
        Segunda función para generar el número de Fibonacci, la clásica,
        forma recursiva. Recorre todos los números anteriores al número,
        no tiene cache, por lo que será muy lenta

        @param numero:  Número a calcular
        @type  int:

        @return:  Regresa el número de Fibonacci convertido de float a int
        @rtype :  int
        """
        if numero <= 1:
            return 1

        fun = Fibonacci.get_fibonacci_number_by_iter
        fibonacci = fun(numero - 1) + fun(numero - 2)

        return fibonacci

    @staticmethod
    @cache
    def get_fibonacci_number_by_iter_cached(numero: int) -> int:
        """
        Tercera función para generar el número de Fibonacci. Esta es la
        versión clásica pero con un cache implementado por el modulo
        functools, es la más rápida y eficiente implementada aca.

        @param numero:  Número a calcular
        @type  int:

        @return:  Regresa el número de Fibonacci convertido de float a int
        @rtype :  int
        """
        if numero <= 1:
            return 1

        fun = Fibonacci.get_fibonacci_number_by_iter_cached
        fibonacci = fun(numero - 1) + fun(numero - 2)

        return fibonacci

    def __fibonacci_generador(self, itero: int) -> Generator:

        fibonacci = 0
        funcion = self.function_get_number

        for numero in range(itero):
            yield fibonacci
            fibonacci = funcion(numero)

    def fibonacci_escribir_sec(self, limite: int):

        archivo = stdout if self._filept == "stdout" else open(
            self._filept, "at")

        cadena: str = ""
        avanze = 0
        generador = self.__fibonacci_generador(limite)
        try:
            for numero in generador:
                if len(cadena) >= self._chunk:
                    cadena += "\n"
                    archivo.write(cadena)
                    cadena = ""
                cadena += f"{numero:,} "
                avanze += 1
                self.update_progress(avanze/limite)

        finally:
            archivo.write(cadena)
            archivo.close()

    def update_progress(self, progress):
        barLength = 20  # Tamaño de la barra de progreso
        status = ""
        if isinstance(progress, int):
            progress = float(progress)
        if not isinstance(progress, float):
            progress = 0
            status = "Error: el valor debe ser tipo float\r\n"
        if progress < 0:
            progress = 0
            status = "Esperando...\r\n"
        if progress >= 1:
            progress = 1
            status = "Hecho...\r\n"
        block = int(round(barLength*progress))
        text = "\rCalculando: [{0}] {1:.2f}% {2}".format(
            "▓"*block + "-"*(barLength-block), progress*100, status)
        stdout.write(text)
        stdout.flush()
