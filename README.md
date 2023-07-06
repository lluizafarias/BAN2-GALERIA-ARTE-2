# Banco de Dados em Grafos com Neo4j Aura DB e Python

## ALUNOS: LUIZA E OTAVIO

## Sobre

O banco de dados apresentado é voltado para o gerenciamento de informações de uma Galeria de Arte. O banco de dados tem como objetivo armazenar informações importantes sobre artistas, obras de arte, clientes e exibições, além de registros de vendas e serviços de pagamentos.

## Requisitos

Para executar a aplicação, é necessário atender aos seguintes requisitos:

* Conta no Neo4j Aura - Crie uma conta no Neo4j Aura acessando [Neo4j Aura Console](https://console.neo4j.io/).
* Python (versão superior a 3.6) - Instale o Python a partir da página de download oficial: [Download page](https://www.python.org/downloads/).
* Biblioteca `neo4j` - Instale a biblioteca `neo4j` para conectar-se ao Neo4j Aura DB através do Python. Você pode instalar a biblioteca usando o gerenciador de pacotes `pip` com o seguinte comando:

  ```
  pip install neo4j
  ```

## Instalação e Execução

Siga as etapas abaixo para instalar e executar o banco de dados em grafos com Neo4j Aura DB e Python:

#### Da instalação do Banco de dados em SQL até a execução do arquivo em Python.

1. Acesse o [Neo4j Aura Console](https://console.neo4j.io/) em seu navegador.
2. Insira um endereço de e-mail e senha e selecione "Register", ou selecione "Continue with Google" para usar uma conta do Google. 
3. Após criar sua conta no AuraDB, clique em "Create a Database" e selecione um banco de dados gratuito.
   ![free database type](https://dist.neo4j.com/wp-content/uploads/free-database-type.png)
4. Preencha o nome e escolha uma região na nuvem para o seu banco de dados e clique em "Create Database". Certifique-se de selecionar "Learn about graphs with a movie dataset" para começar com um conjunto de dados.
   ![recommendation engine free database](https://dist.neo4j.com/wp-content/uploads/recommendation-engine-free-database.png)
5. AuraDB fornecerá a senha para a nova instância enquanto ela estiver sendo configurada. Anote a senha para os próximos passos.
6. Após o banco de dados estar em execução, abra o navegador conforme mostrado abaixo.
   ![open auradb browser](https://dist.neo4j.com/wp-content/uploads/open-auradb-browser.png)
7. Agora você está dentro do Neo4j Browser. Use seu nome de usuário e senha (aqueles que você anotou acima) para fazer login.
8. Em seguida, você pode conectar-se ao Neo4j Aura DB usando o Python. No seu código Python, utilize o seguinte código para estabelecer a conexão:

   ```python
   from neo4j import GraphDatabase
   
   uri = "neo4j://<ENDPOINT>"
   user = "<USERNAME>"
   password = "<PASSWORD>"
   
   driver = GraphDatabase.driver(uri, auth=(user, password))
   ```

   Substitua `<ENDPOINT>` pelo endpoint fornecido pelo Neo4j Aura, `<USERNAME>` pelo seu nome de usuário e `<PASSWORD>` pela senha de acesso ao banco de dados.
   
9. Finalmente você está pronto para executar consultas e operações no banco de dados Neo4j Aura DB usando o Python. Consulte a documentação da biblioteca `neo4j` para obter mais informações sobre como interagir com o banco de dados.

## Recursos adicionais

Para mais informações e recursos sobre o Neo4j Aura DB e o uso de bancos de dados em grafos, consulte:

- [Documentação oficial do Neo4j](https://neo4j.com/docs/)
- [Neo4j Aura Console](https://neo4j.com/cloud/aura/)
- [Repositório oficial da biblioteca neo4j para Python](https://github.com/neo4j/neo4j-python-driver)
