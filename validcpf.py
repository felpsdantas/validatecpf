import os
from flask import Flask, request, jsonify
from flask_cors import CORS
os.environ.get('KEY')

app = Flask(__name__)
CORS(app)


#Funçao para verificar os cpf
def valida_cpf(cpf):
    # Remove caracteres não numericos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF possui 11 digitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro digito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11) if soma % 11 >= 2 else 0

    # Calcula o segundo digito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11) if soma % 11 >= 2 else 0

    # Verifica se os digitos verificadores estão corretos
    return int(cpf[9]) == digito1 and int(cpf[10]) == digito2


@app.route('/validar_cpf', methods=['GET'])
# Obtém o parametro 'cpf' da requisição GET. Se não estiver presente, usa uma string vazia.
def validar_cpf_rota():
    cpf_param = request.args.get('cpf', '')

    if valida_cpf(cpf_param):
        resultado = {'valido': True, 'mensagem': 'CPF válido'}
    else:
        resultado = {'valido': False, 'mensagem': 'CPF inválido'}

    return jsonify(resultado)


if __name__ == '__main__':
    app.run(debug=True, port=8000)

