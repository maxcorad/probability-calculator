import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        contents = [arg for arg in kwargs for _ in range(kwargs[arg])]
        self.contents = contents

    def draw(self, number):
        return [
            self.contents.pop(random.randint(0, len(self.contents) - 1))
            for _ in range(number)
        ] if number < len(self.contents) else self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches = 0
    for _ in range(num_experiments):
        h = copy.deepcopy(hat)
        draw = h.draw(num_balls_drawn)
        matches += 1 if all([
            draw.count(color) >= expected_balls[color]
            for color in expected_balls
        ]) else 0
    return matches / num_experiments
