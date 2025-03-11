import curses
from curses import wrapper
import time
import random

def start(stdscr):
    stdscr.clear()
    while True:
        stdscr.addstr("Enter a difficulty level. 1 for easy, 2 for normal, 3 for hard.\n")
        Difficulty = stdscr.getkey()

        if str(Difficulty) in ("1","2","3"):
            break

        else:
            stdscr.addstr("Please enter a valid choice\n")
            time.sleep(1)
            continue

    stdscr.refresh()
    return Difficulty

def gettext(stdscr, Difficulty):

    textchoice_easy = (
        "The quick red fox runs fast. He jumps over the soft log. The sun is warm and bright. Birds sing in the tall trees.",
        "A small dog naps on the mat. The cat runs past the wall. We sit and chat all day. Life is good and calm.",
        "She had a big red hat. It was soft and warm. He sat by the tall tree. The sky was blue and clear.")
    textchoice_medium = (
        "The gentle breeze moves the golden leaves across the quiet street. A bird perches on the fence, watching the world pass by.",
        "Typing is a skill that improves with practice. The more you type, the faster and more accurate you become over time.",
        "Lisa walked to the park with her book in hand. She found a bench under a tall oak tree and began to read. The afternoon sun cast soft shadows on the grass.")
    textchoice_hard = (
        "As the autumn leaves spiraled downward, a sudden gust of wind sent them scattering across the cobblestone path. The distant chime of a clock tower echoed through the quiet evening.",
        "Rapid movements and precise coordination define a skilled typist. Accuracy outweighs speed, but mastering both leads to effortless efficiency.",
        "Jonathan hesitated before stepping into the dimly lit library. Dust particles floated in the air, illuminated by flickering candlelight. He reached for an ancient, leather-bound book resting on the highest shelf.")


    if Difficulty=="1":
        TText=random.choice(textchoice_easy)
    if Difficulty=="2":
        TText=random.choice(textchoice_medium)
    if Difficulty=="3":
        TText=random.choice(textchoice_hard)

    GText=[]
    wpm=0
    start_time=time.time()
    stdscr.nodelay(True)

    while True:
        stdscr.clear()
        time_elapsed=max(time.time()-start_time,1)
        wpm=round((len(GText)/(time_elapsed/60))/5)
        stdscr.addstr(TText, curses.color_pair(3))
        stdscr.addstr(3,0,"WPM: "+str(wpm),curses.color_pair(3))

        for i, char in enumerate(GText):
            correctchar=TText[i]
            if char == correctchar:
                stdscr.addstr(0, i, char, curses.color_pair(1))
            if char != correctchar:
                stdscr.addstr(0, i, char, curses.color_pair(2))
        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if "".join(GText)==TText:
            stdscr.addstr(4, 0, "Congratulations you have finished the text. Press escape to exit \n",curses.color_pair(3))
            stdscr.nodelay(False)
            break

        if key in ("\b", "\x7f", "KEY_BACKSPACE"):
            if len(GText) > 0:
                GText.pop()

        elif len(GText)<len(TText):
            GText.append(key)

        stdscr.refresh()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    while True:
        Difficulty=start(stdscr)
        gettext(stdscr, Difficulty)
        input = stdscr.getkey()

        if ord(input)==27:
            stdscr.addstr("Thanks you for playing!", curses.color_pair(3))
            break

wrapper(main)