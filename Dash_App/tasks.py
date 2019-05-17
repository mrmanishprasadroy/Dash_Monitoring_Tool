import plotly
import redis
from celery import Celery

from setup_data import *
from segmentdata import *
from measurment_data import *
from srtip_tracking_data import *
from coiler_exit_data import *
from coil_id_tracking_data import *

celery_app = Celery("Celery App", broker=os.environ["REDIS_URL"])
redis_instance = redis.StrictRedis.from_url(os.environ["REDIS_URL"])

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