import curses

def close():
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()

    curses.endwin()

screen = curses.initscr()
key = ''

curses.cbreak()
curses.noecho()

(height, width) = screen.getmaxyx()
height -= 1
width -= 1

key = screen.getch()

while key != '~':
    key = screen.getch()

    screen.addstr(height, 0, "")

    if key == curses.KEY_DOWN:
        screen.addstr(height, 0, "Typing")

    screen.refresh()

close()

# try:
#     key = screen.getch()
#
#     if key == curses.KEY_DOWN:
#         screen.addstr(height, 0, "Typing")
#     else:
#         screen.addstr(height, 0, "Not Typing")
#
#     screen.refresh()
#
#     #close()
#
# except curses.error:
#     print curses.error
#
#     close()


