from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    canvas.create_oval(CANVAS_WIDTH/2 - 75, 225, CANVAS_WIDTH/2 + 75, 375, color="#990099")
    
    canvas.create_oval(25, 25, 175, 175, color="#990000")
    
    canvas.create_line(190, 100, 210, 100)
    canvas.create_line(200, 90, 200, 110)
    
    canvas.create_oval(CANVAS_WIDTH/2 + 25, 25, CANVAS_WIDTH/2 + 175, 175, color="#000099")
    
    canvas.create_line(200, 170, 200, 210)
    canvas.create_line(200, 210, 190, 190)
    canvas.create_line(200, 210, 210, 190)
    

if __name__ == '__main__':
    main()