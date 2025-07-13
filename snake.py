from turtle import Turtle
from typing import List, Tuple

# Game constants
STARTING_POSITIONS: List[Tuple[int, int]] = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Snake appearance
SNAKE_SHAPE = "square"
SNAKE_COLOR = "white"


class Snake:
    """Represents the snake in the game with movement and growth capabilities."""

    def __init__(self):
        """Initialize the snake with starting segments."""
        self.segments: List[Turtle] = []
        self.create_snake()
        self.head = self.segments[0]
        self._last_direction = RIGHT  # Track last direction to prevent 180-degree turns

    def create_snake(self) -> None:
        """Create the initial snake with starting segments."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position) -> None:
        """Add a new segment to the snake at the specified position."""
        new_segment = Turtle(SNAKE_SHAPE)
        new_segment.color(SNAKE_COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self) -> None:
        """Add a new segment to the end of the snake."""
        self.add_segment(self.segments[-1].position())

    def move(self) -> None:
        """Move the snake forward by updating segment positions."""
        # Move all segments except the head to follow the segment in front
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Move the head forward
        self.head.forward(MOVE_DISTANCE)
        self._last_direction = self.head.heading()

    def _can_change_direction(self, new_direction: int) -> bool:
        """Check if the snake can change to the new direction (prevent 180-degree turns)."""
        if len(self.segments) <= 1:
            return True

        # Calculate the difference in direction
        direction_diff = abs(new_direction - self._last_direction)
        return direction_diff != 180

    def up(self) -> None:
        """Change snake direction to up if valid."""
        if self._can_change_direction(UP):
            self.head.setheading(UP)

    def down(self) -> None:
        """Change snake direction to down if valid."""
        if self._can_change_direction(DOWN):
            self.head.setheading(DOWN)

    def left(self) -> None:
        """Change snake direction to left if valid."""
        if self._can_change_direction(LEFT):
            self.head.setheading(LEFT)

    def right(self) -> None:
        """Change snake direction to right if valid."""
        if self._can_change_direction(RIGHT):
            self.head.setheading(RIGHT)

    def reset(self) -> None:
        """Reset the snake to its initial state."""
        # Hide all current segments
        for segment in self.segments:
            segment.hideturtle()

        # Clear segments list and recreate
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self._last_direction = RIGHT

    def get_head_position(self) -> Tuple[float, float]:
        """Get the current position of the snake's head."""
        return (self.head.xcor(), self.head.ycor())

    def get_length(self) -> int:
        """Get the current length of the snake."""
        return len(self.segments)
          
