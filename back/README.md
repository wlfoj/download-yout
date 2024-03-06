## Requerimentos minimos do ambiente
#### Para criar (Se não houver)
```$ python3 -m venv env2.```  
#### Para instalar as depêndencias
```$ pip install -r requirements.txt```

## Ativando o ambiente
### Windows
```$ env2\Scripts\activate.bat``` 
ou  
````env2\Scripts\Activate.ps1````
### Linux ou Mac
```$ source env2/bin/activate```

# Documentação da api
Acesse em ``http://localhost:5000/apidocs/index.html``

## Futuras melhorias
- [ ] Adicionar opção de escolher a resolução
- [ ] Evitar o código repetido para o tratamento das exceções
- [ ] Documentação da api com swagger
- [ ] Incluir testes unitários e de integração
- [ ] Fazer os scripts de instalação e execução
- [ ] Criar exceção para quando não for possível baixar o vídeo ou algo do tipo
- [ ] Separar a camada da main do downloader
- [ ] Criar a exceção para quando não for possível criar a pasta do mesmo dia, para que ele entenda que já foi criado (pq dá erro quando tenta criar com mesmo nome) !!! Nem precisa disso, a função do os.rename já trata disso.