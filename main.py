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

    def ler_clientes(self):
        with open('clientes.txt', 'r') as db_clientes:
            return [cliente.strip().split(";") for cliente in db_clientes]

    def inserir_cliente(self, dados):
        with open('clientes.txt', 'a') as db_clientes:
            db_clientes.write(";".join(dados) + "\n")

    def persistencia_clientes(self, dados):
        with open('clientes.txt', 'w') as db_clientes:
            db_clientes.writelines(";".join(cliente) + "\n" for cliente in dados)

    def pode_cadastrar(self, cpf):
        clientes_cadastrados = self.ler_clientes()
        return any(cliente[2] == cpf for cliente in clientes_cadastrados)
    
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

    def cadastrar_cliente(self):
        cpf = str(input('Digite seu CPF, apenas números e sem espaços: '))
        while self.verificar_preenchimento(cpf):
            cpf = str(input('Digite seu CPF, apenas números e sem espaços: '))
        cpf = self.tratar_string(cpf)

        if self.pode_cadastrar(cpf):
            print("Você já possui cadastro, tente fazer login!")
            senha = str(input('Digite sua senha: '))
            autentica = self.ler_clientes()
            for verificacao in autentica:
                if verificacao[2] == cpf and verificacao[4] == senha:
                    print("Login realizado com sucesso!")
                    return verificacao[0]
        else:
            nome = str(input('Como prefere ser chamado? '))
            while self.verificar_preenchimento(nome):
                nome = str(input('Como prefere ser chamado? '))
            nome = self.tratar_string(nome)

            email = str(input('Digite o seu melhor e-mail: '))
            while self.verificar_preenchimento(email):
                email = str(input('Digite o seu melhor e-mail: '))
            email = self.tratar_string(email)

            senha = str(input('Digite uma senha: '))
            while self.verificar_preenchimento(senha):
                senha = str(input('Digite uma senha: '))

            id_cliente = str(self.contador_clientes)
            pontos = str(self.pontos_cadastro)
            dados = [id_cliente, nome, cpf, email, senha, pontos]

            self.inserir_cliente(dados)
            self.contador_clientes += 1
            print("Cadastrado com Sucesso!")
        

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
        

    def atualizar_cliente(self):
        id_atual = str(input('Digite o ID que deseja atualizar: '))
        clientes_cadastrados = self.ler_clientes()
        
        encontrado = False
        for i, cliente in enumerate(clientes_cadastrados):
            if cliente[0] == id_atual:
                nome = str(input('Como prefere ser chamado? '))
                while self.verificar_preenchimento(nome):
                    nome = str(input('Como prefere ser chamado? '))
                nome = self.tratar_string(nome)

                email = str(input('Digite o seu melhor e-mail: '))
                while self.verificar_preenchimento(email):
                    email = str(input('Digite o seu melhor e-mail: '))
                email = self.tratar_string(email)

                senha = str(input('Digite uma senha: '))
                while self.verificar_preenchimento(senha):
                    senha = str(input('Digite uma senha: '))

                dados = [cliente[0], nome, cliente[2], email, senha]
                clientes_cadastrados[i] = dados
                self.persistencia_clientes(clientes_cadastrados)
                encontrado = True
                print("Dados Atualizados com sucesso!")
                break

        if not encontrado:
            print(f"Cliente com ID {id_atual} não encontrado.")
   

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

    def realizar_login(self):
        cpf = str(input('Digite seu CPF: '))
        senha = str(input('Digite sua senha: '))

        autentica = self.ler_clientes()
        for verificacao in autentica:
            if verificacao[2] == cpf and verificacao[4] == senha:
                print("Login realizado com sucesso!")
                return {'id': verificacao[0], 'Pontos Acumulados': verificacao[5]}

        print("Falha no login. Verifique suas credenciais.")
        return None

    def exibir_recompensas(self):
        for item, recompensa_pontos in self.recompensas.items():
            print(f"{item}: {recompensa_pontos['recompensa']} - Pontos Necessário: {recompensa_pontos['pontos']:.2f}")

    def calcular_pontos_suficientes(self, pontos_necessarios):
        cpf = str(input('Digite seu CPF: '))
        senha = str(input('Digite sua senha: '))

        autentica = self.ler_clientes()
        for verificacao in autentica:
            if verificacao[2] == cpf and verificacao[4] == senha:
                print("Autenticado com sucesso!")
                resultado = float(verificacao[5]) - float(pontos_necessarios)
                if resultado >= 0:
                    return True
                else:
                    print("Falha na autenticação OU Você não possui pontos suficientes")
                    return False

    def resgatar_recompensas(self):
        while True:
            escolha = str(input("Digite o número do item desejado (ou 'S' para sair): "))
            if escolha.upper() == 'S':
                break
            if escolha in self.recompensas:
                pontos_necessarios =[self.recompensas[escolha]['pontos']]
                self.calcular_pontos_suficientes(pontos_necessarios) 
            else:
                print("Opção inválida. Tente novamente.")

            print("teste")

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

    def main(self):
        self.cadastrar_cliente()
        clientes = self.ler_clientes()
        for cliente in clientes:
            print(cliente)
        print("Realize seu pedido:")
        pedido = self.fazer_pedido()
        total = self.calcular_total(pedido)

        print("\nResumo do Pedido:")
        for item, qtd_preco in pedido.items():
            print(f"{qtd_preco['quantidade']}x {item} - R${qtd_preco['preco']:.2f} cada")

        print(f"\nTotal do Pedido: R${total:.2f}")

sistema_restaurante = ZooBurguerClube()
sistema_restaurante.main()