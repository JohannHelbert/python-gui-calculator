import tkinter as tk

# Funktion für das Rechnen


def rechne():
    try:
        zahl1 = float(entry1.get())
        zahl2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":
            ergebnis = zahl1 + zahl2
        elif operator == "-":
            ergebnis = zahl1 - zahl2
        elif operator == "*":
            ergebnis = zahl1 * zahl2
        elif operator == "/":
            if zahl2 != 0:
                ergebnis = zahl1 / zahl2
            else:
                ergebnis = "Fehler: Division durch 0"
        else:
            ergebnis = "Ungültiger Operator"

        label_ergebnis.config(text=f"Ergebnis: {ergebnis}")
    except ValueError:
        label_ergebnis.config(text="Bitte gültige Zahlen eingeben!")


# Fenster erstellen
root = tk.Tk()
root.title("Einfacher Taschenrechner")

# Eingabefelder
entry1 = tk.Entry(root)
entry1.grid(row=0, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=0, column=2)

# Dropdown für Operator
operator_var = tk.StringVar(value="+")
operator_menu = tk.OptionMenu(root, operator_var, "+", "-", "*", "/")
operator_menu.grid(row=0, column=1)

# Button für Berechnung
button = tk.Button(root, text="Berechnen", command=rechne)
button.grid(row=1, column=1)

# Label für Ergebnis
label_ergebnis = tk.Label(root, text="Ergebnis:")
label_ergebnis.grid(row=2, column=1)

# Hauptloop starten
root.mainloop()
