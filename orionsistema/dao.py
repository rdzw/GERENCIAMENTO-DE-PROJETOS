from models import Projeto

SQL_DELETA_PROJETO = 'delete from projeto where id = %s'
SQL_PROJETO_POR_ID = 'SELECT id, nome, dtInicio, dtFim, valorProjeto, risco, participantes from projeto where id = %s'
SQL_ATUALIZA_PROJETO = 'UPDATE projeto SET nome=%s, dtInicio=%s, dtFim=%s, valorProjeto=%s, risco=%s, participantes=%s where id = %s'
SQL_BUSCA_PROJETOS = 'SELECT id, nome, dtInicio, dtFim, valorProjeto, risco, participantes from projeto'
SQL_CRIAR_PROJETO = 'INSERT into projeto (nome, dtInicio, dtFim, valorProjeto, risco, participantes) values (%s, %s, %s, %s, %s, %s)'


class ProjetoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, projeto):
        cursor = self.__db.connection.cursor()

        if (projeto.id):
            cursor.execute(SQL_ATUALIZA_PROJETO, (projeto.nome, projeto.dtInicio, projeto.dtFim,projeto.valorProjeto, projeto.risco, projeto.participantes, projeto.id))
        else:
            cursor.execute(SQL_CRIAR_PROJETO, (projeto.nome, projeto.dtInicio, projeto.dtFim,projeto.valorProjeto, projeto.risco, projeto.participantes))
            projeto.id = cursor.lastrowid
        self.__db.connection.commit()
        return projeto

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_PROJETOS)
        projetos = traduz_projetos(cursor.fetchall())
        return projetos

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_PROJETO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Projeto(tupla[1], tupla[2], tupla[3],tupla[4], tupla[5], tupla[6], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_PROJETO, (id, ))
        self.__db.connection.commit()


def traduz_projetos(projetos):
    def cria_projeto_com_tupla(tupla):
        return Projeto(tupla[1], tupla[2], tupla[3],tupla[4], tupla[5], tupla[6], id=tupla[0])
    return list(map(cria_projeto_com_tupla, projetos))
