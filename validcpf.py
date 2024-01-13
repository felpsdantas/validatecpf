from flask import Flask, request, jsonify, send_from_directory
from flask_cors import cross_origin

app = Flask(__name__)


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


@app.route('/')
def pagina_inicial():
    return 'Bem-vindo à minha página inicial!'


@app.route('/validar_cpf', methods=['GET'])
@cross_origin(supports_credentials=True, origins='*')
def validar_cpf_rota():
    # Obtém todos os parâmetros (GET ou POST) como um dicionário
    params = request.values.to_dict()

    # Obtém o valor do parâmetro 'cpf' do dicionário
    cpf_param = params.get('cpf', '')

    if valida_cpf(cpf_param):
        resultado = {'valido': True, 'mensagem': 'CPF válido'}
    else:
        resultado = {'valido': False, 'mensagem': 'CPF inválido'}

    return jsonify(resultado)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)


