
```.\.venv\Scripts\activate.bat```&nbsp;

```pip install -r requiriments.txt```&nbsp;
### OU&nbsp;
```pip install poetry```&nbsp;

<a href="https://www.facebook.com/isaias.santos.dsouza/" target="_blank">Referência Poetry</a>&nbsp;

### Gerenciador de dependências (Primeira vez que começou o projeto)&nbsp;
```poetry init -n```&nbsp;
### OU&nbsp;
### Toda vez que for instalar o projeto em uma nova máquina (Tendo o aquivo poetry.lock (Versões exatas de instalação) e o pyproject.toml(Dependências do projeto))&nbsp;
```poetry install```&nbsp;

### Ferramenta para testes (Ward)&nbsp;
```poetry add ward -D```&nbsp;

### Ferramenta para testes (Splinter) pelo browser&nbsp;
```poetry add splinter -E flask -D```&nbsp;

### Acessar Ambiente do poetry&nbsp;
```poetry shell```&nbsp;

### Executar testes a partir do ambiente do poetry&nbsp;
```ward```&nbsp;

