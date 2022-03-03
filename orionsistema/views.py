from flask import render_template, request, redirect, flash, url_for
from models import Projeto
from dao import ProjetoDao
from orion import db, app

projeto_dao = ProjetoDao(db)

@app.route('/')
def index():
    lista = projeto_dao.listar()
    return render_template('lista.html', titulo='Projetos',
                           projetos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Projeto')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    dtInicio = request.form['dtInicio']
    dtFim = request.form['dtFim']
    valorProjeto = request.form['valorProjeto']
    risco = request.form['risco']
    participantes = request.form['participantes']
    projeto = Projeto(nome, dtInicio, dtFim,valorProjeto, risco, participantes)
    projeto_dao.salvar(projeto)
    return redirect(url_for('index'))


@app.route('/atualizar', methods=['POST',])
def atualizar():
    nome = request.form['nome']
    dtInicio = request.form['dtInicio']
    dtFim = request.form['dtFim']
    valorProjeto = request.form['valorProjeto']
    risco = request.form['risco']
    participantes = request.form['participantes']
    projeto = Projeto( nome, dtInicio, dtFim, valorProjeto, risco, participantes, id=request.form['id'])
    projeto_dao.salvar(projeto)

    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    projeto_dao.deletar(id)
    flash('O projeto foi removido com sucesso!')
    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
    projeto = projeto_dao.busca_por_id(id)
    return render_template('editar.html', titulo='Editando Projetos', projeto=projeto)