from flask import Flask, request, jsonify
from flask_cors import CORS
import inspect


app = Flask(__name__)
CORS(app)


from flask import request, jsonify
import inspect

def validar_cpf_rota():
    cpf_param = request.args.get('cpf', '')

    # Obtém a assinatura da função valida_cpf
    signature = inspect.signature(valida_cpf)

    # Obtém os parâmetros da função valida_cpf
    parameters = signature.parameters

    # Verifica se o parâmetro 'cpf' está presente na assinatura
    if 'cpf' in parameters:
        # Chama a função valida_cpf com o parâmetro 'cpf'
        if valida_cpf(cpf_param):
            resultado = {'valido': True, 'mensagem': 'CPF válido'}
        else:
            resultado = {'valido': False, 'mensagem': 'CPF inválido'}
    else:
        # Caso o parâmetro 'cpf' não esteja presente na assinatura
        resultado = {'valido': False, 'mensagem': 'Parâmetro CPF ausente'}

    return jsonify(resultado)



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

