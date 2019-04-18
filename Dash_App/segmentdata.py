from telegram_definition_L1 import *
import json
import glob
from datetime import datetime
import numpy as np
import pandas as pd

tel_directory = 'D:\\SMS-Siemag\\Runtime\\JSW-CRC\\PLTCM\\TCM\\L2\\log\\tel'

messageId = {
    'MP00': 'EE13',
    'MP01': 'EE11',
    'MP02': 'EE12',
    'MP03': 'EE21',
    'MP04': 'EE22',
    'MP05': 'EE31',
    'MP06': 'EE32',
    'MP07': 'EE41',
    'MP08': 'EE42',
    'MP09': 'EE51',
    'MP10': 'EE52'
}


def read_segment_data_monitor():
    allTelegram_MP00 = np.array([], dtype=teltype_M23)
    allTelegram_MP01 = np.array([], dtype=teltype_M21)
    allTelegram_MP02 = np.array([], dtype=teltype_M22)
    allTelegram_MP03 = np.array([], dtype=teltype_M21)
    allTelegram_MP04 = np.array([], dtype=teltype_M22)
    allTelegram_MP05 = np.array([], dtype=teltype_M21)
    allTelegram_MP06 = np.array([], dtype=teltype_M22)
    allTelegram_MP07 = np.array([], dtype=teltype_M21)
    allTelegram_MP08 = np.array([], dtype=teltype_M22)
    allTelegram_MP09 = np.array([], dtype=teltype_M21)
    allTelegram_MP10 = np.array([], dtype=teltype_M24)

    tel_directory_MP00 = tel_directory + '\\*' + messageId["MP00"] + '*.tel'
    tel_directory_MP01 = tel_directory + '\\*' + messageId["MP01"] + '*.tel'
    tel_directory_MP02 = tel_directory + '\\*' + messageId["MP02"] + '*.tel'
    tel_directory_MP03 = tel_directory + '\\*' + messageId["MP03"] + '*.tel'
    tel_directory_MP04 = tel_directory + '\\*' + messageId["MP04"] + '*.tel'
    tel_directory_MP05 = tel_directory + '\\*' + messageId["MP05"] + '*.tel'
    tel_directory_MP06 = tel_directory + '\\*' + messageId["MP06"] + '*.tel'
    tel_directory_MP07 = tel_directory + '\\*' + messageId["MP07"] + '*.tel'
    tel_directory_MP08 = tel_directory + '\\*' + messageId["MP08"] + '*.tel'
    tel_directory_MP09 = tel_directory + '\\*' + messageId["MP09"] + '*.tel'
    tel_directory_MP10 = tel_directory + '\\*' + messageId["MP10"] + '*.tel'

    # MP 00 ----------------------------------------------------------------

    filelist = glob.glob(tel_directory_MP00)

    if len(filelist) > 0:
        for file in filelist:
            f = open(file, 'rb')
            onetelegram = np.fromfile(f, dtype=teltype_M23)
            allTelegram_MP00 = np.concatenate((allTelegram_MP00, onetelegram))
            f.close()
        print("MP 00: reading of data done")
    else:
        print("MP 00: no data found")
    df_MP00 = create_dataset(allTelegram_MP00)
    # MP 01 ----------------------------------------------------------------

    filelist = glob.glob(tel_directory_MP01)

    if len(filelist) > 0:
        for file in filelist:
            f = open(file, 'rb')
            onetelegram = np.fromfile(f, dtype=teltype_M21)
            allTelegram_MP01 = np.concatenate((allTelegram_MP01, onetelegram))
            f.close()
        print("MP 01: reading of data done")
    else:
        print("MP 01: no data found")

    df_MP01 = create_dataset(allTelegram_MP01)

    # MP 02 ----------------------------------------------------------------

    filelist = glob.glob(tel_directory_MP02)

    if len(filelist) > 0:
        for file in filelist:
            f = open(file, 'rb')
            onetelegram = np.fromfile(f, dtype=teltype_M22)
            allTelegram_MP02 = np.concatenate((allTelegram_MP02, onetelegram))
            f.close()
        print("MP 02: reading of data done")
    else:
        print("MP 02: no data found")

    df_MP02 = create_dataset(allTelegram_MP02)
    # MP 03 ----------------------------------------------------------------

    filelist = glob.glob(tel_directory_MP03)

    if len(filelist) > 0:
        for file in filelist:
            f = open(file, 'rb')
            onetelegram = np.fromfile(f, dtype=teltype_M21)
            allTelegram_MP03 = np.concatenate((allTelegram_MP03, onetelegram))
            f.close()
        print("MP 03: reading of data done")
    else:
        print("MP 03: no data found")

    df_MP03 = create_dataset(allTelegram_MP03)
    # MP 04 ----------------------------------------------------------------

    filelist = glob.glob(tel_directory_MP04)

    if len(filelist) > 0:
        for file in filelist:
            f = open(file, 'rb')
            onetelegram = np.fromfile(f, dtype=teltype_M22)
            allTelegram_MP04 = np.concatenate((allTelegram_MP04, onetelegram))
            f.close()
        print("MP 04: reading of data done")
    else:
        print("MP 04: no data found")

    df_MP04 = create_dataset(allTelegram_MP04)
    # MP 05 ----------------------------------------------------------------

    filelist = glob.glob(tel_directory_MP05)

    if len(filelist) > 0:
        for file in filelist:
            f = open(file, 'rb')
            onetelegram = np.fromfile(f, dtype=teltype_M21)
            allTelegram_MP05 = np.concatenate((allTelegram_MP05, onetelegram))
            f.close()
        print("MP 05: reading of data done")
    else:
        print("MP 05: no data found")

    df_MP05 = create_dataset(allTelegram_MP05)
    # MP 06 ----------------------------------------------------------------

    filelist = glob.glob(tel_directory_MP06)

    if len(filelist) > 0:
        for file in filelist:
            f = open(file, 'rb')
            onetelegram = np.fromfile(f, dtype=teltype_M22)
            allTelegram_MP06 = np.concatenate((allTelegram_MP06, onetelegram))
            f.close()
        print("MP 06: reading of data done")
    else:
        print("MP 06: no data found")

    df_MP06 = create_dataset(allTelegram_MP06)

    df_MP01 = create_dataset(allTelegram_MP01)
    # MP 07 ----------------------------------------------------------------

    filelist = glob.glob(tel_directory_MP07)

    if len(filelist) > 0:
        for file in filelist:
            f = open(file, 'rb')
            onetelegram = np.fromfile(f, dtype=teltype_M21)
            allTelegram_MP07 = np.concatenate((allTelegram_MP07, onetelegram))
            f.close()
        print("MP 07: reading of data done")
    else:
        print("MP 07: no data found")

    df_MP07 = create_dataset(allTelegram_MP07)
    # MP 08 ----------------------------------------------------------------

    filelist = glob.glob(tel_directory_MP08)

    if len(filelist) > 0:
        for file in filelist:
            f = open(file, 'rb')
            onetelegram = np.fromfile(f, dtype=teltype_M22)
            allTelegram_MP08 = np.concatenate((allTelegram_MP08, onetelegram))
            f.close()
        print("MP 08: reading of data done")
    else:
        print("MP 08: no data found")

    df_MP08 = create_dataset(allTelegram_MP08)
    # MP 09 ----------------------------------------------------------------

    filelist = glob.glob(tel_directory_MP09)

    if len(filelist) > 0:
        for file in filelist:
            f = open(file, 'rb')
            onetelegram = np.fromfile(f, dtype=teltype_M21)
            allTelegram_MP09 = np.concatenate((allTelegram_MP09, onetelegram))
            f.close()
        print("MP 09: reading of data done")
    else:
        print("MP 09: no data found")

    df_MP09 = create_dataset(allTelegram_MP09)

    # MP 10 ----------------------------------------------------------------

    filelist = glob.glob(tel_directory_MP10)

    if len(filelist) > 0:
        for file in filelist:
            f = open(file, 'rb')
            onetelegram = np.fromfile(f, dtype=teltype_M24)
            allTelegram_MP10 = np.concatenate((allTelegram_MP10, onetelegram))
            f.close()
        print("MP 10: reading of data done")
    else:
        print("MP 10: no data found")

    df_MP10 = create_dataset(allTelegram_MP10)

    datasets = {
        'df_01': df_MP01.sort_values(by=['time']).to_json(orient='split', date_format='iso'),
        'df_02': df_MP02.sort_values(by=['time']).to_json(orient='split', date_format='iso'),
        'df_03': df_MP03.sort_values(by=['time']).to_json(orient='split', date_format='iso'),
        'df_04': df_MP04.sort_values(by=['time']).to_json(orient='split', date_format='iso'),
        'df_05': df_MP05.sort_values(by=['time']).to_json(orient='split', date_format='iso'),
        'df_06': df_MP06.sort_values(by=['time']).to_json(orient='split', date_format='iso'),
        'df_07': df_MP07.sort_values(by=['time']).to_json(orient='split', date_format='iso'),
        'df_08': df_MP08.sort_values(by=['time']).to_json(orient='split', date_format='iso'),
        'df_09': df_MP09.sort_values(by=['time']).to_json(orient='split', date_format='iso'),
        'df_10': df_MP10.sort_values(by=['time']).to_json(orient='split', date_format='iso'),
    }
    return json.dumps(datasets)


def create_dataset(allTelegram):
    ti = [datetime(x['TmSegStart'][0], x['TmSegStart'][1], x['TmSegStart'][2],
                   x['TmSegStart'][3], x['TmSegStart'][4], x['TmSegStart'][5], x['TmSegStart'][6] * 1000)
          for x in allTelegram]

    df = pd.DataFrame({
        'time': ti,
        'SegId': allTelegram['SegId'][:],
        'SetupId': allTelegram['SetupId'][:],
        'CoilId': allTelegram['CoilId'][:],
        'CoilIdOut': allTelegram['CoilIdOut'][:],
        'LenSegStart': allTelegram['LenSegStart'][:],
        'TmSinceThread': allTelegram['TmSinceThread'][:],
        'LenSeg': allTelegram['LenSeg'][:],
        'TmSeg': allTelegram['TmSeg'][:],
        'VolSeg': allTelegram['VolSeg'][:],
        'NumValSeg': allTelegram['NumValSeg'][:]
    })

    return df
