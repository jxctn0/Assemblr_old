import curses

def draw_menu(win, selected_row):
    win.clear()
    height, width = win.getmaxyx()

    title = "Basic UI with ncurses"
    win.addstr(0, (width - len(title)) // 2, title)

    menu_options = ["Option 1", "Option 2", "Option 3"]
    for i, option in enumerate(menu_options, start=1):
        x_pos = (width - len(option)) // 2
        y_pos = height // 2 - len(menu_options) + 2 * i

        if i == selected_row:
            win.attron(curses.A_REVERSE)  # Highlight the selected row
            win.addstr(y_pos, x_pos, f"{i}. {option}")
            win.attroff(curses.A_REVERSE)
        else:
            win.addstr(y_pos, x_pos, f"{i}. {option}")

    win.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    selected_row = 1

    while True:
        draw_menu(stdscr, selected_row)

        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == curses.KEY_DOWN or key == 9:  # TAB key
            selected_row = min(selected_row + 1, 3)
        elif key == curses.KEY_UP or key == 353:  # SHIFT + TAB key
            selected_row = max(selected_row - 1, 1)

if __name__ == "__main__":
    curses.wrapper(main)
