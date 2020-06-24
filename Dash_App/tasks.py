import plotly
import pymongo
import redis
from celery import Celery

from setup_data import *
from segmentdata import *
from measurment_data import *
from srtip_tracking_data import *
from coiler_exit_data import *
from coil_id_tracking_data import *
from pymongo import MongoClient

celery_app = Celery("Celery App", broker=os.environ["REDIS_URL"])
redis_instance = redis.StrictRedis.from_url(os.environ["REDIS_URL"])
# mongodb_uri = "mongodb://root:secret@127.0.0.1:27017"
# client = MongoClient(mongodb_uri)
# db = client["TCM_TLG"]

REDIS_HASH_NAME = os.environ.get("DASH_APP_NAME", "app-data")
REDIS_KEYS = {"DATASETUP": "DATASETUP",
              "SETUP_DATE_UPDATED": "SETUP_DATE_UPDATED",
              "DATASEGMENT": "DATASEGMENT",
              "SEGMENT_DATE_UPDATED": "SEGMENT_DATE_UPDATED",
              "MESDATA": "MESDATA",
              "MESDATA_DATE_UPDATED": "MESDATA_DATE_UPDATED",
              "STRIPDATA": "STRIPDATA",
              "STRIPDATA_DATE_UPDATED": "STRIPDATA_DATE_UPDATED",
              "COILERDATA": "COILERDATA",
              "COILERDATA_DATE_UPDATED": "COILERDATA_DATE_UPDATED",
              "COILDATA": "COILDATA",
              "COILDATA_DATE_UPDATED": "COILDATA_DATE_UPDATED"
              }


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    print("----> setup_periodic_tasks")
    sender.add_periodic_task(
        60,  # seconds
        # an alternative to the @app.task decorator:
        # wrap the function in the app.task function
        update_setup_data.s(),
        name="Update setup data",
    )
    sender.add_periodic_task(
        50,  # seconds
        # an alternative to the @app.task decorator:
        # wrap the function in the app.task function
        update_segment_data.s(),
        name="Update segment data",
    )
    sender.add_periodic_task(
        20,  # seconds
        # an alternative to the @app.task decorator:
        # wrap the function in the app.task function
        update_measurment_data.s(),
        name="Update measurment data",
    )
    sender.add_periodic_task(
        10,  # seconds
        # an alternative to the @app.task decorator:
        # wrap the function in the app.task function
        update_strip_data.s(),
        name="Update strip data",
    )
    sender.add_periodic_task(
        40,  # seconds
        # an alternative to the @app.task decorator:
        # wrap the function in the app.task function
        update_coiler_data.s(),
        name="Update coiler data",
    )
    sender.add_periodic_task(
        30,  # seconds
        # an alternative to the @app.task decorator:
        # wrap the function in the app.task function
        update_coil_data.s(),
        name="Update coil data",
    )
    # sender.add_periodic_task(
    #     900, # 15 Minutes
    #     # an alternative to the @app.task decorator:
    #     # wrap the function in the app.task function
    #     #insert_mongos_db.s(),
    #     name="Update coil data",

    #)
