import os
import json
from inspect import stack

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
from dynaconf import settings

from UTILS.generic_functions import get_absolute_path, verify_exists


def get_data_covid(dir_brazil, dir_states):

    """

    OBTÉM OS DADOS QUE SERÃO UTILIZADOS NA DASHBOARD

    1 - DADOS DE COVID - VISÃO PAÍS
    2 - DADOS DE COVID - VISÃO ESTADOS

    # Arguments
        dir_brazil         - Required : Diretório dos
                                        dados - COVID
                                        Brazil (String)
        dir_states         - Required : Diretório dos
                                        dados - COVID
                                        Estados Brasileiros (String)

    # Required
        df_brazil         - Required : Dados - COVID
                                       Brazil (String)
        df_states         - Required : Dados - COVID
                                       Estados Brasileiros (String)

    """

    # INICIANDO OS DATAFRAMES
    df_brazil = df_states = pd.DataFrame()

    # MAPEANDO DEPARA DE DIRETÓRIO E DATAFRAME
    data_covid = {dir_brazil: df_brazil, dir_states: df_states}

    try:
        # PERCORRENDO CADA UM DOS DADOS
        for df_dir, df_key in data_covid.items():

            if verify_exists(df_dir):
                data_covid[df_dir] = pd.read_csv(df_dir)
            else:
                print(
                    "O DATASET NÃO EXISTE {}, POR FAVOR UTILIZAR O SITE: {} E INSERIR O DATASET EM : {}".format(
                        settings.URL_DOWNLOAD_DATA,
                        get_absolute_path(settings.DIR_DATA)
                    )
                )

    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))

    return data_covid


def get_geo(dir_geo):

    """

    OBTÉM OS DADOS DE GEOLOCALIZAÇÃO
    PARA DISPONIBILIZAÇÃO DO MAPA
    E FRONTEIRA ENTRE ESTADOS

    # Arguments
        dir_geo           - Required : Diretório dos
                                       dados -
                                       GEOLOCALIZAÇÃO (String)

    # Required
        df_brazil         - Required : Dados - COVID
                                       Brazil (String)
        df_states         - Required : Dados - COVID
                                       Estados Brasileiros (String)

    """

    # INICIANDO OS DADOS
    data_geo = {}

    try:
        if verify_exists(dir_data_geo):
            # FAZENDO A LEITURA DOS DADOS
            geo_json = json.load(open(dir_data_geo, "r"))
    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))

    return data_geo


# DIRETÓRIO DOS DADOS
dir_data_brazil = os.path.join(
    get_absolute_path(settings.DIR_DATA), settings.NAME_DATA_BRAZIL
)
dir_data_states = os.path.join(
    get_absolute_path(settings.DIR_DATA), settings.NAME_DATA_STATES
)
dir_data_geo = os.path.join(
    get_absolute_path(settings.DIR_DATA_GEO), settings.NAME_DATA_GEO
)

# OBTENDO OS DADOS
df_covid = get_data_covid(
    dir_brazil=dir_data_brazil, dir_states=dir_data_states
)

# OBTENDO OS DADOS DE GEOLOCALIZAÇÃO
json_geo = get_geo(
    dir_geo=dir_data_geo
)

print(json_geo)
