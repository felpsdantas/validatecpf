document.addEventListener('DOMContentLoaded', function() {
    const cpfInput = document.getElementById('cpfInput');
    const resultDiv = document.getElementById('result');
    const validateButton = document.getElementById('validateButton');

    function validateCPF() {
        const cpf = cpfInput.value.replace(/\D/g, ''); // Remover caracteres não numéricos

        fetch(`http://localhost:8000/validar_cpf?cpf=${cpf}`)

            .then(response => response.json())
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
