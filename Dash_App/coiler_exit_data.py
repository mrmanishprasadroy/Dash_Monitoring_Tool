import os
import glob

import numpy as np
import pandas as pd

from datetime import datetime
from telegram_definition_L1 import *
from golabal_def import Dir_Path
import json

# telegram directory (default)

tel_directory = Dir_Path

# initialisation

allTelegram_MP10 = np.array([], dtype=teltype_M24)

messageId = {
    'MP10': 'EE52'
}

display_value = {}
display_color = {}

last_display_value = 0
last_display_color = ''


# functions to determine display value and display color ---------------------

def next_display_value():
    global last_display_value

    next_display_value = last_display_value + 2

    last_display_value = next_display_value

    return next_display_value


def next_display_color():
    global last_display_color

    color_list = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']

    next_display_color = color_list[0]

    for i in range(len(color_list)):
        if color_list[i] == last_display_color:
            if i == (len(color_list) - 1):
                next_display_color = color_list[0]
            else:
                next_display_color = color_list[i + 1]

    last_display_color = next_display_color

    return next_display_color


def determine_display_value(name):
    if name not in display_value:
        display_value[name] = next_display_value()


def determine_display_color(name):
    if name not in display_color:
        display_color[name] = next_display_color()


def read_data():
    global allTelegram_MP10
    timeIndex = []

    allTelegram_MP10 = np.array([], dtype=teltype_M24)

    tel_directory_MP10 = tel_directory + '\\*' + messageId["MP10"] + '*.tel'
    # get data for MP10 ------------------------------------------------------

    filelist = glob.glob(tel_directory_MP10)

    filelist.sort(key=lambda x: os.path.getmtime(x))

    if (len(filelist) > 0):
        for file in filelist:
            f = open(file, 'rb')
            oneTelegram = np.fromfile(f, dtype=teltype_M24)
            allTelegram_MP10 = np.concatenate((allTelegram_MP10, oneTelegram))
            timeIndex.append(datetime.fromtimestamp(os.path.getmtime(file)))
            f.close()
        print("MP 10: reading of data done")
    else:
        print("MP 10: no data found")

    global display_value
    global display_color

    global last_display_value
    global last_display_color

    df_MP10 = pd.DataFrame()

    # create DataFrame for MP10 ----------------------------------------------

    ti_MP10 = [datetime(x['TmSegStart'][0], x['TmSegStart'][1], x['TmSegStart'][2],
                        x['TmSegStart'][3], x['TmSegStart'][4], x['TmSegStart'][5], x['TmSegStart'][6] * 1000) for x in
               allTelegram_MP10]

    coil_id_in_1 = allTelegram_MP10['CoilIdInOnCoiler'][:, 0]
    coil_id_in_2 = allTelegram_MP10['CoilIdInOnCoiler'][:, 1]

    coil_id_out_1 = allTelegram_MP10['CoilIdOutOnCoiler'][:, 0]
    coil_id_out_2 = allTelegram_MP10['CoilIdOutOnCoiler'][:, 1]

    strip_length_1 = allTelegram_MP10['StripLengthCoiler'][:, 0]
    strip_length_2 = allTelegram_MP10['StripLengthCoiler'][:, 1]

    coiler_in_use = allTelegram_MP10['CoilerInUse']

    data = {'coil_id_in_1': coil_id_in_1,
            'coil_id_out_1': coil_id_out_1,
            'coil_id_in_2': coil_id_in_2,
            'coil_id_out_2': coil_id_out_2,
            'strip_length_1': strip_length_1,
            'strip_length_2': strip_length_2,
            'coiler_in_use': coiler_in_use,
            'timeIndex': timeIndex}

    cols = ['coil_id_in_1',
            'coil_id_out_1',
            'coil_id_in_2',
            'coil_id_out_2',
            'strip_length_1',
            'strip_length_2',
            'coiler_in_use',
            'timeIndex']

    df_MP10 = pd.DataFrame(data, columns=cols)

    dataset = {
        'df_01': df_MP10.to_json(orient='split', date_format='iso')
    }

    return json.dumps(dataset)
