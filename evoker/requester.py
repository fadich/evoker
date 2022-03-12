from time import time
from typing import Optional

import aiohttp
import asyncio


class Requester:

    def __init__(
        self,
        url: str,
        concurrency: int = 1000,
        detailed: bool = False,
        loop: Optional[asyncio.BaseEventLoop] = None
    ):
        self.url = url
        self.concurrency = concurrency
        self.detailed = detailed

        if loop is None:
            loop = asyncio.get_event_loop()

        self.loop = loop

    def make_get(self):
        tasks = []
        for _ in range(self.concurrency):
            tasks.append(
                self.loop.create_task(
                    self._make_get()
                )
            )

        wait_tasks = asyncio.wait(tasks)
        results = self.loop.run_until_complete(wait_tasks)

        res = {
            "succeed": [res.result() for res in results[0]],
            "failed": [res.result() for res in results[1]],
        }

        if not self.detailed:
            res["succeed"] = len(res["succeed"])
            res["failed"] = len(res["failed"])

        return res

    async def _make_get(self):
        started = time()

        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                exec_time = time() - started

                result = {
                    "time": exec_time,
                    "status": response.status,
                }

                if self.detailed:
                    html = await response.text()
                    result["html"] = html

                return result
