# Classificador de Emails com IA - Desafio AutoU

**Status do Projeto: Concluído 🚀**

---

## ➡️ Link da Aplicação

**A aplicação está hospedada e pode ser acessada publicamente no seguinte link:**

[**https://huggingface.co/spaces/DiegoVitor/autou-classificador-emails**](https://huggingface.co/spaces/DiegoVitor/autou-classificador-emails)

---

## 📝 Descrição do Projeto

Este projeto foi desenvolvido como parte do processo seletivo da AutoU. O objetivo é uma aplicação web que utiliza Inteligência Artificial para automatizar a leitura e classificação de emails, categorizando-os como **Produtivos** ou **Improdutivos** e sugerindo uma resposta automática apropriada.

---

## ✨ Funcionalidades

-   **Classificação de Texto:** Classifica o conteúdo de um email em `Produtivo` ou `Improdutivo` utilizando um modelo de Zero-Shot Classification da Hugging Face.
-   **Sugestão de Resposta:** Fornece uma resposta automática padrão com base na categoria identificada.
-   **Interface Web Interativa:** Uma interface web limpa e simples, criada com Gradio, onde o usuário pode inserir o texto do email e receber a análise em tempo real.

---

## 🛠️ Stack de Tecnologias

-   **Backend e Lógica de IA:** Python
-   **Modelo de IA:** `valhalla/distilbart-mnli-12-3` (via Hugging Face Transformers)
-   **Interface Web:** Gradio
-   **Hospedagem:** Hugging Face Spaces

---

## 🏛️ Justificativa da Arquitetura e Escolhas Técnicas

A arquitetura final deste projeto, utilizando **Hugging Face Spaces** com uma interface gerada pela biblioteca **Gradio**, foi o resultado de um processo iterativo de desenvolvimento e deploy focado em encontrar a solução mais robusta e adequada para os requisitos e desafios técnicos apresentados.

#### Processo de Avaliação de Plataformas (PaaS)

Durante a fase de implantação (deploy), foram testadas múltiplas plataformas de nuvem com o objetivo de hospedar a aplicação.

1.  **Primeira Tentativa: Vercel**
    -   **Abordagem:** Deploy de uma aplicação Flask + HTML/CSS/JS.
    -   **Resultado:** A implantação falhou consistentemente devido ao erro `Error: Serverless Function has exceeded the unzipped maximum size of 250 MB`.
    -   **Análise:** As dependências necessárias para a aplicação de IA (`torch`, `transformers`) ultrapassaram o limite de tamanho de pacote permitido pela arquitetura de "Serverless Functions" da Vercel.

2.  **Segunda Tentativa: Render.com**
    -   **Abordagem:** Migração para o Render, uma plataforma baseada em contêineres com limites de tamanho mais generosos.
    -   **Resultado:** O build foi bem-sucedido, mas a aplicação falhou em tempo de execução com o erro `Error: Out of Memory (OOM)`, excedendo o limite de 512 MB de RAM do plano gratuito.
    -   **Análise:** O carregamento do modelo de linguagem na memória consumiu mais RAM do que a disponível na instância gratuita.

#### A Solução Adotada: Hugging Face Spaces + Gradio

Após constatar as limitações técnicas das plataformas PaaS generalistas para esta carga de trabalho específica de IA, o projeto foi pivotado para uma arquitetura especializada.

-   **Adequação à Carga de Trabalho:** A plataforma Hugging Face Spaces é projetada especificamente para hospedar aplicações de Machine Learning, oferecendo um ambiente com recursos adequados para as bibliotecas do ecossistema.
-   **Superação das Limitações Técnicas:** Esta abordagem resolveu simultaneamente o limite de tamanho de pacote (Vercel) e o limite de memória RAM (Render).
-   **Alinhamento com o Ecossistema de IA:** Utilizar Gradio é o padrão de mercado para a criação de interfaces de demonstração para modelos de linguagem, demonstrando familiaridade com as ferramentas do ecossistema moderno de IA.
-   **Eficiência e Foco no Core do Desafio:** Ao abstrair a complexidade do frontend, foi possível manter o foco na lógica de IA, que é o coração do desafio, cumprindo todos os requisitos funcionais de forma limpa e eficaz.

Esta decisão final demonstra uma capacidade de **resolução de problemas, adaptação e tomada de decisão baseada em evidências técnicas**, resultando em uma aplicação robusta e funcional.

---

## 🚀 Rodando o Projeto Localmente

Para executar este projeto em sua máquina local, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/diegovitorportella/autoU-desafio.git](https://github.com/diegovitorportella/autoU-desafio.git)
    cd autoU-desafio
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # No Windows
    python -m venv venv
    venv\Scripts\activate

    # No Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    python app.py
    ```

5.  Abra seu navegador e acesse a URL local que aparecerá no terminal (geralmente `http://127.0.0.1:7860`).

---

## 👨‍💻 Autor

Desenvolvido por **Diego Vitor Portella**.

