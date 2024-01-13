document.addEventListener('DOMContentLoaded', function() {
    const cpfInput = document.getElementById('cpfInput');
    const resultDiv = document.getElementById('result');
    const validateButton = document.getElementById('validateButton');

    function validateCPF() {
        const cpf = cpfInput.value.replace(/\D/g, ''); // Remover caracteres não numéricos
        
        // Criar um objeto com os dados a serem enviados
        const dados = { cpf };

        fetch('http://localhost:8000/inserir_dados', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dados),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.valido) {
                resultDiv.innerHTML = `<p style="color: green;">${data.mensagem}</p>`;
            } else {
                resultDiv.innerHTML = `<p style="color: red;">${data.mensagem}</p>`;
            }
        })
        .catch(error => {
            console.error('Erro na requisição:', error);
            resultDiv.innerHTML = '<p style="color: red;">Erro na validação do CPF. Tente novamente.</p>';
        });
    }

    validateButton.addEventListener('click', validateCPF);
});



