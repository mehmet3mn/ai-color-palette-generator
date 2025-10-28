import random

def generate_palette(keyword):
    def random_color():
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return [random_color() for _ in range(5)]