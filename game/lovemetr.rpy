screen lovemetr_mama:
    bar:
        xsize 350
        ysize 50
        xpos 10
        ypos 10
        value AnimatedValue(value=love_mama, range=maxlove, delay=1.0)
        left_bar Frame("gui/bar/left.png", 10, 10)
        right_bar Frame("gui/bar/right.png", 10, 10)

default love_mama = 50

screen lovemetr_alina:
    bar:
        xsize 350
        ysize 50
        xpos 10
        ypos 10
        value AnimatedValue(value=love_alina, range=maxlove, delay=1.0)
        left_bar Frame("gui/bar/left.png", 10, 10)
        right_bar Frame("gui/bar/right.png", 10, 10)

default love_alina = 10

screen lovemetr_bodya:
    bar:
        xsize 350
        ysize 50
        xpos 10
        ypos 10
        value AnimatedValue(value=love_bodya, range=maxlove, delay=1.0)
        left_bar Frame("gui/bar/left.png", 10, 10)
        right_bar Frame("gui/bar/right.png", 10, 10)

default love_bodya = 0

screen lovemetr_currator:
    bar:
        xsize 350
        ysize 50
        xpos 10
        ypos 10
        value AnimatedValue(value=love_currator, range=maxlove, delay=1.0)
        left_bar Frame("gui/bar/left.png", 10, 10)
        right_bar Frame("gui/bar/right.png", 10, 10)

define love_currator = 0


screen lovemetr_kyn:
    bar:
        xsize 350
        ysize 50
        xpos 10
        ypos 10
        value AnimatedValue(value=love_currator, range=maxlove, delay=1.0)
        left_bar Frame("gui/bar/left.png", 10, 10)
        right_bar Frame("gui/bar/right.png", 10, 10)

define love_kyn = 0