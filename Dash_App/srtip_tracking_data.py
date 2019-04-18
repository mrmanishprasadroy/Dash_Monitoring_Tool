from telegram_definition_L1 import *
import json
import glob
from datetime import datetime
import numpy as np
import pandas as pd
import os

tel_directory = 'D:\\SMS-Siemag\\Runtime\\JSW-CRC\\PLTCM\\TCM\\L2\\log\\tel'

messageId = {
    'M10': 'EF81',
}


def read_strip_tracking_data():
    # initialisation
    allTelegram_M10 = np.array([], dtype=teltype_M10)
    timeIndex = []

    # specify telegram type
    tel_directory_M10 = tel_directory + '\\*' + messageId["M10"] + '*.tel'

    # get list of available files
    filelist = glob.glob(tel_directory_M10)

    # sort file list
    filelist.sort(key=lambda x: os.path.getmtime(x))

    if len(filelist) > 0:
        for file in filelist:
            f = open(file, 'rb')
            oneTelegram = np.fromfile(f, dtype=teltype_M10)
            allTelegram_M10 = np.concatenate((allTelegram_M10, oneTelegram))
            timeIndex.append(datetime.fromtimestamp(os.path.getmtime(file)))
            f.close()
        print("M10: reading of data done")
    else:
        print("M10: no data found")

    cols_1 = ['Coil 1',
              'Coil 2']

    cols_2 = ['Stand 1',
              'Stand 2',
              'Stand 3',
              'Stand 4',
              'Stand 5']

    # data selection

    arr_11 = allTelegram_M10['InMillDistSyncToStripEnd'][:, 0]
    arr_12 = allTelegram_M10['InMillDistSyncToStripEnd'][:, 1]

    arr_21 = allTelegram_M10['InMillExitLengthAtStand'][:, 0]
    arr_22 = allTelegram_M10['InMillExitLengthAtStand'][:, 1]
    arr_23 = allTelegram_M10['InMillExitLengthAtStand'][:, 2]
    arr_24 = allTelegram_M10['InMillExitLengthAtStand'][:, 3]
    arr_25 = allTelegram_M10['InMillExitLengthAtStand'][:, 4]

    arr_1 = arr_11
    arr_1 = np.column_stack([arr_1, arr_12])

    arr_2 = arr_21
    arr_2 = np.column_stack([arr_2, arr_22])
    arr_2 = np.column_stack([arr_2, arr_23])
    arr_2 = np.column_stack([arr_2, arr_24])
    arr_2 = np.column_stack([arr_2, arr_25])

    # creation of data frame
    df_coils = pd.DataFrame(arr_1, columns=cols_1, index=timeIndex)
    df_stand = pd.DataFrame(arr_2, columns=cols_2, index=timeIndex)

    df_coils.sort_index(inplace=True)
    df_stand.sort_index(inplace=True)
    datasets = {
        'df_01': df_coils.to_json(orient='split', date_format='iso'),
        'df_02': df_stand.to_json(orient='split', date_format='iso'),
    }
    return json.dumps(datasets)
