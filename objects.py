from dataclasses import dataclass

@dataclass
class Padle:
    position: list[int, int, int, int]
    color: tuple[int, int, int]
    points: int
    velocity_y: float


@dataclass
class Ball:
    position: list[int, int]
    radius: float
    color: tuple[int, int, int]
    velocity_x: float
    velocity_y: float