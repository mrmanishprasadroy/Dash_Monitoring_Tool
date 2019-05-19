from telegram_definition_L1 import *
import json
import glob
import datetime
import numpy as np
import pandas as pd
from golabal_def import Dir_Path

tel_directory = Dir_Path

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


class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """

    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
                            np.int16, np.int32, np.int64, np.uint8,
                            np.uint16, np.uint32, np.uint64)):
            return int(obj)
        elif isinstance(obj, (np.float_, np.float16, np.float32,
                              np.float64)):
            return float(obj)
        elif isinstance(obj, (np.ndarray,)):  # This is the fix
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


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
    df_MP00 = create_dataset_M23(allTelegram_MP00)
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

    df_MP01 = create_dataset_M21(allTelegram_MP01)

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

    df_MP02 = create_dataset_M22(allTelegram_MP02)
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

    df_MP03 = create_dataset_M21(allTelegram_MP03)
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

    df_MP04 = create_dataset_M22(allTelegram_MP04)
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

    df_MP05 = create_dataset_M21(allTelegram_MP05)
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

    df_MP06 = create_dataset_M22(allTelegram_MP06)

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

    df_MP07 = create_dataset_M21(allTelegram_MP07)
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

    df_MP08 = create_dataset_M22(allTelegram_MP08)
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

    df_MP09 = create_dataset_M21(allTelegram_MP09)

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

    df_MP10 = create_dataset_M24(allTelegram_MP10)

    datasets = {
        'df_00': df_MP00.sort_values(by=['time']).to_json(orient='split', date_format='iso'),
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


'''teltype_M23'''


def create_dataset_M23(allTelegram):
    ti = [datetime.datetime(x['TmSegStart'][0], x['TmSegStart'][1], x['TmSegStart'][2],
                            x['TmSegStart'][3], x['TmSegStart'][4], x['TmSegStart'][5], x['TmSegStart'][6] * 1000)
          for x in allTelegram]

    df = pd.DataFrame({
        'time': ti,
        'SegId': allTelegram['SegId'][:] if allTelegram['SegId'].ndim == 1 else allTelegram['SegId'][:, 0],
        'SetupId': allTelegram['SetupId'][:] if allTelegram['SetupId'].ndim == 1 else allTelegram['SetupId'][:, 0],
        'CoilId': allTelegram['CoilId'][:] if allTelegram['CoilId'].ndim == 1 else allTelegram['CoilId'][:, 0],
        'CoilIdOut': allTelegram['CoilIdOut'][:] if allTelegram['CoilIdOut'].ndim == 1 else allTelegram['CoilIdOut'][:,
                                                                                            0],
        'LenSegStart': allTelegram['LenSegStart'][:] if allTelegram['LenSegStart'].ndim == 1 else allTelegram[
                                                                                                      'LenSegStart'][:,
                                                                                                  0],
        'TmSinceThread': allTelegram['TmSinceThread'][:] if allTelegram['TmSinceThread'].ndim == 1 else allTelegram[
                                                                                                            'TmSinceThread'][
                                                                                                        :, 0],
        'LenSeg': allTelegram['LenSeg'][:] if allTelegram['LenSeg'].ndim == 1 else allTelegram['LenSeg'][:, 0],
        'TmSeg': allTelegram['TmSeg'][:] if allTelegram['TmSeg'].ndim == 1 else allTelegram['TmSeg'][:, 0],
        'VolSeg': allTelegram['VolSeg'][:] if allTelegram['VolSeg'].ndim == 1 else allTelegram['VolSeg'][:, 0],
        'NumValSeg': allTelegram['NumValSeg'][:] if allTelegram['NumValSeg'].ndim == 1 else allTelegram['NumValSeg'][:,
                                                                                            0],
        'PassNo': allTelegram['PassNo'][:] if allTelegram['PassNo'].ndim == 1 else allTelegram['PassNo'][:, 0],
        'TmSegStart': allTelegram['TmSegStart'][:] if allTelegram['TmSegStart'].ndim == 1 else allTelegram[
                                                                                                   'TmSegStart'][:, 0],
        'SegType': allTelegram['SegType'][:] if allTelegram['SegType'].ndim == 1 else allTelegram['SegType'][:, 0],
        'StripTemp': allTelegram['StripTemp'][:] if allTelegram['StripTemp'].ndim == 1 else allTelegram['StripTemp'][:,
                                                                                            0],
        'StripTempSta': allTelegram['StripTempSta'][:] if allTelegram['StripTempSta'].ndim == 1 else allTelegram[
                                                                                                         'StripTempSta'][
                                                                                                     :, 0],
        'StripSpeed': allTelegram['StripSpeed'][:] if allTelegram['StripSpeed'].ndim == 1 else allTelegram[
                                                                                                   'StripSpeed'][:, 0],
        'StripSpeedSta': allTelegram['StripSpeedSta'][:] if allTelegram['StripSpeedSta'].ndim == 1 else allTelegram[
                                                                                                            'StripSpeedSta'][
                                                                                                        :, 0],
        'StripThick': allTelegram['StripThick'][:] if allTelegram['StripThick'].ndim == 1 else allTelegram[
                                                                                                   'StripThick'][:, 0],
        'ThickDev': allTelegram['ThickDev'][:] if allTelegram['ThickDev'].ndim == 1 else allTelegram['ThickDev'][:, 0],
        'ThickDevSta': allTelegram['ThickDevSta'][:] if allTelegram['ThickDevSta'].ndim == 1 else allTelegram[
                                                                                                      'ThickDevSta'][:,
                                                                                                  0],
        'StripWidth': allTelegram['StripWidth'][:] if allTelegram['StripWidth'].ndim == 1 else allTelegram[
                                                                                                   'StripWidth'][:, 0],
        'StripWidthSta': allTelegram['StripWidthSta'][:] if allTelegram['StripWidthSta'].ndim == 1 else allTelegram[
                                                                                                            'StripWidthSta'][
                                                                                                        :, 0],
        'TensionOpOffset': allTelegram['TensionOpOffset'][:] if allTelegram['TensionOpOffset'].ndim == 1 else
        allTelegram['TensionOpOffset'][:, 0],
        'TensionOpOffsetSta': allTelegram['TensionOpOffsetSta'][:] if allTelegram['TensionOpOffsetSta'].ndim == 1 else
        allTelegram['TensionOpOffsetSta'][:, 0],
        'TargetThick': allTelegram['TargetThick'][:] if allTelegram['TargetThick'].ndim == 1 else allTelegram[
                                                                                                      'TargetThick'][:,
                                                                                                  0],
        'TargetThickSta': allTelegram['TargetThickSta'][:] if allTelegram['TargetThickSta'].ndim == 1 else allTelegram[
                                                                                                               'TargetThickSta'][
                                                                                                           :, 0],
        'PayoffReelRevol': allTelegram['PayoffReelRevol'][:] if allTelegram['PayoffReelRevol'].ndim == 1 else
        allTelegram['PayoffReelRevol'][:, 0],
        'PayoffReelRevolSta': allTelegram['PayoffReelRevolSta'][:] if allTelegram['PayoffReelRevolSta'].ndim == 1 else
        allTelegram['PayoffReelRevolSta'][:, 0],
        'PayoffReelPower': allTelegram['PayoffReelPower'][:] if allTelegram['PayoffReelPower'].ndim == 1 else
        allTelegram['PayoffReelPower'][:, 0],
        'PayoffReelPowerSta': allTelegram['PayoffReelPowerSta'][:] if allTelegram['PayoffReelPowerSta'].ndim == 1 else
        allTelegram['PayoffReelPowerSta'][:, 0],
        'PayoffReelCurrent': allTelegram['PayoffReelCurrent'][:] if allTelegram['PayoffReelCurrent'].ndim == 1 else
        allTelegram['PayoffReelCurrent'][:, 0],
        'PayoffReelCurrentSta': allTelegram['PayoffReelCurrentSta'][:] if allTelegram[
                                                                              'PayoffReelCurrentSta'].ndim == 1 else
        allTelegram['PayoffReelCurrentSta'][:, 0],
        'PayoffReelTorque': allTelegram['PayoffReelTorque'][:] if allTelegram['PayoffReelTorque'].ndim == 1 else
        allTelegram['PayoffReelTorque'][:, 0],
        'PayoffReelTorqueSta': allTelegram['PayoffReelTorqueSta'][:] if allTelegram[
                                                                            'PayoffReelTorqueSta'].ndim == 1 else
        allTelegram['PayoffReelTorqueSta'][:, 0],
        'DeflectRollRevol': allTelegram['DeflectRollRevol'][:] if allTelegram['DeflectRollRevol'].ndim == 1 else
        allTelegram['DeflectRollRevol'][:, 0],
        'DeflectRollRevolSta': allTelegram['DeflectRollRevolSta'][:] if allTelegram[
                                                                            'DeflectRollRevolSta'].ndim == 1 else
        allTelegram['DeflectRollRevolSta'][:, 0],
        'DeflectRollCurrent': allTelegram['DeflectRollCurrent'][:] if allTelegram['DeflectRollCurrent'].ndim == 1 else
        allTelegram['DeflectRollCurrent'][:, 0],
        'DeflectRollCurrentSta': allTelegram['DeflectRollCurrentSta'][:] if allTelegram[
                                                                                'DeflectRollCurrentSta'].ndim == 1 else
        allTelegram['DeflectRollCurrentSta'][:, 0],
        'DeflectRollTorque': allTelegram['DeflectRollTorque'][:] if allTelegram['DeflectRollTorque'].ndim == 1 else
        allTelegram['DeflectRollTorque'][:, 0],
        'DeflectRollTorqueSta': allTelegram['DeflectRollTorqueSta'][:] if allTelegram[
                                                                              'DeflectRollTorqueSta'].ndim == 1 else
        allTelegram['DeflectRollTorqueSta'][:, 0],
        'CoilDiamInner': allTelegram['CoilDiamInner'][:] if allTelegram['CoilDiamInner'].ndim == 1 else allTelegram[
                                                                                                            'CoilDiamInner'][
                                                                                                        :, 0],
        'CoilDiamInnerSta': allTelegram['CoilDiamInnerSta'][:] if allTelegram['CoilDiamInnerSta'].ndim == 1 else
        allTelegram['CoilDiamInnerSta'][:, 0],
        'CoilDiamOuter': allTelegram['CoilDiamOuter'][:] if allTelegram['CoilDiamOuter'].ndim == 1 else allTelegram[
                                                                                                            'CoilDiamOuter'][
                                                                                                        :, 0],
        'CoilDiamOuterSta': allTelegram['CoilDiamOuterSta'][:] if allTelegram['CoilDiamOuterSta'].ndim == 1 else
        allTelegram['CoilDiamOuterSta'][:, 0],
        'OffCentreEntry': allTelegram['OffCentreEntry'][:] if allTelegram['OffCentreEntry'].ndim == 1 else allTelegram[
                                                                                                               'OffCentreEntry'][
                                                                                                           :, 0],
        'OffCentreEntrySta': allTelegram['OffCentreEntrySta'][:] if allTelegram['OffCentreEntrySta'].ndim == 1 else
        allTelegram['OffCentreEntrySta'][:, 0],
        'NumMeasStripPhase': allTelegram['NumMeasStripPhase'][:] if allTelegram['NumMeasStripPhase'].ndim == 1 else
        allTelegram['NumMeasStripPhase'][:, 0],
    })

    return df


'''teltype_M24'''


def create_dataset_M24(allTelegram):
    ti = [datetime.datetime(x['TmSegStart'][0], x['TmSegStart'][1], x['TmSegStart'][2],
                            x['TmSegStart'][3], x['TmSegStart'][4], x['TmSegStart'][5], x['TmSegStart'][6] * 1000)
          for x in allTelegram]

    df = pd.DataFrame({
        'time': ti,
        'SegId': allTelegram['SegId'][:] if allTelegram['SegId'].ndim == 1 else allTelegram['SegId'][:, 0],
        'SetupId': allTelegram['SetupId'][:] if allTelegram['SetupId'].ndim == 1 else allTelegram['SetupId'][:, 0],
        'CoilId': allTelegram['CoilId'][:] if allTelegram['CoilId'].ndim == 1 else allTelegram['CoilId'][:, 0],
        'CoilIdOut': allTelegram['CoilIdOut'][:] if allTelegram['CoilIdOut'].ndim == 1 else allTelegram['CoilIdOut'][:,
                                                                                            0],
        'PassNo': allTelegram['PassNo'][:] if allTelegram['PassNo'].ndim == 1 else allTelegram['PassNo'][:, 0],
        'TmSegStart': allTelegram['TmSegStart'][:] if allTelegram['TmSegStart'].ndim == 1 else allTelegram[
                                                                                                   'TmSegStart'][:, 0],
        'LenSegStart': allTelegram['LenSegStart'][:] if allTelegram['LenSegStart'].ndim == 1 else allTelegram[
                                                                                                      'LenSegStart'][:,
                                                                                                  0],
        'TmSinceThread': allTelegram['TmSinceThread'][:] if allTelegram['TmSinceThread'].ndim == 1 else allTelegram[
                                                                                                            'TmSinceThread'][
                                                                                                        :, 0],
        'SegType': allTelegram['SegType'][:] if allTelegram['SegType'].ndim == 1 else allTelegram['SegType'][:, 0],
        'LenSeg': allTelegram['LenSeg'][:] if allTelegram['LenSeg'].ndim == 1 else allTelegram['LenSeg'][:, 0],
        'TmSeg': allTelegram['TmSeg'][:] if allTelegram['TmSeg'].ndim == 1 else allTelegram['TmSeg'][:, 0],
        'VolSeg': allTelegram['VolSeg'][:] if allTelegram['VolSeg'].ndim == 1 else allTelegram['VolSeg'][:, 0],
        'NumValSeg': allTelegram['NumValSeg'][:] if allTelegram['NumValSeg'].ndim == 1 else allTelegram['NumValSeg'][:,
                                                                                            0],
        'StripTemp': allTelegram['StripTemp'][:] if allTelegram['StripTemp'].ndim == 1 else allTelegram['StripTemp'][:,
                                                                                            0],
        'StripTempSta': allTelegram['StripTempSta'][:] if allTelegram['StripTempSta'].ndim == 1 else allTelegram[
                                                                                                         'StripTempSta'][
                                                                                                     :, 0],
        'StripSpeed': allTelegram['StripSpeed'][:] if allTelegram['StripSpeed'].ndim == 1 else allTelegram[
                                                                                                   'StripSpeed'][:, 0],
        'StripSpeedSta': allTelegram['StripSpeedSta'][:] if allTelegram['StripSpeedSta'].ndim == 1 else allTelegram[
                                                                                                            'StripSpeedSta'][
                                                                                                        :, 0],
        'StripThick': allTelegram['StripThick'][:] if allTelegram['StripThick'].ndim == 1 else allTelegram[
                                                                                                   'StripThick'][:, 0],
        'StripThickSta': allTelegram['StripThickSta'][:] if allTelegram['StripThickSta'].ndim == 1 else allTelegram[
                                                                                                            'StripThickSta'][
                                                                                                        :, 0],
        'ThickDev': allTelegram['ThickDev'][:] if allTelegram['ThickDev'].ndim == 1 else allTelegram['ThickDev'][:, 0],
        'ThickDevSta': allTelegram['ThickDevSta'][:] if allTelegram['ThickDevSta'].ndim == 1 else allTelegram[
                                                                                                      'ThickDevSta'][:,
                                                                                                  0],
        'StripWidth': allTelegram['StripWidth'][:] if allTelegram['StripWidth'].ndim == 1 else allTelegram[
                                                                                                   'StripWidth'][:, 0],
        'StripWidthSta': allTelegram['StripWidthSta'][:] if allTelegram['StripWidthSta'].ndim == 1 else allTelegram[
                                                                                                            'StripWidthSta'][
                                                                                                        :, 0],
        'TensionOpOffset': allTelegram['TensionOpOffset'][:] if allTelegram['TensionOpOffset'].ndim == 1 else
        allTelegram['TensionOpOffset'][:, 0],
        'TensionOpOffsetSta': allTelegram['TensionOpOffsetSta'][:] if allTelegram['TensionOpOffsetSta'].ndim == 1 else
        allTelegram['TensionOpOffsetSta'][:, 0],
        'TargetThick': allTelegram['TargetThick'][:] if allTelegram['TargetThick'].ndim == 1 else allTelegram[
                                                                                                      'TargetThick'][:,
                                                                                                  0],
        'TargetThickSta': allTelegram['TargetThickSta'][:] if allTelegram['TargetThickSta'].ndim == 1 else allTelegram[
                                                                                                               'TargetThickSta'][
                                                                                                           :, 0],
        'FlatnessVal': allTelegram['FlatnessVal'][:] if allTelegram['FlatnessVal'].ndim == 1 else allTelegram[
                                                                                                      'FlatnessVal'][:,
                                                                                                  0],
        'FlatnessValSta': allTelegram['FlatnessValSta'][:] if allTelegram['FlatnessValSta'].ndim == 1 else allTelegram[
                                                                                                               'FlatnessValSta'][
                                                                                                           :, 0],
        'FlatnessRollRevol': allTelegram['FlatnessRollRevol'][:] if allTelegram['FlatnessRollRevol'].ndim == 1 else
        allTelegram['FlatnessRollRevol'][:, 0],
        'FlatnessRollRevolSta': allTelegram['FlatnessRollRevolSta'][:] if allTelegram[
                                                                              'FlatnessRollRevolSta'].ndim == 1 else
        allTelegram['FlatnessRollRevolSta'][:, 0],
        'FlatnessRollCurrent': allTelegram['FlatnessRollCurrent'][:] if allTelegram[
                                                                            'FlatnessRollCurrent'].ndim == 1 else
        allTelegram['FlatnessRollCurrent'][:, 0],
        'FlatnessRollCurrentSta': allTelegram['FlatnessRollCurrentSta'][:] if allTelegram[
                                                                                  'FlatnessRollCurrentSta'].ndim == 1 else
        allTelegram['FlatnessRollCurrentSta'][:, 0],
        'FlatnessRollTorque': allTelegram['FlatnessRollTorque'][:] if allTelegram['FlatnessRollTorque'].ndim == 1 else
        allTelegram['FlatnessRollTorque'][:, 0],
        'FlatnessRollTorqueSta': allTelegram['FlatnessRollTorqueSta'][:] if allTelegram[
                                                                                'FlatnessRollTorqueSta'].ndim == 1 else
        allTelegram['FlatnessRollTorqueSta'][:, 0],
        'TargetFlatCoeff': allTelegram['TargetFlatCoeff'][:] if allTelegram['TargetFlatCoeff'].ndim == 1 else
        allTelegram['TargetFlatCoeff'][:, 0],
        'TargetFlatCoeffSta': allTelegram['TargetFlatCoeffSta'][:] if allTelegram['TargetFlatCoeffSta'].ndim == 1 else
        allTelegram['TargetFlatCoeffSta'][:, 0],
        'MeasFlatCoeff': allTelegram['MeasFlatCoeff'][:] if allTelegram['MeasFlatCoeff'].ndim == 1 else allTelegram[
                                                                                                            'MeasFlatCoeff'][
                                                                                                        :, 0],
        'MeasFlatCoeffSta': allTelegram['MeasFlatCoeffSta'][:] if allTelegram['MeasFlatCoeffSta'].ndim == 1 else
        allTelegram['MeasFlatCoeffSta'][:, 0],
        'CoilerInUse': allTelegram['CoilerInUse'][:] if allTelegram['CoilerInUse'].ndim == 1 else allTelegram[
                                                                                                      'CoilerInUse'][:,
                                                                                                  0],
        'TensionReelRevol': allTelegram['TensionReelRevol'][:] if allTelegram['TensionReelRevol'].ndim == 1 else
        allTelegram['TensionReelRevol'][:, 0],
        'TensionReelRevolSta': allTelegram['TensionReelRevolSta'][:] if allTelegram[
                                                                            'TensionReelRevolSta'].ndim == 1 else
        allTelegram['TensionReelRevolSta'][:, 0],
        'TensionReelPower': allTelegram['TensionReelPower'][:] if allTelegram['TensionReelPower'].ndim == 1 else
        allTelegram['TensionReelPower'][:, 0],
        'TensionReelPowerSta': allTelegram['TensionReelPowerSta'][:] if allTelegram[
                                                                            'TensionReelPowerSta'].ndim == 1 else
        allTelegram['TensionReelPowerSta'][:, 0],
        'CoilDiamInner': allTelegram['CoilDiamInner'][:] if allTelegram['CoilDiamInner'].ndim == 1 else allTelegram[
                                                                                                            'CoilDiamInner'][
                                                                                                        :, 0],
        'CoilDiamInnerSta': allTelegram['CoilDiamInnerSta'][:] if allTelegram['CoilDiamInnerSta'].ndim == 1 else
        allTelegram['CoilDiamInnerSta'][:, 0],
        'CoilDiamOuter': allTelegram['CoilDiamOuter'][:] if allTelegram['CoilDiamOuter'].ndim == 1 else allTelegram[
                                                                                                            'CoilDiamOuter'][
                                                                                                        :, 0],
        'CoilDiamOuterSta': allTelegram['CoilDiamOuterSta'][:] if allTelegram['CoilDiamOuterSta'].ndim == 1 else
        allTelegram['CoilDiamOuterSta'][:, 0],
        'OffCentreExit': allTelegram['OffCentreExit'][:] if allTelegram['OffCentreExit'].ndim == 1 else allTelegram[
                                                                                                            'OffCentreExit'][
                                                                                                        :, 0],
        'OffCentreExitSta': allTelegram['OffCentreExitSta'][:] if allTelegram['OffCentreExitSta'].ndim == 1 else
        allTelegram['OffCentreExitSta'][:, 0],
        'CoilIdInOnCoiler': allTelegram['CoilIdInOnCoiler'][:] if allTelegram['CoilIdInOnCoiler'].ndim == 1 else
        allTelegram['CoilIdInOnCoiler'][:, 0],
        'CoilIdOutOnCoiler': allTelegram['CoilIdOutOnCoiler'][:] if allTelegram['CoilIdOutOnCoiler'].ndim == 1 else
        allTelegram['CoilIdOutOnCoiler'][:, 0],
        'StripLengthCoiler': allTelegram['StripLengthCoiler'][:] if allTelegram['StripLengthCoiler'].ndim == 1 else
        allTelegram['StripLengthCoiler'][:, 0],
        'SpoolInd': allTelegram['SpoolInd'][:] if allTelegram['SpoolInd'].ndim == 1 else allTelegram['SpoolInd'][:, 0],
        'SpoolDiamOuter': allTelegram['SpoolDiamOuter'][:] if allTelegram['SpoolDiamOuter'].ndim == 1 else allTelegram[
                                                                                                               'SpoolDiamOuter'][
                                                                                                           :, 0],
        'SpoolDiamInner': allTelegram['SpoolDiamInner'][:] if allTelegram['SpoolDiamInner'].ndim == 1 else allTelegram[
                                                                                                               'SpoolDiamInner'][
                                                                                                           :, 0],
        'SpoolWidth': allTelegram['SpoolWidth'][:] if allTelegram['SpoolWidth'].ndim == 1 else allTelegram[
                                                                                                   'SpoolWidth'][:, 0],
        'NumMeasStripPhase': allTelegram['NumMeasStripPhase'][:] if allTelegram['NumMeasStripPhase'].ndim == 1 else
        allTelegram['NumMeasStripPhase'][:, 0],
        'ARUActivePower': allTelegram['ARUActivePower'][:] if allTelegram['ARUActivePower'].ndim == 1 else allTelegram[
                                                                                                               'ARUActivePower'][
                                                                                                           :, 0],
        'ARUActivePowerSta': allTelegram['ARUActivePowerSta'][:] if allTelegram['ARUActivePowerSta'].ndim == 1 else
        allTelegram['ARUActivePowerSta'][:, 0],
        'ARUCurrent': allTelegram['ARUCurrent'][:] if allTelegram['ARUCurrent'].ndim == 1 else allTelegram[
                                                                                                   'ARUCurrent'][:, 0],
        'ARUCurrentSta': allTelegram['ARUCurrentSta'][:] if allTelegram['ARUCurrentSta'].ndim == 1 else allTelegram[
                                                                                                            'ARUCurrentSta'][
                                                                                                        :, 0],
        'LVPower': allTelegram['LVPower'][:] if allTelegram['LVPower'].ndim == 1 else allTelegram['LVPower'][:, 0],
        'LVPowerSta': allTelegram['LVPowerSta'][:] if allTelegram['LVPowerSta'].ndim == 1 else allTelegram[
                                                                                                   'LVPowerSta'][:, 0],
        'LVLineCurrent': allTelegram['LVLineCurrent'][:] if allTelegram['LVLineCurrent'].ndim == 1 else allTelegram[
                                                                                                            'LVLineCurrent'][
                                                                                                        :, 0],
        'LVLineCurrentSta': allTelegram['LVLineCurrentSta'][:] if allTelegram['LVLineCurrentSta'].ndim == 1 else
        allTelegram['LVLineCurrentSta'][:, 0],
        'LVDCVoltage': allTelegram['LVDCVoltage'][:] if allTelegram['LVDCVoltage'].ndim == 1 else allTelegram[
                                                                                                      'LVDCVoltage'][:,
                                                                                                  0],
        'LVDCVoltageSta': allTelegram['LVDCVoltageSta'][:] if allTelegram['LVDCVoltageSta'].ndim == 1 else allTelegram[
                                                                                                               'LVDCVoltageSta'][
                                                                                                           :, 0],

    })

    return df


'''teltype_M21'''


def create_dataset_M21(allTelegram):
    ti = [datetime.datetime(x['TmSegStart'][0], x['TmSegStart'][1], x['TmSegStart'][2],
                            x['TmSegStart'][3], x['TmSegStart'][4], x['TmSegStart'][5], x['TmSegStart'][6] * 1000)
          for x in allTelegram]

    df = pd.DataFrame({
        'time': ti,
        'SegId': allTelegram['SegId'][:] if allTelegram['SegId'].ndim == 1 else allTelegram['SegId'][:, 0],
        'SetupId': allTelegram['SetupId'][:] if allTelegram['SetupId'].ndim == 1 else allTelegram['SetupId'][:, 0],
        'CoilId': allTelegram['CoilId'][:] if allTelegram['CoilId'].ndim == 1 else allTelegram['CoilId'][:, 0],
        'CoilIdOut': allTelegram['CoilIdOut'][:] if allTelegram['CoilIdOut'].ndim == 1 else allTelegram['CoilIdOut'][:,
                                                                                            0],
        'PassNo': allTelegram['PassNo'][:] if allTelegram['PassNo'].ndim == 1 else allTelegram['PassNo'][:, 0],
        'TmSegStart': allTelegram['TmSegStart'][:] if allTelegram['TmSegStart'].ndim == 1 else allTelegram[
                                                                                                   'TmSegStart'][:, 0],
        'LenSegStart': allTelegram['LenSegStart'][:] if allTelegram['LenSegStart'].ndim == 1 else allTelegram[
                                                                                                      'LenSegStart'][:,
                                                                                                  0],
        'TmSinceThread': allTelegram['TmSinceThread'][:] if allTelegram['TmSinceThread'].ndim == 1 else allTelegram[
                                                                                                            'TmSinceThread'][
                                                                                                        :, 0],
        'SegType': allTelegram['SegType'][:] if allTelegram['SegType'].ndim == 1 else allTelegram['SegType'][:, 0],
        'LenSeg': allTelegram['LenSeg'][:] if allTelegram['LenSeg'].ndim == 1 else allTelegram['LenSeg'][:, 0],
        'TmSeg': allTelegram['TmSeg'][:] if allTelegram['TmSeg'].ndim == 1 else allTelegram['TmSeg'][:, 0],
        'VolSeg': allTelegram['VolSeg'][:] if allTelegram['VolSeg'].ndim == 1 else allTelegram['VolSeg'][:, 0],
        'NumValSeg': allTelegram['NumValSeg'][:] if allTelegram['NumValSeg'].ndim == 1 else allTelegram['NumValSeg'][:,
                                                                                            0],
        'ExitThicknessGCS': allTelegram['ExitThicknessGCS'][:] if allTelegram['ExitThicknessGCS'].ndim == 1 else
        allTelegram['ExitThicknessGCS'][:, 0],
        'ExitThicknessGCSSta': allTelegram['ExitThicknessGCSSta'][:] if allTelegram[
                                                                            'ExitThicknessGCSSta'].ndim == 1 else
        allTelegram['ExitThicknessGCSSta'][:, 0],
        'RollForceOS': allTelegram['RollForceOS'][:] if allTelegram['RollForceOS'].ndim == 1 else allTelegram[
                                                                                                      'RollForceOS'][:,
                                                                                                  0],
        'RollForceOSSta': allTelegram['RollForceOSSta'][:] if allTelegram['RollForceOSSta'].ndim == 1 else allTelegram[
                                                                                                               'RollForceOSSta'][
                                                                                                           :, 0],
        'RollForceDS': allTelegram['RollForceDS'][:] if allTelegram['RollForceDS'].ndim == 1 else allTelegram[
                                                                                                      'RollForceDS'][:,
                                                                                                  0],
        'RollForceDSSta': allTelegram['RollForceDSSta'][:] if allTelegram['RollForceDSSta'].ndim == 1 else allTelegram[
                                                                                                               'RollForceDSSta'][
                                                                                                           :, 0],
        'WrBendOS': allTelegram['WrBendOS'][:] if allTelegram['WrBendOS'].ndim == 1 else allTelegram['WrBendOS'][:, 0],
        'WrBendOSSta': allTelegram['WrBendOSSta'][:] if allTelegram['WrBendOSSta'].ndim == 1 else allTelegram[
                                                                                                      'WrBendOSSta'][:,
                                                                                                  0],
        'WrBendDS': allTelegram['WrBendDS'][:] if allTelegram['WrBendDS'].ndim == 1 else allTelegram['WrBendDS'][:, 0],
        'WrBendDSSta': allTelegram['WrBendDSSta'][:] if allTelegram['WrBendDSSta'].ndim == 1 else allTelegram[
                                                                                                      'WrBendDSSta'][:,
                                                                                                  0],
        'WrBendOpOffset': allTelegram['WrBendOpOffset'][:] if allTelegram['WrBendOpOffset'].ndim == 1 else allTelegram[
                                                                                                               'WrBendOpOffset'][
                                                                                                           :, 0],
        'WrBendOpOffsetSta': allTelegram['WrBendOpOffsetSta'][:] if allTelegram['WrBendOpOffsetSta'].ndim == 1 else
        allTelegram['WrBendOpOffsetSta'][:, 0],
        'IrBendOS': allTelegram['IrBendOS'][:] if allTelegram['IrBendOS'].ndim == 1 else allTelegram['IrBendOS'][:, 0],
        'IrBendOSSta': allTelegram['IrBendOSSta'][:] if allTelegram['IrBendOSSta'].ndim == 1 else allTelegram[
                                                                                                      'IrBendOSSta'][:,
                                                                                                  0],
        'IrBendDS': allTelegram['IrBendDS'][:] if allTelegram['IrBendDS'].ndim == 1 else allTelegram['IrBendDS'][:, 0],
        'IrBendDSSta': allTelegram['IrBendDSSta'][:] if allTelegram['IrBendDSSta'].ndim == 1 else allTelegram[
                                                                                                      'IrBendDSSta'][:,
                                                                                                  0],
        'IrBendOpOffset': allTelegram['IrBendOpOffset'][:] if allTelegram['IrBendOpOffset'].ndim == 1 else allTelegram[
                                                                                                               'IrBendOpOffset'][
                                                                                                           :, 0],
        'IrBendOpOffsetSta': allTelegram['IrBendOpOffsetSta'][:] if allTelegram['IrBendOpOffsetSta'].ndim == 1 else
        allTelegram['IrBendOpOffsetSta'][:, 0],
        'DriveRevol': allTelegram['DriveRevol'][:] if allTelegram['DriveRevol'].ndim == 1 else allTelegram[
                                                                                                   'DriveRevol'][:, 0],
        'DriveRevolSta': allTelegram['DriveRevolSta'][:] if allTelegram['DriveRevolSta'].ndim == 1 else allTelegram[
                                                                                                            'DriveRevolSta'][
                                                                                                        :, 0],
        'DrivePower': allTelegram['DrivePower'][:] if allTelegram['DrivePower'].ndim == 1 else allTelegram[
                                                                                                   'DrivePower'][:, 0],
        'DrivePowerSta': allTelegram['DrivePowerSta'][:] if allTelegram['DrivePowerSta'].ndim == 1 else allTelegram[
                                                                                                            'DrivePowerSta'][
                                                                                                        :, 0],
        'DriveTorque': allTelegram['DriveTorque'][:] if allTelegram['DriveTorque'].ndim == 1 else allTelegram[
                                                                                                      'DriveTorque'][:,
                                                                                                  0],
        'DriveTorqueSta': allTelegram['DriveTorqueSta'][:] if allTelegram['DriveTorqueSta'].ndim == 1 else allTelegram[
                                                                                                               'DriveTorqueSta'][
                                                                                                           :, 0],
        'DriveCurrent': allTelegram['DriveCurrent'][:] if allTelegram['DriveCurrent'].ndim == 1 else allTelegram[
                                                                                                         'DriveCurrent'][
                                                                                                     :, 0],
        'DriveCurrentSta': allTelegram['DriveCurrentSta'][:] if allTelegram['DriveCurrentSta'].ndim == 1 else
        allTelegram['DriveCurrentSta'][:, 0],
        'DriveTemp': allTelegram['DriveTemp'][:] if allTelegram['DriveTemp'].ndim == 1 else allTelegram['DriveTemp'][:,
                                                                                            0],
        'DriveTempSta': allTelegram['DriveTempSta'][:] if allTelegram['DriveTempSta'].ndim == 1 else allTelegram[
                                                                                                         'DriveTempSta'][
                                                                                                     :, 0],
        'RollSpeed': allTelegram['RollSpeed'][:] if allTelegram['RollSpeed'].ndim == 1 else allTelegram['RollSpeed'][:,
                                                                                            0],
        'RollSpeedSta': allTelegram['RollSpeedSta'][:] if allTelegram['RollSpeedSta'].ndim == 1 else allTelegram[
                                                                                                         'RollSpeedSta'][
                                                                                                     :, 0],
        'RollRevol': allTelegram['RollRevol'][:] if allTelegram['RollRevol'].ndim == 1 else allTelegram['RollRevol'][:,
                                                                                            0],
        'RollRevolSta': allTelegram['RollRevolSta'][:] if allTelegram['RollRevolSta'].ndim == 1 else allTelegram[
                                                                                                         'RollRevolSta'][
                                                                                                     :, 0],
        'RollTorque': allTelegram['RollTorque'][:] if allTelegram['RollTorque'].ndim == 1 else allTelegram[
                                                                                                   'RollTorque'][:, 0],
        'RollTorqueSta': allTelegram['RollTorqueSta'][:] if allTelegram['RollTorqueSta'].ndim == 1 else allTelegram[
                                                                                                            'RollTorqueSta'][
                                                                                                        :, 0],
        'SlipForwCalc': allTelegram['SlipForwCalc'][:] if allTelegram['SlipForwCalc'].ndim == 1 else allTelegram[
                                                                                                         'SlipForwCalc'][
                                                                                                     :, 0],
        'SlipForwCalcSta': allTelegram['SlipForwCalcSta'][:] if allTelegram['SlipForwCalcSta'].ndim == 1 else
        allTelegram['SlipForwCalcSta'][:, 0],
        'HydPosOS': allTelegram['HydPosOS'][:] if allTelegram['HydPosOS'].ndim == 1 else allTelegram['HydPosOS'][:, 0],
        'HydPosOSSta': allTelegram['HydPosOSSta'][:] if allTelegram['HydPosOSSta'].ndim == 1 else allTelegram[
                                                                                                      'HydPosOSSta'][:,
                                                                                                  0],
        'HydPosDS': allTelegram['HydPosDS'][:] if allTelegram['HydPosDS'].ndim == 1 else allTelegram['HydPosDS'][:, 0],
        'HydPosDSSta': allTelegram['HydPosDSSta'][:] if allTelegram['HydPosDSSta'].ndim == 1 else allTelegram[
                                                                                                      'HydPosDSSta'][:,
                                                                                                  0],
        'HydPosOpOffset': allTelegram['HydPosOpOffset'][:] if allTelegram['HydPosOpOffset'].ndim == 1 else allTelegram[
                                                                                                               'HydPosOpOffset'][
                                                                                                           :, 0],
        'HydPosOpOffsetSta': allTelegram['HydPosOpOffsetSta'][:] if allTelegram['HydPosOpOffsetSta'].ndim == 1 else
        allTelegram['HydPosOpOffsetSta'][:, 0],
        'GapPos': allTelegram['GapPos'][:] if allTelegram['GapPos'].ndim == 1 else allTelegram['GapPos'][:, 0],
        'GapPosSta': allTelegram['GapPosSta'][:] if allTelegram['GapPosSta'].ndim == 1 else allTelegram['GapPosSta'][:,
                                                                                            0],
        'Tilting': allTelegram['Tilting'][:] if allTelegram['Tilting'].ndim == 1 else allTelegram['Tilting'][:, 0],
        'TiltingSta': allTelegram['TiltingSta'][:] if allTelegram['TiltingSta'].ndim == 1 else allTelegram[
                                                                                                   'TiltingSta'][:, 0],
        'TiltingOpOffset': allTelegram['TiltingOpOffset'][:] if allTelegram['TiltingOpOffset'].ndim == 1 else
        allTelegram['TiltingOpOffset'][:, 0],
        'TiltingOpOffsetSta': allTelegram['TiltingOpOffsetSta'][:] if allTelegram['TiltingOpOffsetSta'].ndim == 1 else
        allTelegram['TiltingOpOffsetSta'][:, 0],
        'CVCShiftTop': allTelegram['CVCShiftTop'][:] if allTelegram['CVCShiftTop'].ndim == 1 else allTelegram[
                                                                                                      'CVCShiftTop'][:,
                                                                                                  0],
        'CVCShiftTopSta': allTelegram['CVCShiftTopSta'][:] if allTelegram['CVCShiftTopSta'].ndim == 1 else allTelegram[
                                                                                                               'CVCShiftTopSta'][
                                                                                                           :, 0],
        'CVCShiftBot': allTelegram['CVCShiftBot'][:] if allTelegram['CVCShiftBot'].ndim == 1 else allTelegram[
                                                                                                      'CVCShiftBot'][:,
                                                                                                  0],
        'CVCShiftBotSta': allTelegram['CVCShiftBotSta'][:] if allTelegram['CVCShiftBotSta'].ndim == 1 else allTelegram[
                                                                                                               'CVCShiftBotSta'][
                                                                                                           :, 0],
        'CVCShiftOpOffset': allTelegram['CVCShiftOpOffset'][:] if allTelegram['CVCShiftOpOffset'].ndim == 1 else
        allTelegram['CVCShiftOpOffset'][:, 0],
        'CVCShiftOpOffsetSta': allTelegram['CVCShiftOpOffsetSta'][:] if allTelegram[
                                                                            'CVCShiftOpOffsetSta'].ndim == 1 else
        allTelegram['CVCShiftOpOffsetSta'][:, 0],
        'RollCoolTemp': allTelegram['RollCoolTemp'][:] if allTelegram['RollCoolTemp'].ndim == 1 else allTelegram[
                                                                                                         'RollCoolTemp'][
                                                                                                     :, 0],
        'RollCoolTempSta': allTelegram['RollCoolTempSta'][:] if allTelegram['RollCoolTempSta'].ndim == 1 else
        allTelegram['RollCoolTempSta'][:, 0],
        'RollCollPress': allTelegram['RollCollPress'][:] if allTelegram['RollCollPress'].ndim == 1 else allTelegram[
                                                                                                            'RollCollPress'][
                                                                                                        :, 0],
        'RollCollPressSta': allTelegram['RollCollPressSta'][:] if allTelegram['RollCollPressSta'].ndim == 1 else
        allTelegram['RollCollPressSta'][:, 0],
        'RollCoolDist': allTelegram['RollCoolDist'][:] if allTelegram['RollCoolDist'].ndim == 1 else allTelegram[
                                                                                                         'RollCoolDist'][
                                                                                                     :, 0],
        'RollCoolDistSta': allTelegram['RollCoolDistSta'][:] if allTelegram['RollCoolDistSta'].ndim == 1 else
        allTelegram['RollCoolDistSta'][:, 0],
        'GcsActive': allTelegram['GcsActive'][:] if allTelegram['GcsActive'].ndim == 1 else allTelegram['GcsActive'][:,
                                                                                            0],
        'FcsActive': allTelegram['FcsActive'][:] if allTelegram['FcsActive'].ndim == 1 else allTelegram['FcsActive'][:,
                                                                                            0],
        'PgmActive': allTelegram['PgmActive'][:] if allTelegram['PgmActive'].ndim == 1 else allTelegram['PgmActive'][:,
                                                                                            0],
        'MillState': allTelegram['MillState'][:] if allTelegram['MillState'].ndim == 1 else allTelegram['MillState'][:,
                                                                                            0],
        'NumMeasStripPhase': allTelegram['NumMeasStripPhase'][:] if allTelegram['NumMeasStripPhase'].ndim == 1 else
        allTelegram['NumMeasStripPhase'][:, 0],
        'ActiveSetup': allTelegram['ActiveSetup'][:] if allTelegram['ActiveSetup'].ndim == 1 else allTelegram[
                                                                                                      'ActiveSetup'][:,
                                                                                                  0],
        'StandAvailable': allTelegram['StandAvailable'][:] if allTelegram['StandAvailable'].ndim == 1 else allTelegram[
                                                                                                               'StandAvailable'][
                                                                                                           :, 0],
        'EntryTensionOS': allTelegram['EntryTensionOS'][:] if allTelegram['EntryTensionOS'].ndim == 1 else allTelegram[
                                                                                                               'EntryTensionOS'][
                                                                                                           :, 0],
        'EntryTensionOSSta': allTelegram['EntryTensionOSSta'][:] if allTelegram['EntryTensionOSSta'].ndim == 1 else
        allTelegram['EntryTensionOSSta'][:, 0],
        'EntryTensionDS': allTelegram['EntryTensionDS'][:] if allTelegram['EntryTensionDS'].ndim == 1 else allTelegram[
                                                                                                               'EntryTensionDS'][
                                                                                                           :, 0],
        'EntryTensionDSSta': allTelegram['EntryTensionDSSta'][:] if allTelegram['EntryTensionDSSta'].ndim == 1 else
        allTelegram['EntryTensionDSSta'][:, 0],
        'ExitTensionOS': allTelegram['ExitTensionOS'][:] if allTelegram['ExitTensionOS'].ndim == 1 else allTelegram[
                                                                                                            'ExitTensionOS'][
                                                                                                        :, 0],
        'ExitTensionOSSta': allTelegram['ExitTensionOSSta'][:] if allTelegram['ExitTensionOSSta'].ndim == 1 else
        allTelegram['ExitTensionOSSta'][:, 0],
        'ExitTensionDS': allTelegram['ExitTensionDS'][:] if allTelegram['ExitTensionDS'].ndim == 1 else allTelegram[
                                                                                                            'ExitTensionDS'][
                                                                                                        :, 0],
        'ExitTensionDSSta': allTelegram['ExitTensionDSSta'][:] if allTelegram['ExitTensionDSSta'].ndim == 1 else
        allTelegram['ExitTensionDSSta'][:, 0],
        'EntryStripSpeed': allTelegram['EntryStripSpeed'][:] if allTelegram['EntryStripSpeed'].ndim == 1 else
        allTelegram['EntryStripSpeed'][:, 0],
        'EntryStripSpeedSta': allTelegram['EntryStripSpeedSta'][:] if allTelegram['EntryStripSpeedSta'].ndim == 1 else
        allTelegram['EntryStripSpeedSta'][:, 0],
        'ExitStripSpeed': allTelegram['ExitStripSpeed'][:] if allTelegram['ExitStripSpeed'].ndim == 1 else allTelegram[
                                                                                                               'ExitStripSpeed'][
                                                                                                           :, 0],
        'ExitStripSpeedSta': allTelegram['ExitStripSpeedSta'][:] if allTelegram['ExitStripSpeedSta'].ndim == 1 else
        allTelegram['ExitStripSpeedSta'][:, 0],
        'AxialFrShiftTop': allTelegram['AxialFrShiftTop'][:] if allTelegram['AxialFrShiftTop'].ndim == 1 else
        allTelegram['AxialFrShiftTop'][:, 0],
        'AxialFrShiftTopSta': allTelegram['AxialFrShiftTopSta'][:] if allTelegram['AxialFrShiftTopSta'].ndim == 1 else
        allTelegram['AxialFrShiftTopSta'][:, 0],
        'AxialFrShiftBot': allTelegram['AxialFrShiftBot'][:] if allTelegram['AxialFrShiftBot'].ndim == 1 else
        allTelegram['AxialFrShiftBot'][:, 0],
        'AxialFrShiftBotSta': allTelegram['AxialFrShiftBotSta'][:] if allTelegram['AxialFrShiftBotSta'].ndim == 1 else
        allTelegram['AxialFrShiftBotSta'][:, 0],
        'LoadCellFrOS': allTelegram['LoadCellFrOS'][:] if allTelegram['LoadCellFrOS'].ndim == 1 else allTelegram[
                                                                                                         'LoadCellFrOS'][
                                                                                                     :, 0],
        'LoadCellFrOSSta': allTelegram['LoadCellFrOSSta'][:] if allTelegram['LoadCellFrOSSta'].ndim == 1 else
        allTelegram['LoadCellFrOSSta'][:, 0],
        'LoadCellFrDS': allTelegram['LoadCellFrDS'][:] if allTelegram['LoadCellFrDS'].ndim == 1 else allTelegram[
                                                                                                         'LoadCellFrDS'][
                                                                                                     :, 0],
        'LoadCellFrDSSta': allTelegram['LoadCellFrDSSta'][:] if allTelegram['LoadCellFrDSSta'].ndim == 1 else
        allTelegram['LoadCellFrDSSta'][:, 0],
        'PgmOffsetWrBending': allTelegram['PgmOffsetWrBending'][:] if allTelegram['PgmOffsetWrBending'].ndim == 1 else
        allTelegram['PgmOffsetWrBending'][:, 0],
        'PgmOffsetWrBendingSta': allTelegram['PgmOffsetWrBendingSta'][:] if allTelegram[
                                                                                'PgmOffsetWrBendingSta'].ndim == 1 else
        allTelegram['PgmOffsetWrBendingSta'][:, 0],
        'PgmOffsetIrBending': allTelegram['PgmOffsetIrBending'][:] if allTelegram['PgmOffsetIrBending'].ndim == 1 else
        allTelegram['PgmOffsetIrBending'][:, 0],
        'PgmOffsetIrBendingSta': allTelegram['PgmOffsetIrBendingSta'][:] if allTelegram[
                                                                                'PgmOffsetIrBendingSta'].ndim == 1 else
        allTelegram['PgmOffsetIrBendingSta'][:, 0],
        'PgmOffsetShift': allTelegram['PgmOffsetShift'][:] if allTelegram['PgmOffsetShift'].ndim == 1 else allTelegram[
                                                                                                               'PgmOffsetShift'][
                                                                                                           :, 0],
        'PgmOffsetShiftSta': allTelegram['PgmOffsetShiftSta'][:] if allTelegram['PgmOffsetShiftSta'].ndim == 1 else
        allTelegram['PgmOffsetShiftSta'][:, 0],
        'FcsOffsetWrBending': allTelegram['FcsOffsetWrBending'][:] if allTelegram['FcsOffsetWrBending'].ndim == 1 else
        allTelegram['FcsOffsetWrBending'][:, 0],
        'FcsOffsetWrBendingSta': allTelegram['FcsOffsetWrBendingSta'][:] if allTelegram[
                                                                                'FcsOffsetWrBendingSta'].ndim == 1 else
        allTelegram['FcsOffsetWrBendingSta'][:, 0],
        'FcsOffsetIrBending': allTelegram['FcsOffsetIrBending'][:] if allTelegram['FcsOffsetIrBending'].ndim == 1 else
        allTelegram['FcsOffsetIrBending'][:, 0],
        'FcsOffsetIrBendingSta': allTelegram['FcsOffsetIrBendingSta'][:] if allTelegram[
                                                                                'FcsOffsetIrBendingSta'].ndim == 1 else
        allTelegram['FcsOffsetIrBendingSta'][:, 0],
        'FcsOffsetShift': allTelegram['FcsOffsetShift'][:] if allTelegram['FcsOffsetShift'].ndim == 1 else allTelegram[
                                                                                                               'FcsOffsetShift'][
                                                                                                           :, 0],
        'FcsOffsetShiftSta': allTelegram['FcsOffsetShiftSta'][:] if allTelegram['FcsOffsetShiftSta'].ndim == 1 else
        allTelegram['FcsOffsetShiftSta'][:, 0],
        'RefWrBendingSetup': allTelegram['RefWrBendingSetup'][:] if allTelegram['RefWrBendingSetup'].ndim == 1 else
        allTelegram['RefWrBendingSetup'][:, 0],
        'RefWrBendingSetupSta': allTelegram['RefWrBendingSetupSta'][:] if allTelegram[
                                                                              'RefWrBendingSetupSta'].ndim == 1 else
        allTelegram['RefWrBendingSetupSta'][:, 0],
        'RefIrBendingSetup': allTelegram['RefIrBendingSetup'][:] if allTelegram['RefIrBendingSetup'].ndim == 1 else
        allTelegram['RefIrBendingSetup'][:, 0],
        'RefIrBendingSetupSta': allTelegram['RefIrBendingSetupSta'][:] if allTelegram[
                                                                              'RefIrBendingSetupSta'].ndim == 1 else
        allTelegram['RefIrBendingSetupSta'][:, 0],
        'RefShiftSetup': allTelegram['RefShiftSetup'][:] if allTelegram['RefShiftSetup'].ndim == 1 else allTelegram[
                                                                                                            'RefShiftSetup'][
                                                                                                        :, 0],
        'RefShiftSetupSta': allTelegram['RefShiftSetupSta'][:] if allTelegram['RefShiftSetupSta'].ndim == 1 else
        allTelegram['RefShiftSetupSta'][:, 0],
        'RefTiltSetup': allTelegram['RefTiltSetup'][:] if allTelegram['RefTiltSetup'].ndim == 1 else allTelegram[
                                                                                                         'RefTiltSetup'][
                                                                                                     :, 0],
        'RefTiltSetupSta': allTelegram['RefTiltSetupSta'][:] if allTelegram['RefTiltSetupSta'].ndim == 1 else
        allTelegram['RefTiltSetupSta'][:, 0],
        'RefGapSetup': allTelegram['RefGapSetup'][:] if allTelegram['RefGapSetup'].ndim == 1 else allTelegram[
                                                                                                      'RefGapSetup'][:,
                                                                                                  0],
        'RefGapSetupSta': allTelegram['RefGapSetupSta'][:] if allTelegram['RefGapSetupSta'].ndim == 1 else allTelegram[
                                                                                                               'RefGapSetupSta'][
                                                                                                           :, 0],
        'LDCThickCorrOp': allTelegram['LDCThickCorrOp'][:] if allTelegram['LDCThickCorrOp'].ndim == 1 else allTelegram[
                                                                                                               'LDCThickCorrOp'][
                                                                                                           :, 0],
        'LDCThickCorrOpSta': allTelegram['LDCThickCorrOpSta'][:] if allTelegram['LDCThickCorrOpSta'].ndim == 1 else
        allTelegram['LDCThickCorrOpSta'][:, 0],
        'LDCThickCorrAuto': allTelegram['LDCThickCorrAuto'][:] if allTelegram['LDCThickCorrAuto'].ndim == 1 else
        allTelegram['LDCThickCorrAuto'][:, 0],
        'LDCThickCorrAutoSta': allTelegram['LDCThickCorrAutoSta'][:] if allTelegram[
                                                                            'LDCThickCorrAutoSta'].ndim == 1 else
        allTelegram['LDCThickCorrAutoSta'][:, 0],

    })

    return df


'''teltype_M22'''


def create_dataset_M22(allTelegram):
    ti = [datetime.datetime(x['TmSegStart'][0], x['TmSegStart'][1], x['TmSegStart'][2],
                            x['TmSegStart'][3], x['TmSegStart'][4], x['TmSegStart'][5], x['TmSegStart'][6] * 1000)
          for x in allTelegram]

    df = pd.DataFrame({
        'time': ti,
        'SegId': allTelegram['SegId'][:] if allTelegram['SegId'].ndim == 1 else allTelegram['SegId'][:, 0],
        'SetupId': allTelegram['SetupId'][:] if allTelegram['SetupId'].ndim == 1 else allTelegram['SetupId'][:, 0],
        'CoilId': allTelegram['CoilId'][:] if allTelegram['CoilId'].ndim == 1 else allTelegram['CoilId'][:, 0],
        'CoilIdOut': allTelegram['CoilIdOut'][:] if allTelegram['CoilIdOut'].ndim == 1 else allTelegram['CoilIdOut'][:,
                                                                                            0],
        'PassNo': allTelegram['PassNo'][:] if allTelegram['PassNo'].ndim == 1 else allTelegram['PassNo'][:, 0],
        'TmSegStart': allTelegram['TmSegStart'][:] if allTelegram['TmSegStart'].ndim == 1 else allTelegram[
                                                                                                   'TmSegStart'][:, 0],
        'LenSegStart': allTelegram['LenSegStart'][:] if allTelegram['LenSegStart'].ndim == 1 else allTelegram[
                                                                                                      'LenSegStart'][:,
                                                                                                  0],
        'TmSinceThread': allTelegram['TmSinceThread'][:] if allTelegram['TmSinceThread'].ndim == 1 else allTelegram[
                                                                                                            'TmSinceThread'][
                                                                                                        :, 0],
        'SegType': allTelegram['SegType'][:] if allTelegram['SegType'].ndim == 1 else allTelegram['SegType'][:, 0],
        'LenSeg': allTelegram['LenSeg'][:] if allTelegram['LenSeg'].ndim == 1 else allTelegram['LenSeg'][:, 0],
        'TmSeg': allTelegram['TmSeg'][:] if allTelegram['TmSeg'].ndim == 1 else allTelegram['TmSeg'][:, 0],
        'VolSeg': allTelegram['VolSeg'][:] if allTelegram['VolSeg'].ndim == 1 else allTelegram['VolSeg'][:, 0],
        'NumValSeg': allTelegram['NumValSeg'][:] if allTelegram['NumValSeg'].ndim == 1 else allTelegram['NumValSeg'][:,
                                                                                            0],
        'StripTemp': allTelegram['StripTemp'][:] if allTelegram['StripTemp'].ndim == 1 else allTelegram['StripTemp'][:,
                                                                                            0],
        'StripTempSta': allTelegram['StripTempSta'][:] if allTelegram['StripTempSta'].ndim == 1 else allTelegram[
                                                                                                         'StripTempSta'][
                                                                                                     :, 0],
        'StripSpeed': allTelegram['StripSpeed'][:] if allTelegram['StripSpeed'].ndim == 1 else allTelegram[
                                                                                                   'StripSpeed'][:, 0],
        'StripSpeedSta': allTelegram['StripSpeedSta'][:] if allTelegram['StripSpeedSta'].ndim == 1 else allTelegram[
                                                                                                            'StripSpeedSta'][
                                                                                                        :, 0],
        'StripThick': allTelegram['StripThick'][:] if allTelegram['StripThick'].ndim == 1 else allTelegram[
                                                                                                   'StripThick'][:, 0],
        'StripThickSta': allTelegram['StripThickSta'][:] if allTelegram['StripThickSta'].ndim == 1 else allTelegram[
                                                                                                            'StripThickSta'][
                                                                                                        :, 0],
        'ThickDev': allTelegram['ThickDev'][:] if allTelegram['ThickDev'].ndim == 1 else allTelegram['ThickDev'][:, 0],
        'ThickDevSta': allTelegram['ThickDevSta'][:] if allTelegram['ThickDevSta'].ndim == 1 else allTelegram[
                                                                                                      'ThickDevSta'][:,
                                                                                                  0],
        'StripWidth': allTelegram['StripWidth'][:] if allTelegram['StripWidth'].ndim == 1 else allTelegram[
                                                                                                   'StripWidth'][:, 0],
        'StripWidthSta': allTelegram['StripWidthSta'][:] if allTelegram['StripWidthSta'].ndim == 1 else allTelegram[
                                                                                                            'StripWidthSta'][
                                                                                                        :, 0],
        'TensionOpOffset': allTelegram['TensionOpOffset'][:] if allTelegram['TensionOpOffset'].ndim == 1 else
        allTelegram['TensionOpOffset'][:, 0],
        'TensionOpOffsetSta': allTelegram['TensionOpOffsetSta'][:] if allTelegram['TensionOpOffsetSta'].ndim == 1 else
        allTelegram['TensionOpOffsetSta'][:, 0],
        'TargetThick': allTelegram['TargetThick'][:] if allTelegram['TargetThick'].ndim == 1 else allTelegram[
                                                                                                      'TargetThick'][:,
                                                                                                  0],
        'TargetThickSta': allTelegram['TargetThickSta'][:] if allTelegram['TargetThickSta'].ndim == 1 else allTelegram[
                                                                                                               'TargetThickSta'][
                                                                                                           :, 0],
        'FlatnessVal': allTelegram['FlatnessVal'][:] if allTelegram['FlatnessVal'].ndim == 1 else allTelegram[
                                                                                                      'FlatnessVal'][:,
                                                                                                  0],
        'FlatnessValSta': allTelegram['FlatnessValSta'][:] if allTelegram['FlatnessValSta'].ndim == 1 else allTelegram[
                                                                                                               'FlatnessValSta'][
                                                                                                           :, 0],
        'FlatnessRollRevol': allTelegram['FlatnessRollRevol'][:] if allTelegram['FlatnessRollRevol'].ndim == 1 else
        allTelegram['FlatnessRollRevol'][:, 0],
        'FlatnessRollRevolSta': allTelegram['FlatnessRollRevolSta'][:] if allTelegram[
                                                                              'FlatnessRollRevolSta'].ndim == 1 else
        allTelegram['FlatnessRollRevolSta'][:, 0],
        'FlatnessRollCurrent': allTelegram['FlatnessRollCurrent'][:] if allTelegram[
                                                                            'FlatnessRollCurrent'].ndim == 1 else
        allTelegram['FlatnessRollCurrent'][:, 0],
        'FlatnessRollCurrentSta': allTelegram['FlatnessRollCurrentSta'][:] if allTelegram[
                                                                                  'FlatnessRollCurrentSta'].ndim == 1 else
        allTelegram['FlatnessRollCurrentSta'][:, 0],
        'FlatnessRollTorque': allTelegram['FlatnessRollTorque'][:] if allTelegram['FlatnessRollTorque'].ndim == 1 else
        allTelegram['FlatnessRollTorque'][:, 0],
        'FlatnessRollTorqueSta': allTelegram['FlatnessRollTorqueSta'][:] if allTelegram[
                                                                                'FlatnessRollTorqueSta'].ndim == 1 else
        allTelegram['FlatnessRollTorqueSta'][:, 0],
        'TargetFlatCoeff': allTelegram['TargetFlatCoeff'][:] if allTelegram['TargetFlatCoeff'].ndim == 1 else
        allTelegram['TargetFlatCoeff'][:, 0],
        'TargetFlatCoeffSta': allTelegram['TargetFlatCoeffSta'][:] if allTelegram['TargetFlatCoeffSta'].ndim == 1 else
        allTelegram['TargetFlatCoeffSta'][:, 0],
        'MeasFlatCoeff': allTelegram['MeasFlatCoeff'][:] if allTelegram['MeasFlatCoeff'].ndim == 1 else allTelegram[
                                                                                                            'MeasFlatCoeff'][
                                                                                                        :, 0],
        'MeasFlatCoeffSta': allTelegram['MeasFlatCoeffSta'][:] if allTelegram['MeasFlatCoeffSta'].ndim == 1 else
        allTelegram['MeasFlatCoeffSta'][:, 0],
        'OffCentreExit': allTelegram['OffCentreExit'][:] if allTelegram['OffCentreExit'].ndim == 1 else allTelegram[
                                                                                                            'OffCentreExit'][
                                                                                                        :, 0],
        'OffCentreExitSta': allTelegram['OffCentreExitSta'][:] if allTelegram['OffCentreExitSta'].ndim == 1 else
        allTelegram['OffCentreExitSta'][:, 0],
        'StripCoolTemp': allTelegram['StripCoolTemp'][:] if allTelegram['StripCoolTemp'].ndim == 1 else allTelegram[
                                                                                                            'StripCoolTemp'][
                                                                                                        :, 0],
        'StripCoolTempSta': allTelegram['StripCoolTempSta'][:] if allTelegram['StripCoolTempSta'].ndim == 1 else
        allTelegram['StripCoolTempSta'][:, 0],
        'StripCoolPress': allTelegram['StripCoolPress'][:] if allTelegram['StripCoolPress'].ndim == 1 else allTelegram[
                                                                                                               'StripCoolPress'][
                                                                                                           :, 0],
        'StripCoolPressSta': allTelegram['StripCoolPressSta'][:] if allTelegram['StripCoolPressSta'].ndim == 1 else
        allTelegram['StripCoolPressSta'][:, 0],
        'StripCoolDist': allTelegram['StripCoolDist'][:] if allTelegram['StripCoolDist'].ndim == 1 else allTelegram[
                                                                                                            'StripCoolDist'][
                                                                                                        :, 0],
        'StripCoolDistSta': allTelegram['StripCoolDistSta'][:] if allTelegram['StripCoolDistSta'].ndim == 1 else
        allTelegram['StripCoolDistSta'][:, 0],
        'NumMeasStripPhase': allTelegram['NumMeasStripPhase'][:] if allTelegram['NumMeasStripPhase'].ndim == 1 else
        allTelegram['NumMeasStripPhase'][:, 0],

    })

    return df
