import curses
import random
import time


def matrix(stdscr):
    """Render a Matrix-style rain effect with bounds checking."""
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.nodelay(True)

    height, width = stdscr.getmaxyx()
    columns = [0] * width

    while True:
        stdscr.erase()
        height, width = stdscr.getmaxyx()
        if len(columns) < width:
            columns.extend([0] * (width - len(columns)))
        elif len(columns) > width:
            columns = columns[:width]

        for i, y in enumerate(columns):
            char = chr(random.randint(33, 126))
            if 0 <= y < height and 0 <= i < width:
                try:
                    stdscr.addstr(y, i, char, curses.color_pair(1))
                except curses.error:
                    pass
            columns[i] = y + 1 if y + 1 < height else 0

        stdscr.refresh()
        time.sleep(0.05)


if __name__ == "__main__":
    curses.wrapper(matrix)
