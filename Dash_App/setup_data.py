import glob
import os
from datetime import datetime
import json
import numpy as np
import pandas as pd
from pandas import DataFrame
import time

from telegram_definition_L1 import *

# telegram directory (default)
tel_directory = 'D:\\SMS-Siemag\\Runtime\\JSW-CRC\\PLTCM\\TCM\\L2\\log\\tel'

# initialisation

selTelegram_N02 = np.array([], dtype=teltype_N02)
appended_allTelegram_N02 = []

timeIndex = []
alltimeIndex = []

messageId = {
    'N02': 'EF21',
}


def read_unique_coil():
    # initialisation
    start_time = time.time()
    allTelegram_N02 = np.array([], dtype=teltype_N02)
    selTelegram_N02 = np.array([], dtype=teltype_N02)
    # specificy telegram type
    tel_directory_N02 = tel_directory + '\\*' + messageId["N02"] + '*.tel'

    # get list of available files

    filelist = glob.glob(tel_directory_N02)

    # sort  file list

    filelist.sort(key=lambda x: os.path.getmtime(x))

    if len(filelist) > 0:
        for file in filelist:
            f = open(file, 'rb')
            one_telegram = np.fromfile(f, dtype=teltype_N02)
            selTelegram_N02 = np.concatenate((selTelegram_N02, one_telegram))
            alltimeIndex.append(datetime.fromtimestamp(os.path.getmtime(file)))
            f.close()
        elaps_time = "- %s seconds ---" % (time.time() - start_time)
        print("N02: no data found time" + elaps_time)

    else:
        print("N02: no data found")

    arr_coilids = selTelegram_N02['CoilIdOut'][:]
    coils = []
    for coil in np.nditer(np.unique(arr_coilids)):
        coils.append(coil)

    df_coils = pd.DataFrame(np.unique(arr_coilids), columns=['coils'])

    return df_coils


