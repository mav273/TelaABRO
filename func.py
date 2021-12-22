from consulta import cursor,cnxn

#Deletar

def delete_data(nome):
	cursor.execute('DELETE FROM cadastro WHERE nome="{}"'.format(nome))
	cnxn.commit()

def delete_anamnese(nome):
	cursor.execute('DELETE FROM anamnese1 WHERE nome=?'.format(nome))
	cnxn.commit()

def delete_sociais(nome):
	cursor.execute('DELETE FROM sociais WHERE nome="{}"'.format(nome))
	cnxn.commit()



#Nomes das Colunas
def get_coluna():
	cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='sql10459891' AND TABLE_NAME='cadastro' ")
	data = cursor.fetchall()
	return data


def get_coluna_a():
	cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='sql10459891' AND TABLE_NAME='anamnese1' ")
	data = cursor.fetchall()
	return data

def get_coluna_s():
	cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='sql10459891' AND TABLE_NAME='sociais' ")
	data = cursor.fetchall()
	return data

#Alterar

def update(coluna,novo,nome):
    cursor.execute("update cadastro set `{}` = '{}' where nome = '{}'".format(coluna,novo,nome))
    cnxn.commit()

def update_a(coluna,novo,nome):
    cursor.execute("update anamnese1 set `{}` = '{}' where nome = '{}'".format(coluna,novo,nome))
    cnxn.commit()

def update_s(coluna,novo,nome):
    cursor.execute("update sociais set `{}` = '{}' where nome = '{}'".format(coluna,novo,nome))
    cnxn.commit()

#Consultar os dados
def cadastro_pnome(nome):
	cursor.execute('SELECT * FROM cadastro WHERE nome="{}"'.format(nome))
	data = cursor.fetchall()
	return data

def anamnese_pnome(nome):
    cursor.execute('SELECT * FROM anamnese1 WHERE nome="{}"'.format(nome))
    data = cursor.fetchall()
    return data

def sociais_pnome(nome):
    cursor.execute('SELECT * FROM sociais WHERE nome="{}"'.format(nome))
    data = cursor.fetchall()
    return data

def ver_nomes():
	cursor.execute('SELECT nome FROM cadastro')
	data = cursor.fetchall()
	return data

def consulta():
    cursor.execute('Select * from cadastro')
    data = cursor.fetchall()
    return data
