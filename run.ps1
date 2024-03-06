#!/bin/bash

# !!
$caminhoAtual = $PSScriptRoot
# Exibe o caminho
Write-Host "O caminho do diretório atual é: $caminhoAtual"
#!!


# Chama o script responsável por iniciar o frontend no Windows
. "front/start.ps1"

# Chama o script responsável por iniciar o backend no Windows
. "back/start.ps1"