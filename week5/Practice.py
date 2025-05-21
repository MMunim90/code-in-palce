from graphics import Canvas
import time

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_line(0, 0, 500, 500)
    canvas.create_rectangle(70, 70, 150, 150, "blue")
    canvas.create_rectangle(250, 150, 500, 500)
    canvas.create_oval     (250, 150, 500, 500, "red")
    canvas.create_image(0, 200, "simba.png")
    canvas.create_text(50, 20, 
        "Programming is Awesome!!!", 
        color="blue", 
        font="Courier", 
        font_size=28)

    canvas.create_rectangle(0, 800, 10, 810)
    
    show_mouse_position(canvas)
    
def show_mouse_position(canvas):
    while True:
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
        print(f"x = {x}, y = {y}")
        time.sleep(1/50)

if __name__ == '__main__':
    main()