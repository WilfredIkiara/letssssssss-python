import curses
from curses import wrapper
import random
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed typing test!",curses.color_pair(1))
    stdscr.addstr("\nPress any key to begin",curses.color_pair(1))
    stdscr.addstr("\nTo quit the game press escape", curses.color_pair(2))
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm = 0):
    stdscr.addstr(target)
    stdscr.addstr(5, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
            correct_char = target[i]
            color = curses.color_pair(3)
            if char != correct_char:
                color = curses.color_pair(2)
                
            stdscr.addstr(0, i, char,color)
    
def load_text():
     with open("text_speed.txt", "r") as f:
          lines = f.readlines()  
          return random.choice(lines).strip()  #.strip removes the whitespace characters the  newline character for the file to know its a new line

def wpm_test(stdscr):
    target_text = "club along if you feel like thats what you wanna do, because im happy ....clap along if you feel like hapiness is the truth"
    current_text=[]
    wpm = 0 
    #random.shuffle(text)
    #target_text = text[0]

    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text)/(time_elapsed/60))/5)

        stdscr.clear() 
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
             continue

        if len(key) == 1 and ord(key) == 27: 
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
                current_text.append(key)

        
def main(stdscr):
    #standard output screen
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)

        stdscr.addstr(5, 0, "You completed the text, press any key to cointinue... ")
        key = stdscr.getkey()

        if ord(key) == 27:
             break 

wrapper(main) 

