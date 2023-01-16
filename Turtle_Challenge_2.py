class Challenge2:

    import turtle as t

    tom_the_turtle = t.Turtle()
    tom_the_turtle.shape("turtle")

    def dashed_line(self, dash_value, space_value):
        for _ in range(50):
            self.tom_the_turtle.forward(dash_value)
            self.tom_the_turtle.penup()
            self.tom_the_turtle.forward(space_value)
            self.tom_the_turtle.pendown()

