# Projeto de Reconhecimento de Fala e Detecção de Idioma

Este projeto é uma aplicação Python que utiliza reconhecimento de fala para captar áudio e detecta automaticamente o idioma falado. A aplicação é construída usando o Flask para o backend e a biblioteca SpeechRecognition para o reconhecimento de fala.

| :placard: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | **API para Tradução**
| :label: Tecnologias | Python
| :rocket: URL         | 
| :fire: Desafio     | 


Pré-requisitos
Antes de executar o projeto, você precisa ter o Python instalado em sua máquina. Você também precisará de uma chave de API do Google para utilizar a funcionalidade de tradução e detecção de idioma.

Uso
Acesse a aplicação no seu navegador.
Clique no botão "Iniciar Reconhecimento de Fala".
Fale algo em um idioma suportado.
O texto reconhecido e o idioma detectado serão exibidos na tela.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.

Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

Contato
Para perguntas ou feedback, entre em contato:
## Funcionalidades

- Detecção de idioma usando a biblioteca googletrans.
- Interface simples para interagir com a aplicação.
- Tecnologias Utilizadas
- Python 3.x
- Flask
- googletrans
- Flask-CORS

## Instalação

Clone o repositório:

```bash
git clone https://github.com/iagolopess/adaTranslatorBackEnd
cd seu-repositorio
```
Crie um ambiente virtual (opcional, mas recomendado):

Instale as dependências:

```bash
pip install -r requirements.txt
```

Executando a Aplicação
Para iniciar o servidor Flask, execute:

```bash
python run.py
A aplicação será executada em http://127.0.0.1:5000/.
```
## Documentação da API

#### Retorna a tradução

```http
  POST /api/translate

```

Passar o JSON como Body da requisição
```bash
  {
  "text": "Hello World",
    "lang": "pt"        
}
```

O output será: Olá Mundo"

