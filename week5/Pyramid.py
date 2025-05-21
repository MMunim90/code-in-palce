from graphics import Canvas

CANVAS_WIDTH = 600      
CANVAS_HEIGHT = 300     

BRICK_WIDTH = 30        
BRICK_HEIGHT = 12       
BRICKS_IN_BASE = 14     

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    for row in range(BRICKS_IN_BASE):
        bricks_in_row = BRICKS_IN_BASE - row
        total_row_width = bricks_in_row * BRICK_WIDTH
        start_x = (CANVAS_WIDTH - total_row_width) / 2
        y = CANVAS_HEIGHT - (row + 1) * BRICK_HEIGHT

        for brick in range(bricks_in_row):
            x = start_x + brick * BRICK_WIDTH
            canvas.create_rectangle(
                x, y,
                x + BRICK_WIDTH, y + BRICK_HEIGHT,
                "yellow", "black"
            )

if __name__ == '__main__':
    main()
