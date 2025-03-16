import tkinter as tk
from sympy import symbols, diff, integrate, sympify, SympifyError, lambdify, limit, solve, simplify, Subs, oo
import matplotlib.pyplot as plt
import numpy as np
from differenzialrechnung import differenzialrechnung
from Analysis import analysis

next_row = 1
plot_color = 0



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



def umkehrfunktion():
    x, y = symbols('x y')

    function = e1.get()

    try:
        sympify_function = sympify(function)  
        equation = y - sympify_function 

        inverse_solution = solve(equation, x)  
        
        if inverse_solution:
            result_y = inverse_solution[0]  
        else:
            result_y = "Keine Umkehrfunktion gefunden"
    except SympifyError:
        result_y = "Ungültiger Ausdruck. Bitte gültige Funktion eingeben."

    y_label = tk.Label(root, text=f"{function}: Umkehrfunktion von {function} = {result_y}")
    y_label.grid(row=next_row, column=0, columnspan=2, sticky="w", pady=5)



def lgs_window():
    global entry_matrix, entry_vector, rows, cols, create_btn 

    lgs_win = tk.Toplevel(root)
    lgs_win.title("Lineares Gleichungssystem lösen")
    
    tk.Label(lgs_win, text="Anzahl der Gleichungen:").grid(row=0, column=0)
    tk.Label(lgs_win, text="Anzahl der Variablen:").grid(row=1, column=0)

    entry_rows = tk.Entry(lgs_win)
    entry_cols = tk.Entry(lgs_win)
    entry_rows.grid(row=0, column=1)
    entry_cols.grid(row=1, column=1)

    def create_matrix_inputs():
        """Erstellt Eingabefelder für die Koeffizientenmatrix und das Ergebnis."""
        global entry_matrix, entry_vector, rows, cols, create_btn
        rows = int(entry_rows.get())
        cols = int(entry_cols.get())

        matrix_frame = tk.Frame(lgs_win)
        matrix_frame.grid(row=3, column=0, columnspan=cols+2, sticky="we")

        entry_matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                entry = tk.Entry(matrix_frame, width=5) 
                row.append(entry)
            entry_matrix.append(row)

        entry_vector = []
        for i in range(rows):
            entry = tk.Entry(matrix_frame, width=5) 
            entry_vector.append(entry)

        for i in range(rows):
            for j in range(cols):
                entry_matrix[i][j].grid(row=i+3, column=j, padx=0, pady=0)

        for i in range(rows):
            entry_vector[i].grid(row=i+3, column=cols+1)

        solve_button = tk.Button(lgs_win, text="Lösen", command=solve_lgs)
        solve_button.grid(row=rows+4, column=0, columnspan=cols+2)

        det_button = tk.Button(lgs_win, text='Determinante berechnen', command=solve_det)
        det_button.grid(row=rows+5, column=0, columnspan=cols+2)

        create_btn.destroy()
        for j in range(cols + 2):
            matrix_frame.columnconfigure(j, weight=0, uniform="matrix_col")

    create_btn = tk.Button(lgs_win, text="Eingabefelder erstellen", command=create_matrix_inputs)
    create_btn.grid(row=2, column=1)


def solve_lgs():
    """Löst das lineare Gleichungssystem."""
    global entry_matrix, entry_vector, rows, cols, next_row
    try:
        A = []
        for i in range(rows):  # Durchläuft jede Zeile der Matrix
            row = []
            for j in range(cols):  # Durchläuft jede Spalte der aktuellen Zeile
                value = float(entry_matrix[i][j].get())  # Holt den Wert aus dem Eingabefeld und wandelt ihn in eine Zahl um
                row.append(value)  # Fügt den Wert zur aktuellen Zeile hinzu
            A.append(row)  # Fügt die Zeile zur Matrix hinzu

        A = np.array(A)


        b = []
        for i in range(rows):  # Durchläuft alle Zeilen (da der Vektor nur eine Spalte hat)
            value = float(entry_vector[i].get())  # Holt den Wert aus dem Eingabefeld
            b.append(value)  # Fügt den Wert zur Liste hinzu

        b = np.array(b)  # Wandelt die Liste in ein NumPy-Array um

        solution = np.linalg.solve(A, b)

        result_label = tk.Label(root, text=f"Lösung LGS: {solution}")
        result_label.grid(row=next_row, column=0, columnspan=2, sticky="w", pady=5)

        next_row += 1

    except np.linalg.LinAlgError:
        error_label = tk.Label(root, text="Keine eindeutige Lösung (Singuläre Matrix).")
        error_label.grid(row=next_row, column=0, columnspan=2, sticky="w", pady=5)
        next_row += 1
    except ValueError:
        error_label = tk.Label(root, text="Bitte gültige Zahlen eingeben.")
        error_label.grid(row=next_row, column=0, columnspan=2, sticky="w", pady=5)
        next_row += 1

def solve_det():
    global entry_matrix, rows, cols, next_row
    try:
        A = []
        for i in range(rows):  
            row = []
            for j in range(cols):  
                value = float(entry_matrix[i][j].get()) 
                row.append(value)
            A.append(row)  

        A = np.array(A)  
        det_A = round(np.linalg.det(A), 4) 

        result_label = tk.Label(root, text=f"Determinante: {det_A}")
        result_label.grid(row=next_row, column=0, columnspan=2, sticky="w", pady=5)
        next_row += 1
    
    except np.linalg.LinAlgError:
        error_label = tk.Label(root, text="Determinante nicht definiert (keine quadratische Matrix).")
        error_label.grid(row=next_row, column=0, columnspan=2, sticky="w", pady=5)
        next_row += 1
    except ValueError:
        error_label = tk.Label(root, text="Bitte gültige Zahlen eingeben.")
        error_label.grid(row=next_row, column=0, columnspan=2, sticky="w", pady=5)
        next_row += 1


def plotten():
    global g_e, plot_color

    plot_color += 1

    function1 = sympify(e1.get())
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta', 'yellow']

    f_lambda = lambdify(x, function1, 'numpy')

    func1_x_vals = np.linspace(-7, 7, 200)
    func1_y_vals = f_lambda(func1_x_vals)

    color = colors[plot_color % len(colors)]


    plt.plot(func1_x_vals, func1_y_vals, label=str(function1), color=color, linestyle='-', linewidth=2)


    plt.ylim(-50, 50)
    plt.xlabel('x-Achse', fontsize=12, color='black')  
    plt.ylabel('f(x)', fontsize=12, color='black')  


    plt.grid(True, color='black', linestyle='--', linewidth=0.7)  


    plt.gca().set_facecolor('white')  


    plt.legend(facecolor='white', loc='upper left', fontsize=10, frameon=True, edgecolor='black')  


    plt.gca().set_autoscale_on(True)  

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

analysis_menu.add_command(label='Umkehrfunktion bilden', command=umkehrfunktion)

analysis_menu.add_command(label='LGS lösen', command=lgs_window)

menu.add_cascade(label='Analysis', menu=analysis_menu)
    

plot_menu = tk.Menu(menu, tearoff=0)
plot_menu.add_command(label='anzeigen', command=plotten)
menu.add_cascade(menu=plot_menu, label='Funktionen')

tk.Label(root, text="f(x) =").grid(row=0, column=0, sticky="w")
e1 = tk.Entry(root)
e1.grid(row=0, column=1, sticky="we", padx=5, pady=5)

root.grid_columnconfigure(1, weight=1)

root.config(menu=menu)


root.mainloop()