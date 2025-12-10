# Coloração em Grafos - Algoritmo DSATUR

Coloração em Grafos é o problema de atribuir cores a vértices de um grafo para que vizinhos não tenham a mesma cor, buscando o mínimo de cores (número cromático). O Algoritmo DSATUR (Degree of SATuration) é uma heurística gulosa eficiente que escolhe o próximo vértice a colorir com base no grau de saturação (número de cores distintas em seus vizinhos), priorizando o mais "saturado", e usa o maior grau original como desempate, encontrando soluções ótimas para certos grafos como os bipartidos.

## Clonar o repositório

```bash
git clone https://github.com/Elildes/grafos-coloracao.git
cd grafos-coloracao
```

## Criar um ambiente virtual

```bash
python -m venv venv
```

## Ativar o ambiente virtual (Windows)

```bash
venv\Scripts\activate
```

## Ativar o ambiente virtual (Linux/macOS)

```bash
source venv/bin/activate
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar a aplicação web (Windows)

```bash
.\devserver.bat
```

## Executar a aplicação web (Linux)

```bash
./devserver.sh
```

Depois clicar no link que aparecerá no terminal ou digitar no navehagor [http://127.0.0.1:8080](http://127.0.0.1:8080).  

**Obs.:** o comando `.\devserver.bat` (windows) ou `./devserver.sh` (linux) é usado somente em modo `desenvolvedor`, não use ele no modo de `produção`.  

## Estrutura do projeto


```
grafos-coloracao/ 
|   ├── app.py              # Servidor API da aplicação (Flask)  
|   ├── devserver.sh        # Script para execução em Linux  
|   ├── devserver.bat       # Script para execução em Windows  
|   ├── README.md           # Descrição do projeto e instruções de uso  
|   └── requirements.txt    # Lista de dependências do projeto  
| 
├── /src 
|   ├── __init__.py 
|   ├── graph_dsatur.py # Módulo para representação do grafo (Matriz Adj.) 
|   └── dsatur_algorithm.py # Implementação do Algoritmo de DSATUR 
| 
|   ├── /static             # Pasta padrão do Flask para arquivos estáticos  
|   ├── /css 
|   |    └── styles.css     # Estilos CSS  
|   └── /js 
|       └── main.js         # Script para interagir com a API do DSATUR 
| 
└── /templates   
     └── index.html         # Página inicial (Interface do DSATUR) 
```

# Flask Web App Starter

A Flask starter template as per [these docs](https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application).
