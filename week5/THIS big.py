from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
THIS_BIG = 144
CENTER_X = 160
CENTER_Y = 160

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    top_left_x = CENTER_X - THIS_BIG / 2
    top_left_y = CENTER_Y - THIS_BIG / 2
    bottom_right_x = top_left_x + THIS_BIG
    bottom_right_y = top_left_y + THIS_BIG

    canvas.create_rectangle(top_left_x, top_left_y, bottom_right_x, bottom_right_y)


if __name__ == '__main__':
    main()