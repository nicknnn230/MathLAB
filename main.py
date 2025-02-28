import tkinter as tk
from sympy import symbols, diff, integrate, sympify, SympifyError, lambdify, limit, solve, simplify, Subs, oo
import matplotlib.pyplot as plt
import numpy as np
from differenzialrechnung import differenzialrechnung
from Analysis import analysis

next_row = 1



# f(X) _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
x = symbols('x')

def ableiten():
    global next_row

    function = e1.get()

    ableitung = differenzialrechnung()
    differentiation = ableitung.differenzieren(function)


    diff_label = tk.Label(root, text=f"Ableitung von {function}:  {differentiation}")
    diff_label.grid(row=next_row, column=0, columnspan=2, sticky="w", pady=5)

    next_row += 1



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
    global next_row

    function = e1.get()
    x0 = int(entry_x0.get())

    tang = differenzialrechnung()
    tangente_function = tang.tangente(function, x0)

    tangenten_label = tk.Label(root, text=f"Tangente von {function} an der Stelle {x0}:  {tangente_function}")
    tangenten_label.grid(row=next_row, column=0, columnspan=2, sticky="w", pady=5)

    next_row += 1


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
    global next_row

    function = e1.get()
    x0 = int(entry_x0_normale.get())

    norma = differenzialrechnung()
    normale_function = norma.normale(function, x0)

    normalen_label = tk.Label(root, text=f"Normale von {function} an der Stelle {x0}:  {normale_function}")
    normalen_label.grid(row=next_row, column=0, columnspan=2, sticky="w", pady=5)

    next_row += 1

def integrieren():
    global next_row

    function = e1.get()

    expression_integration = analysis()
    integration = expression_integration.integrieren(function)

    if integration != "Ungültiger Ausdruck. Bitte gültige Funktion eingeben.":
        text = f"Stammfunktion von {function}:  {integration} + c"
    else:
        text = f"Stammfunktion von {function}:  {integration}"

    integrate_label = tk.Label(root, text=text)
    integrate_label.grid(row=next_row, column=0, columnspan=2, sticky="w", pady=5)

    next_row += 1



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
    global next_row
    global e1_a, e2_b

    a = e1_a.get()
    b = e2_b.get()
    function = e1.get()

    integration = analysis()
    b_integration = integration.bestimmt_integrieren(function, a, b)

    bestimmt_integrieren_label = tk.Label(root, text=f"Bestimmte Integration von {function} von {a} bis {b}: {b_integration}")
    bestimmt_integrieren_label.grid(row=next_row, column=0, columnspan=2, sticky="w", pady=5)

    next_row += 1


    

def Nullstellen():
    global next_row
    function = e1.get()

    nullstellen_f = analysis()
    nullstellen = nullstellen_f.Nullstellen(function)

    solve_label = tk.Label(root, text=f"Nullstellen von {function}:  {nullstellen}")
    solve_label.grid(row=next_row, column=0, columnspan=2, sticky="w", pady=5)

    next_row += 1


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
    global next_row
    global e1_limes

    lim = e1_limes.get()
    function = e1.get()

    limes_calc = analysis()
    grenzwert = limes_calc.grenzwert(function, lim)

    limit_label = tk.Label(root, text=f"{function}: lim(x→{lim}) = {grenzwert}")
    limit_label.grid(row=next_row, column=0, columnspan=2, sticky="w", pady=5)

    next_row += 1















def plotten():
    global g_e

    function1 = sympify(e1.get())



    f_lambda = lambdify(x, function1, 'numpy')

    func1_x_vals = np.linspace(-7, 7, 200)
    func1_y_vals = f_lambda(func1_x_vals)

    func1_x_vals = np.linspace(-7, 7, 200)
    func1_y_vals = f_lambda(func1_x_vals)


    plt.plot(func1_x_vals, func1_y_vals, label = str(function1), color='blue')


    plt.ylim(-50, 50)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)

    plt.gca().set_facecolor('#333333')
    plt.grid(color='lightblue', linestyle=':', linewidth=0.5)

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