# DRAPE-bot

Chatbot desenvolvido para a plataforma DRAPE (Designing Trust and Privacy into Research): apoio à literacia e conformidade de projetos de investigação em saúde com o RGPD.

Desenvolvido em português.


### Instruções
#### Uso local
A presente versão funciona com o Langflow 1.4.1 localmente e com o Ollama 0.7.0.

Fazer upload do ficheiro **DRAPE-bot.json**, no Langflow local, e usá-lo na aba **Playground**, no canto superior direito. Colocar **API keys** no Qdrant e no Groq, selecionar **llama-3.3-70b-versatile** como modelo a ser usado no Groq e, caso dê erro de limite de tokens, abrir um novo chat. 

#### Instalação - uma das maneiras usando pip
Criar pasta com nome langflow e de seguida criar ambiente virtual.

1. langflow pasta -> abril shell
2. python -m venv venv       (criar ambiente virtual)
3. .\venv\Scripts\activate     (ativar ambiente virtual)
4. pip install langflow      (dentro do ambiente virtual criado)

Com o comando **langflow run** inicia-se o langflow e depois é só aceder à porta do host.

1. Download Ollama no site
2. ollama      (coloque na shell para verificar que está instalado)
3. ollama pull nomic-embed-text      (baixar localmente o modelo de embeddings a ser utilizado)
4. ollama pull llama3 

#### Variáveis
Para acesso à base de dados criada será necessário uma **API key**.

Para o chatbot funcionar, correr localmente o ficheiro **DRAPE-bot.json**, presente no repositório na pasta **Flows**. Mais uma vez, será necessário colocar a **API key** tanto do Qdrant como do Groq. 

Adicionalmente, para avaliar a performance, colocar na pasta do Langflow o script **.env**, com uma **API key** do Langsmith.

#### Repositório
Este repositório contém a pasta **Artigos**, com cada artigo do RGPD separado num ficheiro .txt. Contém também a pasta **Detalhes**, onde está presente o **spitbyarticles.py** (script usado para dividir o **regulamento.pdf** por artigos), o logótipo do projeto DRAPE (futuramente a ser implementado no chatbot) e o script **.env** com as variáveis de ambiente do Langsmith (componente extra, para avaliar a performance).

---

Versão online ainda por sair. Este protótipo foi desenhado somente para uso local.
