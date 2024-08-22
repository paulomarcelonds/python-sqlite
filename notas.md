# Notas sobre Sqlite


## 1. Principais caracerísticas

- Autocontido

>Significa que o SQlite precisa de suporte minímo do sistema ou de biblioteca para funcionar.

- Sem servidor

>Ou seja não requer um sevidor para funcionar, conceito de *servelerss*.

- Configuração zero

>Por conta da sua arquitetura *serverless* não é preciso configurar ou instalar, basta apenas colocar os arquivos necessários e ele é feito em *C*.

- Transacional

>Todas as transações são compatíveis com ACIC significa que todas as alterações são consistentes e atômicas.

## 2. SQlite outros recursos

- Emprega tipos dinâmicos para as tabelas.

> Ou seja pode armazenar qualquer valor em qualquer coluna.

- Permite vários acessos com conexão única

> É possíve lque uma unica conexão acesse várias tabelas simutaneamente no *BD*. Sendo possível unir tabelas em vários banco de dados.

- Uso de RAM e não de ROM.

> Capaz de criar banco de dados na memória de acesso ao invez de gravar no disco rigído, sendo assim mais rápido a recuperação da informação. 








