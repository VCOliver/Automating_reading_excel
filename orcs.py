import pandas as pd
import re

orcinhos_df = pd.read_excel('Orcs_Orcinhos.xlsx')

def CPF_Formating(CPF):
    CPF_List = re.findall('...?', CPF)
    CPF_List.insert(1, '.')
    CPF_List.insert(3, '.')
    CPF_List.insert(5, '-')
    return ''.join(map(str, CPF_List))

    return

for i, nome in enumerate(orcinhos_df['Nomes']):
    matricula = str(orcinhos_df.loc[i, 'Matrícula'])
    RG = str(orcinhos_df.loc[i, 'RG'])
    emissao = orcinhos_df.loc[i, 'Emissão_RG']
    CPF = str(f"{orcinhos_df.loc[i, 'CPF']:011d}")
    CPF = CPF_Formating(CPF)
    endereco = orcinhos_df.loc[i, 'Endereço_Completo ']
    orc = f"{nome}, Brasileiro(a), estudante, solteiro(a), portador(a) do RG nº. {RG}-{emissao} e CPF sob o nº. {CPF}, residente e domiciliado(a) em {endereco}, voluntário(a) na empresa júnior desde Janeiro de 2022, sob a matrícula {matricula}.\n"
    print(orc)
    
