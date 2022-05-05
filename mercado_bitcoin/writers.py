import datetime
import json
import os
from typing import List


class DataTypeNotSupportforIngestionException(Exception):

    def __init__(self, data):
        self.data = data
        self.message = f"Data type {type(data)} is not supported for ingestion"
        super().__init__(self.message)


class DataWriter():

    def __init__(self, coin: str, api: str) -> None:
        self.coin = coin
        self.api = api
        self.datatime_now = datetime.datetime.now().strftime('%Y%m%d-%H-%M-%S')
        self.filename = f"{self.api}/{self.coin}/{self.datatime_now}.json"

    def _write_row(self, row: str) -> None:
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, "a") as f:
            f.write(row)

    def write(self, data: [List, dict]):
        if isinstance(data, dict):
            self._write_row(json.dumps(data) + "\n")
        elif isinstance(data, List):
            for element in data:
                self.write(element)
        else:
            raise DataTypeNotSupportforIngestionException(data)