# @celery_app.task
# def insert_mongos_db():
#     # Setup Data
#     print("----> Start Inserting SetupData to Database")
#     SetupData = db["SetupData"]
#     df_setup = setup_data()
#     data = json.loads(df_setup)
#     col = pd.read_json(data['df_01'], orient='split')
#    # data = [{"id": id(datetime), "Data":col}]
#     resp = SetupData.create_index([ ("Time", -1) ], unique=True)
#     print("index response:", resp)
#     try:
#         x = SetupData.insert_many(col.to_dict('records'))
#         print("  %d  No of Setup Id Inserted in to Database"%len(x.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("SetupData caught exceptions for %d" %len(panic))
#
#     print("----> End Inserting SetupData to Database")
#     # Segment Data
#     print("----> Start Inserting Segment Data to Database")
#     SegmentDataMP_00 = db["SegmentData_MP00"]
#     SegmentDataMP_01 = db["SegmentData_MP01"]
#     SegmentDataMP_02 = db["SegmentData_MP02"]
#     SegmentDataMP_03 = db["SegmentData_MP03"]
#     SegmentDataMP_04 = db["SegmentData_MP04"]
#     SegmentDataMP_05 = db["SegmentData_MP05"]
#     SegmentDataMP_06 = db["SegmentData_MP06"]
#     SegmentDataMP_07 = db["SegmentData_MP07"]
#     SegmentDataMP_08 = db["SegmentData_MP08"]
#     SegmentDataMP_09 = db["SegmentData_MP09"]
#     SegmentDataMP_10 = db["SegmentData_MP10"]
#
#     df_segment = read_segment_data_monitor()
#     data = json.loads(df_segment)
#     MP_00 = pd.read_json(data['df_00'], orient='split')
#     MP_01 = pd.read_json(data['df_01'], orient='split')
#     MP_02 = pd.read_json(data['df_02'], orient='split')
#     MP_03 = pd.read_json(data['df_03'], orient='split')
#     MP_04 = pd.read_json(data['df_04'], orient='split')
#     MP_05 = pd.read_json(data['df_05'], orient='split')
#     MP_06 = pd.read_json(data['df_06'], orient='split')
#     MP_07 = pd.read_json(data['df_07'], orient='split')
#     MP_08 = pd.read_json(data['df_08'], orient='split')
#     MP_09 = pd.read_json(data['df_09'], orient='split')
#     MP_10 = pd.read_json(data['df_10'], orient='split')
#     # data = [{"id": id(datetime), "Data":col}]
#     resp_0 = SegmentDataMP_00.create_index([("time", -1)], unique=True)
#     resp_1 = SegmentDataMP_01.create_index([("time", -1)], unique=True)
#     resp_2 = SegmentDataMP_02.create_index([("time", -1)], unique=True)
#     resp_3 = SegmentDataMP_03.create_index([("time", -1)], unique=True)
#     resp_4 = SegmentDataMP_04.create_index([("time", -1)], unique=True)
#     resp_5 = SegmentDataMP_05.create_index([("time", -1)], unique=True)
#     resp_6 = SegmentDataMP_06.create_index([("time", -1)], unique=True)
#     resp_7 = SegmentDataMP_07.create_index([("time", -1)], unique=True)
#     resp_8 = SegmentDataMP_08.create_index([("time", -1)], unique=True)
#     resp_9 = SegmentDataMP_09.create_index([("time", -1)], unique=True)
#     resp_10 = SegmentDataMP_10.create_index([("time", -1)], unique=True)
#     print("index response:", resp_0)
#     try:
#         x0 = SegmentDataMP_00.insert_many(MP_00.to_dict('records'))
#         print("  %d  No of SegmentDataMP_00 Id Inserted in to Database" % len(x0.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("SegmentDataMP_00 caught exceptions")
#     try:
#         x1 = SegmentDataMP_01.insert_many(MP_01.to_dict('records'))
#         print("  %d  No ofSegmentDataMP_01 Id Inserted in to Database" % len(x1.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("SegmentDataMP_01 caught exceptions")
#     try:
#         x2 = SegmentDataMP_02.insert_many(MP_02.to_dict('records'))
#         print("  %d  No of SegmentDataMP_02 Id Inserted in to Database" % len(x2.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("SegmentDataMP_02 caught exceptions")
#     try:
#         x3 = SegmentDataMP_03.insert_many(MP_03.to_dict('records'))
#         print("  %d  No of SegmentDataMP_03 Id Inserted in to Database" % len(x3.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("SegmentDataMP_03 caught exceptions")
#     try:
#         x4 = SegmentDataMP_04.insert_many(MP_04.to_dict('records'))
#         print("  %d  No of SegmentDataMP_04 Id Inserted in to Database" % len(x4.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("SegmentDataMP_04 caught exceptions")
#     try:
#         x5 = SegmentDataMP_05.insert_many(MP_05.to_dict('records'))
#         print("  %d  No of SegmentDataMP_05 Id Inserted in to Database" % len(x5.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("SegmentDataMP_05 caught exceptions")
#     try:
#         x6 = SegmentDataMP_06.insert_many(MP_06.to_dict('records'))
#         print("  %d  No of SegmentDataMP_06 Id Inserted in to Database" % len(x6.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("SegmentDataMP_06 caught exceptions")
#     try:
#         x7 = SegmentDataMP_07.insert_many(MP_07.to_dict('records'))
#         print("  %d  No of SegmentDataMP_07 Id Inserted in to Database" % len(x7.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("SegmentDataMP_07 caught exceptions")
#     try:
#         x8 = SegmentDataMP_08.insert_many(MP_08.to_dict('records'))
#         print("  %d  No of SegmentDataMP_08 Inserted in to Database" % len(x8.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = filter(lambda x: x['code'] != 11000, e.details['writeErrors'])
#     try:
#         x9 = SegmentDataMP_09.insert_many(MP_09.to_dict('records'))
#         print("  %d  No of SegmentDataMP_09 Id Inserted in to Database" % len(x9.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("SegmentDataMP_09 caught exceptions")
#     try:
#         x10= SegmentDataMP_10.insert_many(MP_10.to_dict('records'))
#         print("  %d  No of SegmentDataMP_10 Inserted in to Database" % len(x10.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("SegmentDataMP_10 caught exceptions")
#     print("----> End Inserting SegmentData to Database")
#
#     #Measurment Data
#     print("----> Start Inserting Measurment to Database")
#     MeasData = db["MeasData"]
#     df_mesdata = read_measurment_data()
#     data = json.loads(df_mesdata)
#     col = pd.read_json(data['df_01'], orient='split')
#     # data = [{"id": id(datetime), "Data":col}]
#     resp = MeasData.create_index([("timeIndex", -1)], unique=True)
#     print("index response:", resp)
#     try:
#         x = MeasData.insert_many(col.to_dict('records'))
#         print("  %d  No of MeasData Id Inserted in to Database" % len(x.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("Measurment Data caught exceptions")
#     print("----> End Inserting Measurment to Database")
#
#     # Coiler Data
#     print("----> Start Inserting CoilerData to Database")
#     CoilerData = db["CoilerData"]
#     df_coilerdata = read_coiler_data()
#     data = json.loads(df_coilerdata)
#     col = pd.read_json(data['df_01'], orient='split')
#     # data = [{"id": id(datetime), "Data":col}]
#     resp = CoilerData.create_index([("timeIndex", -1)], unique=True)
#     print("index response:", resp)
#     try:
#         x = CoilerData.insert_many(col.to_dict('records'))
#         print("  %d  No of CoilerData Id Inserted in to Database" % len(x.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("CoilerData Data caught exceptions")
#     print("----> End Inserting CoilerData to Database")
#
#     # StripTracking Data
#     print("----> Start Inserting StripTrackingData to Database")
#     CoilTrackingData = db["StripTracking_coils"]
#     StandTrackingData = db["StripTracking_Stand"]
#     df_stripTrackingdata = read_strip_tracking_data()
#     data = json.loads(df_stripTrackingdata)
#     col1 = pd.read_json(data['df_02'], orient='split')
#     col2 = pd.read_json(data['df_01'], orient='split')
#     # data = [{"id": id(datetime), "Data":col}]
#     resp1 = CoilTrackingData.create_index([("timeIndex", -1)], unique=True)
#     resp2 = StandTrackingData.create_index([("timeIndex", -1)], unique=True)
#     print("index response:", resp)
#     try:
#         x1 = CoilTrackingData.insert_many(col1.to_dict('records'))
#         print("  %d  No of CoilTrackingData Id Inserted in to Database" % len(x1.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("StripTrackingCoil Data caught exceptions")
#     try:
#         x2 = StandTrackingData.insert_many(col2.to_dict('records'))
#         print("  %d  No of StandTrackingData Id Inserted in to Database" % len(x2.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("StripTrackingStand Data caught exceptions")
#     print("----> End Inserting StripTrackingData to Database")
#
#     # Coile Data
#     print("----> Start Inserting CoilData to Database")
#     CoilData = db["CoilData"]
#     df_coildata = read_coilid_data()
#     data = json.loads(df_coildata)
#     col = pd.read_json(data['df_01'], orient='split')
#     # data = [{"id": id(datetime), "Data":col}]
#     resp = CoilData.create_index([("timeIndex", -1)], unique=True)
#     print("index response:", resp)
#     try:
#         x = CoilData.insert_many(col.to_dict('records'))
#         print("  %d  No of CoilData Id Inserted in to Database" % len(x.inserted_ids))
#     except pymongo.errors.BulkWriteError as e:
#         panic = [filter(lambda x: x['code'] != 11000, e.details['writeErrors'])]
#         if len(panic) > 0:
#             print("CoilData Data caught exceptions")
#     print("----> End Inserting CoilData to Database")



