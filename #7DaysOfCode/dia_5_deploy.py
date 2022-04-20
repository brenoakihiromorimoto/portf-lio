import numpy as np
import joblib
import pickle
from flask import Flask, request, jsonify
import os
import surprise

app = Flask(__name__)

modelo = pickle.load(open('C:/Users/Akihiro/Desktop/TERA/7_days_of_code/deploy/modelo_finalizado.pk1', 'rb'))

@app.route('/')
def verificar_api_online():
    return 'api online', 200

@app.route('/previsão', methods=['POST'])
def previsão():
    dados = request.get_json(force=True)
    previsão = modelo.predict(np.array([list(dados.values())]))
    resultado=previsão[0]
    resposta = {'Previsão da Avaliação do Filme': resultado}
    return jsonify(resposta)

if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)