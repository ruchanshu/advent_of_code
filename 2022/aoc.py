import requests

from datetime import date
from functools import cached_property

from constants import URL


class AoCData:
    def __init__(self):
        self._session = None

    def _read_session(self):
        with open(".session", "r") as file:
            for line in file.readlines():
                key, value = line.split("=")
                if key == "AOC_SESSION":
                    self._session = value
                    return
                raise RuntimeError("AOC_SESSION not found in .session file")

    @cached_property
    def __cookies(self):
        if self._session is None:
            self._read_session()

        return {"session": self._session}

    @cached_property
    def input_url(self):
        today = date.today()
        return f"{URL}{today.year}/day/{today.day}/input"

    def get_input(self):
        response = requests.get(self.input_url, cookies=self.__cookies)
        if response.ok:
            return response.text.strip()
        response.raise_for_status()

    def get_input_lines(self):
        data = self.get_input()
        return data.split("\n")
