
```.\.venv\Scripts\activate.bat```

```pip install -r requiriments.txt```
OU
```pip install poetry```

![Referência Poetry](https://python-poetry.org/docs/cli/)&nbsp;
Gerenciador de dependências (Primeira vez que começou o projeto)
```poetry init -n```
OU
Toda vez que for instalar o projeto em uma nova máquina (Tendo o aquivo poetry.lock (Versões exatas de instalação) e o pyproject.toml(Dependências do projeto))
```poetry install```

Ferramenta para testes (Ward)
```poetry add ward -D```

Ferramenta para testes (Splinter) pelo browser
```poetry add splinter -E flask -D```

Acessar Ambiente do poetry
```poetry shell```

Executar testes a partir do ambiente do poetry
```ward```

