import curses

def draw_menu(win):
    win.clear()
    height, width = win.getmaxyx()

    title = "Basic UI with ncurses"
    win.addstr(0, (width - len(title)) // 2, title)

    menu_options = ["Option 1", "Option 2", "Option 3"]
    for i, option in enumerate(menu_options, start=1):
        x_pos = (width - len(option)) // 2
        y_pos = height // 2 - len(menu_options) + 2 * i
        win.addstr(y_pos, x_pos, f"{i}. {option}")

    win.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    while True:
        draw_menu(stdscr)

        key = stdscr.getch()
        if key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)
