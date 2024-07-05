import dataclasses
import json
import pathlib
import random

extra_dir = pathlib.Path(__file__).parent / 'extra'

motivational_quotes_path = extra_dir / 'motivational_quotes.json'


@dataclasses.dataclass(frozen=True)
class MotivationalQuote:
    quote: str
    author: str


def get_random_motivational_quote() -> MotivationalQuote:
    with motivational_quotes_path.open() as json_file:
        quotes = json.load(json_file)
    data = random.choice(quotes)
    return MotivationalQuote(data['text'], data['from'])
