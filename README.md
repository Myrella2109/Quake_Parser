Este projeto tem como objetivo realizar a analise de um arquivo games.log gerado pelo servidor de quake 3 arena e disponibilizar as informações extraídas por meio de uma API desenvolvida em Python utilizando o framework FastAPI.

A aplicação foi criada para identificar cada partida iniciada no arquivo de log, computar o número total de mortes, listar os jogadores presentes e registrar quantas eliminações cada um realizou. Adicionalmente, ela cria uma classificação geral com a soma das mortes de todos os jogos analisados. Segundo as regras do jogo, quando o "world" elimina um jogador, sua pontuação diminui.

Para rodar o projeto, o primeiro passo é instalar o ambiente virtual utilizando o comando (python -m venv .venv), em seguida ativá-lo usando (.venv\Scripts\activate) caso estaja usando Windows ou (source .venv/bin/activate) caso esteja usando Linux/macOS. O segundo passo é instalar as dependências utilizando o comando pip install fastapi uvicorn. Depois, execute o arquivo main.py para processar o log e criar um relatório completo no arquivo data/report.json. Após isso, a API pode ser iniciada com o comando uvicorn src.api:app --reload.

A aplicação estará acessível em http://127.0.0.1:8000, e a documentação interativa automática pode ser encontrada em http://127.0.0.1:8000/docs.

A rota inicial (/) exibe um resumo geral do sistema, mostrando o número total de jogos processados, o total geral de mortes e a classificação geral dos jogadores. A rota /games/{id} permite visualizar os dados de um jogo específico, enquanto a rota /ranking mostra a classificação geral consolidada.

O relatório final processado é salvo no arquivo data/report.json, que serve como a base de dados para as consultas feitas pela API.