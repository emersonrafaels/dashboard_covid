"""

    FUNÇÕES GENÉRICAS UTILIZANDO PYTHON.

    # Arguments

    # Returns


"""

__version__ = "1.0"
__author__ = """Emerson V. Rafael (EMERVIN)"""
__data_atualizacao__ = "04/07/2021"


import datetime
import time
import re
from collections import OrderedDict
from inspect import stack
from os import path, makedirs, listdir
from typing import Union
from pathlib import Path

import pandas as pd


def verify_exists(dir: str) -> bool:

    """

    FUNÇÃO PARA VERIFICAR SE UM DIRETÓRIO (PATH) EXISTE.

    # Arguments
        dir                  - Required : Diretório a ser verificado (String)

    # Returns
        validator            - Required : validator da função (Boolean)

    """

    # INICIANDO O validator DA FUNÇÃO
    validator = False

    try:
        validator = path.exists(dir)
    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {]".format(stack()[0][3], ex))

    return validator


def create_path(dir: str) -> bool:

    """

    FUNÇÃO PARA CRIAR UM DIRETÓRIO (PATH).

    # Arguments
        dir                  - Required : Diretório a ser criado (String)

    # Returns
        validator            - Required : validator da função (Boolean)

    """

    # INICIANDO O validator DA FUNÇÃO
    validator = False

    try:
        # REALIZANDO A CRIAÇÃO DO DIRETÓRIO
        makedirs(dir)

        validator = True
    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {]".format(stack()[0][3], ex))

    return validator


def get_absolute_path(dir):

    """

    OBTÉM O CAMINHO ABSOLUTO ATÉ UM DIRETÓRIO
    DADO UM DIRETÓRIO RELATIVO.

    # Arguments
        dir          - Required : Diretório a ser analisado (String)

    """

    return path.join(str(Path(path.dirname(__file__)).parent), dir)


def get_files_directory(
    directory: str, format_types_accepted: Union[tuple, list]
) -> list:

    """

    FUNÇÃO PARA OBTER OS ARQUIVOS EM UM DETERMINADO DIRETÓRIO
    FILTRANDO APENAS OS ARQUIVOS DOS FORMATOS ACEITOS POR ESSA API

    # Arguments
        directory                    - Required : Caminho/Diretório para obter os arquivos (String)
        format_types_accepted        - Required : Tipos de arquivos aceitos (List)

    # Returns
        list_archives_accepted       - Required : Caminho dos arquivos listados (List)

    """

    # INICIANDO A VARIÁVEL QUE ARMAZENARÁ TODOS OS ARQUIVOS DO DIRETÓRIO
    list_files = []

    try:
        # VERIFICANDO SE É DIRETÓRIO
        if path.isdir(directory):

            # OBTENDO OS ARQUIVOS NO DIRETÓRIO
            list_files = [path.join(directory, name) for name in listdir(directory)]

            if format_types_accepted:

                if not isinstance(format_types_accepted, tuple):
                    format_types_accepted = tuple(format_types_accepted)


                list_files = [
                    arq
                    for arq in list_files
                    if arq.lower().endswith((format_types_accepted))
                ]

        else:
            list_files = [directory]


    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {]".format(stack()[0][3], ex))

    return list_files


def converte_int(valor_para_converter: Union[str, int]) -> int:

    """

    FUNÇÃO GENÉRICA PARA CONVERTER UM VALOR PARA FORMATO INTEIRO.


    # Arguments
        valor_para_converter              - Required : Valor para converter (Object)

    # Returns
        valor_para_converter              - Required : Valor após conversão (Integer)

    """

    try:
        if isinstance(valor_para_converter, int):
            return valor_para_converter
        else:
            return int(valor_para_converter)
    except Exception as ex:
        print(ex)
        return None


def convert_list_bi_to_unidimensional(list_bid: Union[tuple, list]) -> list:

    """

    FUNÇÃO QUE PERMITE A CONVERSÃO DE UMA LISTA BIDIMENSIONAL PARA UMA LISTA SIMPLES.

    # Arguments
        list_bid           - Required : Lista Bidimensional. (List)

    # Returns
        list_uni_result    - Required : Lista Unidimensional. (List)

    """

    list_uni_result = []

    try:
        for list_uni in list_bid:
            for value in list_uni:
                list_uni_result.append(value)

    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {]".format(stack()[0][3], ex))
        list_uni_result = list_bid

    return list_uni_result


