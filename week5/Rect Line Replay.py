import graphics

def main():
    canvas = graphics.create_canvas(300, 300)
    
    for i in range(20):
        value = i * 10
        
        left_x = value
        top_y = value
        right_x = value + 10
        bottom_y = value + 10
        
        canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
        
        print(i)
        
if __name__ == '__main__':
    main()