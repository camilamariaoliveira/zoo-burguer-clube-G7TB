from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá, Esse é o Aplicativo da Zoo Burguer Clube!'

@app.route('/cliente',methods = ["POST"])
def cadastrar():
    contador_clientes = 1
    dados = request.get_json()
    cliente = {
        "id": str(contador_clientes),
        "cpf": dados.get("cpf"),
        "nome": dados.get("nome"),
        "email": dados.get("email"),
        "senha": dados.get("senha")
    }
    formatando_dados = ";".join(str(value) for value in cliente.values()) + "\n"
    with open("clientes.txt", "a") as db_clientes:
        db_clientes.write(formatando_dados)
    contador_clientes += 1
    return jsonify("Cadastro realizado com sucesso"),200

@app.route('/clientes')
def ler_registros():
    with open('clientes.txt', 'r') as db_clientes:
        registros = [linha.strip().split(';') for linha in db_clientes.readlines()]
        db_clientes.close()
        return jsonify(registros),200

@app.route('/cliente<id>')
def ler_registro_por_id(id):
    with open('clientes.txt', 'r') as db_clientes:
        for cliente in db_clientes:
            registro = cliente.strip().split(';')
            if registro[0] == str(id):
                db_clientes.close()
                return jsonify(registro),200
    db_clientes.close()
    return None

@app.route('/cliente<id>',methods = ["POST"])
def atualizar_cliente(id):
    dados = request.get_json()
    novos_dados = {
        "cpf": dados.get("cpf"),
        "nome": dados.get("nome"),
        "email": dados.get("email"),
        "senha": dados.get("senha")
    }
    formatando_dados = ";".join(str(value) for value in novos_dados.values()) + "\n"
    with open('clientes.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
    
    encontrado = False
    with open('clientes.txt', 'w') as arquivo:
        for linha in linhas:
            registro = linha.strip().split(';')
            if registro[0] == str(id):
                arquivo.write(formatando_dados)
                encontrado = True
            else:
                arquivo.write(linha)
    
    if encontrado:
        return jsonify("Atualizado com sucesso"), 200
    else:
        return jsonify("Cliente não encontrado"), 404

@app.route('/remove<id>')
def remover_cliente(id):
    with open('clientes.txt', 'r') as db_clientes:
        linhas = db_clientes.readlines()

    with open('clientes.txt', 'w') as arquivo:
        removido = False
        for linha in linhas:
            registro = linha.strip().split(';')
            if registro[0] != str(id):
                arquivo.write(linha)
            else:
                removido = True

        if removido:
            return jsonify("Cliente removido com sucesso"), 200
        else:
            return jsonify("Cliente não encontrado"), 404

if __name__ == '__main__':
    app.run(debug=True)