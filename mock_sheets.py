import os
import json
import gspread

def consultar_planilha(nome_planilha, nome_aba,query):
    try:
        # Autentica usando as credenciais do arquivo JSON
        credentials_json = os.environ.get('GOOGLE_SHEETS_CREDENTIALS')
        if not credentials_json:
            raise Exception("Variável de ambiente 'GOOGLE_SHEETS_CREDENTIALS' não encontrada.")
            
        credentials_dict = json.loads(credentials_json)
        gc = gspread.service_account_from_dict(credentials_dict)

        # Abre a planilha pelo nome
        planilha = gc.open(nome_planilha)

        # Seleciona a aba específica
        aba = planilha.worksheet(nome_aba)

        # Obtém todos os valores da aba
        dados = aba.findall(query=query,case_sensitive=False,in_column=9,)

        mock = []
        if dados:
            for value in dados:
                mock.append(aba.row_values(value._row))    

        return mock

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None

def consulta_agencia(agency_number,bank_name:str):

    my_dict = {}
    i = 1

    dados_da_minha_planilha = consultar_planilha("teste", "dados",agency_number)


    if dados_da_minha_planilha:
        for dados in dados_da_minha_planilha:
            if(bank_name.upper() in dados[6]):
                my_dict[str(i)] = {'municipio':dados[1],'uf':dados[3],'nome_agencia':dados[5],'banco':bank_name,'codigo':agency_number,'endereço':dados[9],'bairro':dados[10],'cep':dados[11]} 
                i += 1      
        return my_dict
    
    return None


