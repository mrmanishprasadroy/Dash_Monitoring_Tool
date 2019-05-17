import plotly
import redis
from celery import Celery

from setup_data import *
from segmentdata import *

celery_app = Celery("Celery App", broker=os.environ["REDIS_URL"])
redis_instance = redis.StrictRedis.from_url(os.environ["REDIS_URL"])

REDIS_HASH_NAME = os.environ.get("DASH_APP_NAME", "app-data")
REDIS_KEYS = {"DATASETUP": "DATASETUP",
              "SETUP_DATE_UPDATED": "SETUP_DATE_UPDATED",
              "DATASEGMENT": "DATASEGMENT",
              "SEGMENT_DATE_UPDATED": "SEGMENT_DATE_UPDATED"
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
        30,  # seconds
        # an alternative to the @app.task decorator:
        # wrap the function in the app.task function
        update_segment_data.s(),
        name="Update segment data",
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
