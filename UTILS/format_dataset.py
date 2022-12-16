import os

import pandas as pd
from tabulate import tabulate

from UTILS.generic_functions import get_files_directory, get_absolute_path

# DEFININDO DIRETÓRIO CONTENDO OS DADOS
dir_data = get_absolute_path("DATA_DOWNLOAD")
format_type_data = [".csv", ".xlsx"]

# OBTENDO TODOS OS DATASETS (BASES DISPONÍVEIS)
list_files_data = get_files_directory(directory=dir_data,
                                      format_types_accepted=format_type_data)

# INICIANDO OS DATAFRAMES QUE ARMAZENARÃO OS RESULTADOS
df_country = df_state = df_aux = pd.DataFrame()

# PERCORRENDO CADA UM DOS DATAFRAMES
for file in list_files_data:

    # REALIZANDO A LEITURA DO CSV
    df_aux = pd.read_csv(file, sep=";")

    # OBTENDO A BASE COM INFORMAÇÕES DO BRASIL NA COVID
    df_country = df_country.append(df_aux[df_aux["regiao"] == "Brasil"])

    # OBTENDO A BASE COM INFORMAÇÕES DOS ESTADOS NA COVID
    df_state = df_state.append(df_aux[df_aux["regiao"] != "Brasil"])

# EXPORTANDO AS BASES FINAIS
dir_save = get_absolute_path("DATA")
df_country.to_csv(os.path.join(dir_save, "HIST_PAINEL_COVIDBR_BRAZIL_COUNTRY.csv"),
                  index=None)
df_state.to_csv(os.path.join(dir_save, "HIST_PAINEL_COVIDBR_BRAZIL_STATES.csv"),
                index=None)

print("BASES SALVAS COM SUCESSO")