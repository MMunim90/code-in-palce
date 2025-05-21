from graphics import Canvas

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
FIRST_LINE_LEFT_X = 50
FIRST_LINE_TOP_Y = 50
FONT_SIZE = 24
LINE_SPACING = FONT_SIZE + 10

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    line1 = "An old silent pond..."
    line2 = "A frog jumps into the pond,"
    line3 = "splash! Silence again."

    canvas.create_text(FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y, text=line1, font='Courier', font_size=FONT_SIZE, anchor='nw')
    canvas.create_text(FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y + LINE_SPACING, text=line2, font='Courier', font_size=FONT_SIZE, anchor='nw')
    canvas.create_text(FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y + 2 * LINE_SPACING, text=line3, font='Courier', font_size=FONT_SIZE, anchor='nw')

if __name__ == '__main__':
    main()