@celery_app.task
def update_setup_data():
    print("----> update_setup_data")
    # Create a dataframe with sample data
    # In practice, this function might be making calls to databases,
    # performing computations, etc
    setups = setup_data()

    # Save the dataframe in redis so that the Dash app, running on a separate
    # process, can read it
    redis_instance.hset(
        REDIS_HASH_NAME,
        REDIS_KEYS["DATASETUP"],
        json.dumps(
            setups,
            # This JSON Encoder will handle things like numpy arrays
            # and datetimes
            cls=plotly.utils.PlotlyJSONEncoder,
        ),
    )
    # Save the timestamp that the dataframe was updated
    redis_instance.hset(
        REDIS_HASH_NAME, REDIS_KEYS["SETUP_DATE_UPDATED"], str(datetime.datetime.now())
    )


@celery_app.task
def update_segment_data():
    print("----> update_segment_data")
    # Create a dataframe with sample data
    # In practice, this function might be making calls to databases,
    # performing computations, etc
    segmentdata = read_segment_data_monitor()

    # Save the dataframe in redis so that the Dash app, running on a separate
    # process, can read it
    redis_instance.hset(
        REDIS_HASH_NAME,
        REDIS_KEYS["DATASEGMENT"],
        json.dumps(
            segmentdata,
            # This JSON Encoder will handle things like numpy arrays
            # and datetimes
            cls=plotly.utils.PlotlyJSONEncoder,
        ),
    )
    # Save the timestamp that the dataframe was updated
    redis_instance.hset(
        REDIS_HASH_NAME, REDIS_KEYS["SEGMENT_DATE_UPDATED"], str(datetime.datetime.now())
    )


