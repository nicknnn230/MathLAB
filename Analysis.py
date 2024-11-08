import tkinter as tk
from sympy import symbols, diff, integrate, sympify, SympifyError, lambdify, limit, solve, simplify, Subs, oo
import matplotlib.pyplot as plt
import numpy as np


class analysis:

    def integrieren(self, function):
        x = symbols('x')

        try:

            expression_inte = sympify(function)

            integration = integrate(expression_inte, x)
            simplify(integration)
        except SympifyError:
            integration = "Ungültiger Ausdruck. Bitte gültige Funktion eingeben."

        return integration


    def bestimmt_integrieren(function, a, b):
        x = symbols('x')
        try:

            expression_inte = sympify(function)
            expression_a = sympify(a)
            expression_b = sympify(b)

            integration = integrate(expression_inte, x)

            simplify(integration)

            result_a = integration.subs(x, expression_a)
            result_b = integration.subs(x, expression_b)

            b_integration = result_b - result_a

        except SympifyError:
            b_integration = "Ungültiger Ausdruck. Bitte gültige Funktion eingeben oder Grenzen überprüfen."

        return b_integration
    
    def Nullstellen(self, function):
        x = symbols('x')

        try:

            expression_solve = sympify(function)

            nullstellen = solve(expression_solve, x)

        except SympifyError:
            nullstellen = "Ungültiger Ausdruck. Bitte gültige Funktion eingeben."

        return nullstellen
    
    def grenzwert(self, function, x0):
        x = symbols('x')

        try:
            expression_limit = sympify(function)

            grenzwert = limit(expression_limit, x, x0)

        except SympifyError:
            grenzwert = "Ungültiger Ausdruck. Bitte gültige Funktion eingeben."

        return grenzwert