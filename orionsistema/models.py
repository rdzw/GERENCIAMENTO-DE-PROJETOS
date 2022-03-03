class Projeto:
    def __init__(self, nome, dtInicio, dtFim, valorProjeto, risco, participantes, id=None):
        self.id = id
        self.nome = nome
        self.dtInicio = dtInicio
        self.dtFim = dtFim
        self.valorProjeto = valorProjeto
        self.risco = risco
        self.participantes = participantes


class Risco:
    tipos_de_riscos = {
        (0, 'Baixo'),
        (1, 'Medio'),
        (2, 'Alta')
    }