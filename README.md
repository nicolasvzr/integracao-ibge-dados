<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projeto ETL: Integração com a API do IBGE</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #004085;
            color: white;
            padding: 20px;
            text-align: center;
        }
        h1, h2 {
            font-size: 24px;
        }
        section {
            padding: 20px;
            margin: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        code {
            background-color: #f1f1f1;
            padding: 2px 6px;
            font-size: 16px;
            font-family: monospace;
        }
        pre {
            background-color: #f1f1f1;
            padding: 15px;
            font-family: monospace;
            overflow-x: auto;
        }
        .list-item {
            margin-bottom: 10px;
        }
        footer {
            background-color: #222;
            color: white;
            text-align: center;
            padding: 10px;
            position: absolute;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>

    <header>
        <h1>Projeto ETL: Integração com a API do IBGE</h1>
        <p>Extração, Transformação e Carga de dados de frequência de nomes no Brasil</p>
    </header>

    <section>
        <h2>Descrição</h2>
        <p>Este projeto realiza a extração, transformação e carga (ETL) de dados da API pública do IBGE, especificamente para o censo de nomes, e armazena essas informações em um banco de dados MySQL.</p>
    </section>

    <section>
        <h2>Estrutura do Projeto</h2>
        <ul>
            <li class="list-item"><strong>Extração de Dados (Extract):</strong> Requisições HTTP para obter dados da API do IBGE.</li>
            <li class="list-item"><strong>Transformação (Transform):</strong> Processamento e limpeza dos dados recebidos.</li>
            <li class="list-item"><strong>Carga (Load):</strong> Inserção dos dados processados no banco de dados MySQL.</li>
        </ul>
    </section>

    <section>
        <h2>Funcionalidades</h2>
        <ul>
            <li class="list-item"><strong>Extração de Dados:</strong> Coleta de dados de frequência de nomes via API do IBGE.</li>
            <li class="list-item"><strong>Processamento:</strong> Limpeza e organização dos dados.</li>
            <li class="list-item"><strong>Armazenamento:</strong> Inserção dos dados processados em uma tabela MySQL.</li>
            <li class="list-item"><strong>Conexão com o Banco de Dados:</strong> Conexão com MySQL para execução de operações.</li>
        </ul>
    </section>

    <section>
        <h2>Tecnologias Utilizadas</h2>
        <ul>
            <li class="list-item"><strong>Python:</strong> Linguagem de programação utilizada.</li>
            <li class="list-item"><strong>requests:</strong> Biblioteca para fazer requisições HTTP para a API do IBGE.</li>
            <li class="list-item"><strong>mysql.connector:</strong> Biblioteca para interação com o MySQL.</li>
            <li class="list-item"><strong>Tabulate:</strong> Biblioteca para exibição de dados em formato tabular.</li>
            <li class="list-item"><strong>MySQL:</strong> Sistema de gerenciamento de banco de dados.</li>
        </ul>
    </section>

    <section>
        <h2>Pré-requisitos</h2>
        <p>Antes de rodar o projeto, certifique-se de que você tem os seguintes pré-requisitos:</p>
        <ul>
            <li class="list-item"><code>Python 3.x</code> instalado.</li>
            <li class="list-item"><code>MySQL</code> instalado e em execução.</li>
            <li class="list-item">Banco de dados configurado com a tabela necessária para armazenar os dados.</li>
        </ul>
    </section>

    <footer>
        <p>&copy; 2024 Projeto ETL - Integração com a API do IBGE</p>
    </footer>

</body>
</html>

