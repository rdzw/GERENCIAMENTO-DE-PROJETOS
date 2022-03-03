import MySQLdb
print('Conectando...')

conn = MySQLdb.connect(user='root', passwd='root', host='127.0.0.1', port=3306)

criar_tabelas = '''CREATE DATABASE `orion` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    USE `orion`;
    CREATE TABLE `projeto` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `dtInicio` varchar(40) NOT NULL,
      `dtFim` varchar(20) NOT NULL,
      `valorProjeto` varchar(20) NOT NULL,
      `risco` varchar(20) NOT NULL,
      `participantes` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabelas)
conn.commit()
