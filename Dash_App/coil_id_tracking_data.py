import glob
import os
from datetime import datetime
import json
import numpy as np
import pandas as pd
from pandas import DataFrame
import time

from telegram_definition_L1 import *
from golabal_def import Dir_Path

# telegram directory (default)
tel_directory = Dir_Path

# initialisation

allTelegram_M06 = np.array([], dtype=teltype_M06)

timeIndex = []

messageId = {
    'M06': 'E2D4'
}


def read_coilid_data():
    start_time = time.time()
    # initialisation
    allTelegram_M06 = np.array([], dtype=teltype_M06)
    timeIndex = []

    # specify telegram type
    tel_directory_M06 = tel_directory + '\\*' + messageId["M06"] + '*.tel'

    # get list of available files
    filelist = glob.glob(tel_directory_M06)

    # sort file list
    filelist.sort(key=lambda x: os.path.getmtime(x))

    if (len(filelist) > 0):
        for file in filelist:
            f = open(file, 'rb')
            oneTelegram = np.fromfile(f, dtype=teltype_M06)
            allTelegram_M06 = np.concatenate((allTelegram_M06, oneTelegram))
            timeIndex.append(datetime.fromtimestamp(os.path.getmtime(file)))
            f.close()
        print("M06: reading of data done")
    else:
        print("M06: no data found")

    df_1 = pd.DataFrame({
        'timeindex': timeIndex,
        'coil_1': allTelegram_M06['CoilIdOut'][:, 0],
        'coil_2': allTelegram_M06['CoilIdOut'][:, 2],
        'coil_3': allTelegram_M06['CoilIdOut'][:, 3],
        'coil_4': allTelegram_M06['CoilIdOut'][:, 1],
        'coil_5': allTelegram_M06['CoilIdOut'][:, 4],
        'coil_6': allTelegram_M06['CoilIdOut'][:, 5],
        'coil_7': allTelegram_M06['CoilIdOut'][:, 6],
        'coil_8': allTelegram_M06['CoilIdOut'][:, 7],
        'coil_9': allTelegram_M06['CoilIdOut'][:, 8],
        'coil_10': allTelegram_M06['CoilIdOut'][:, 9],
        'coil_11': allTelegram_M06['CoilIdOut'][:, 10],
        'coil_12': allTelegram_M06['CoilIdOut'][:, 11],

    })
    datasets = {
        'df_01': df_1.to_json(orient='split', date_format='iso'),
    }
    elaps1_time = "- %s seconds ---" % (time.time() - start_time)
    print(elaps1_time + 'coilId_Tracking compile')

    return json.dumps(datasets)