def drop_duplicates_list(list_values: list) -> list:

    """

    REMOVE DUPLICIDADES EM UMA LISTA DE VALORES

    # Arguments
        list_values                - Required : Lista de input. (List)

    # Returns
        list_without_duplicates    - Required : Lista sem duplicidades. (List)

    """

    if not isinstance(list_values, (tuple, list)):

        list_values = list_values.split()

    return list(OrderedDict.fromkeys(list_values))


def has_number(value_test: str) -> bool:

    """

    FUNÇÃO QUE ANALISA SE HÁ NÚMEROS EM UMA STRING

    # Arguments
        value_test         - Required : String a ser testada. (String)

    # Returns
        list_uni_result    - Required : Lista Unidimensional. (List)

    """

    # OBTENDO O PATTERN DE APENAS NÚMEROS
    pattern_number = "[^\d]"

    try:
        # REALIZANDO A VERIFICAÇÃO
        if len(re.sub(pattern=pattern_number, string=str(value_test), repl="")) > 0:
            # A STRING POSSUI NÚMEROS
            return True
    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))

    return False


def get_split_dir(dir: str) -> [str, str]:

    """

    USADO PARA DIVIDIR O NOME DO CAMINHO EM UM PAR DE CABEÇA E CAUDA.
    AQUI, CAUDA É O ÚLTIMO COMPONENTE DO NOME DO CAMINHO E CABEÇA É TUDO QUE LEVA A ISSO.

    EX: nome do caminho = '/home/User/Desktop/file.txt'
    CABEÇA: '/home/User/Desktop'
    CAUDA: 'file.txt'

    * O DIR PODE SER UMA BASE64

    # Arguments
        dir                 - Required : Caminho a ser splitado (String)

    # Returns
        directory           - Required : Cabeça do diretório (String)
        filename            - Required : Cauda do diretório (String)

    """

    # INICIANDO AS VARIÁVEIS A SEREM OBTIDAS
    directory = filename = None

    try:
        directory, filename = path.split(dir)
    except Exception as ex:
        print(ex)

    return directory, filename


def read_csv(data_dir: str) -> [bool, pd.DataFrame]:

    """

    REALIZA LEITURA DA BASE (CSV)

    # Arguments
        data_dir                      - Required : Diretório da base a ser lida (String)

    # Returns
        validator                     - Required : Validação da função (Boolean)
        dataframe                     - Required : Base lida (DataFrame)

    """

    # INICIANDO O validator
    validator = False

    # INICIANDO O DATAFRAME DE RESULTADO DA LEITURA
    dataframe = pd.DataFrame()

    try:
        dataframe = pd.read_csv(data_dir, encoding="utf-8")

        validator = True
    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))

    return validator, dataframe


def save_excel(dataframe_to_save: pd.DataFrame, data_dir: str) -> bool:

    """

    REALIZA SAVE DA BASE (CSV)

    # Arguments
        dataframe_to_save             - Required : Base a ser salva (DataFrame)
        data_dir                      - Required : Diretório da base a ser salva (String)

    # Returns
        validator                     - Required : Validação da função (Boolean)

    """

    # INICIANDO O validator
    validator = False

    try:
        dataframe_to_save.to_excel(data_dir, index=None)

        validator = True
    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))

    return validator


def get_date_time_now(return_type: str) -> str:

    """

    OBTÉM TODOS OS POSSÍVEIS RETORNOS DE DATA_DOWNLOAD E TEMPO.

    # Arguments
        return_type                    - Required : Formato de retorno. (String)

    # Returns

    """

    """%d/%m/%Y %H:%M:%S | %Y-%m-%d %H:%M:%S
    Dia: %d
    Mês: %
    Ano: %Y
    Data: %Y/%m/%d

    Hora: %H
    Minuto: %M
    Segundo: %S"""

    try:
        ts = time.time()
        stfim = datetime.datetime.fromtimestamp(ts).strftime(return_type)

        return stfim
    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))
        return datetime.datetime.now()