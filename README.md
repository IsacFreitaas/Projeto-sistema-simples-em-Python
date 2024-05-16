# Criando Um Sistema Bancário Simples com Python.

Foi passado uma atividade de criação de um programa de sistema bancário simples, com somente as funcões mais primitivas de um banco, no curso [Python AI Backend Developer](https://web.dio.me/track/coding-future-vivo-python-ai-backend-developer), desenvolvido pela VIVO: Coding The Future, na platafoma [Dio](https://web.dio.me/).





O objetivo desse projeto é criar um sistema bancário simples com as seguintes operações:




  ### Depósito, Saque e Extrato.





Decidi fazer esse programa com uma interface interativa para esse sistema simples.






Pequena demonstração de como ficou o programa:



<div align="center">
<video src="https://github.com/IsacFreitaas/projeto-sistema-simples-em-python/assets/65254733/5a9fef75-7ac9-4ed2-aa55-a63fb1570b37"></video>
</div>


Abaixo está tudo sobre como eu fiz cada parte do código. Confira!




-----------------------
### Parte 1:
-----------------------



Então, começando o desenvolvimento, apenas fui escrevendo no código o roteiro do que eu iria fazer, junto a algumas observações:
    
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



-----------------------
### Parte 2:
-----------------------






Acredito que o básico de uma interface interativa são botões. Eles dão ao usuário o poder de escolha, fazendo assim um programa tangível, e intuitivo.





Para isso, usei a biblioteca multiuso Tkinter e importei as funções "messagebox" (exibe mensagens ou alertas ao usuário) e "simpledialog" (exibe caixas de diálogo para entrada de dados [por exemplo digitar um valor ou senha]) para fazer toda a interface e caixas de entrada e avisos, tendo em mente uma interface interativa para esse sistema simples..




Iniciou-se assim:

    import tkinter as tk
    from tkinter import messagebox, simpledialog



Defini uma classe chamada "SistemaBancario" e defini uma função °__init__ e defini a janela principal ("master"), o título da janela ("title"), a resolução da janela ("geometry"), o estilo da fonte do texto ("font_style"), a tela inicial ("main_frame", posicionado no centro da janela ("place").




O código ficou assim:

    class SistemaBancario:
      def __init__(self, master):
          self.master = master
          master.title('Sistema Bancário') # Título da janela
          master.geometry('800x600') # resolução da interface
          self.font_style = ('Arial', 18) # Tamanho e fonte
          self.main_frame = tk.Frame(master)
          self.main_frame.place(relx=0.5, rely=0.5, anchor='center') # Declarar interface e centralizar



Agora que já defini a janela, está na hora de definir o que vai ser apresentado na iterface.

Decidi que no cabeçalho da interface será um texto de boas vindas ao usuário, no caso o cliente do banco. No rodapé, mostrará o saldo em R$ do cliente. E no meio da tela, apresentará 4 botões: Depósito, Saque, Extrato e Sair. Cada um com suas respectivas funções.




Então fiz um esboço de como eu queria que ficasse a interface do programa.





Esse foi meu esboço da interface que fiz no Paint:





(eu prometo que o resultado final vai ficar melhor que isso...)





<div align="center">
<img src="https://github.com/IsacFreitaas/projeto-sistema-simples-em-python/assets/65254733/8a5dc1fd-e951-4915-9e92-7aee80d669f0" width="600px" />
</div>



O código ficou assim: 

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


*Note que cada botão tem sua respectiva linha (row), para sempre manter a organização





Agora defino as variáveis do sistema e o saldo do usuário na interface:

          # Variáveis do sistema
          self.saldo = 0 # Saldo Inicial
          self.historico_transacoes = list() # Usei list() dessa forma para identificar se já houveram ou não transações.
          self.limite_saque_diario = 1500.00
          self.contador_saques = 0 # Inicia em 0

          # Atualização do saldo na interface
          self.label_saldo = tk.Label(self.main_frame, text=f"Saldo: R${self.saldo:.2f}", font=self.font_style)
          self.label_saldo.grid(row=5, column=0, columnspan=2, pady=10)


-----------------------
### Parte 3:
-----------------------

Criei as seguintes funções:

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

def deposito -> Solicita o valor do depósito ao usuário e valida se o valor é positivo. Então adiciona o valor ao saldo e atualiza o histórico de transações.

def saque -> Verifica se o limite de saques diários não foi atingido, solicita o valor do saque ao usuário, valida se o valor é positivo e se o saldo é suficiente, então subtrai o valor do saldo e atualiza o histórico de transações então mostra uma mensagem de sucesso ou erro ao usuário.
    
def extrato -> Verifica se há histórico de transações. Mostra o saldo atual e o histórico de transações ao usuário. Mostra uma mensagem informando que não há histórico se não houver transações.



---------------------------





Resultado final:




<div align="center">
<img src="https://github.com/IsacFreitaas/projeto-sistema-simples-em-python/assets/65254733/2bd6c1e4-66c3-45d2-a1a4-60d3369c258d" width="800px" />
</div>





O resultado ficou simples, mas funcionando corretamente.


<div align="center">
<video src="https://github.com/IsacFreitaas/projeto-sistema-simples-em-python/assets/65254733/5a9fef75-7ac9-4ed2-aa55-a63fb1570b37"></video>
</div>


Então básicamente, é isso.




Você pode conferir o resultado desse projeto no arquivo "sistema_bancario_projeto.py".




Obrigado por me acompanhar nestes testes até aqui!

--------------------------

Então é isso.

# Este foi o meu primeiro projeto em Python, em meus estudos em Ciência de Dados.





Obrigado pela atenção!





--------------------------

Sobre mim:
# Isac Freitas
Estudante de Ciência de Dados e Inteligência Artificial.

### Me encontre:

Insta: @isac.sfreitas



Twitter: @isaczeitgeist
