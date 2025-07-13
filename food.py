from turtle import Turtle
import random
from typing import List, Tuple, Optional

# Food appearance constants
FOOD_SHAPE = "circle"
FOOD_COLOR = "red"
FOOD_SIZE = 0.5

# Game boundaries
FOOD_BOUNDARY = 280
FOOD_GRID_SIZE = 20  # Align food with snake movement grid


class Food(Turtle):
    """Represents the food that the snake can eat to grow."""

    def __init__(self):
        """Initialize the food with proper appearance and position."""
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=FOOD_SIZE, stretch_wid=FOOD_SIZE)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.current_position = (0, 0)
        self.refresh()

    def _generate_grid_position(self) -> Tuple[int, int]:
        """Generate a position that aligns with the snake's movement grid."""
        # Calculate grid-aligned coordinates
        x = random.randint(-FOOD_BOUNDARY // FOOD_GRID_SIZE,
                           FOOD_BOUNDARY // FOOD_GRID_SIZE) * FOOD_GRID_SIZE
        y = random.randint(-FOOD_BOUNDARY // FOOD_GRID_SIZE,
                           FOOD_BOUNDARY // FOOD_GRID_SIZE) * FOOD_GRID_SIZE
        return (x, y)

    def _generate_random_position(self) -> Tuple[int, int]:
        """Generate a random position within the game boundaries."""
        x = random.randint(-FOOD_BOUNDARY, FOOD_BOUNDARY)
        y = random.randint(-FOOD_BOUNDARY, FOOD_BOUNDARY)
        return (x, y)

    def refresh(self, snake_positions: Optional[List[Tuple[float, float]]] = None) -> None:
        """Move food to a new random position, avoiding snake if positions provided."""
        if snake_positions is None:
            snake_positions = []

        attempts = 0
        max_attempts = 100

        while attempts < max_attempts:
            # Use grid-aligned positioning for better gameplay
            new_position = self._generate_grid_position()

            # Check if the new position overlaps with the snake
            if not self._position_overlaps_snake(new_position, snake_positions):
                self.current_position = new_position
                self.goto(new_position)
                return

            attempts += 1

        # Fallback to random positioning if grid positioning fails
        self.current_position = self._generate_random_position()
        self.goto(self.current_position)

    def _position_overlaps_snake(self, position: Tuple[int, int],
                                 snake_positions: List[Tuple[float, float]]) -> bool:
        """Check if the given position overlaps with any snake segment."""
        for snake_pos in snake_positions:
            distance = ((position[0] - snake_pos[0]) ** 2 +
                        (position[1] - snake_pos[1]) ** 2) ** 0.5
            if distance < FOOD_GRID_SIZE:
                return True
        return False

    def get_position(self) -> Tuple[float, float]:
        """Get the current position of the food."""
        return self.current_position

    def change_color(self, color: str) -> None:
        """Change the food color."""
        self.color(color)

    def change_size(self, size: float) -> None:
        """Change the food size."""
        self.shapesize(stretch_len=size, stretch_wid=size)
