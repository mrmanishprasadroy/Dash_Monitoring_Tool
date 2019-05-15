import plotly
import redis
from celery import Celery

from setup_data import *

celery_app = Celery("Celery App", broker=os.environ["REDIS_URL"])
redis_instance = redis.StrictRedis.from_url(os.environ["REDIS_URL"])

REDIS_HASH_NAME = os.environ.get("DASH_APP_NAME", "app-data")
REDIS_KEYS = {"DATASETUP": "DATASETUP", "DATE_UPDATED": "DATE_UPDATED"}


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    print("----> setup_periodic_tasks")
    sender.add_periodic_task(
        50,  # seconds
        # an alternative to the @app.task decorator:
        # wrap the function in the app.task function
        update_setup_data.s(),
        name="Update setup data",
    )


@celery_app.task
def update_setup_data():
    print("----> update_data")
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
        REDIS_HASH_NAME, REDIS_KEYS["DATE_UPDATED"], str(datetime.datetime.now())
    )
