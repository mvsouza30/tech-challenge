import psycopg2
import os
import uuid
import mercadopago
from validate_docbr import CPF
from flask import Flask, request, jsonify, render_template, redirect
from dotenv import load_dotenv
from adaptadores.adaptador_acompanhamentos import recebe_info_acompanhamentos
from adaptadores.adaptador_bebidas import recebe_info_bebidas
from dominio.repositorio_acompanhamentos import servico_acompanhamentos
from dominio.repositorio_bebidas import servico_bebidas
from dominio.servico_criar_pagamento import MercadoPagoService

app = Flask(__name__, static_folder='static')

# Definição da string de conexão com o banco de dados
url_conexao = 'postgresql://postgres:C0n3ct4@db:5432/qtop_db'

# Carregando as variáveis de ambiente
load_dotenv()

#Conectando ao banco de dados
conexao = psycopg2.connect(url_conexao)

# Rota para pagina inicial
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validar-cpf', methods=['POST'])
def validar_cpf():
    cpf = request.form["cpf"]

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM qtop_clientes WHERE cliente_cpf = %s", (cpf,))
    cliente = cursor.fetchone()
    cursor.close()

    if cliente:
        return redirect("/lanches")
    else:
        return "CPF inválido"

@app.route("/lanches")
def cardapio():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM qtop_lanches")

    lanches = []
    for lanche in cursor.fetchall():
        lanches.append({
            'lanche_nome': lanche[1],
            'lanche_descricao': lanche[2],
            'lanche_preco': lanche[3],
            'lanche_foto': lanche[4]
        })
    cursor.close()

    return render_template('lanches.html', lanches=lanches)


@app.route("/acompanhamentos")
def acompanhamentos():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM qtop_acompanhamentos")

    acompanhamentos = []
    for acompanhamento in cursor.fetchall():
        acompanhamentos.append({
            'acomp_nome': acompanhamento[1],
            'acomp_descricao': acompanhamento[2],
            'acomp_preco': acompanhamento[3],
            'acomp_foto': acompanhamento[4]
        })
    cursor.close()

    return render_template('acompanhamentos.html', acompanhamentos=acompanhamentos)

@app.route("/bebidas")
def bebidas():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM qtop_bebidas")

    bebidas = []
    for bebida in cursor.fetchall():
        bebidas.append({
            'bebida_nome': bebida[1],
            'bebida_descricao': bebida[2],
            'bebida_preco': bebida[3],
            'bebida_foto': bebida[4]
        })
    cursor.close()

    return render_template('bebidas.html', bebidas=bebidas)

@app.route("/sobremesas")
def sobremesas():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM qtop_sobremesas")

    sobremesas = []
    for sobremesa in cursor.fetchall():
        sobremesas.append({
            'sobrem_nome': sobremesa[1],
            'sobrem_descricao': sobremesa[2],
            'sobrem_preco': sobremesa[3],
            'sobrem_foto': sobremesa[4]
        })
    cursor.close()

    return render_template('sobremesas.html', sobremesas=sobremesas)

@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    email = request.form.get('email')

    # Cadastrar cliente
    try:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO qtop_clientes (cliente_nome, cliente_cpf, cliente_email) VALUES (%s, %s, %s)", (nome, cpf, email))

        conexao.commit()
        cursor.close()

        # Redirecionar para a página cardápio
        return render_template('confirmacao.html')

    except psycopg2.Error as e:
        # Tratar algum erro que possa ocorrer ao inserir os dados no banco
        print(f"Erro ao cadastrar: {e}")

@app.route('/confirmacao')
def confirmacao():
        return render_template('confirmacao.html')


@app.route('/adicionar_acompanhamento', methods=['POST'])
def adicionar_acompanhamento():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    preco = float(request.form.get('preco'))
    foto = request.files.get('foto')

    nome_arquivo = foto.filename

    caminho_arquivo = os.path.join('static', nome_arquivo)
    foto.save(caminho_arquivo)

    cursor = conexao.cursor()
    cursor.execute("INSERT INTO qtop_acompanhamentos (acomp_nome, acomp_descricao, acomp_preco, acomp_foto) VALUES (%s, %s, %s, %s)",
                   (nome, descricao, preco, nome_arquivo))
    conexao.commit()
    cursor.close()

    return render_template('confirmo_insercao.html')


@app.route('/adicionar_bebida', methods=['POST'])
def adicionar_bebida():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    preco = float(request.form.get('preco'))
    foto = request.files.get('foto')
    nome_arquivo = foto.filename

    caminho_arquivo = os.path.join('static', nome_arquivo)
    foto.save(caminho_arquivo)

    cursor = conexao.cursor()
    cursor.execute("INSERT INTO qtop_bebidas (bebida_nome, bebida_descricao, bebida_preco, bebida_foto) VALUES (%s, %s, %s, %s)",
                   (nome, descricao, preco, nome_arquivo))
    conexao.commit()
    cursor.close()

    return render_template('confirmo_insercao.html')


@app.route('/adicionar_lanche', methods=['POST'])
def adicionar_lanche():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    preco = float(request.form.get('preco'))
    foto = request.files.get('foto')
    nome_arquivo = foto.filename

    caminho_arquivo = os.path.join('static', nome_arquivo)
    foto.save(caminho_arquivo)

    cursor = conexao.cursor()
    cursor.execute("INSERT INTO qtop_lanches (lanche_nome, lanche_descricao, lanche_preco, lanche_foto) VALUES (%s, %s, %s, %s)",
                   (nome, descricao, preco, nome_arquivo))
    conexao.commit()
    cursor.close()

    return render_template('confirmo_insercao.html')


@app.route('/adicionar_sobremesa', methods=['POST'])
def adicionar_sobremesa():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    preco = float(request.form.get('preco'))
    foto = request.files.get('foto')
    nome_arquivo = foto.filename

    caminho_arquivo = os.path.join('static', nome_arquivo)
    foto.save(caminho_arquivo)

    cursor = conexao.cursor()
    cursor.execute("INSERT INTO qtop_sobremesas (sobrem_nome, sobrem_descricao, sobrem_preco, sobrem_foto) VALUES (%s, %s, %s, %s)",
                   (nome, descricao, preco, nome_arquivo))
    conexao.commit()
    cursor.close()

    return render_template('confirmo_insercao.html')



@app.route('/confirmo_insercao')
def confirmo_insercao():
    return render_template('confirmo_insercao.html')


@app.route("/additens")
def additens():
    return render_template('additens.html')

mercado_pago_service = MercadoPagoService()

@app.route('/finalizar_pedido', methods=['POST'])
def finalizar_pedido():
    pagamento_data = request.get_json()

    try:
        pagamento = mercado_pago_service.criar_pagamento(pagamento_data)
        return jsonify(pagamento)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/buscar_pagamentos', methods=['GET'])
def buscar_pagamentos():
    external_reference = request.args.get('external_reference')

    try:
        pagamentos = mercado_pago_service.buscar_pagamentos(external_reference)
        return jsonify(pagamentos)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
