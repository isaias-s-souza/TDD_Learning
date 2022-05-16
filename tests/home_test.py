from ward import test
from splinter import Browser
from app import create_app

# Criando um cenário de teste
@test("Visitante visita página inicial com sucesso")
def _():
    app = create_app() # Cria contexto da aplicação
    app.testing = True # Ativa o modo de teste
    app_context = app.test_request_context() # Cria contexto de teste
    app_context.push() # Põe o contexto de teste na pilha

    browser = Browser("flask", app=app) # Cria navegador
    browser.visit("/")

    assert browser.status_code == 200
    assert browser.is_text_present("Home Page")