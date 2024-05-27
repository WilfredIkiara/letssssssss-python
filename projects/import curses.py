import curses
from curses import wrapper
import random
import time

def start_screen(stdscr):
    stdscr.clear()
    # Capitalize the first letter of each sentence for consistency
    stdscr.addstr("Welcome to the speed typing test!", curses.color_pair(1))
    stdscr.addstr("\nPress any key to begin.", curses.color_pair(1))
    stdscr.addstr("\nTo quit the game, press Escape.", curses.color_pair(2))
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target_text, current_text, wpm=0):
    stdscr.addstr(target_text)
    # Adjust the position to avoid overwriting the target text
    stdscr.addstr(len(target_text) + 10, 0, f"WPM: {wpm}")

    for i, char in enumerate(current_text):
        correct_char = target_text[i]
        color = curses.color_pair(3)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

def wpm_test(stdscr):
    target_text = "The Future of Space Exploration Space exploration continues to captivate the imagination and drive technological innovation. With the advent of private spaceflight companies and international collaborations, the next decades promise to expand our understanding of the cosmos and our place within it, potentially leading to manned missions to Mars and beyond."
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(''.join(current_text)) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if ''.join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ('KEY_BACKSPACE', '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)

        stdscr.addstr(2, 0, "You completed the text! Press any key to continue or ESC to quit.")
        key = stdscr.getkey()

        if ord(key) == 27:
            break

wrapper(main)
