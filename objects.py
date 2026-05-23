class Padle:
    def __init__(self, position: list, color: str, points: int, velocity_y: int):
        self.position = position
        self.color = color
        self.points = points
        self.velocity_y = velocity_y


class Ball:
    def __init__(self, position: list, radius: float, color: str, velocity_x: float, velocity_y: float):
        self.position = position
        self.radius = radius
        self.color = color
        self.velocity_x= velocity_x
        self.velocity_y= velocity_y