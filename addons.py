import dataclasses
import datetime
import json
import pathlib
import secrets
import random
import time

extra_dir = pathlib.Path(__file__).parent / 'extra'

motivational_quotes_path = extra_dir / 'motivational_quotes.json'
programming_jokes_path = extra_dir / 'programming_jokes.json'
physical_challenges_path = extra_dir / 'physical_challenges.json'
call_to_action_path = extra_dir / 'call_to_action.json'


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


@dataclasses.dataclass
class TimeReminder:
    min_sec: int
    max_sec: int
    current: int = 0
    started: float = 0.

    def __post_init__(self):
        self.new()

    def new(self) -> int:
        self.started = time.perf_counter()
        self.current = random.randint(self.min_sec, self.max_sec)
        return self.current

    def is_over(self) -> bool:
        return time.perf_counter()-self.started >= self.current

    @staticmethod
    def get_current_time() -> str:
        now = datetime.datetime.now()
        return now.strftime("Now is %B %d %Y - %H:%M:%S")


def get_random_motivational_quote() -> MotivationalQuote:
    with motivational_quotes_path.open() as json_file:
        quotes = json.load(json_file)
    data = secrets.choice(quotes)
    emoji = secrets.choice(['⚡️', '🔥', '🌟' '💪'])
    return MotivationalQuote(emoji + ' ' + data['text'], data['from'])


def get_random_programming_joke() -> str:
    with programming_jokes_path.open() as json_file:
        jokes = json.load(json_file)
    data = secrets.choice(jokes)
    joke = ProgrammingJoke(data['joke'])
    if joke.is_start_with_question():
        return 'Wait! Do you know ' + joke.text[0].lower() + joke.text[1:] + ' ' + '😂'
    return joke.text + ' 😂'


@dataclasses.dataclass(frozen=True)
class PhysicalChallenge:
    text: str
    call_to_action: list[int]

    def repeat(self):
        for call in self.call_to_action:
            yield f'💪 {call}: {self.text}'


def get_random_physical_challenge() -> PhysicalChallenge:
    with physical_challenges_path.open() as json_file:
        data = json.load(json_file)
    with call_to_action_path.open() as json_file:
        calls = json.load(json_file)
    challenge = PhysicalChallenge(secrets.choice(data),
                                  [secrets.choice(calls) for _ in range(5)])
    return challenge


functions = [
    get_random_motivational_quote,
    get_random_programming_joke,
]
