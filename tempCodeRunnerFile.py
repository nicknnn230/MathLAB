
        expression_inte = sympify(function)

        integration = integrate(expression_inte, x)
        simplify(integration)
    except SympifyError:
        integration = "Ungültiger Ausdruck. Bitte gültige Funktion eingeben."