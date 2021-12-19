import streamlit as st
from template.template_anamnese import anamnesetemp0,anamnesetemp1,anamnesetemp2,anamnesetemp3,anamnesetemp4,anamnesetemp5,anamnesetemp6,anamnesetemp7,anamnesetemp8,anamnesetemp9,anamnesetemp10,anamnesetemp11,anamnesetemp12,anamnesetemp13,anamnesetemp14,anamnesetemp15,anamnesetemp16
from template.template_sociais import sociaistemp0,sociaistemp1

#conexão


import mysql.connector
cnxn = mysql.connector.connect(host=st.secrets["host"], user=st.secrets["user"], passwd= st.secrets["passwd"], db= st.secrets["db"])
cursor = cnxn.cursor()

#html and css

#trocar o nome da pagina e o icone
st.set_page_config(page_title = "ABRO - Odontologia Especializada", page_icon="favicon.ico")

#remover o botão de Menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

fundo = """

"""
html_temp = """
<div style="background-color:{};padding:10px;border-radius:10px">
<h1 style="color:{};text-align:center;">Simple Blog </h1>
</div>
"""
title_temp ="""
<div style="background-color:#37302b;padding:10px;border-radius:10px;margin:10px;box-shadow: 5px 5px 5px rgba(0,0,0,0.5);">
<h4 style="color:#f9b03d;text-align:center;">Cadastro: {}</h1>
<br/>
<br/> 
<p style="color:#f9b03d;text-align:center;font-family: monospace;">Telefone: {}</p>
<p style="color:#f9b03d;text-align:center;font-family: monospace;">CPF: {}</p>
</div>
"""


article_temp ="""
<div style="background-color:#37302b;padding:10px;border-radius:5px;margin:10px;box-shadow: 5px 5px 5px rgba(0,0,0,0.5);">
<h4 style="color:#f9b03d;text-align:center;">Qual O Motivo Da Consulta ?</h1>
<br/>
<br/>
<p style="color:#f9b03d;text-align:center;font-family: monospace;"><br/>{}</p>
</div>
"""

head_message_temp ="""
<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h1>
<h6>Author:{}</h6> 
<h6>Post Date: {}</h6> 
</div>
"""
full_message_temp ="""
<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
<p style="text-align:justify;color:black;padding:10px">{}</p>
</div>
"""


# Funções_______________________________________________________________________________________________________



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

#Update

def update(coluna,novo,nome):
    cursor.execute("update cadastro set `{}` = '{}' where nome = '{}'".format(coluna,novo,nome))
    cnxn.commit()

def update_a(coluna,novo,nome):
    cursor.execute("update anamnese1 set `{}` = '{}' where nome = '{}'".format(coluna,novo,nome))
    cnxn.commit()

def update_s(coluna,novo,nome):
    cursor.execute("update sociais set `{}` = '{}' where nome = '{}'".format(coluna,novo,nome))
    cnxn.commit()

#fetchall()
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

def view_all_titles():
	cursor.execute('SELECT nome FROM cadastro')
	data = cursor.fetchall()
	return data

def consulta():
    cursor.execute('Select * from cadastro')
    data = cursor.fetchall()
    return data



#Menu
menu = ["Consultar","Alterar","Deletar"]
choice = st.sidebar.selectbox("Menu",menu)

