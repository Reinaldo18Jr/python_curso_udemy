# O módulo request para requisições HTTP no Python
# HTTP (HyperText Transfer Protocol) é um protocolo usado enviar e receber dados na
# internet. Ele funciona no modo cliente/servidor, onde o cliente (navegador) faz
# uma requisição ao servidor (site) que responde com os dados adequados.

# A mensagem de requisição do cliente deve incluir dados como:
# - O método HTTP
#   - leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos suportados)
#   - escrita - POST, PUT (substitui), PATCH (atualiza), DELETE
# - O endereço do recurso a ser acessado (/users/)
# - Os cabeçalhos HTTP (Content-Type, Authorization)
# - O corpo da mensagem (caso preciso, de acordo com o método HTTP)

# A mensagem de resposta do servidor deve incluir dados como:
# - código de status HTTP (200 sucess, 404 Not found, 301 Moved Permanently)
# - os cabeçalhos HTTP (Content-Type, Accept)
# - o corpo da mensagem (pode estar em vazio em alguns casos)

# NO AMBIENTE VIRTUAL DO PROJETO(dentro da pasta raiz)
# python -m http.server -d aula190_site/ 3333

# no navegador acessar -> localhost:3333
