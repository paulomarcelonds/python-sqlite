# Notas sobre Sqlite


## 1. Principais caracerísticas

- Autocontido.
>Significa que o SQlite precisa de suporte minímo do sistema ou de biblioteca para funcionar.
- Sem servidor.
>Ou seja não requer um sevidor para funcionar, conceito de *servelerss*.
- Configuração zero.
>Por conta da sua arquitetura *serverless* não é preciso configurar ou instalar, basta apenas colocar os arquivos necessários e ele é feito em *C*.
- Transacional.
>Todas as transações são compatíveis com ACIC significa que todas as alterações são consistentes e atômicas.

## 2. SQlite outros recursos

- Emprega tipos dinâmicos para as tabelas.
> Ou seja pode armazenar qualquer valor em qualquer coluna.
- Permite vários acessos com conexão única
> É possíve lque uma unica conexão acesse várias tabelas simutaneamente no *BD*. Sendo possível unir tabelas em vários banco de dados.
- Uso de RAM e não de ROM.
> Capaz de criar banco de dados na memória de acesso ao invez de gravar no disco rigído, sendo assim mais rápido a recuperação da informação.

## 3. Conceitos básicos - Conector

- Conector ou adaptador.
> É uma biblioteca ou modulo que fornece interface para se conectar ao banco de dados específico. Geralmente oferecem metódos para estabelezer conexões.
- Exemplos de modulos.
> 1. psycopg2 para  PostgreSQL
> 2. pymysql para MySQL.
> 3. sqlite3 para SQLite


## 4. Conceitos básicos - Cursor

- O que é o cursor?
> É um obejto utilizado para navegar e manipular os resultados das consultas que iremos criar, são os resultados obtidos das através da conexão com o banco de dados e permite executar, iterar sobre os resultados e acessar dados recuperados.
O *cursor* também é responsável por gerenciar as transações no banco de dados.

## Conceitos básicos: Transação

- O que é uma transação?
> Sequencia de operações tratadas como unica unidade de trabalho em um banco de dados, podendo ser: inserções atualizações, exclusões ou consultas.

- O que é o conceito ACID?
> As transações são garantidas pelo conceito **ACID** que significa: **atomicidade**, **consistencia**, **isolamento** e **durabilidade**.

- Gerenciadas pelo métodos dos conectores.
> As transações são gerenciadas pelo métodos dos conecores tais como: **commit()** para confirmar as alterações ou **rollback** para reverter as alterações realizadas.

## Fluxo de trabalho resumido

- Resumo de um fluxo de trabalho usando o banco de dados SQLite.
> 1. Criação da conexão com o banco de dados usando o metodo **connect**.
> 2. Criação do cursor com a conexão, responsavel por enviar comandos ao banco de dados.
> 3. Utlizar o cursor para executar as tarefas como criar obejtos, inserir linhas, criar tabelas, consultar registros e outras coisas mais.
> 4. Efetivar as alterações com o metodo **commit** da conexão ou para desfazer usando o **rollback**
> 5. Fechar o cursor e a conexão.











