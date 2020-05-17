import pathlib
import requests

from typing import Iterator


class Tabletopia_data:
    domain_name = "http://tabletopia.com/games"

    def _get_game_pages(self) -> Iterator[requests.Request]:
        STATUS_OK = 200
        payload = {"page": 1}
        while True:
            page = requests.get(self.domain_name, params=payload)
            if r.status_code == STATUS_OK:
                payload["page"] += 1
                yield page
            else:
                break
