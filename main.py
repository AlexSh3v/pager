import random
import types
import typing

import bext
import time

import addons


def main():
    bext.hide_cursor()
    bext.clear()
    time_reminder = addons.TimeReminder(*TIME_REMINDER_RANGE_SECONDS)
    while True:

        if time_reminder.is_over():
            render(time_reminder.get_current_time)
            time_reminder.new()
            continue

        picked_function = random.choice(addons.functions)
        if picked_function == addons.get_random_motivational_quote:
            quote = picked_function()
            render(f'"{quote.quote}" — {quote.author}')
        elif picked_function == addons.get_random_programming_joke:
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


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        bext.show_cursor()
