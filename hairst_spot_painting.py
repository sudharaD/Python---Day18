import colorgram

COLOR_LIST = []


class SpotPainting:
    colors = colorgram.extract("image.jpg", 10)
    for color in range(10):
        single_color_rgb_values = []
        single_color_rgb_values.append(colors[color].rgb.r)
        single_color_rgb_values.append(colors[color].rgb.b)
        single_color_rgb_values.append(colors[color].rgb.g)
        COLOR_LIST.append(tuple(single_color_rgb_values))
    print(COLOR_LIST)

