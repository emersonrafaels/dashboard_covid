import os
import json
from inspect import stack

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
from dynaconf import settings

from UTILS.generic_functions import get_absolute_path

def get_data_covid(dir_brazil, dir_states):

    # INICIANDO OS DATAFRAMES
    df_brazil = df_states = pd.DataFrame()

    try:
        df_brazil = pd.read_csv(dir_brazil)
        df_states = pd.read_csv(dir_states)
    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))

    return df_brazil, df_states

# DIRETÓRIO DOS DADOS
dir_data_brazil = os.path.join(get_absolute_path(settings.DIR_DATA),
                               settings.NAME_DATA_BRAZIL)
dir_data_states = os.path.join(get_absolute_path(settings.DIR_DATA),
                               settings.NAME_DATA_STATES)

# OBTENDO OS DADOS
df_brazil, df_states = get_data_covid(dir_brazil=dir_data_brazil,
                                      dir_states=dir_data_states)

print(df_states)