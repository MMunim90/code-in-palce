from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Create mirror line
    canvas.create_line(
        CANVAS_WIDTH // 2, 
        0, 
        CANVAS_WIDTH // 2, 
        CANVAS_HEIGHT)
    
    # Create red rectangle
    rect_left_x = 20
    rect_top_y = 50
    rect_width = 100
    rect_height = 200
    canvas.create_rectangle(
        rect_left_x, 
        rect_top_y, 
        rect_left_x + rect_width, 
        rect_top_y + rect_height, 
        'red')
    
    # Create blue rectangle
    blue_left_x = CANVAS_WIDTH - rect_left_x - rect_width
    canvas.create_rectangle(
        blue_left_x,
        rect_top_y,
        blue_left_x + rect_width,
        rect_top_y + rect_height,
        'blue'
    )


if __name__ == '__main__':
    main()