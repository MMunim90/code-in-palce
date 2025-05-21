from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
SQUARE_SIZE = 100

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    middle_x = CANVAS_WIDTH/2
    middle_y = CANVAS_HEIGHT/2
    
    left_x = middle_x - SQUARE_SIZE/2
    top_y = middle_y - SQUARE_SIZE/2
    
    right_x = left_x + SQUARE_SIZE
    bottom_y = top_y + SQUARE_SIZE
    
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

if __name__ == '__main__':
    main()