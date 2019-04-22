from telegram_definition_L1 import *
import json
import glob
from datetime import datetime
import numpy as np
import pandas as pd
import os
from golabal_def import Dir_Path
tel_directory = Dir_Path

messageId = {
    'M26': 'EE53',
}


def read_measurment_data():
    # initialisation
    allTelegram_M26 = np.array([], dtype=teltype_M26)
    timeIndex = []

    # specify telegram type
    tel_directory_M26 = tel_directory + '\\*' + messageId["M26"] + '*.tel'

    # get list of available files
    filelist = glob.glob(tel_directory_M26)

    # sort file list
    filelist.sort(key=lambda x: os.path.getmtime(x))

    if len(filelist) > 0:
        for file in filelist:
            f = open(file, 'rb')
            oneTelegram = np.fromfile(f, dtype=teltype_M26)
            allTelegram_M26 = np.concatenate((allTelegram_M26, oneTelegram))
            timeIndex.append(datetime.fromtimestamp(os.path.getmtime(file)))
            f.close()
        print("M26: reading of data done")
    else:
        print("M26: no data found")

    cols_1 = ['Thickness 1']

    cols_2 = ['Length 1']

    cols_3 = ['StripSpeed 1']

    cols_4 = ['GcsActive G1',
              'GcsActive G2',
              'GcsActive G3',
              'GcsActive G4',
              'GcsActive G5']

    cols_5 = ['FcsActive G1',
              'FcsActive G2',
              'FcsActive G3',
              'FcsActive G4',
              'FcsActive G5']

    # data selection

    arr_11 = allTelegram_M26['Thickness'][:, 0]

    arr_21 = allTelegram_M26['Length'][:, 0]

    arr_31 = allTelegram_M26['StripSpeed'][:, 0]

    arr_41 = allTelegram_M26['GcsActive'][:, 0]
    arr_42 = allTelegram_M26['GcsActive'][:, 1]
    arr_43 = allTelegram_M26['GcsActive'][:, 2]
    arr_44 = allTelegram_M26['GcsActive'][:, 3]
    arr_45 = allTelegram_M26['GcsActive'][:, 4]

    arr_51 = allTelegram_M26['FcsActive'][:, 0]
    arr_52 = allTelegram_M26['FcsActive'][:, 1]
    arr_53 = allTelegram_M26['FcsActive'][:, 2]
    arr_54 = allTelegram_M26['FcsActive'][:, 3]
    arr_55 = allTelegram_M26['FcsActive'][:, 4]

    arr_1 = arr_11

    arr_2 = arr_21

    arr_3 = arr_31

    arr_4 = arr_41
    arr_4 = np.column_stack([arr_4, arr_42])
    arr_4 = np.column_stack([arr_4, arr_43])
    arr_4 = np.column_stack([arr_4, arr_44])
    arr_4 = np.column_stack([arr_4, arr_45])

    arr_5 = arr_51
    arr_5 = np.column_stack([arr_5, arr_52])
    arr_5 = np.column_stack([arr_5, arr_53])
    arr_5 = np.column_stack([arr_5, arr_54])
    arr_5 = np.column_stack([arr_5, arr_55])

    # creation of data frame
    df_thickness = pd.DataFrame(arr_1, columns=cols_1, index=timeIndex)
    df_length = pd.DataFrame(arr_2, columns=cols_2, index=timeIndex)
    df_stripspeed = pd.DataFrame(arr_3, columns=cols_3, index=timeIndex)
    df_GcsActive = pd.DataFrame(arr_4, columns=cols_4, index=timeIndex)
    df_FcsActive = pd.DataFrame(arr_5, columns=cols_5, index=timeIndex)

    df_big_data = pd.concat([df_thickness, df_length, df_stripspeed, df_GcsActive, df_FcsActive], axis=1, sort=False)
    df_big_data.sort_index(inplace=True)
    datasets = {
        'df_01': df_big_data.to_json(orient='split', date_format='iso')
    }
    return json.dumps(datasets)
