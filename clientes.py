contador_clientes = 1

def ler_clientes():
  db_clientes = open("clientes.txt","r")
  clientes_cadastrados = db_clientes.readlines()
  clientes_cadastrados = [cliente.strip().split(";") for cliente in clientes_cadastrados ]
  db_clientes.close()
  return clientes_cadastrados

def inserir_cliente(dados):
  db_clientes = open("clientes.txt","a")
  formatando_dados = ";".join(dados)
  db_clientes.writelines(formatando_dados,"\n")
  db_clientes.close()

def persistencia_clientes(dados):
  db_clientes = open("clientes.txt","w")
  formatando_dados = ";".join(dados)
  db_clientes.writelines(formatando_dados,"\n")
  db_clientes.close()

def pode_cadastrar(cpf):
  clientes_cadastrados = ler_clientes()
  for cliente in clientes_cadastrados:
    if cliente[2] == cpf:
      print("Você já possui cadastro, tente fazer login!")
      return True
    
def login():
  cpf = str(input('Digite seu cpf: '))
  senha = str(input('Digite sua senha: '))
  autentica = ler_clientes()
  for verificacao in autentica:
    if (verificacao[2] == cpf) & (verificacao[4] == senha):
      print("Login realizado com sucesso!")
      return verificacao[0]
    
def verificar_prenchimento(dado):
  if dado.isspace() or dado == "":
    print("Preencha com uma informação válida")
    return True
  else:
    return False
  
def tratar_string(dado):
  dado_sem_espacos = dado.strip()
  dado_sem_ponto_ou_virgula = dado_sem_espacos.strip(",.")
  dado_tudo_minusculo = dado_sem_ponto_ou_virgula.casefold()
  return dado_tudo_minusculo

#CREATE
def cadastrar_cliente():
    cpf = str(input('Digite seu cpf, apenas numeros e sem espaços: '))
    while verificar_prenchimento(cpf):
        cpf = str(input('Digite seu cpf, apenas numeros e sem espaços: '))
    cpf = tratar_string(cpf)

    if pode_cadastrar(cpf):
        senha = str(input('Digite sua senha: '))
        autentica = ler_clientes()
    for verificacao in autentica:
        if (verificacao[2] == cpf) & (verificacao[4] == senha):
            print("Login realizado com sucesso!")
    else:
        nome = str(input('Como prefere ser chamado? '))
        while verificar_prenchimento(nome):
            nome = str(input('Como prefere ser chamado? '))
        nome = tratar_string(nome)

        email = str(input('Digite o seu melhor email: '))
        while verificar_prenchimento(email):
            email = str(input('Digite o seu melhor email: '))
        email = tratar_string(email)

        senha = str(input('Digite uma senha: '))
        while verificar_prenchimento(senha):
            senha = str(input('Digite uma senha: '))

        id = str(contador_clientes)
        dados = [id, nome, cpf, email, senha]

        inserir_cliente(dados)
        contador_clientes = contador_clientes + 1
        print("Cadastrado com Sucesso")

#READ
def cliente_por_id():
    id_atual = str(input('Digite o id do cliente que deseja analisar: '))
    clientes_cadastrados = ler_clientes()
    for cliente in clientes_cadastrados:
        if cliente[0] == id_atual:
            print(cliente)

#UPDATE
def atualizar_cliente():
    clientes_cadastrados = ler_clientes()
    id_atual = str(input('Digite o id que deseja atualizar: '))
    for cliente in clientes_cadastrados:
        if cliente[0] == id_atual:
            nome = str(input('Como prefere ser chamado? '))
            while verificar_prenchimento(nome):
                nome = str(input('Como prefere ser chamado? '))
            nome = tratar_string(nome)

            email = str(input('Digite o seu melhor email: '))
            while verificar_prenchimento(email):
                email = str(input('Digite o seu melhor email: '))
            email = tratar_string(email)

            senha = str(input('Digite uma senha: '))
            while verificar_prenchimento(senha):
                senha = str(input('Digite uma senha: '))

            dados = [cliente[0], nome, cliente[2], email, senha]
            clientes_cadastrados.remove(cliente)
            clientes_cadastrados.append(dados)
            persistencia_clientes(clientes_cadastrados)
            print("Dados Atualizados com sucesso!")

#DELETE
def remover_cliente():
    clientes_cadastrados = ler_clientes()
    id_cliente = str(input('Digite o id que deseja remover o cadastro: '))
    for cliente in clientes_cadastrados:
        if cliente[0] == id_cliente:
            clientes_cadastrados.remove(cliente)
            for cliente in clientes_cadastrados:
                inserir_cliente(cliente)