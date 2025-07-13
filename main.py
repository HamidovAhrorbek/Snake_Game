from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Game constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GAME_SPEED = 0.1
FOOD_COLLISION_DISTANCE = 15
WALL_COLLISION_THRESHOLD = 280
TAIL_COLLISION_DISTANCE = 10


class SnakeGame:
    def __init__(self):
        self.screen = Screen()
        self.setup_screen()

        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()

        self.game_is_on = True
        self.setup_controls()

    def setup_screen(self):
        """Initialize the game screen with proper settings."""
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)

    def setup_controls(self):
        """Set up keyboard controls for the snake."""
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")
        self.screen.onkey(self.snake.up, "w")
        self.screen.onkey(self.snake.down, "s")
        self.screen.onkey(self.snake.left, "a")
        self.screen.onkey(self.snake.right, "d")

    def check_food_collision(self):
        """Check if snake head collides with food."""
        if self.snake.head.distance(self.food) < FOOD_COLLISION_DISTANCE:
            # Get all snake segment positions to avoid placing food on snake
            snake_positions = [(seg.xcor(), seg.ycor())
                               for seg in self.snake.segments]
            self.food.refresh(snake_positions)
            self.snake.extend()
            self.scoreboard.increase_score()

    def check_wall_collision(self):
        """Check if snake head collides with walls."""
        head_x = self.snake.head.xcor()
        head_y = self.snake.head.ycor()

        if (abs(head_x) > WALL_COLLISION_THRESHOLD or
                abs(head_y) > WALL_COLLISION_THRESHOLD):
            return True
        return False

    def check_tail_collision(self):
        """Check if snake head collides with its own tail."""
        for segment in self.snake.segments[1:]:  # Skip the head
            if self.snake.head.distance(segment) < TAIL_COLLISION_DISTANCE:
                return True
        return False

    def game_over(self):
        """Handle game over state."""
        self.game_is_on = False
        self.scoreboard.game_over()

    def run(self):
        """Main game loop."""
        while self.game_is_on:
            self.screen.update()
            time.sleep(GAME_SPEED)
            self.snake.move()

            # Check collisions
            self.check_food_collision()

            if self.check_wall_collision():
                self.game_over()
                break

            if self.check_tail_collision():
                self.game_over()
                break

        self.screen.exitonclick()


def main():
    """Main function to start the game."""
    game = SnakeGame()
    game.run()


if __name__ == "__main__":
    main()
