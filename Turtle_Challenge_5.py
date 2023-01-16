class Challenge5:
    import turtle as t
    import random

    tory_the_turtle = t.Turtle()
    tory_the_turtle.shape("turtle")
    screen = t.Screen()
    screen.colormode(255)
    tory_the_turtle.speed("fastest")

    def random_color(self):
        r = self.random.randint(0, 255)
        g = self.random.randint(0, 255)
        b = self.random.randint(0, 255)
        random_color_tuple = (r, g, b)
        return random_color_tuple

    def spirograph(self, number_of_loops, radius):
        angle = 360 / number_of_loops
        for _ in range(number_of_loops):
            self.tory_the_turtle.pencolor(self.random_color())
            self.tory_the_turtle.circle(radius)
            self.tory_the_turtle.right(angle)



