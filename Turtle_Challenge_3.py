class DifferentShapes:
    import turtle as t

    terry_the_turtle = t.Turtle()
    terry_the_turtle.shape("turtle")
    screen = t.Screen()
    screen.colormode(255)

    def random_color(self):
        from random import randint
        color_tuple = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.terry_the_turtle.pencolor(color_tuple)

    #     Test code to find the color
        print(self.terry_the_turtle.pencolor())

    def different_shape_drawer(self, line_length, shapes):
        angle = 0
        for line_count in range(3, shapes+1):
            self.terry_the_turtle.forward(line_length)
            self.random_color()
            for _ in range(line_count-1):
                angle = 360 / line_count
                self.terry_the_turtle.right(angle)
                self.terry_the_turtle.forward(line_length)
            self.terry_the_turtle.right(angle)
