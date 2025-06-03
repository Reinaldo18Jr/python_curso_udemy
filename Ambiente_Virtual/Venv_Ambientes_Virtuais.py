# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação do Python
# para uma pasta no caminho escolhido. Ao ativar um ambiente
# virtual, a instalação do ambiente virtual será usada. venv é
# o módulo que vamos usar para criar ambientes virtuais. Pode 
# nomear do jeito que preferir, mas os mais comuns são:
# venv, env, .venv, .env

# Comando no Powershell para CRIAR:
# python -m venv Nome_Da_Venv (py -m venv venv)

# Como ATIVAR a venv:
# Seguir os caminhos das pastas no comando Powershell
# venv\Scripts\activate

# Como DESATIVAR a venv:
# No Powershell digitar
# deactivate

# Como INSTALAR bibliotecas de terceiros (Django, PyMySql, etc):
# pip install pymysql

# Como DESINSTALAR bibliotecas de terceiros (Django, PyMySql, etc):
# pip uninstall pymysql

# Comando 'pip freeze':
# mostra os pacotes instalados na venv

# Criar REQUIREMENTS.TXT para usar em novo ambiente virtual:
# usar comando: pip freeze > requirements.txt

# Instalar o REQUIREMENTS.TXT em um novo ambiente virtual:
# usar comando: pip install -r .\requirements.txt

# Atualizar o REQUIREMENTS.TXT com novos pacotes para salvar:
# mesmo caminho do Criar: pip freeze > requirements.txt
