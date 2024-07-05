import dataclasses
import json
import pathlib
import random

extra_dir = pathlib.Path(__file__).parent / 'extra'

motivational_quotes_path = extra_dir / 'motivational_quotes.json'
programming_jokes_path = extra_dir / 'programming_jokes.json'


@dataclasses.dataclass(frozen=True)
class MotivationalQuote:
    quote: str
    author: str


@dataclasses.dataclass(frozen=True)
class ProgrammingJoke:
    text: str

    def is_start_with_question(self) -> bool:
        dot_index = self.text.find('.')
        question_index = self.text.find('?')
        return (question_index < dot_index) or (question_index > 0 and dot_index == -1)


def get_random_motivational_quote() -> MotivationalQuote:
    with motivational_quotes_path.open() as json_file:
        quotes = json.load(json_file)
    data = random.choice(quotes)
    return MotivationalQuote(data['text'], data['from'])


def get_random_programming_joke() -> str:
    with programming_jokes_path.open() as json_file:
        jokes = json.load(json_file)
    data = random.choice(jokes)
    joke = ProgrammingJoke(data['joke'])
    if joke.is_start_with_question():
        return 'Wait! Do you know ' + joke.text[0].lower() + joke.text[1:]
    return joke.text


functions = [
    get_random_motivational_quote,
    get_random_programming_joke,
]
