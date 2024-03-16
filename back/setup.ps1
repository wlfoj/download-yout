##! Script para instalar as dependências do backend

# Cria o ambiente, se não houver
. python -m venv .\back\env
# Habilita o ambiente
. back\env\Scripts\activate
# Instala as depêndencias no ambiente
. pip install -r .\back\requirements.txt