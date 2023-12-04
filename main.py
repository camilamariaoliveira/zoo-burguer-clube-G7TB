class ZooBurguerClube:
    def __init__(self):
        self.contador_clientes = 1
        self.pontos_cadastro = 0
        self.recompensas = {
            '1': {'recompensa': 'Brownie', 'pontos': 70},
            '2': {'recompensa': 'Batata Frita', 'pontos': 75},
            '3': {'recompensa': 'Batata Frita + Refri', 'pontos': 100},
            '4': {'recompensa': 'Milk-Shake', 'pontos': 150},
            '5': {'recompensa': 'Sanduíche ELERU', 'pontos': 150},
            '6': {'recompensa': 'Cupom Entrega Grátis', 'pontos': 175},
            '7': {'recompensa': 'Sanduíche SUPERZOO', 'pontos': 200},
            '8': {'recompensa': 'ELERU + Milk-Shake', 'pontos': 250},
            '9': {'recompensa': 'SUPERZOO + Milk-Shake', 'pontos': 275},
            '10': {'recompensa': 'Sanduíche ZOO ESPECIAL', 'pontos': 300},
            '11': {'recompensa': 'ZOO ESPECIAL + Milk-Shake', 'pontos': 350},
            '12': {'recompensa': 'ZOO ESPECIAL + ELERU', 'pontos': 350},
            '13': {'recompensa': 'Combo completo (1,2 ou 3)', 'pontos': 400}
        }
        self.cardapio = {
            '1': {'nome': 'ELERU', 'preco': 11.9, 'descricao': 'Pão bola, 70 gramas de filé de frango, queijo, bacon e verdura'},
            '2': {'nome': 'ZOO ESPECIAL', 'preco': 20.5, 'descricao': 'Pão bola, 70 gramas de filé mignon, queijo, presunto, ovo, bacon crocante, creme de milho especial, alface e tomate'},
            '3': {'nome': 'SUPERZOO', 'preco': 13.9, 'descricao': 'Pão bola, 70 gramas de filé de frango, queijo, presunto, ovo, bacon crocante, creme de milho especial, alface e tomate'},
            '4': {'nome': 'ZOOPICANHA', 'preco': 15.5, 'descricao': 'Pão bola, 70 gramas de filé de picanha, calabresa, alface e tomate'},
            '5': {'nome': 'URSAURO', 'preco': 15.9, 'descricao': 'Pão bola, 70 gramas de carne de hambúrguer artesanal de picanha com bacon, queijo, calabresa, creme de milho especial, alface e tomate'},
            '6': {'nome': 'Batata frita', 'preco': 6.0},
            '7': {'nome': 'Milk-Shake', 'preco': 12.0},
            '8': {'nome': 'Refrigerante', 'preco': 10.0}
        }
        self.pagamentos = {
            '1': {'tipo': 'Cartão'},
            '2': {'tipo': 'Pix'},
            '3': {'tipo': 'Dinheiro'}
        }

    #MANIPULAÇÕES DE ARQUIVO
    def ler_clientes(self):
      try:
        with open('clientes.txt', 'r') as db_clientes:
            return [cliente.strip().split(";") for cliente in db_clientes]
      except (FileNotFoundError, IOError) as e:
        print("Problema no banco de dados, Dados não foram encontrados")

    def inserir_cliente(self, dados):
      try:
        with open('clientes.txt', 'a') as db_clientes:
            db_clientes.write(";".join(dados) + "\n")
      except (IOError, PermissionError) as e:
          print(f"Erro ao inserir cliente: {e}")

    def persistencia_clientes(self, dados):
        try:
          with open('clientes.txt', 'w') as db_clientes:
              for cliente in dados:
                  db_clientes.write(";".join(cliente) + "\n")
        except (IOError, PermissionError) as e:
            print(f"Erro na persistência dos dados: {e}")

    def pode_cadastrar(self, cpf):
        clientes_cadastrados = self.ler_clientes()
        return any(cliente[2] == cpf for cliente in clientes_cadastrados)

    #ÚTEIS
    def verificar_preenchimento(self, dado):
        if dado.isspace() or dado == "":
            print("Preencha com uma informação válida")
            return True
        else:
            return False

    def tratar_string(self, dado):
        dado_sem_espacos = dado.strip()
        dado_sem_ponto_ou_virgula = dado_sem_espacos.strip(",.")
        dado_tudo_minusculo = dado_sem_ponto_ou_virgula.casefold()
        return dado_tudo_minusculo

    def solicitar_cpf(self):
        cpf = str(input('Digite seu CPF, apenas números e sem espaços: '))
        while self.verificar_preenchimento(cpf) :
            cpf = str(input('CPF inválido ou em branco. Digite seu CPF, apenas números e sem espaços: '))
        return self.tratar_string(cpf)

    def solicitar_nome(self):
        nome = str(input('Como prefere ser chamado? '))
        while self.verificar_preenchimento(nome):
            nome = str(input('Como prefere ser chamado? '))
        return self.tratar_string(nome)

    def solicitar_email(self):
        email = str(input('Digite o seu melhor e-mail: '))
        while self.verificar_preenchimento(email):
            email = str(input('Digite o seu melhor e-mail: '))
        return self.tratar_string(email)

    def solicitar_senha(self):
        senha = str(input('Digite uma senha: '))
        while self.verificar_preenchimento(senha):
            senha = str(input('Digite uma senha: '))
        return senha

    #CREATE
    def cadastrar_cliente(self):
      try:
        cpf = self.solicitar_cpf()

        if self.pode_cadastrar(cpf):
            print("Você já possui cadastro! Vamos te reecaminharpara o login!")
            return self.realizar_login()

        else:
            nome = self.solicitar_nome()
            email = self.solicitar_email()
            senha = self.solicitar_senha()

            id_cliente = str(self.contador_clientes)
            pontos = str(self.pontos_cadastro)

            dados = [id_cliente, nome, cpf, email, senha, pontos]

            self.inserir_cliente(dados)
            self.contador_clientes += 1
            print("Cadastrado com Sucesso!")
            return dados
      except Exception as e:
        print(f"Erro ao cadastrar: {e}")

    #READ
    def cliente_por_id(self):
        id_atual = str(input('Digite o ID do cliente que deseja analisar: '))
        clientes_cadastrados = self.ler_clientes()

        encontrado = False
        for cliente in clientes_cadastrados:
            if cliente[0] == id_atual:
                print(cliente)
                encontrado = True
                break

        if not encontrado:
            print(f"Cliente com ID {id_atual} não encontrado.")

    #UPDATE
    def atualizar_cliente(self):
        id_atual = str(input('Digite o ID que deseja atualizar: '))
        clientes_cadastrados = self.ler_clientes()

        encontrado = False
        for i, cliente in enumerate(clientes_cadastrados):
            if cliente[0] == id_atual:
                nome = self.solicitar_nome()
                email = self.solicitar_email()
                senha = self.solicitar_senha()

                pontos = cliente[5]
                dados = [cliente[0], nome, cliente[2], email, senha, pontos]
                clientes_cadastrados[i] = dados
                self.persistencia_clientes(clientes_cadastrados)

                encontrado = True
                print("Dados Atualizados com sucesso!")
                break

        if not encontrado:
            print(f"Cliente com ID {id_atual} não encontrado.")

    #DELETE
    def remover_cliente(self):
        id_cliente = str(input('Digite o ID que deseja remover o cadastro: '))
        clientes_cadastrados = self.ler_clientes()

        removido = False
        for cliente in clientes_cadastrados:
            if cliente[0] == id_cliente:
                clientes_cadastrados.remove(cliente)
                self.persistencia_clientes(clientes_cadastrados)
                removido = True
                print(f"Cadastro do cliente com ID {id_cliente} removido com sucesso.")
                break

        if not removido:
            print(f"Cliente com ID {id_cliente} não encontrado.")

    #LOGIN
    def realizar_login(self):
        cpf = self.solicitar_cpf()
        senha = self.solicitar_senha()

        autentica = self.ler_clientes()
        for verificacao in autentica:
            if verificacao[2] == cpf and verificacao[4] == senha:
                print(f"Login realizado com sucesso!\n Olá {verificacao[1].title()}, você possui um saldo de {verificacao[5]} pontos")
                return verificacao

        print("Falha no login. Verifique suas credenciais.")
        return False

    #PONTOS
    def exibir_recompensas(self):
        for item, recompensa_pontos in self.recompensas.items():
            print(f"{item}: {recompensa_pontos['recompensa']} - Pontos Necessário: {recompensa_pontos['pontos']:.2f}")

    def calcular_credito_de_pontos(self, saldo_de_pontos, total_pedido):
      try:
        resultado = float(saldo_de_pontos) + float(total_pedido)
        if resultado >= 0:
            print(f"\nApós finalizar o pedido, o seu saldo será de {resultado} pontos")
            return resultado
        else:
            print("Você não possui pontos suficientes")
            return False
      except (ValueError, TypeError) as e:
        print(f"Erro no cálculo de pontos: {e}")
        return False

    def calcular_pontos_suficientes(self, pontos_necessarios, saldo_de_pontos):
      try:
        resultado = float(saldo_de_pontos) - float(pontos_necessarios)
        if resultado >= 0:
            print(f"\nApós finalizar o pedido, o seu saldo será de {resultado} pontos")
            return resultado
        else:
            print("Você não possui pontos suficientes")
            return False
      except (ValueError, TypeError) as e:
        print(f"Erro no cálculo de pontos: {e}")
        return False

    def resgatar_recompensas(self, id_cliente, saldo_de_pontos):
        resgates = {}
        while True:
            escolha = str(input("Digite o número do item desejado (ou 'S' para sair): "))
            if escolha.upper() == 'S':
                break
            if escolha in self.recompensas:
                resgates[self.recompensas[escolha]['recompensa']] = { 'recompensa': self.recompensas[escolha]['recompensa'] , 'pontos': self.recompensas[escolha]['pontos']}
                #verifica pontos necessários uma função
                pontos_necessarios =[self.recompensas[escolha]['pontos']]

                pontos_suficientes = self.calcular_pontos_suficientes(pontos_necessarios[0], saldo_de_pontos)

                if pontos_suficientes >=0:
                    self.atualizar_pontos(id_cliente, pontos_suficientes)
                    print("Pronto, sua recompensa foi resgatada!")
                    return resgates

            else:
                print("Opção inválida. Você parece não ter pontos suficientes.")

    def atualizar_pontos(self, id_atual, novo_saldo):
        clientes_cadastrados = self.ler_clientes()
        atualizado = False
        for i, cliente in enumerate(clientes_cadastrados):
            if cliente[0] == id_atual:
              pontos = str(novo_saldo)
              dados = [cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], pontos]
              clientes_cadastrados[i] = dados
              self.persistencia_clientes(clientes_cadastrados)
              atualizado = True
              print("O seu saldo de pontos já foi atualizado!")
              break

        if not atualizado:
            print(f"Cliente com ID {id_atual} não encontrado. Tente logar novamente e recomerçar")


    #PEDIDOS
    def exibir_cardapio(self):
        for item, nome_preco in self.cardapio.items():
            print(f"{item}: {nome_preco['nome']} - R${nome_preco['preco']:.2f}")

    def fazer_pedido(self):
        pedido = {}
        while True:
            self.exibir_cardapio()
            escolha = str(input("Digite o número do item desejado (ou 'S' para sair): "))
            if escolha.upper() == 'S':
                break

            if escolha in self.cardapio:
                quantidade = int(input(f"Quantidade de {self.cardapio[escolha]['nome']}: "))
                pedido[self.cardapio[escolha]['nome']] = {'quantidade': quantidade, 'preco': self.cardapio[escolha]['preco']}
            else:
                print("Opção inválida. Tente novamente.")

        return pedido

    def calcular_total(self, pedido):
        total = 0
        for item, qtd_preco in pedido.items():
            total += qtd_preco['quantidade'] * qtd_preco['preco']
        return total


    #PAGAMENTOS
    def exibir_metodos_pagamento(self):
        for item, valor in self.pagamentos.items():
            print(f"{item} - {valor['tipo']}")
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
          print('Esperando Aprovação do Pagamento em Cartão')
        elif opcao == 2:
          print('Esperando Operação Pix')
        elif opcao == 3:
          pagamento = int(input('Precisa de troco para quanto? '))
          print('Agora é só aguardar, pagamento será realizado na entrega!')
        else:
          print('Opção inválida!')

    #MAIN

    def main(self):
        dados_cliente =self.cadastrar_cliente()

        resgate = {}
        if float(dados_cliente[5]) > 0:
           self.exibir_recompensas()
           resgate = self.resgatar_recompensas(dados_cliente[0], dados_cliente[5])

        print("Realize seu pedido:")

        pedido = self.fazer_pedido()
        total = self.calcular_total(pedido)

        pontos_gerados = self.calcular_credito_de_pontos(dados_cliente[5],total)

        print("\nResumo do Pedido:")
        if resgate:
          for item, recompensa_pontos in resgate.items():
            print(f"Resgate de recompensas: {recompensa_pontos['recompensa']} - {recompensa_pontos['pontos']} pontos.")
        for item, qtd_preco in pedido.items():
            print(f"{qtd_preco['quantidade']}x {item} - R${qtd_preco['preco']:.2f} cada")

        print(f"\nTotal do Pedido: R${total:.2f}")
        self.exibir_metodos_pagamento()

        pagamento_aprovado = str(input('aguardando confirmação'))

        if pagamento_aprovado:
          print("Pagamento Aprovado, Seu pedido está sendo preparado!")
          self.atualizar_pontos(dados_cliente[0],pontos_gerados)
        else:
          print('Parece que sua compra não foi aprovada, tente novamente!')


sistema_restaurante = ZooBurguerClube()
sistema_restaurante.main()