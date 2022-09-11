
# Nome do projeto: api-voice

Api para realizar a conexão com a API do GOOGLE DRIVE e realizar o download de nuvem do áudio que foi feito o upload pela ri-api em java, transcrever para texto o áudio e fazer a avaliação desse áudio podendo ser de 5 para perfeito e 1 para péssimo

## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/DiegoSousaRodrigues2/api-voice.git
```

Entre no diretório do projeto

```bash
  cd api-voice
```

Instale as dependências

```bash
  Usar Python 3.8
  pip install flask
  pip install google-auth-oauthlib
  pip install --upgrade google-api-python-client
  pip install SpeechRecognition
```

Inicie o servidor

```bash
  python urlMapping.py
```


# Nome do grupo: RateIt
#### Integrantes

- [@Diego Sousa Rodrigues - RM87910](https://www.github.com/DiegoSousaRodrigues2)
- [@Emily Keyt Manfrin - RM87198](https://www.github.com/404)
- [@Gabriel Rodrigues Cordeiro - RM87265](https://github.com/GabrielCordeiro2412)
- [@Giovana Nelo Furlan - RM88936](https://www.github.com/giovanafurlan)
- [@Heloisa Beatriz de Oliveira Costa - RM85589](https://www.github.com/Helloisa22)
- [@Glória Maria Ribeiro Souza - RM 88613](https://www.github.com/404)


## Documentação da API
#### Teste se a API esta funcionando

```http
  GET /health
```

| Retorno   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `Message` | `String` | Retorná se a API esta funcional ou não |

#### Retorna todos os itens

```http
  GET /listAudios
```

| Retorno   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | O id do video |
| `name`    | `string` | O nome do video |


```http
  GET /getAudioById?id=file_id
```
### Retorna apenas o id e name de um video


| Parametro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`        | `string`   | O id do video, Id do video pode ser verificado com o endpoint /listAudios |

| Retorno   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | O id do video |
| `name`    | `string` | O nome do video |


```http
  GET /getAudioById?id=file_id
```
### Retorna apenas o id e name de um video


| Parametro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`        | `string`   | O id do video, Id do video pode ser verificado com o endpoint /listAudios |
| `name`      | `string`   | Esse é o nome que será salvo o video, por favor utilizar extensao .wav    |


| Retorno   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `Message` | `string`  | Speach-to-text do audio  |
| `Star`    | `Integer` | Quantidade de estrela |
| `Status`  | `HTTPS`   | Status da requisição |

## Fluxograma e Proposta de Solução

 - [Miro](https://miro.com/app/board/uXjVPbhgzVs=/)



## Fluxograma

<a href="https://ibb.co/kG8GLp0"><img src="https://i.ibb.co/Cw7wjqv/Whats-App-Image-2022-09-11-at-16-37-00.jpg" alt="Whats-App-Image-2022-09-11-at-16-37-00" border="0"/></a>

## Proposta de Solução

<a href="https://ibb.co/wwpVtCM"><img src="https://i.ibb.co/qWmK69k/Whats-App-Image-2022-09-11-at-16-36-41.jpg" alt="Whats-App-Image-2022-09-11-at-16-36-41" border="0"/>
</a>
