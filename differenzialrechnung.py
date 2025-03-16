import tkinter as tk
from sympy import symbols, diff, integrate, sympify, SympifyError, lambdify, limit, solve, simplify, Subs, oo
import matplotlib.pyplot as plt
import numpy as np

class differenzialrechnung:

    def differenzieren(self, function):
        x = symbols('x')
        try:

            expression_diff = sympify(function)

            differentiation = diff(expression_diff, x)
            simplify(differentiation)

        except SympifyError:
            differentiation = "Ungültiger Ausdruck. Bitte gültige Funktion eingeben."

        return differentiation

    def tangente(self, function, x0):
        x = symbols('x')

        sympify_function = sympify(function)

        function_1_tangente = sympify_function
        function_2_tangente = self.differenzieren(sympify_function)

        result_function_1_tangente = function_1_tangente.subs(x, x0)
        result_function_2_tangente = function_2_tangente.subs(x, x0)

        tangente = result_function_2_tangente * (x-x0) + result_function_1_tangente
        simplify(tangente)


        return tangente

    def normale(self, function, x0):
        x = symbols('x')

        sympify_function = sympify(function)

        function_1_tangente = sympify_function
        function_2_tangente = self.differenzieren(sympify_function)

        result_function_1_tangente = function_1_tangente.subs(x, x0)
        result_function_2_tangente = function_2_tangente.subs(x, x0)

        normale = -1/(result_function_2_tangente) * (x-x0) + result_function_1_tangente
        simplify(normale)


        return normale
