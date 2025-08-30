import gradio as gr
from transformers import pipeline

# Carrega o modelo de IA (pipeline) uma única vez ao iniciar
print("Carregando modelo de IA... Isso pode levar alguns minutos.")
try:
    # Usamos o modelo menor que já tínhamos selecionado
    classifier = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-3")
    print("Modelo de IA carregado com sucesso.")
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")
    classifier = None

# --- Definições do nosso problema ---
CATEGORIAS = ["Produtivo", "Improdutivo"]
RESPOSTAS_SUGERIDAS = {
    "Produtivo": "Recebemos sua solicitação e nossa equipe já está trabalhando nela. Em breve, você receberá uma atualização. Obrigado pelo contato.",
    "Improdutivo": "Agradecemos a sua mensagem! Tenha um ótimo dia."
}

# --- Função principal que o Gradio vai usar ---
def classifica_email(texto_do_email):
    if not classifier:
        return "Erro", "Modelo de IA não pôde ser carregado.", "Verifique os logs do servidor."
    
    if not texto_do_email or len(texto_do_email.strip()) < 10:
        return "Entrada Inválida", "N/A", "Por favor, insira um texto de email com pelo menos 10 caracteres."

    try:
        # Faz a classificação
        resultado = classifier(texto_do_email, candidate_labels=CATEGORIAS)
        
        # Pega os dados do resultado
        categoria = resultado['labels'][0]
        confianca = f"{resultado['scores'][0]:.2%}"
        resposta = RESPOSTAS_SUGERIDAS.get(categoria, "Resposta não encontrada.")
        
        return categoria, confianca, resposta
    except Exception as e:
        print(f"Erro durante a classificação: {e}")
        return "Erro", "N/A", "Ocorreu um erro ao processar o email."

# --- Criação da Interface Web com Gradio ---
interface = gr.Interface(
    fn=classifica_email,
    inputs=gr.Textbox(lines=10, placeholder="Cole o conteúdo do email aqui..."),
    outputs=[
        gr.Textbox(label="Categoria"),
        gr.Textbox(label="Nível de Confiança"),
        gr.Textbox(label="Resposta Sugerida", lines=4)
    ],
    title="AutoU - Classificador de Emails com IA",
    description="Desafio de código. Cole um email para classificá-lo como Produtivo ou Improdutivo e obter uma sugestão de resposta.",
    allow_flagging="never",
    examples=[
        ["Olá, gostaria de saber o status do meu pedido 1234. Obrigado."],
        ["Feliz natal para toda a equipe!"],
        ["Apenas para informar que o documento foi recebido. Grato."]
    ]
)

# --- Lançamento da Aplicação ---
if __name__ == "__main__":
    interface.launch()