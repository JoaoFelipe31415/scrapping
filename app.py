from flask import Flask, request, jsonify, Response
from mock_sheets import consulta_agencia
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/consultar-dados', methods=['GET'])
def get_dados_planilha():
    # Pega os parâmetros da requisição HTTP (ex: /consultar-dados?planilha=MinhaPlanilha&aba=Sheet1&query=termo)
    agency = request.args.get('agency')
    bank = request.args.get('bank')
    if not all([agency,bank]):
        return jsonify({"error": "Parâmetros 'agency' e 'bank' são obrigatórios."}), 400

    dados = consulta_agencia(agency,bank)

    if dados is not None:
            return Response(
                json.dumps(dados, ensure_ascii=False),
                content_type='application/json; charset=utf-8'
            )
    else:
        return jsonify({"error": "Não foi possível consultar a planilha."}), 500    