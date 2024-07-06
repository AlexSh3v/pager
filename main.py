import random
import secrets
import typing

import bext
import time

import addons


def make_a_choice(options: list[str], *, inform_message: str = "", delay_seconds: int = 0):
    bext.clear()
    items = options.copy()
    start_y = bext.height()//2-len(items)//2
    index = 0
    event = None

    bext.goto(0, start_y - 1)
    print(inform_message.center(bext.width()))

    is_awaited = (delay_seconds == 0)

    while event != '\n':
        bext.clear()

        for i in range(len(items)):
            bext.goto(0, start_y+i)
            cursor = '> ' if (i == index) and not is_awaited else ''
            s = cursor + items[i]
            print(s.center(bext.width()))

        if not is_awaited:
            time.sleep(delay_seconds)
            is_awaited = True
            continue

        event = bext.get_key()

        if event == 'down':
            index = (index + 1) % len(items)
        elif event == 'up':
            index = index - 1
            if index < 0:
                index = len(items)-1


def main():
    bext.hide_cursor()
    bext.clear()
    time_reminder = addons.TimeReminder(*TIME_REMINDER_RANGE_SECONDS)
    converted = (it*60 for it in PHYSICAL_REMINDER_RANGE_MINUTES)
    physical_activity = addons.TimeReminder(*converted)
    while True:

        if time_reminder.is_over():
            render(time_reminder.get_current_time)
            time_reminder.new()

        if physical_activity.is_over():
            challenge = addons.get_random_physical_challenge()
            for s in challenge.repeat():
                render(s)
            physical_activity.new()

        picked_function = random.choice(addons.functions)
        chance_10_percent = secrets.randbelow(10) == 0
        if picked_function == addons.get_random_motivational_quote:
            quote = picked_function()
            render(f'"{quote.quote}" — {quote.author}')
        elif picked_function == addons.get_random_programming_joke:
            render(picked_function())
        elif picked_function == addons.get_exchange_rate and chance_10_percent:
            render(picked_function())


def demo():
    text = "Hello, World! 🌎"
    bext.hide_cursor()
    bext.clear()
    render(text)
    time.sleep(1)
    bext.show_cursor()


def scroll_from_beyond_right_to_beyond_left(text: str | typing.Callable[[], str], width: int):

    def get_text():
        t = text
        if isinstance(text, typing.Callable):
            t = text()
        return t.strip() + ' '  # hack

    left_edge_x = width
    right_x = -len(get_text())
    height = bext.height() // 2

    for i in range(len(get_text()) + width):
        bext.clear()
        bext.goto(0, height)

        left_space = ' ' * max(left_edge_x - i, 0)
        right_space = ' ' * max(right_x, 0)
        start_index = max(-left_edge_x + i, 0)

        s = left_space + get_text()[start_index:i] + right_space
        print(s)

        bext.goto(0, height+1)
        print(' ' * width)

        time.sleep(DELAY_SECONDS)


def render(s: str | typing.Callable[[], str]):
    scroll_from_beyond_right_to_beyond_left(s, bext.width())
    # scroll_till_edge(s, bext.width())
    # scroll_beyond_edge(s, bext.width())
    time.sleep(1)


DELAY_SECONDS = 0.1
TIME_REMINDER_RANGE_SECONDS = (60, 80)
PHYSICAL_REMINDER_RANGE_MINUTES = (5, 7)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        bext.show_cursor()
