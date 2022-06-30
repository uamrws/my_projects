import turtle

if __name__ == '__main__':
    color_list = [
        'red','yellow','green','blue','black','pink','purple'
    ]
    num=0
    # turtle.begin_fill()
    while True:
        turtle.color(color_list[num])
        turtle.forward(200)
        turtle.left(120)
        if abs(turtle.pos()) < 1:
            print(turtle.pos())
            break
        num+=1
        if num>=len(color_list):
            num =0
    # turtle.end_fill()
    turtle.done()

