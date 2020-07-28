class Config():
    FPS = 9
    MENU_FPS = 60
    WINDOW_WIDTH = 640
    WINDOWS_HEIGHT = 480
    CELLSIZE = 20
    assert WINDOW_WIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
    assert WINDOWS_HEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
    CELLWIDTH = int(WINDOW_WIDTH / CELLSIZE)
    CELLHEIGHT = int(WINDOWS_HEIGHT / CELLSIZE)

    # Colours
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    DARKGREEN = (0, 155, 0)
    DARKGRAY = (40, 40, 0)
    BG_COLOR = BLACK
