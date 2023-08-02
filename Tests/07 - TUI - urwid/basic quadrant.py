import urwid

def exit_program(button):
    raise urwid.ExitMainLoop()

# Function to handle keyboard input
def handle_input(key):
    if key in ('q', 'Q'):
        exit_program(None)

if __name__ == "__main__":
    # Create widgets for each section
    title_widget = urwid.Text("4-Section TUI using Urwid")
    left_widget = urwid.Text("This is the left section")
    right_widget = urwid.Text("This is the right section")
    bottom_widget = urwid.Text("Press 'Q' to quit")

    # Combine widgets into Pile and Frame widgets
    left_column = urwid.Pile([left_widget, urwid.Divider()])
    right_column = urwid.Pile([right_widget, urwid.Divider()])

    body = urwid.Columns([left_column, right_column], dividechars=1)
    footer = urwid.Pile([bottom_widget, urwid.Divider()])

    # Combine all sections in a Vertical Pile
    layout = urwid.Pile([title_widget, urwid.Divider(), body])

    # Create a Filler widget for the footer to stay fixed at the bottom
    footer_filler = urwid.Filler(footer, valign='bottom')

    # Create a Frame widget to add a border around the layout
    frame = urwid.Frame(layout, footer=footer_filler)

    # Create a top-level widget for the main loop
    main_loop = urwid.MainLoop(frame, unhandled_input=handle_input)

    # Run the TUI
    main_loop.run()
