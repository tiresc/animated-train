import curses
import random
import time


def matrix(stdscr):
    """Render cascading green text reminiscent of the Matrix."""
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.nodelay(True)

    height, width = stdscr.getmaxyx()
    columns = [None] * width  # Track active streams per column

    while True:
        stdscr.erase()
        height, width = stdscr.getmaxyx()
        if len(columns) < width:
            columns.extend([None] * (width - len(columns)))
        elif len(columns) > width:
            columns = columns[:width]

        for i, stream in enumerate(columns):
            if stream is None:
                # Randomly start a new stream
                if random.random() < 0.02:
                    length = random.randint(3, height // 2 or 1)
                    columns[i] = {"y": 0, "length": length}
            else:
                y, length = stream["y"], stream["length"]
                for offset in range(length):
                    char_y = y - offset
                    if 0 <= char_y < height:
                        try:
                            stdscr.addstr(
                                char_y, i, chr(random.randint(33, 126)), curses.color_pair(1)
                            )
                        except curses.error:
                            pass
                stream["y"] += 1
                if stream["y"] - length > height:
                    columns[i] = None

        stdscr.refresh()
        time.sleep(0.05)


if __name__ == "__main__":
    curses.wrapper(matrix)
