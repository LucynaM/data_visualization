from random import choice

class RandomWalk():
    """A class to generate random walks"""
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # Start point at (0, 0) coordinates
        self.x_values = [0]
        self.y_values = [0]

        
    def get_step(self):
        # Decide which direction to go, and how far to go in that direction
        point_direction = choice([1, -1])
        point_distance = choice(list(range(5)))
        point_step = point_direction * point_distance
        return point_step

    def get_next_step(self, values, step):
        # Calculate the next x and y values
        next_step = values[-1] + step
        values.append(next_step)


    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go, and how far to go in that direction
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values
            self.get_next_step(self.x_values, x_step)
            self.get_next_step(self.y_values, y_step)
