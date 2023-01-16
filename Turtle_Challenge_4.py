class Challenge4:
    import turtle as t
    from random import choice

    timothy_the_turtle = t.Turtle()
    timothy_the_turtle.shape("turtle")
    color_list = ["deep sky blue", "spring green", "yellow", "red", "magenta", "black"]
    angles = [90, 180, 270, 360]

    def random_walk(self, distance):
        self.timothy_the_turtle.right(self.choice(self.angles))
        self.timothy_the_turtle.forward(distance)
        self.timothy_the_turtle.color(self.choice(self.color_list))



