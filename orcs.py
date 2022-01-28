import pandas as pd

f = open("test.txt", "a")

orcinhos_df = pd.read_excel('Orcs_Orcinhos-Cadastro2021_2(respostas).xlsx')

for i, nome in enumerate(orcinhos_df['Nome Completo']):
    matricula = str(int(orcinhos_df.loc[i, 'Matrícula']))
    RG = str(int(orcinhos_df.loc[i, 'RG']))
    CPF = str(int(orcinhos_df.loc[i, 'CPF']))
    endereco = orcinhos_df.loc[i, 'Endereço']
    orc = f"{nome}, Brasileiro(a), estudante, solteiro(a), portador(a) do RG nº. {RG}-DF e CPF sob o nº. {CPF}, residente e domiciliado(a) em {endereco}, voluntário(a) na empresa júnior desde Dezembro de 2022, sob a matrícula {matricula}.\n"
    f.write(orc)
    
f.close
