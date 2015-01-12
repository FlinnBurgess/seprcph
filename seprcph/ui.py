from seprcph.ui_elements import Window, Container, Label, Clickable

def initialise_ui(size, surface):
    c = Container((100, 100), (100, 100), [])
    win = Window(size, (0, 0), [], surface)
    win.update()
    return win