@celery_app.task
def update_measurment_data():
    print("----> update_measurment_data")
    # Create a dataframe with sample data
    # In practice, this function might be making calls to databases,
    # performing computations, etc
    measurment_data = read_measurment_data()

    # Save the dataframe in redis so that the Dash app, running on a separate
    # process, can read it
    redis_instance.hset(
        REDIS_HASH_NAME,
        REDIS_KEYS["MESDATA"],
        json.dumps(
            measurment_data,
            # This JSON Encoder will handle things like numpy arrays
            # and datetimes
            cls=plotly.utils.PlotlyJSONEncoder,
        ),
    )
    # Save the timestamp that the dataframe was updated
    redis_instance.hset(
        REDIS_HASH_NAME, REDIS_KEYS["MESDATA_DATE_UPDATED"], str(datetime.datetime.now())
    )


@celery_app.task
def update_strip_data():
    print("----> update_strip_data")
    # Create a dataframe with sample data
    # In practice, this function might be making calls to databases,
    # performing computations, etc
    strip_data = read_strip_tracking_data()

    # Save the dataframe in redis so that the Dash app, running on a separate
    # process, can read it
    redis_instance.hset(
        REDIS_HASH_NAME,
        REDIS_KEYS["STRIPDATA"],
        json.dumps(
            strip_data,
            # This JSON Encoder will handle things like numpy arrays
            # and datetimes
            cls=plotly.utils.PlotlyJSONEncoder,
        ),
    )
    # Save the timestamp that the dataframe was updated
    redis_instance.hset(
        REDIS_HASH_NAME, REDIS_KEYS["STRIPDATA_DATE_UPDATED"], str(datetime.datetime.now())
    )


@celery_app.task
def update_coiler_data():
    print("----> update_coiler_data")
    # Create a dataframe with sample data
    # In practice, this function might be making calls to databases,
    # performing computations, etc
    coiler_data = read_coiler_data()
    # Save the dataframe in redis so that the Dash app, running on a separate
    # process, can read it
    redis_instance.hset(
        REDIS_HASH_NAME,
        REDIS_KEYS["COILERDATA"],
        json.dumps(
            coiler_data,
            # This JSON Encoder will handle things like numpy arrays
            # and datetimes
            cls=plotly.utils.PlotlyJSONEncoder,
        ),
    )
    # Save the timestamp that the dataframe was updated
    redis_instance.hset(
        REDIS_HASH_NAME, REDIS_KEYS["COILERDATA_DATE_UPDATED"], str(datetime.datetime.now())
    )


@celery_app.task
def update_coil_data():
    print("----> update_coil_data")
    # Create a dataframe with sample data
    # In practice, this function might be making calls to databases,
    # performing computations, etc
    coil_data = read_coilid_data()
    # Save the dataframe in redis so that the Dash app, running on a separate
    # process, can read it
    redis_instance.hset(
        REDIS_HASH_NAME,
        REDIS_KEYS["COILDATA"],
        json.dumps(
            coil_data,
            # This JSON Encoder will handle things like numpy arrays
            # and datetimes
            cls=plotly.utils.PlotlyJSONEncoder,
        ),
    )
    # Save the timestamp that the dataframe was updated
    redis_instance.hset(
        REDIS_HASH_NAME, REDIS_KEYS["COILDATA_DATE_UPDATED"], str(datetime.datetime.now())
    )