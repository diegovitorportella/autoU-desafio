from flask import Flask, request, jsonify, render_template
from transformers import pipeline

# Inicializa o Flask App
# O Vercel precisa que os templates e estáticos sejam referenciados a partir do root
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Carrega os pipelines da Hugging Face
try:
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
except Exception as e:
    print(f"Erro ao carregar o modelo de classificação: {e}")
    classifier = None

CATEGORIAS = ["Produtivo", "Improdutivo"]

RESPOSTAS_SUGERIDAS = {
    "Produtivo": "Recebemos sua solicitação e nossa equipe já está trabalhando nela. Em breve, você receberá uma atualização. Obrigado pelo contato.",
    "Improdutivo": "Agradecemos a sua mensagem! Tenha um ótimo dia."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_email():
    if not classifier:
        return jsonify({"error": "Modelo de IA não está disponível."}), 500

    data = request.json
    email_text = data.get('email_text')

    if not email_text or len(email_text.strip()) == 0:
        return jsonify({"error": "Texto do email não pode ser vazio."}), 400

    try:
        result = classifier(email_text, candidate_labels=CATEGORIAS)
        categoria = result['labels'][0]
        score = result['scores'][0]
        resposta_sugerida = RESPOSTAS_SUGERIDAS.get(categoria, "Não foi possível gerar uma resposta.")

        return jsonify({
            "categoria": categoria,
            "confianca": f"{score:.2%}",
            "resposta_sugerida": resposta_sugerida
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Adicionado: Bloco que inicia o servidor para testes locais
if __name__ == '__main__':
    app.run(debug=True, port=5000)