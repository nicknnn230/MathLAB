import tkinter as tk
from sympy import symbols, diff, integrate, sympify, SympifyError, lambdify, limit, solve, simplify, Subs, oo
import matplotlib.pyplot as plt
import numpy as np
from differenzialrechnung import differenzialrechnung
from Analysis import analysis


x = symbols('x')

def ableiten():
    global diff_label


    function = e1.get()

    ableitung = differenzialrechnung()
    differentiation = ableitung.differenzieren(function)

    if diff_label is None:

        diff_label = tk.Label(root, text=f"1. Ableitung von f(x):               {differentiation}")
        diff_label.grid(row=1, column=0, columnspan=2, sticky="w")
    else:

        diff_label.config(text=f"1. Ableitung von f(x):             {differentiation}")



def tangente_window():
    global entry_x0
    t_n_window = tk.Toplevel(root)
    t_n_window.title("x0 bestimmen (Tangente)")
    t_n_window.geometry("300x100")

    w = tk.Label(t_n_window, text=f"x-Stelle der Tangente")
    w.grid(row=0, column=0, sticky='w')

    tk.Label(t_n_window, text="x0 =").grid(row=1, column=0, sticky="w")
    entry_x0 = tk.Entry(t_n_window)
    entry_x0.grid(row=1, column=0, sticky="w", padx=25, pady=5)

    button_tangente = tk.Button(t_n_window, text='ausführen', command=tangente)
    button_tangente.grid(row=3, column=0, sticky="w", padx=25, pady=5)

def tangente():
    global tangenten_label
    global entry_x0

    function = e1.get()

    x0 = int(entry_x0.get())

    tang = differenzialrechnung()
    tangente_function = tang.tangente(function, x0)

    if tangenten_label is None:

        tangenten_label = tk.Label(root, text=f"Tangente von f(x) an der Stelle {x0}:               {tangente_function}")
        tangenten_label.grid(row=2, column=0, columnspan=2, sticky="w")
    else:

        tangenten_label.config(text=f"Tangente von f(x) an der Stelle {x0}:             {tangente_function}")


def normalen_window():
    global entry_x0_normale

    n_window = tk.Toplevel(root)
    n_window.title("x0 bestimmen (Normale)")
    n_window.geometry("300x100")

    w = tk.Label(n_window, text=f"x-Stelle der Normalen")
    w.grid(row=0, column=0, sticky='w')

    tk.Label(n_window, text="x0 =").grid(row=1, column=0, sticky="w")
    entry_x0_normale = tk.Entry(n_window)
    entry_x0_normale.grid(row=1, column=0, sticky="w", padx=25, pady=5)

    button_normale = tk.Button(n_window, text='ausführen', command=normale)
    button_normale.grid(row=3, column=0, sticky="w", padx=25, pady=5)

def normale():
    global normalen_label
    global entry_x0_normale

    function = e1.get()

    x0 = int(entry_x0_normale.get())

    norma = differenzialrechnung()
    normale_function = norma.normale(function, x0)

    if normalen_label is None:

        normalen_label = tk.Label(root, text=f"Normale von f(x) an der Stelle {x0}:               {normale_function}")
        normalen_label.grid(row=3, column=0, columnspan=2, sticky="w")
    else:

        normalen_label.config(text=f"Normale von f(x) an der Stelle {x0}:             {normale_function}")

def integrieren():
    global integrate_label

    

    function = e1.get()
    
    expression_integration = analysis()
    integration = expression_integration.integrieren(function)

    if integration != "Ungültiger Ausdruck. Bitte gültige Funktion eingeben.":
        if integrate_label is None:

            integrate_label = tk.Label(root, text=f"Stammfunktion von f(x):             {integration} + c")
            integrate_label.grid(row=4, column=0, columnspan=2, sticky="w")
        else:

            integrate_label.config(text=f"Stammfunktion von f(x):               {integration} + c")
    else:
        if integrate_label is None:

            integrate_label = tk.Label(root, text=f"Stammfunktion von f(x):             {integration}")
            integrate_label.grid(row=4, column=0, columnspan=2, sticky="w")
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

    integration = analysis
    b_integration = integration.bestimmt_integrieren(function, a, b)


    if bestimmt_integrieren_label is None:

        bestimmt_integrieren_label = tk.Label(root, text=f"Bestimmte Integration von {a} bis {b}:             {b_integration}")
        bestimmt_integrieren_label.grid(row=5, column=0, columnspan=2, sticky="w")
    else:

        bestimmt_integrieren_label.config(text=f"Bestimmte Integration von {a} bis {b}:               {b_integration}")    

    

def Nullstellen():
    global solve_label
    function = e1.get()


    nullstellen_f = analysis()
    nullstellen = nullstellen_f.Nullstellen(function)

    if solve_label is None:

        solve_label = tk.Label(root, text=f"Nullstellen von f(x):               {nullstellen}")
        solve_label.grid(row=6, column=0, columnspan=2, sticky="w")
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

    limes = analysis()
    grenzwert = limes.grenzwert(function, lim)



    if limit_label is None:

        limit_label = tk.Label(root, text=f"lim(x->{lim}):              {grenzwert}")
        limit_label.grid(row=7, column=0, columnspan=2, sticky="w")
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
differenzial_menu = tk.Menu(analysis_menu, tearoff=0)
analysis_menu.add_cascade(label='Differenzialrechnung', menu=differenzial_menu)
differenzial_menu.add_command(label='Ableiten', command=ableiten)
diff_label = None
differenzial_menu.add_command(label='Tangentenbestimmung', command=tangente_window)
tangenten_label = None
entry_x0 = None
differenzial_menu.add_command(label='Normalenbestimmung', command=normalen_window)
normalen_label = None
entry_x0_normale = None
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