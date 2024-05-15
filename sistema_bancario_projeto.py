# Objetivo: Criar um sistema bancário com as seguinte operações:
    # Depósito
    # Saque
    # Extrato

# OBSERVAÇÕES:
    # 1- Não é preciso identificar número da agência nem conta bancária;
    # 2- Só deve ser possível depositar valores positivos;
    # 3- Todos os depósitos e saques devem ser armazenados em uma variável e exibidos na operação de extrato.
    # 4- O sistema permite realizar 3 saques diários (R$1500,00 máx.), com limite de R$500,00 por saque.
    # 5- Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível realizar o saque por falta de saldo.

# EXTRATO: Os valores devem ser exibidos utilizando o formato R$0000.00. (R$1.545,34 => R$1545.34)

import tkinter as tk
from tkinter import messagebox, simpledialog

class SistemaBancario:
    def __init__(self, master):
        self.master = master
        master.title('Sistema Bancário') # Título da janela
        master.geometry('800x600') # resolução da interface
        self.font_style = ('Arial', 18) # Tamanho e fonte
        self.main_frame = tk.Frame(master)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center') # Declarar interface e centralizar

        # Label de Boas-vindas
        self.label_boas_vindas = tk.Label(self.main_frame, text="Olá caro cliente. O que deseja realizar hoje?", font=self.font_style)
        self.label_boas_vindas.grid(row=0, column=0, columnspan=2, pady=10)

        # Botão de Depósito
        self.botao_deposito = tk.Button(self.main_frame, text='Depósito', command=self.deposito, font=self.font_style)
        self.botao_deposito.grid(row=1, column=0, columnspan=2, pady=10)

        # Botão de Saque
        self.botao_saque = tk.Button(self.main_frame, text='Saque', command=self.saque, font=self.font_style)
        self.botao_saque.grid(row=2, column=0, columnspan=2, pady=10)

        # Botão de Extrato
        self.botao_extrato = tk.Button(self.main_frame, text='Extrato', command=self.extrato, font=self.font_style)
        self.botao_extrato.grid(row=3, column=0, columnspan=2, pady=10)

        # Botão Sair
        self.botao_sair = tk.Button(self.main_frame, text='Sair', command=master.quit, font=self.font_style)
        self.botao_sair.grid(row=4, column=0, columnspan=2, pady=10)

        # Variáveis do sistema
        self.saldo = 0
        self.historico_transacoes = list() # para identificar se já houveram ou não transações para serem exibidas.
        self.limite_saque_diario = 1500.00
        self.contador_saques = 0

        # Atualização do saldo na interface
        self.label_saldo = tk.Label(self.main_frame, text=f"Saldo: R${self.saldo:.2f}", font=self.font_style)
        self.label_saldo.grid(row=5, column=0, columnspan=2, pady=10)

    def deposito(self):
        valor = simpledialog.askfloat("Depósito", "Valor do depósito:", minvalue=0.01)
        if valor:
            self.saldo += valor
            self.historico_transacoes.append(('Depósito', valor))
            messagebox.showinfo("Sucesso", f"Depósito de R${valor:.2f} realizado com sucesso.")
            self.atualizar_saldo()
        else:
            messagebox.showerror("Erro", "O depósito foi cancelado.") # Ao clicar no botão cancelar

    def saque(self):
        if self.contador_saques < 3:
            valor = simpledialog.askfloat("Saque", "Quanto você deseja sacar? \nValor mínimo: R$0.01. \nValor máximo: R$500.00.", minvalue=0.01, maxvalue=500) # Valor mínimo: 1 centavo. Valor máximo: 500 reais por saque.
            if valor and self.saldo >= valor:
                self.saldo -= valor
                self.contador_saques += 1
                self.historico_transacoes.append(('Saque', valor))
                messagebox.showinfo("Sucesso", f"Saque de R${valor:.2f} realizado com sucesso.")
                self.atualizar_saldo()
            elif valor and self.saldo <= valor:
                messagebox.showerror("Erro", "O saque não pôde ser realizado: saldo insuficiente ou valor de saque inválido.")
            else:
                messagebox.showerror("Erro", "Saque cancelado.")
        else:
            messagebox.showwarning("Erro", f"O limite de saques diários da sua conta (3 ao dia ou R${self.limite_saque_diario:.2f} de limite) foi antingido.")

    def extrato(self):
        if self.historico_transacoes: # Se houver um histórico de transações
            extrato_str = "\n".join(f"{tipo}: R${valor:.2f}" for tipo, valor in self.historico_transacoes)
            messagebox.showinfo("Extrato", f"Saldo atual: R${self.saldo:.2f}\n\nHistórico de transações:\n{extrato_str}") # mostra extrato
        else:
            messagebox.showinfo("Extrato", "Não há históricos de transações para serem visualizados.") # Ainda não houveram movimentações

    def atualizar_saldo(self):
        self.label_saldo.config(text=f"Saldo: R${self.saldo:.2f}")
        print(f"Saldo em conta: R${self.saldo:.2f}")

if __name__ == '__main__':
    root = tk.Tk()
    app = SistemaBancario(root)
    root.mainloop()
