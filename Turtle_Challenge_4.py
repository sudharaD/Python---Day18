class Challenge4:
    import turtle as t
    from random import choice

    timothy_the_turtle = t.Turtle()
    timothy_the_turtle.shape("turtle")
    timothy_the_turtle.pensize(5)
    color_list = ["deep sky blue", "spring green", "yellow", "red", "magenta", "black"]
    angles = [0, 90, 180, 270]

    screen = t.Screen()
    screen.delay(1)

    def random_walk(self, distance, loops):
        for _ in range(loops):
            self.timothy_the_turtle.setheading(self.choice(self.angles))
            self.timothy_the_turtle.forward(distance)
            self.timothy_the_turtle.pencolor(self.choice(self.color_list))



