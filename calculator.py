import tkinter as tk
import math

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
        elif operator == "^":
            ergebnis = zahl1 ** zahl2
        elif operator == "√":
            if zahl1 >= 0:
                ergebnis = math.sqrt(zahl1)
            else:
                ergebnis = "Fehler: Negative Zahl"
        else:
            ergebnis = "Ungültiger Operator"

        label_ergebnis.config(text=f"Ergebnis: {ergebnis}")

    except ValueError:
        label_ergebnis.config(text="Bitte gültige Zahlen eingeben!")

# ⬇ Vorzeichen der ersten Zahl wechseln


def wechsle_vorzeichen():
    try:
        wert = float(entry1.get())
        entry1.delete(0, tk.END)
        entry1.insert(0, str(-wert))
    except ValueError:
        pass


# Hauptfenster
root = tk.Tk()
root.title("Einfacher Taschenrechner")
root.configure(bg="#f0f0f0")

# Eingabefelder
entry1 = tk.Entry(root, font=("Arial", 14))
entry1.grid(row=0, column=0, padx=5, pady=10)

entry2 = tk.Entry(root, font=("Arial", 14))
entry2.grid(row=0, column=2, padx=5, pady=10)

# Operator-Dropdown
operator_var = tk.StringVar(value="+")
operator_menu = tk.OptionMenu(root, operator_var, "+", "-", "*", "/", "^", "√")
operator_menu.config(font=("Arial", 12))
operator_menu.grid(row=0, column=1)

# Buttons
button = tk.Button(
    root,
    text="Berechnen",
    command=rechne,
    bg="lightgray",       # Hintergrund
    fg="black",           # Textfarbe
    font=("Arial", 12),   # Schriftart
    relief="raised",      # 3D-Effekt
    padx=10,
    pady=5
)

button.grid(row=1, column=1, pady=10)

button_vz = tk.Button(root, text="± Vorzeichen", font=(
    "Arial", 10), command=wechsle_vorzeichen)
button_vz.grid(row=1, column=0)

# Ergebnis anzeigen
label_ergebnis = tk.Label(root, text="Ergebnis:",
                          font=("Arial", 14), bg="#f0f0f0")
label_ergebnis.grid(row=2, column=0, columnspan=3)

# App starten
root.mainloop()
