document.addEventListener('DOMContentLoaded', () => {
    const classifyBtn = document.getElementById('classify-btn');
    const emailTextInput = document.getElementById('email-text');
    const resultsArea = document.getElementById('results-area');
    const loadingIndicator = document.getElementById('loading');
    const errorArea = document.getElementById('error-area');
    const categoryTag = document.getElementById('result-category');

    classifyBtn.addEventListener('click', async () => {
        const emailText = emailTextInput.value;

        if (!emailText.trim()) {
            showError("Por favor, insira o texto do email.");
            return;
        }

        hideError();
        resultsArea.classList.add('hidden');
        loadingIndicator.classList.remove('hidden');
        classifyBtn.disabled = true;

        try {
            const response = await fetch('/classify', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email_text: emailText }),
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || "Ocorreu um erro no servidor.");
            }

            document.getElementById('result-confidence').textContent = data.confianca;
            document.getElementById('result-suggestion').textContent = data.resposta_sugerida;
            
            categoryTag.textContent = data.categoria;
            categoryTag.className = 'tag'; // Reset class
            if (data.categoria === 'Produtivo') {
                categoryTag.classList.add('produtivo');
            } else {
                categoryTag.classList.add('improdutivo');
            }

            resultsArea.classList.remove('hidden');

        } catch (error) {
            showError(error.message);
        } finally {
            loadingIndicator.classList.add('hidden');
            classifyBtn.disabled = false;
        }
    });
    
    function showError(message) {
        resultsArea.classList.add('hidden');
        errorArea.classList.remove('hidden');
        document.getElementById('error-message').textContent = message;
    }

    function hideError() {
        errorArea.classList.add('hidden');
    }
});