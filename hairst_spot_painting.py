import colorgram
import turtle as t
import random

turtle = t.Turtle()
screen = t.Screen()
turtle.penup()
turtle.hideturtle()
screen_width = screen.screensize()[0] * -1
screen_height = screen.screensize()[1] * -1
turtle.setx(screen_width)
turtle.sety(screen_height)
turtle.speed("fastest")

screen.colormode(255)
COLOR_LIST = []
EXTRACTED_COLORS = [(198, 32, 12), (250, 17, 237), (39, 189, 76),
                    (38, 68, 217), (238, 5, 227), (229, 46, 159), (27, 157, 40), (215, 12, 74), (15, 16, 154),
                    (199, 10, 14), (242, 252, 246), (243, 165, 33), (229, 121, 17), (73, 31, 9), (60, 8, 14),
                    (224, 211, 141), (10, 61, 97), (221, 9, 160), (17, 43, 18), (46, 232, 214), (11, 239, 227),
                    (81, 214, 73), (238, 220, 156), (74, 167, 213), (77, 202, 234), (52, 243, 234), (3, 40, 67)]

class SpotPainting:
    # colors = colorgram.extract("image.jpg", 30)
    # for color in range(30):
    #     single_color_rgb_values = []
    #     single_color_rgb_values.append(colors[color].rgb.r)
    #     single_color_rgb_values.append(colors[color].rgb.b)
    #     single_color_rgb_values.append(colors[color].rgb.g)
    #     COLOR_LIST.append(tuple(single_color_rgb_values))
    # print(COLOR_LIST)

    def spot_painting(self, spot_size, h_value, v_value, space):
        vertical_move = screen_height
        for vertical in range(v_value):
            for horizontal in range(h_value):
                turtle.dot(spot_size, random.choice(EXTRACTED_COLORS))
                turtle.forward(space)

            vertical_move += space
            turtle.setx(screen_width)
            turtle.sety(vertical_move)





