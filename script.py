import tkinter as tk


class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        # campo de entrada
        self.entrada = tk.Entry(root, width=20, font=("Arial", 20))
        self.entrada.grid(row=0, column=0, columnspan=4)

        # botões
        botoes = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "C", "=", "+"
        ]

        linha = 1
        coluna = 0

        for botao in botoes:
            comando = lambda x=botao: self.clique(x)

            tk.Button(root, text=botao, width=5, height=2,
                      font=("Arial", 14),
                      command=comando).grid(row=linha, column=coluna)

            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1

    def clique(self, valor):
        if valor == "C":
            self.entrada.delete(0, tk.END)

        elif valor == "=":
            try:
                resultado = eval(self.entrada.get())
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, str(resultado))
            except:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Erro")

        else:
            self.entrada.insert(tk.END, valor)


# iniciar app
root = tk.Tk()
app = CalculadoraGUI(root)
root.mainloop()