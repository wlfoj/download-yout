# Observação importante *** Os caminhos tem que ser relativos ao diretório raiz da aplicação e não de onde está o script
# Uma melhoria a se fazer é retirar esse relativismo e deixar caminhos absolutos
#Start-Process "front/teste.html"

# !!
#$caminhoAtual = $PSScriptRoot
# Exibe o caminho
#echo "O caminho do diretório atual é: $caminhoAtual"
# !!

#echo "Front-end em execução"

cd front/yt-f-d
npm start