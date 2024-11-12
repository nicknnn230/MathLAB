import tkinter as tk
from tkinter import font
from sympy import symbols, diff, integrate, sympify, SympifyError, lambdify, limit, solve, simplify, Subs, oo
import matplotlib.pyplot as plt
import numpy as np
from differenzialrechnung import differenzialrechnung
from Analysis import analysis



# f(X) _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
x = symbols('x')

def ableiten():
    global diff_label


    function = e1.get()

    ableitung = differenzialrechnung()
    differentiation = ableitung.differenzieren(function)

    if diff_label is None:

        diff_label = tk.Label(root, text=f"1. Ableitung von f(x):               {differentiation}")
        diff_label.grid(row=5, column=0, columnspan=2, sticky="w")
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
        tangenten_label.grid(row=6, column=0, columnspan=2, sticky="w")
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
        normalen_label.grid(row=7, column=0, columnspan=2, sticky="w")
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
            integrate_label.grid(row=8, column=0, columnspan=2, sticky="w")
        else:

            integrate_label.config(text=f"Stammfunktion von f(x):               {integration} + c")
    else:
        if integrate_label is None:

            integrate_label = tk.Label(root, text=f"Stammfunktion von f(x):             {integration}")
            integrate_label.grid(row=8, column=0, columnspan=2, sticky="w")
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
        bestimmt_integrieren_label.grid(row=9, column=0, columnspan=2, sticky="w")
    else:

        bestimmt_integrieren_label.config(text=f"Bestimmte Integration von {a} bis {b}:               {b_integration}")    

    

def Nullstellen():
    global solve_label
    function = e1.get()


    nullstellen_f = analysis()
    nullstellen = nullstellen_f.Nullstellen(function)

    if solve_label is None:

        solve_label = tk.Label(root, text=f"Nullstellen von f(x):               {nullstellen}")
        solve_label.grid(row=10, column=0, columnspan=2, sticky="w")
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
        limit_label.grid(row=11, column=0, columnspan=2, sticky="w")
    else:

        limit_label.config(text=f"lim(x->{lim}):              {grenzwert}")




# g(X) _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

def g_ableiten():
    global g_diff_label


    function = g_e.get()

    g_ableitung = differenzialrechnung()
    g_differentiation = g_ableitung.differenzieren(function)

    if g_diff_label is None:

        g_diff_label = tk.Label(root, text=f"1. Ableitung von g(x):               {g_differentiation}")
        g_diff_label.grid(row=5, column=1, columnspan=2, sticky="w", padx=300)
    else:

        g_diff_label.config(text=f"1. Ableitung von g(x):             {g_differentiation}")
















def plotten():
    global g_e

    function1 = sympify(e1.get())

    if g_e != None:
        function2 = sympify(g_e.get())

        f2_lambda = lambdify(x, function2, 'numpy')
        func2_x_vals = np.linspace(-7, 7, 200)
        func2_y_vals = f2_lambda(func2_x_vals)

        func2_x_vals = np.linspace(-7, 7, 200)
        func2_y_vals = f2_lambda(func2_x_vals)

        plt.plot(func2_x_vals, func2_y_vals, label = str(function2), color='red')



    f_lambda = lambdify(x, function1, 'numpy')

    func1_x_vals = np.linspace(-7, 7, 200)
    func1_y_vals = f_lambda(func1_x_vals)

    func1_x_vals = np.linspace(-7, 7, 200)
    func1_y_vals = f_lambda(func1_x_vals)


    plt.plot(func1_x_vals, func1_y_vals, label = str(function1), color='blue')


    plt.ylim(-50, 50)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph der Funktionen')
    plt.legend()
    plt.grid(True)

    plt.gca().set_facecolor('#333333')
    plt.grid(color='lightblue', linestyle=':', linewidth=0.5)

    plt.show()


def funktion_hinzufügen():
    global plus_function
    global g_e

    plus_function = plus_function + 1

    if plus_function > 0:
        g_analysis_menu = tk.Menu(menu, tearoff=0)
        g_differenzial_menu = tk.Menu(g_analysis_menu, tearoff=0)
        g_analysis_menu.add_cascade(label='Differenzialrechnung g(x)', menu=g_differenzial_menu)
        g_differenzial_menu.add_command(label='Ableiten g(x)', command=g_ableiten)
        g_differenzial_menu.add_command(label='Tangentenbestimmung g(x)', command=None)
        g_differenzial_menu.add_command(label='Normalenbestimmung g(x)', command=None)
        g_analysis_menu.add_command(label='Stammfunktion g(x)', command=None)
        g_analysis_menu.add_command(label='Bestimmt Integrieren g(x)', command=None)
        g_analysis_menu.add_command(label='Nullstellen g(x)', command=None)
        g_analysis_menu.add_command(label='Limes g(x)', command=None)
        menu.insert_cascade(2, label='Analysis g(x)', menu=g_analysis_menu)

        tk.Label(root, text="g(x)", font=my_font).grid(row=3, column=1, sticky="w", padx=300)

        tk.Label(root, text="g(x) =").grid(row=1, column=0, sticky="w")
        g_e = tk.Entry(root)
        g_e.grid(row=1, column=1, sticky="we", padx=5, pady=5)

g_e = None





root = tk.Tk()
root.geometry('900x700')
root.title('MathLAB')


menu = tk.Menu(root)

analysis_menu = tk.Menu(menu, tearoff=0)
differenzial_menu = tk.Menu(analysis_menu, tearoff=0)
analysis_menu.add_cascade(label='Differenzialrechnung', menu=differenzial_menu)

differenzial_menu.add_command(label='Ableiten', command=ableiten)
diff_label = None
g_diff_label = None

differenzial_menu.add_command(label='Tangentenbestimmung', command=tangente_window)
tangenten_label = None
entry_x0 = None
g_tangenten_label = None

differenzial_menu.add_command(label='Normalenbestimmung', command=normalen_window)
normalen_label = None
entry_x0_normale = None
g_normalen_label = None

analysis_menu.add_command(label='Stammfunktion', command=integrieren)
integrate_label = None
g_integrate_label = None

analysis_menu.add_command(label='Bestimmt Integrieren', command=open_window)
bestimmt_integrieren_label = None
e1_a = None
e2_b = None
g_bestimmt_integrieren_label = None

analysis_menu.add_command(label='Nullstellen', command=Nullstellen)
solve_label = None
g_solve_label = None


analysis_menu.add_command(label='Limes', command=limes_window)
limit_label = None
e1_limes = None
g_limit_label = None

menu.add_cascade(label='Analysis', menu=analysis_menu)

plus_function_menu = tk.Menu(menu, tearoff=0)
plus_function_menu.add_command(label='Funktion hinzufügen', command=funktion_hinzufügen)
plus_function = 0
menu.add_cascade(label='Funktionen hinzufügen', menu=plus_function_menu)

    

plot_menu = tk.Menu(menu, tearoff=0)
plot_menu.add_command(label='Plot', command=plotten)
menu.add_cascade(menu=plot_menu, label='Plotten')

my_font = font.Font(size=12)
tk.Label(root, text="f(x)", font=my_font).grid(row=3, column=0, sticky="w")

tk.Label(root, text="f(x) =").grid(row=0, column=0, sticky="w")
e1 = tk.Entry(root)
e1.grid(row=0, column=1, sticky="we", padx=5, pady=5)

root.grid_columnconfigure(1, weight=1)

root.config(menu=menu)


root.mainloop()