import enum

import bext
import time


def main():
    demo()


class Direction(enum.Enum):
    Left = -1
    Right = 1


def demo():
    text = "Hello, World! 🌎"
    width = bext.width()
    bext.hide_cursor()
    bext.clear()
    scroll_till_edge(text, width, direction=Direction.Right)
    scroll_beyond_edge(text, width, direction=Direction.Right)
    time.sleep(1)
    bext.show_cursor()


def scroll_till_edge(text, width, *, direction=Direction.Left):
    # Animate the text
    for i in range(width - len(text)):
        bext.goto(0, 0)
        # print(' ' * (width - i) + text[:i])
        if direction == Direction.Left:
            print(text.rjust(width-i, ' '))
        else:
            print(text.rjust(len(text)+i, ' '))

        # ensure next line is clear
        bext.goto(0, 1)
        print(' '*width)

        time.sleep(DELAY_SECONDS)


def scroll_beyond_edge(text, width, *, direction=Direction.Right):
    for i in range(1, len(text) + 1):
        bext.goto(0, 0)
        if direction == Direction.Left:
            print(text[i:].ljust(width, ' '))
        else:
            print(text[:-i].rjust(width, ' '))
        time.sleep(DELAY_SECONDS)


if __name__ == '__main__':
    DELAY_SECONDS = 0.1
    main()
