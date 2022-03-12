from celery import Celery

from evoker.config import CELERY_BROKER_URL
from evoker.requester import Requester

app = Celery('hello', broker=CELERY_BROKER_URL)


@app.task
def make_request(url: str, concurrency: int = 1000, detailed: bool = False):
    requester = Requester(
        url=url,
        concurrency=concurrency,
        detailed=detailed
    )

    return requester.make_get()
