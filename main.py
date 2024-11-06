import tkinter as tk
from sympy import symbols, diff, integrate, sympify, SympifyError, lambdify, limit, solve, simplify, Subs
import matplotlib.pyplot as plt
import numpy as np


x = symbols('x')

def ableiten():
    global diff_label


    function = e1.get()
    try:

        expression_diff = sympify(function)

        differentiation = diff(expression_diff, x)
        simplify(differentiation)
    except SympifyError:
        differentiation = "Ungültiger Ausdruck. Bitte gültige Funktion eingeben."


    if diff_label is None:

        diff_label = tk.Label(root, text=f"1. Ableitung von f(x):               {differentiation}")
        diff_label.grid(row=1, column=0, columnspan=2, sticky="w")
    else:

        diff_label.config(text=f"1. Ableitung von f(x):             {differentiation}")




def integrieren():
    global integrate_label

    

    function = e1.get()
    try:

        expression_inte = sympify(function)

        integration = integrate(expression_inte, x)
        simplify(integration)
    except SympifyError:
        integration = "Ungültiger Ausdruck. Bitte gültige Funktion eingeben."

    if integration != "Ungültiger Ausdruck. Bitte gültige Funktion eingeben.":
        if integrate_label is None:

            integrate_label = tk.Label(root, text=f"Stammfunktion von f(x):             {integration} + c")
            integrate_label.grid(row=2, column=0, columnspan=2, sticky="w")
        else:

            integrate_label.config(text=f"Stammfunktion von f(x):               {integration} + c")
    else:
        if integrate_label is None:

            integrate_label = tk.Label(root, text=f"Stammfunktion von f(x):             {integration}")
            integrate_label.grid(row=2, column=0, columnspan=2, sticky="w")
        else:

            integrate_label.config(text=f"Stammfunktion von f(x):               {integration}")


def open_window():
    global e1_a
    global e2_b


    bestimmt_integrieren_window = tk.Toplevel(root)
    bestimmt_integrieren_window.title("Bestimmte Integration")
    bestimmt_integrieren_window.geometry("300x200")

    w = tk.Label(bestimmt_integrieren_window, text="Grenzen der bestimmten Integration von f(x)")
    w.grid(row=0, column=0)

    tk.Label(bestimmt_integrieren_window, text="a =").grid(row=1, column=0, sticky="w")
    e1_a = tk.Entry(bestimmt_integrieren_window)
    e1_a.grid(row=1, column=0, sticky="w", padx=25, pady=5)

    tk.Label(bestimmt_integrieren_window, text="b =").grid(row=2, column=0, sticky="w")
    e2_b = tk.Entry(bestimmt_integrieren_window)
    e2_b.grid(row=2, column=0, sticky="w", padx=25, pady=5)

    button_integrieren = tk.Button(bestimmt_integrieren_window, text='ausführen', command=bestimmt_integrieren)
    button_integrieren.grid(row=3, column=0, sticky="w", padx=25, pady=5)


def bestimmt_integrieren():
    global bestimmt_integrieren_label
    global e1_a
    global e2_b
    

    a = e1_a.get()
    b = e2_b.get()
    function = e1.get()

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


    if bestimmt_integrieren_label is None:

        bestimmt_integrieren_label = tk.Label(root, text=f"Bestimmte Integration von {expression_a} bis {expression_b}:             {b_integration}")
        bestimmt_integrieren_label.grid(row=3, column=0, columnspan=2, sticky="w")
    else:

        bestimmt_integrieren_label.config(text=f"Bestimmte Integration von {expression_a} bis {expression_b}:               {b_integration}")    

    

def Nullstellen():
    global solve_label
    function = e1.get()
    try:

        expression_solve = sympify(function)

        nullstellen = solve(expression_solve, x)

    except SympifyError:
        nullstellen = "Ungültiger Ausdruck. Bitte gültige Funktion eingeben."


    if solve_label is None:

        solve_label = tk.Label(root, text=f"Nullstellen von f(x):               {nullstellen}")
        solve_label.grid(row=4, column=0, columnspan=2, sticky="w")
    else:

        solve_label.config(text=f"Nullstellen von f(x):             {nullstellen}")   

def limes_window():
    global e1_limes


    limes_window = tk.Toplevel(root)
    limes_window.title("Limes")
    limes_window.geometry("300x80")

    tk.Label(limes_window, text="x ->").grid(row=1, column=0, sticky="w")
    e1_limes = tk.Entry(limes_window)
    e1_limes.grid(row=1, column=0, sticky="w", padx=25, pady=5)

    button_limes = tk.Button(limes_window, text='ausführen', command=limes)
    button_limes.grid(row=3, column=0, sticky="w", padx=25, pady=5)

def limes():
    global limit_label
    global e1_limes

    lim = e1_limes.get()

    function = e1.get()

    try:

        expression_limit = sympify(function)

        grenzwert = limit(expression_limit, x, lim)

    except SympifyError:
        grenzwert = "Ungültiger Ausdruck. Bitte gültige Funktion eingeben."



    if limit_label is None:

        limit_label = tk.Label(root, text=f"lim(x->{lim}):              {grenzwert}")
        limit_label.grid(row=5, column=0, columnspan=2, sticky="w")
    else:

        limit_label.config(text=f"lim(x->{lim}):              {grenzwert}")


def plotten():
    function = e1.get()

    f_lambda = lambdify(x, function, 'numpy')

    x_vals = np.linspace(-50, 50, 500)
    y_vals = f_lambda(x_vals)


    plt.plot(x_vals, y_vals, label = str(function), color='blue')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph der Funktion f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()



root = tk.Tk()
root.geometry('900x700')
root.title('MathLAB')


menu = tk.Menu(root)

analysis_menu = tk.Menu(menu, tearoff=0)
analysis_menu.add_command(label='Ableiten', command=ableiten)
diff_label = None
analysis_menu.add_command(label='Stammfunktion', command=integrieren)
integrate_label = None
analysis_menu.add_command(label='Bestimmt Integrieren', command=open_window)
bestimmt_integrieren_label = None
e1_a = None
e2_b = None
analysis_menu.add_command(label='Nullstellen', command=Nullstellen)
solve_label = None
analysis_menu.add_command(label='Limes', command=limes_window)
limit_label = None
e1_limes = None
menu.add_cascade(label='Analysis', menu=analysis_menu)

plot_menu = tk.Menu(menu, tearoff=0)
plot_menu.add_command(label='Plot', command=plotten)
menu.add_cascade(menu=plot_menu, label='Plotten')


tk.Label(root, text="f(x) =").grid(row=0, column=0, sticky="w")
e1 = tk.Entry(root)
e1.grid(row=0, column=1, sticky="we", padx=5, pady=5)

root.grid_columnconfigure(1, weight=1)

root.config(menu=menu)


root.mainloop()