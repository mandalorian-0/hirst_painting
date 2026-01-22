import turtle as t

import colorgram
import random


def color_from_image(image):
    color_bank = colorgram.extract(image, 10)
    color = random.choice(color_bank)
    return color.rgb

# screen = t.Screen()
# screen.setup(600, 600)

# timmy = t.Turtle()

# t.colormode(255)

# timmy.pencolor(color_from_image("drop_painting.jpg"))

# timmy.forward(100)

# t.mainloop()