#Consulta
if choice == "Consultar":
    st.subheader("Consulte os dados")


    t_nomes = [i[0] for i in view_all_titles()]
    nome4 = st.selectbox("Nome",t_nomes)
    escolha = cadastro_pnome(nome4)
    escolha_a = anamnese_pnome(nome4)
    escolha_s = sociais_pnome(nome4)
    c1 = st.checkbox('Cadastro')
    c2 = st.checkbox('Anamnese')
    c3 = st.checkbox('Sociais')
    if c1: 
        for i in escolha:
            b_nome = i[1]
            b_telefone = i[2]
            b_cpf = i[3]
            st.markdown(title_temp.format(nome4,b_telefone,b_cpf),unsafe_allow_html=True)
    if c2:

            for i in escolha_a:
                b_motivo = i[1]
                b_tratamento = i[2]
                if b_tratamento=="Sim":
                    st.warning("Está Fazendo Tratamento")
                b_medicamento = i[3]
                if b_medicamento == "Sim":
                    st.warning("Faz Uso De Medicamentos")
                b_qmedicamento = i[4]
                b_alergia = i[5]
                if b_alergia=="Sim":
                    st.warning("Tem Alergias")
                b_qalergia = i[6]
                b_anestisia = i[7]
                if b_anestisia=="Sim":
                    st.warning("Apresenta Reação A Anestesia")
                b_ultimo = i[8]
                b_canal = i[9]
                b_gengiva = i[10]
                if b_gengiva == "Sim":
                    st.warning("Gengiva Sangra Com Frequência")
                b_fuma = i[11]
                b_sangra = i[12]
                b_dor = i[13]
                b_desmaio = i[14]
                if b_desmaio == "Sim":
                    st.warning("Quadros De Desmaios e/ou Epilepsia")
                b_gravida = i[15]
                if b_gravida == "Sim":
                    st.warning("Pode Estar Gravida")
                b_botox = i[16]



            st.markdown(anamnesetemp0.format(nome4),unsafe_allow_html=True)
            st.markdown(anamnesetemp1.format(b_motivo),unsafe_allow_html=True)
            st.markdown(anamnesetemp2.format(b_tratamento),unsafe_allow_html=True)
            st.markdown(anamnesetemp3.format(b_medicamento),unsafe_allow_html=True)
            st.markdown(anamnesetemp4.format(b_qmedicamento),unsafe_allow_html=True)
            st.markdown(anamnesetemp5.format(b_alergia),unsafe_allow_html=True)
            st.markdown(anamnesetemp6.format(b_qalergia),unsafe_allow_html=True)
            st.markdown(anamnesetemp7.format(b_anestisia),unsafe_allow_html=True)
            st.markdown(anamnesetemp8.format(b_ultimo),unsafe_allow_html=True)
            st.markdown(anamnesetemp9.format(b_canal),unsafe_allow_html=True)
            st.markdown(anamnesetemp10.format(b_gengiva),unsafe_allow_html=True)
            st.markdown(anamnesetemp11.format(b_fuma),unsafe_allow_html=True)
            st.markdown(anamnesetemp12.format(b_sangra),unsafe_allow_html=True)
            st.markdown(anamnesetemp13.format(b_dor),unsafe_allow_html=True)
            st.markdown(anamnesetemp14.format(b_desmaio),unsafe_allow_html=True)
            st.markdown(anamnesetemp15.format(b_gravida),unsafe_allow_html=True)
            st.markdown(anamnesetemp16.format(b_botox),unsafe_allow_html=True)
    if c3:

            st.markdown(sociaistemp0.format(nome4),unsafe_allow_html=True)
    
            for i in escolha_s:
                profissao = i[1]
                time = i[2]
                qtime = i[3]
                animal = i[4]
                qanimal = i[5]
                filho = i[6]
                nfilho = i[7]
                medo = i[8]
                sorriso = i[9]
                facebook = i[10]
                instagram = i[11]
                qinstagram = i[12]
                hobby = i[13]
                qhobby = i[14]
                ambiente = i[15]
                generom = i[16]
                programacao = i[17]
                generof = i[18]

            st.markdown(sociaistemp1.format(profissao,time,qtime,animal,qanimal,filho,nfilho,medo,sorriso,facebook,instagram,qinstagram,hobby,qhobby,ambiente,generom,programacao,generof),unsafe_allow_html=True)
        








#Deletar
if choice == "Deletar":
    st.subheader("Delete os Dados") 
    
    sonomes = [i[0] for i in view_all_titles()]
    delete_blog_by_title = st.selectbox("Nome",sonomes)
		        
    st.error('ATENÇÃO! Depois de deletado não há como resgatar os dados do paciente selecionado')
    st.write('Deseja apagar os dados?')
    if st.button ('Sim'):
        delete_data(delete_blog_by_title)
        delete_anamnese(delete_blog_by_title)
        delete_sociais(delete_blog_by_title)
        st.success('Paciente Deletado')


#Alterar
if choice == "Alterar":

    st.subheader("Altere os Dados")

    st.warning('ATENÇÃO! Tente não alterar o nome, cpf ou o id paciente das tabelas')
    nomes = [i[0] for i in view_all_titles()]
    result = [i[0] for i in get_coluna()]
    result_a = [i[0] for i in get_coluna_a()]
    result_s = [i[0] for i in get_coluna_s()]
    nome2 = st.selectbox("Nome",nomes)

    c4 = st.checkbox('Cadastro')
    c5 = st.checkbox('Anamnese')
    c6 = st.checkbox('Sociais')
        #pd1 = pd.DataFrame(result,columns=["'Colunas'"])    
        #st.dataframe(pd1)
        
    

    st.write('')
    st.write('')
    if c4:
        coluna = st.selectbox("Coluna do Cadastro",result)
        novo = st.text_input("Insira o novo dado")

        if st.button("Altere o cadastro"):
            update(coluna,novo,nome2)
            st.success('Dado alterado com sucesso') 

        st.write('')
        st.write('')
        st.write('')
        st.write('')
    if c5:
        coluna_a = st.selectbox("Coluna do Anamnese",result_a)
        novo_a = st.text_input("Insira o novo dado",key='chave')
        
        if st.button("Alterar Anamnese"):
            update_a(coluna_a,novo_a,nome2)
            st.success('Dado alterado com sucesso') 

        st.write('')
        st.write('')
        st.write('')
        st.write('')
    if c6:
        coluna_s = st.selectbox("Coluna do Sociais",result_s)
        novo_s = st.text_input("Insira o novo dado",key='chave1')
        
        if st.button("Alterar Social"):
            update_s(coluna_s,novo_s,nome2)
            st.success('Dado alterado com sucesso') 