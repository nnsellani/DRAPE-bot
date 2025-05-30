# DRAPE-bot

Chatbot desenvolvido para a plataforma DRAPE: apoio à literacia e conformidade de projetos de investigação em saúde com o RGPD.

Desenvolvido em português.


### Instruções
#### Uso local
A presente versão funciona com o Langflow 1.4.1 localmente e com o Ollama 0.7.0.

#### Instalação
Criar pasta com nome langflow e de seguida criar ambiente virtual.

1. langflow pasta -> abril shell
2. python -m venv venv       (criar ambiente virtual)
3. .\venv\Scripts\activate     (ativar ambiente virtual)
4. pip install langflow      (dentro do ambiente virtual criado)

Com o comando **langflow run** inicia-se o langflow e depois é só aceder à porta do host.

1. Download Ollama no site
2. ollama      (coloque na shell para verificar que está instalado)
3. ollama pull nomic-embed-text      (baixar localmente o modelo de embeddings a ser utilizado)

#### Variáveis
Para acesso à base de dados criada será necessário uma **API key**.

Para o chatbot funcionar, correr localmente o ficheiro **DRAPE-bot online.json**, presente na pasta **Flows**. Mais uma vez, será necessário colocar a **API key** tanto do Qdrant como do Groq.
