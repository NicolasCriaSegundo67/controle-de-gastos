import tkinter as tk
from tkinter import ttk, messagebox
import json

gastos = []

# -------- FUNÇÕES -------- #

def adicionar_gasto():
    try:
            valor = float(entry_valor.get())
                    categoria = combo_categoria.get()

                            if categoria == "":
                                        messagebox.showwarning("Erro", "Escolha uma categoria!")
                                                    return

                                                            gasto = {"valor": valor, "categoria": categoria}
                                                                    gastos.append(gasto)

                                                                            atualizar_lista()
                                                                                    atualizar_total()

                                                                                            entry_valor.delete(0, tk.END)

                                                                                                except:
                                                                                                        messagebox.showerror("Erro", "Digite um valor válido!")

                                                                                                        def atualizar_lista():
                                                                                                            lista_gastos.delete(0, tk.END)
                                                                                                                for g in gastos:
                                                                                                                        lista_gastos.insert(tk.END, f"R$ {g['valor']:.2f} - {g['categoria']}")

                                                                                                                        def atualizar_total():
                                                                                                                            total = sum(g["valor"] for g in gastos)
                                                                                                                                label_total.config(text=f"Total: R$ {total:.2f}")

                                                                                                                                def remover_gasto():
                                                                                                                                    try:
                                                                                                                                            index = lista_gastos.curselection()[0]
                                                                                                                                                    gastos.pop(index)
                                                                                                                                                            atualizar_lista()
                                                                                                                                                                    atualizar_total()
                                                                                                                                                                        except:
                                                                                                                                                                                messagebox.showwarning("Erro", "Selecione um gasto!")

                                                                                                                                                                                def salvar_dados():
                                                                                                                                                                                    with open("gastos.json", "w") as f:
                                                                                                                                                                                            json.dump(gastos, f)
                                                                                                                                                                                                messagebox.showinfo("Sucesso", "Dados salvos!")

                                                                                                                                                                                                def carregar_dados():
                                                                                                                                                                                                    global gastos
                                                                                                                                                                                                        try:
                                                                                                                                                                                                                with open("gastos.json", "r") as f:
                                                                                                                                                                                                                            gastos = json.load(f)
                                                                                                                                                                                                                                    atualizar_lista()
                                                                                                                                                                                                                                            atualizar_total()
                                                                                                                                                                                                                                                except:
                                                                                                                                                                                                                                                        pass

                                                                                                                                                                                                                                                        # -------- INTERFACE -------- #

                                                                                                                                                                                                                                                        janela = tk.Tk()
                                                                                                                                                                                                                                                        janela.title("Controle de Gastos 💸")
                                                                                                                                                                                                                                                        janela.geometry("420x500")
                                                                                                                                                                                                                                                        janela.configure(bg="#1e1e2f")

                                                                                                                                                                                                                                                        # Título
                                                                                                                                                                                                                                                        titulo = tk.Label(janela, text="Controle de Gastos", font=("Arial", 18, "bold"), bg="#1e1e2f", fg="white")
                                                                                                                                                                                                                                                        titulo.pack(pady=10)

                                                                                                                                                                                                                                                        # Frame entrada
                                                                                                                                                                                                                                                        frame_input = tk.Frame(janela, bg="#1e1e2f")
                                                                                                                                                                                                                                                        frame_input.pack(pady=10)

                                                                                                                                                                                                                                                        # Campo valor
                                                                                                                                                                                                                                                        entry_valor = tk.Entry(frame_input, font=("Arial", 12))
                                                                                                                                                                                                                                                        entry_valor.grid(row=0, column=0, padx=5)

                                                                                                                                                                                                                                                        # Combo categorias
                                                                                                                                                                                                                                                        combo_categoria = ttk.Combobox(frame_input, values=["Alimentação", "Transporte", "Lazer", "Outros"])
                                                                                                                                                                                                                                                        combo_categoria.grid(row=0, column=1, padx=5)

                                                                                                                                                                                                                                                        # Botão adicionar
                                                                                                                                                                                                                                                        btn_add = tk.Button(janela, text="Adicionar", bg="#4CAF50", fg="white", command=adicionar_gasto)
                                                                                                                                                                                                                                                        btn_add.pack(pady=5)

                                                                                                                                                                                                                                                        # Lista
                                                                                                                                                                                                                                                        lista_gastos = tk.Listbox(janela, bg="#2a2a40", fg="white", font=("Arial", 11))
                                                                                                                                                                                                                                                        lista_gastos.pack(pady=10, fill=tk.BOTH, expand=True)

                                                                                                                                                                                                                                                        # Botão remover
                                                                                                                                                                                                                                                        btn_remover = tk.Button(janela, text="Remover Selecionado", bg="#f44336", fg="white", command=remover_gasto)
                                                                                                                                                                                                                                                        btn_remover.pack(pady=5)

                                                                                                                                                                                                                                                        # Total
                                                                                                                                                                                                                                                        label_total = tk.Label(janela, text="Total: R$ 0.00", font=("Arial", 14), bg="#1e1e2f", fg="white")
                                                                                                                                                                                                                                                        label_total.pack(pady=10)

                                                                                                                                                                                                                                                        # Botões salvar/carregar
                                                                                                                                                                                                                                                        frame_botoes = tk.Frame(janela, bg="#1e1e2f")
                                                                                                                                                                                                                                                        frame_botoes.pack(pady=10)

                                                                                                                                                                                                                                                        btn_salvar = tk.Button(frame_botoes, text="Salvar", bg="#2196F3", fg="white", command=salvar_dados)
                                                                                                                                                                                                                                                        btn_salvar.grid(row=0, column=0, padx=10)

                                                                                                                                                                                                                                                        btn_carregar = tk.Button(frame_botoes, text="Carregar", bg="#FF9800", fg="white", command=carregar_dados)
                                                                                                                                                                                                                                                        btn_carregar.grid(row=0, column=1, padx=10)

                                                                                                                                                                                                                                                        # Iniciar com dados salvos
                                                                                                                                                                                                                                                        carregar_dados()

                                                                                                                                                                                                                                                        janela.mainloop()0