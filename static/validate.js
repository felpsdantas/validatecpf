document.addEventListener('DOMContentLoaded', function() {
    const cpfInput = document.getElementById('cpfInput');
    const resultDiv = document.getElementById('result');
    const validateButton = document.getElementById('validateButton');

    function validateCPF() {
        const cpf = cpfInput.value.replace(/\D/g, ''); // Remover caracteres não numéricos
        fetch(`http://127.0.0.1:5000/api/validar_cpf/${cpf}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Erro HTTP! Status: ${response.status}`);
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