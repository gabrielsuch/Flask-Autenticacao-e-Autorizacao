# Projeto

### Este é um projeto para a criação de um usuário, que após logado terá a sua Autorização e Autenticação, para ter acesso das rotas da API. 

#

# Como iniciar o projeto

### Após fazer o git clone do repositório, deve-se usar o comando "flask db upgrade", para atualizar seu Banco de Dados, e então estára pronto para o uso.
### Caso contrário dê errado, deve-se seguir os seguintes comandos:
- ### "flask db init": para a inicialização do migration
- ### "flask db migrate -m 'COMENTÁRIO' ": para criar uma versão atual do banco de dados.
- ### "flask db upgrade": para atualizar/criar o banco de dados. 

#

# V1 do Projeto

### Onde sua Autorização e Autenticação é feita através da API Key, que ao logar na conta, esta chave é guardada e salva banco de dados, para conseguir o acesso das rotas protegidas é necessário o uso desta chave (API Key).

#

# V2 do Projeto

### Onde sua Autorização e Autenticação é feita através do JWT, que cada vez que é logado na conta, é retornado um access token (token de acesso), necessita deste token para acessar as rotas que são protegidas, caso contrário, seu acesso é negado.

#