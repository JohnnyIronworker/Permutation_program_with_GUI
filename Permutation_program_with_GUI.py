import tkinter as tk
from tkinter import filedialog

def perm(A):
    wynik = []
    if not A:
        return [[]]
    else:
        for i in range(len(A)):
            elem = A[i]
            reszta = A[:i] + A[i+1:]
            for d in perm(reszta):
                wynik.append([elem] + d)
    return wynik

def zapisz_per():
    variable = list(map(int, input_text.get().split(',')))
    permutacje = perm(variable)
    
    plik_nazwa = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")])
    with open(plik_nazwa, "w") as plik_wynikowy:
        for p in permutacje:
            plik_wynikowy.write(str(p) + "\n")
    
    # Create a new window
    window = tk.Tk()
    window.title("Permutations")
    window.geometry("300x300")  # set the size of the window
    window.configure(bg="green")  # set the background color of the window
    window.attributes("-topmost", True)  # make the window appear on top of other windows
    
    # Change the color of the title bar
    window.wm_attributes("-topmost", 1)
    window.wm_attributes("-transparentcolor", "green")
    
    # Create a Text widget and add the output
    text = tk.Text(window, width=50, height=20)
    text.insert(tk.END, str(permutacje))
    text.pack()
    
    # Start the event loop
    window.mainloop()

def main():
    global input_text
    # Create a window for user input
    root = tk.Tk()
    root.title("Permutations")
    root.configure(bg="green")  # set the background color of the window
    label = tk.Label(root, text="Enter a list of integers separated by comma ", bg="green", fg="white")
    label.pack(padx=10, pady=10)
    input_text = tk.Entry(root, bg="light green")
    input_text.pack(padx=10, pady=10)
    button = tk.Button(root, text="Save permutations", command=zapisz_per)
    button.pack(padx=10, pady=10)
    signature_label = tk.Label(root, text="Jan Ślusarek", font=("Arial", 10, "italic"), bg="green", fg="white")
    signature_label.pack(side="bottom", padx=5, pady=5)
    root.mainloop()

if __name__ == "__main__":
    main()
