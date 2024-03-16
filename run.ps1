##! Script para executar o app

# Chama o script responsável por iniciar o backend no Windows, em um novo terminal
Start-Process powershell -ArgumentList "-NoExit", "-Command", "back/start.ps1"

# Chama o script responsável por iniciar o frontend no Windows, não inicia outra janela
. "front/start.ps1"