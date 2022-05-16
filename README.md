
```.\.venv\Scripts\activate.bat```&nbsp;

```pip install -r requiriments.txt```&nbsp;
OU&nbsp;
```pip install poetry```&nbsp;

<a href="https://www.facebook.com/isaias.santos.dsouza/" target="_blank">Referência Poetry</a>&nbsp;

Gerenciador de dependências (Primeira vez que começou o projeto)
```poetry init -n```&nbsp;
OU
Toda vez que for instalar o projeto em uma nova máquina (Tendo o aquivo poetry.lock (Versões exatas de instalação) e o pyproject.toml(Dependências do projeto))
```poetry install```

Ferramenta para testes (Ward)
```poetry add ward -D```&nbsp;

Ferramenta para testes (Splinter) pelo browser
```poetry add splinter -E flask -D```&nbsp;

Acessar Ambiente do poetry
```poetry shell```&nbsp;

Executar testes a partir do ambiente do poetry
```ward```&nbsp;