def setup_data():
    # initialisation
    start_time = time.time()
    allTelegram_N02 = np.array([], dtype=teltype_N02)
    selTelegram_N02 = np.array([], dtype=teltype_N02)
    # specificy telegram type
    tel_directory_N02 = tel_directory + '\\*' + messageId["N02"] + '*.tel'

    # get list of available files

    filelist = glob.glob(tel_directory_N02)

    # sort  file list

    filelist.sort(key=lambda x: os.path.getmtime(x))

    if len(filelist) > 0:
        for file in filelist:
            f = open(file, 'rb')
            one_telegram = np.fromfile(f, dtype=teltype_N02)
            selTelegram_N02 = np.concatenate((selTelegram_N02, one_telegram))
            timeIndex.append(datetime.fromtimestamp(os.path.getmtime(file)))
            f.close()
        elaps_time = "- %s seconds ---" % (time.time() - start_time)
        print("N02: no data found time" + elaps_time)

    else:
        print("N02: no data found")

    # Alloy composition
    df_chem = DataFrame(selTelegram_N02['AlloyComposition'][:, :7])
    df_chem.columns = ['chem_1', 'chem_2', 'chem_3', 'chem_4', 'chem_5', 'chem_6', 'chem_7']

    # ExitThick
    df_ext_thick_G1 = DataFrame(selTelegram_N02['ExitThick'][:, 2])
    df_ext_thick_G2 = DataFrame(selTelegram_N02['ExitThick'][:, 7])
    df_ext_thick_G3 = DataFrame(selTelegram_N02['ExitThick'][:, 12])
    df_ext_thick_G4 = DataFrame(selTelegram_N02['ExitThick'][:, 17])
    df_ext_thick_G5 = DataFrame(selTelegram_N02['ExitThick'][:, 22])
    df_ext_thick = pd.concat(
        [df_ext_thick_G1, df_ext_thick_G2, df_ext_thick_G3, df_ext_thick_G4, df_ext_thick_G5],
        axis=1, sort=False)
    df_ext_thick.columns = ['ExitThick_G1', 'ExitThick_G2', 'ExitThick_G3', 'ExitThick_G4', 'ExitThick_G5']

    # ExitTemp
    df_ext_temp_G1 = DataFrame(selTelegram_N02['ExitTemp'][:, 2])
    df_ext_temp_G2 = DataFrame(selTelegram_N02['ExitTemp'][:, 7])
    df_ext_temp_G3 = DataFrame(selTelegram_N02['ExitTemp'][:, 12])
    df_ext_temp_G4 = DataFrame(selTelegram_N02['ExitTemp'][:, 17])
    df_ext_temp_G5 = DataFrame(selTelegram_N02['ExitTemp'][:, 22])
    df_Exit_Temp = pd.concat(
        [df_ext_temp_G1, df_ext_temp_G2, df_ext_temp_G3, df_ext_temp_G4, df_ext_temp_G5],
        axis=1, sort=False)
    df_Exit_Temp.columns = ['ExitTemp_G1', 'ExitTemp_G2', 'ExitTemp_G3', 'ExitTemp_G4', 'ExitTemp_G5']

    # RollSpeed
    df_RollSpeed_G1 = DataFrame(selTelegram_N02['RollSpeed'][:, 2])  # [:, :5])
    df_RollSpeed_G2 = DataFrame(selTelegram_N02['RollSpeed'][:, 7])  # [:, 5:10])
    df_RollSpeed_G3 = DataFrame(selTelegram_N02['RollSpeed'][:, 12])  # [:, 10:15])
    df_RollSpeed_G4 = DataFrame(selTelegram_N02['RollSpeed'][:, 17])  # [:, 15:20])
    df_RollSpeed_G5 = DataFrame(selTelegram_N02['RollSpeed'][:, 22])  # [:, 20:25])
    df_RollSpeed = pd.concat(
        [df_RollSpeed_G1, df_RollSpeed_G2, df_RollSpeed_G3, df_RollSpeed_G4, df_RollSpeed_G5],
        axis=1, sort=False)
    df_RollSpeed.columns = ['RollSpeed_G1', 'RollSpeed_G2', 'RollSpeed_G3', 'RollSpeed_G4', 'RollSpeed_G5']

    # TensionEntry
    df_TensionEntry_G1 = DataFrame(selTelegram_N02['TensionEntry'][:, 2])  # [:, :5])
    df_TensionEntry_G2 = DataFrame(selTelegram_N02['TensionEntry'][:, 7])  # [:, 5:10])
    df_TensionEntry_G3 = DataFrame(selTelegram_N02['TensionEntry'][:, 12])  # [:, 10:15])
    df_TensionEntry_G4 = DataFrame(selTelegram_N02['TensionEntry'][:, 17])  # [:, 15:20])
    df_TensionEntry_G5 = DataFrame(selTelegram_N02['TensionEntry'][:, 22])  # [:, 20:25])
    df_TensionEntry = pd.concat(
        [df_TensionEntry_G1, df_TensionEntry_G2, df_TensionEntry_G3, df_TensionEntry_G4, df_TensionEntry_G5],
        axis=1, sort=False)
    df_TensionEntry.columns = ['TensionEntry_G1', 'TensionEntry_G2', 'TensionEntry_G3', 'TensionEntry_G4',
                               'TensionEntry_G5']

    # TensionExit
    df_TensionExit_G1 = DataFrame(selTelegram_N02['TensionExit'][:, 2])  # [:, :5])
    df_TensionExit_G2 = DataFrame(selTelegram_N02['TensionExit'][:, 7])  # [:, 5:10])
    df_TensionExit_G3 = DataFrame(selTelegram_N02['TensionExit'][:, 12])  # [:, 10:15])
    df_TensionExit_G4 = DataFrame(selTelegram_N02['TensionExit'][:, 17])  # [:, 15:20])
    df_TensionExit_G5 = DataFrame(selTelegram_N02['TensionExit'][:, 22])  # [:, 20:25])
    df_TensionExit = pd.concat(
        [df_TensionExit_G1, df_TensionExit_G2, df_TensionExit_G3, df_TensionExit_G4, df_TensionExit_G5], axis=1,
        sort=False)
    df_TensionExit.columns = ['TensionExit_G1', 'TensionExit_G2', 'TensionExit_G3', 'TensionExit_G4', 'TensionExit_G5']

    # RollForceOS
    df_RollForceOS_G1 = DataFrame(selTelegram_N02['RollForceOS'][:, 2])  # [:, :5])
    df_RollForceOS_G2 = DataFrame(selTelegram_N02['RollForceOS'][:, 7])  # [:, 5:10])
    df_RollForceOS_G3 = DataFrame(selTelegram_N02['RollForceOS'][:, 12])  # [:, 10:15])
    df_RollForceOS_G4 = DataFrame(selTelegram_N02['RollForceOS'][:, 17])  # [:, 15:20])
    df_RollForceOS_G5 = DataFrame(selTelegram_N02['RollForceOS'][:, 22])  # [:, 20:25])
    df_RollForceOS = pd.concat(
        [df_RollForceOS_G1, df_RollForceOS_G2, df_RollForceOS_G3, df_RollForceOS_G4, df_RollForceOS_G5], axis=1,
        sort=False)
    df_RollForceOS.columns = ['RollForceOS_G1', 'RollForceOS_G2', 'RollForceOS_G3', 'RollForceOS_G4', 'RollForceOS_G5']

    # RollForceDS
    df_RollForceDS_G1 = DataFrame(selTelegram_N02['RollForceDS'][:, 2])  # [:, :5])
    df_RollForceDS_G2 = DataFrame(selTelegram_N02['RollForceDS'][:, 7])  # [:, 5:10])
    df_RollForceDS_G3 = DataFrame(selTelegram_N02['RollForceDS'][:, 12])  # [:, 10:15])
    df_RollForceDS_G4 = DataFrame(selTelegram_N02['RollForceDS'][:, 17])  # [:, 15:20])
    df_RollForceDS_G5 = DataFrame(selTelegram_N02['RollForceDS'][:, 22])  # [:, 20:25])
    df_RollForceDS = pd.concat(
        [df_RollForceDS_G1, df_RollForceDS_G2, df_RollForceDS_G3, df_RollForceDS_G4, df_RollForceDS_G5], axis=1,
        sort=False)
    df_RollForceDS.columns = ['RollForceDS_G1', 'RollForceDS_G2', 'RollForceDS_G3', 'RollForceDS_G4', 'RollForceDS_G5']

    # BendWROS
    df_BendWROS_G1 = DataFrame(selTelegram_N02['BendWROS'][:, 2])  # [:, :5])
    df_BendWROS_G2 = DataFrame(selTelegram_N02['BendWROS'][:, 7])  # [:, 5:10])
    df_BendWROS_G3 = DataFrame(selTelegram_N02['BendWROS'][:, 12])  # [:, 10:15])
    df_BendWROS_G4 = DataFrame(selTelegram_N02['BendWROS'][:, 17])  # [:, 15:20])
    df_BendWROS_G5 = DataFrame(selTelegram_N02['BendWROS'][:, 22])  # [:, 20:25])
    df_BendWROS = pd.concat(
        [df_BendWROS_G1, df_BendWROS_G2, df_BendWROS_G3, df_BendWROS_G4, df_BendWROS_G5], axis=1,
        sort=False)
    df_BendWROS.columns = ['BendWROS_G1', 'BendWROS_G2', 'BendWROS_G3', 'BendWROS_G4', 'BendWROS_G5']
    # BendWRDS
    df_BendWRDS_G1 = DataFrame(selTelegram_N02['BendWRDS'][:, 2])  # [:, :5])
    df_BendWRDS_G2 = DataFrame(selTelegram_N02['BendWRDS'][:, 7])  # [:, 5:10])
    df_BendWRDS_G3 = DataFrame(selTelegram_N02['BendWRDS'][:, 12])  # [:, 10:15])
    df_BendWRDS_G4 = DataFrame(selTelegram_N02['BendWRDS'][:, 17])  # [:, 15:20])
    df_BendWRDS_G5 = DataFrame(selTelegram_N02['BendWRDS'][:, 22])  # [:, 20:25])
    df_BendWRDS = pd.concat(
        [df_BendWRDS_G1, df_BendWRDS_G2, df_BendWRDS_G3, df_BendWRDS_G4, df_BendWRDS_G5], axis=1,
        sort=False)
    df_BendWRDS.columns = ['BendWRDS_G1', 'BendWRDS_G2', 'BendWRDS_G3', 'BendWRDS_G4', 'BendWRDS_G5']
    # BendIROS
    df_BendIROS_G1 = DataFrame(selTelegram_N02['BendIROS'][:, 2])  # [:, :5])
    df_BendIROS_G2 = DataFrame(selTelegram_N02['BendIROS'][:, 7])  # [:, 5:10])
    df_BendIROS_G3 = DataFrame(selTelegram_N02['BendIROS'][:, 12])  # [:, 10:15])
    df_BendIROS_G4 = DataFrame(selTelegram_N02['BendIROS'][:, 17])  # [:, 15:20])
    df_BendIROS_G5 = DataFrame(selTelegram_N02['BendIROS'][:, 22])  # [:, 20:25])
    df_BendIROS = pd.concat(
        [df_BendIROS_G1, df_BendIROS_G2, df_BendIROS_G3, df_BendIROS_G4, df_BendIROS_G5], axis=1,
        sort=False)
    df_BendIROS.columns = ['BendIROS_G1', 'BendIROS_G2', 'BendIROS_G3', 'BendIROS_G4', 'BendIROS_G5']
    # BendIRDS
    df_BendIRDS_G1 = DataFrame(selTelegram_N02['BendIRDS'][:, 2])  # [:, :5])
    df_BendIRDS_G2 = DataFrame(selTelegram_N02['BendIRDS'][:, 7])  # [:, 5:10])
    df_BendIRDS_G3 = DataFrame(selTelegram_N02['BendIRDS'][:, 12])  # [:, 10:15])
    df_BendIRDS_G4 = DataFrame(selTelegram_N02['BendIRDS'][:, 17])  # [:, 15:20])
    df_BendIRDS_G5 = DataFrame(selTelegram_N02['BendIRDS'][:, 22])  # [:, 20:25])
    df_BendIRDS = pd.concat(
        [df_BendIRDS_G1, df_BendIRDS_G2, df_BendIRDS_G3, df_BendIRDS_G4, df_BendIRDS_G5], axis=1,
        sort=False)
    df_BendIRDS.columns = ['BendIRDS_G1', 'BendIRDS_G2', 'BendIRDS_G3', 'BendIRDS_G4', 'BendIRDS_G5']

    # ShiftCVC
    df_ShiftCVC_G1 = DataFrame(selTelegram_N02['ShiftCVC'][:, 2])  # [:, :5])
    df_ShiftCVC_G2 = DataFrame(selTelegram_N02['ShiftCVC'][:, 7])  # [:, 5:10])
    df_ShiftCVC_G3 = DataFrame(selTelegram_N02['ShiftCVC'][:, 12])  # [:, 10:15])
    df_ShiftCVC_G4 = DataFrame(selTelegram_N02['ShiftCVC'][:, 17])  # [:, 15:20])
    df_ShiftCVC_G5 = DataFrame(selTelegram_N02['ShiftCVC'][:, 22])  # [:, 20:25])
    df_ShiftCVC = pd.concat(
        [df_ShiftCVC_G1, df_ShiftCVC_G2, df_ShiftCVC_G3, df_ShiftCVC_G4, df_ShiftCVC_G5], axis=1,
        sort=False)
    df_ShiftCVC.columns = ['ShiftCVC_G1', 'ShiftCVC_G2', 'ShiftCVC_G3', 'ShiftCVC_G4', 'ShiftCVC_G5']
    # SlipForward
    df_SlipForward_G1 = DataFrame(selTelegram_N02['SlipForward'][:, 2])  # [:, :5])
    df_SlipForward_G2 = DataFrame(selTelegram_N02['SlipForward'][:, 7])  # [:, 5:10])
    df_SlipForward_G3 = DataFrame(selTelegram_N02['SlipForward'][:, 12])  # [:, 10:15])
    df_SlipForward_G4 = DataFrame(selTelegram_N02['SlipForward'][:, 17])  # [:, 15:20])
    df_SlipForward_G5 = DataFrame(selTelegram_N02['SlipForward'][:, 22])  # [:, 20:25])
    df_SlipForward = pd.concat(
        [df_SlipForward_G1, df_SlipForward_G2, df_SlipForward_G3, df_SlipForward_G4, df_SlipForward_G5], axis=1,
        sort=False)
    df_SlipForward.columns = ['SlipForward_G1', 'SlipForward_G2', 'SlipForward_G3', 'SlipForward_G4', 'SlipForward_G5']
    # HydPosOS
    df_HydPosOS_G1 = DataFrame(selTelegram_N02['HydPosOS'][:, 2])  # [:, :5])
    df_HydPosOS_G2 = DataFrame(selTelegram_N02['HydPosOS'][:, 7])  # [:, 5:10])
    df_HydPosOS_G3 = DataFrame(selTelegram_N02['HydPosOS'][:, 12])  # [:, 10:15])
    df_HydPosOS_G4 = DataFrame(selTelegram_N02['HydPosOS'][:, 17])  # [:, 15:20])
    df_HydPosOS_G5 = DataFrame(selTelegram_N02['HydPosOS'][:, 22])  # [:, 20:25])
    df_HydPosOS = pd.concat(
        [df_HydPosOS_G1, df_HydPosOS_G2, df_HydPosOS_G3, df_HydPosOS_G4, df_HydPosOS_G5], axis=1,
        sort=False)
    df_HydPosOS.columns = ['HydPosOS_G1', 'HydPosOS_G2', 'HydPosOS_G3', 'HydPosOS_G4', 'HydPosOS_G5']
    # HydPosDS
    df_HydPosDS_G1 = DataFrame(selTelegram_N02['HydPosDS'][:, 2])  # [:, :5])
    df_HydPosDS_G2 = DataFrame(selTelegram_N02['HydPosDS'][:, 7])  # [:, 5:10])
    df_HydPosDS_G3 = DataFrame(selTelegram_N02['HydPosDS'][:, 12])  # [:, 10:15])
    df_HydPosDS_G4 = DataFrame(selTelegram_N02['HydPosDS'][:, 17])  # [:, 15:20])
    df_HydPosDS_G5 = DataFrame(selTelegram_N02['HydPosDS'][:, 22])  # [:, 20:25])
    df_HydPosDS = pd.concat(
        [df_HydPosDS_G1, df_HydPosDS_G2, df_HydPosDS_G3, df_HydPosDS_G4, df_HydPosDS_G5], axis=1,
        sort=False)
    df_HydPosDS.columns = ['HydPosDS_G1', 'HydPosDS_G2', 'HydPosDS_G3', 'HydPosDS_G4', 'HydPosDS_G5']

    #  DriveTorque
    df_DriveTorque_G1 = DataFrame(selTelegram_N02['DriveTorque'][:, 2])  # [:, :5])
    df_DriveTorque_G2 = DataFrame(selTelegram_N02['DriveTorque'][:, 7])  # [:, 5:10])
    df_DriveTorque_G3 = DataFrame(selTelegram_N02['DriveTorque'][:, 12])  # [:, 10:15])
    df_DriveTorque_G4 = DataFrame(selTelegram_N02['DriveTorque'][:, 17])  # [:, 15:20])
    df_DriveTorque_G5 = DataFrame(selTelegram_N02['DriveTorque'][:, 22])  # [:, 20:25])
    df_DriveTorque = pd.concat(
        [df_DriveTorque_G1, df_DriveTorque_G2, df_DriveTorque_G3, df_DriveTorque_G4, df_DriveTorque_G5], axis=1,
        sort=False)
    df_DriveTorque.columns = ['DriveTorque_G1', 'DriveTorque_G2', 'DriveTorque_G3', 'DriveTorque_G4', 'DriveTorque_G5']

    df1 = DataFrame({'Time': timeIndex,
                     'CoilId': selTelegram_N02['CoilId'][:],
                     'CoilIdOut': selTelegram_N02['CoilIdOut'][:],
                     'SeqCoilOut': selTelegram_N02['SeqCoilOut'][:],
                     'SetupNo': selTelegram_N02['SetupNo'][:],
                     'ReturnCode': selTelegram_N02['ReturnCode'][:],
                     'SetupValidCode': selTelegram_N02['SetupValidCode'][:],
                     'NoPasses': selTelegram_N02['NoPasses'][:],
                     'AlloyCode': selTelegram_N02['AlloyCode'][:],
                     'AnalysisFlag': selTelegram_N02['AnalysisFlag'][:],
                     'Width': selTelegram_N02['Width'][:],
                     'LengthStart': selTelegram_N02['LengthStart'][:, ],
                     'Length0': selTelegram_N02['Length0'][:],
                     'Length1_G1': selTelegram_N02['Length1'][:, 0],
                     'Length1_G2': selTelegram_N02['Length1'][:, 1],
                     'Length1_G3': selTelegram_N02['Length1'][:, 2],
                     'Length1_G4': selTelegram_N02['Length1'][:, 3],
                     'Length1_G5': selTelegram_N02['Length1'][:, 3],
                     'EntryThick': selTelegram_N02['EntryThick'][:, 0],
                     'EntryTemp': selTelegram_N02['EntryTemp'][:, 1],
                     'const_force_mode': selTelegram_N02['ConstForceMode'][:],
                     'flag_setup_trans_mode': selTelegram_N02['FlagSetupTransMode'][:],
                     'return_code': selTelegram_N02['ReturnCode'][:],
                     'setup_valid_code': selTelegram_N02['SetupValidCode'][:],
                     'thread_speed_mode': selTelegram_N02['ThreadSpeedMode'][:],
                     'threading_mode': selTelegram_N02['ThreadingMode'][:],
                     'tail_out_mode': selTelegram_N02['TailOutMode'][:],
                     'ThreadAssist': selTelegram_N02['ThreadAssist'][:],
                     'SpoolInd': selTelegram_N02['SpoolInd'][:],
                     'SpoolOuterDiam': selTelegram_N02['SpoolOuterDiam'][:],
                     'SpoolWidth': selTelegram_N02['SpoolWidth'][:],
                     'TargetTransLength': selTelegram_N02['TargetTransLength'][:],
                     'TargetPosWeldSeam': selTelegram_N02['TargetPosWeldSeam'][:],
                     'TargetThickHeadLength': selTelegram_N02['TargetThickHeadLength'][:],
                     'ArtifSleeveUsage': selTelegram_N02['ArtifSleeveUsage'][:],
                     'TensionCurveID': selTelegram_N02['TensionCurveID'][:],
                     'TensionCurveNoPos': selTelegram_N02['TensionCurveNoPos'][:],
                     'yield_strength_calc': selTelegram_N02['YieldStrengthCalc'][:],
                     'StandSwitchOff_G1 ': selTelegram_N02['StandSwitchOff'][:, 0],
                     'StandSwitchOff_G2 ': selTelegram_N02['StandSwitchOff'][:, 1],
                     'StandSwitchOff_G3 ': selTelegram_N02['StandSwitchOff'][:, 2],
                     'StandSwitchOff_G4 ': selTelegram_N02['StandSwitchOff'][:, 3],
                     'StandSwitchOff_G5 ': selTelegram_N02['StandSwitchOff'][:, 4],
                     'TargetCoilTempLimit': selTelegram_N02['TargetCoilTempLimit'][:],
                     'ThermalCrown_G1 ': selTelegram_N02['ThermalCrown'][:, 0],
                     'ThermalCrown_G2 ': selTelegram_N02['ThermalCrown'][:, 1],
                     'ThermalCrown_G3 ': selTelegram_N02['ThermalCrown'][:, 2],
                     'ThermalCrown_G4 ': selTelegram_N02['ThermalCrown'][:, 3],
                     'ThermalCrown_G5 ': selTelegram_N02['ThermalCrown'][:, 4],
                     'FfcCtrlUsage_G1 ': selTelegram_N02['FfcCtrlUsage'][:, 0],
                     'FfcCtrlUsage_G2 ': selTelegram_N02['FfcCtrlUsage'][:, 1],
                     'FfcCtrlUsage_G3 ': selTelegram_N02['FfcCtrlUsage'][:, 2],
                     'FfcCtrlUsage_G4 ': selTelegram_N02['FfcCtrlUsage'][:, 3],
                     'FfcCtrlUsage_G5 ': selTelegram_N02['FfcCtrlUsage'][:, 4],
                     'FbcCtrlUsage_G1 ': selTelegram_N02['FbcCtrlUsage'][:, 0],
                     'FbcCtrlUsage_G2 ': selTelegram_N02['FbcCtrlUsage'][:, 1],
                     'FbcCtrlUsage_G3 ': selTelegram_N02['FbcCtrlUsage'][:, 2],
                     'FbcCtrlUsage_G4 ': selTelegram_N02['FbcCtrlUsage'][:, 3],
                     'FbcCtrlUsage_G5 ': selTelegram_N02['FbcCtrlUsage'][:, 4],
                     'VfcCtrlUsage_G1 ': selTelegram_N02['VfcCtrlUsage'][:, 0],
                     'VfcCtrlUsage_G2 ': selTelegram_N02['VfcCtrlUsage'][:, 1],
                     'VfcCtrlUsage_G3 ': selTelegram_N02['VfcCtrlUsage'][:, 2],
                     'VfcCtrlUsage_G4 ': selTelegram_N02['VfcCtrlUsage'][:, 3],
                     'VfcCtrlUsage_G5 ': selTelegram_N02['VfcCtrlUsage'][:, 4]
                     })

    export_database = pd.concat([df1, df_ext_thick, df_Exit_Temp, df_RollSpeed,
                                 df_TensionEntry, df_TensionExit, df_RollForceOS,
                                 df_RollForceDS, df_BendWROS, df_BendWRDS, df_BendIROS,
                                 df_BendIRDS, df_ShiftCVC, df_SlipForward, df_HydPosOS, df_HydPosDS, df_DriveTorque,
                                 df_chem],
                                axis=1, sort=False)

    datasets = {
        'df_01': export_database.to_json(orient='split', date_format='iso'),
    }
    return json.dumps(datasets)
