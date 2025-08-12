from flask import Flask, request, jsonify
# Importe o CORS da biblioteca
from flask_cors import CORS
from mock_sheets import consulta_agencia
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app)

@app.route('/consultar-dados', methods=['GET'])
def get_dados_planilha():
    agency = request.args.get('agency')
    bank = request.args.get('bank')
    
    if not all([agency, bank]):
        return jsonify({"error": "Parâmetros 'agency' e 'bank' são obrigatórios."}), 400

    dados = consulta_agencia(agency, bank)

    if dados is not None:
        return jsonify(dados)
    else:
        # A resposta abaixo é mais apropriada, usando status 404 (Not Found)
        # para indicar que os dados específicos não foram encontrados.
        return jsonify({"error": "Dados para a agência e banco não encontrados."}), 404