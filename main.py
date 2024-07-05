import bext
import time

import addons


def main():
    bext.hide_cursor()
    bext.clear()
    while True:
        quote = addons.get_random_motivational_quote()
        render(f'"{quote.quote}" — {quote.author}')


def demo():
    text = "Hello, World! 🌎"
    bext.hide_cursor()
    bext.clear()
    render(text)
    time.sleep(1)
    bext.show_cursor()


def scroll_from_beyond_right_to_beyond_left(text, width):
    text = text.strip() + ' '  # hack
    left_edge_x = width
    right_x = -len(text)

    for i in range(len(text) + width):
        bext.goto(0, 0)

        left_space = ' ' * max(left_edge_x - i, 0)
        right_space = ' ' * max(right_x, 0)
        start_index = max(-left_edge_x + i, 0)

        s = left_space + text[start_index:i] + right_space
        print(s)

        time.sleep(DELAY_SECONDS)


def render(s: str):
    scroll_from_beyond_right_to_beyond_left(s, bext.width())
    # scroll_till_edge(s, bext.width())
    # scroll_beyond_edge(s, bext.width())
    time.sleep(1)


DELAY_SECONDS = 0.1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        bext.show_cursor()
