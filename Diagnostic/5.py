from graphics import Canvas

def main():
    canvas = Canvas(400, 400)
    
    x = 10
    y = 10
    draw_car(canvas, x, y)  

    x = 100
    y = 100
    draw_car(canvas, x, y)  

def draw_car(canvas, x, y):
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()
