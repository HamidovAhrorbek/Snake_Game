    """Manages the game score display and high score tracking."""

    def __init__(self):
        """Initialize the scoreboard with proper display settings."""
        super().__init__()
        self.score = 0
        self.high_score = self._load_high_score()

        # Setup display properties
        self.color("white")
        self.penup()
        self.hideturtle()

        # Initial display
        self.update_scoreboard()

    def _load_high_score(self) -> int:
        """Load the high score from file, return 0 if file doesn't exist."""
        try:
            with open(HIGH_SCORE_FILE, "r") as file:
                return int(file.read().strip())
        except (FileNotFoundError, ValueError):
            return 0

    def _save_high_score(self) -> None:
        """Save the current high score to file."""
        try:
            with open(HIGH_SCORE_FILE, "w") as file:
                file.write(str(self.high_score))
        except IOError:
            # Silently fail if we can't save the high score
            pass

    def update_scoreboard(self) -> None:
        """Update the score display on screen."""
        self.clear()
        self.goto(SCORE_POSITION)
        self.write(f"Score: {self.score} | High Score: {self.high_score}",
                   align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self) -> None:
        """Increase the score by 1 and update display."""
        self.score += 1
        self.update_scoreboard()

    def game_over(self) -> None:
        """Display game over message and update high score if needed."""
        # Check if current score is a new high score
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()
            self._display_new_high_score()

        # Display game over message
        self.goto(GAME_OVER_POSITION)
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)

    def _display_new_high_score(self) -> None:
        """Display a message for achieving a new high score."""
        self.goto(HIGH_SCORE_POSITION)
        self.write("🎉 NEW HIGH SCORE! 🎉",
                   align=ALIGNMENT, font=HIGH_SCORE_FONT)

    def reset_score(self) -> None:
        """Reset the current score to 0."""
        self.score = 0
        self.update_scoreboard()

    def get_score(self) -> int:
        """Get the current score."""
        return self.score

    def get_high_score(self) -> int:
        """Get the high score."""
        return self.high_score

    def display_pause_message(self) -> None:
        """Display a pause message."""
        self.goto(GAME_OVER_POSITION)
        self.write("PAUSED - Press SPACE to continue",
                   align=ALIGNMENT, font=SCORE_FONT)

    def clear_pause_message(self) -> None:
        """Clear the pause message."""
        self.goto(GAME_OVER_POSITION)
        self.clear()
        self.update_scoreboard()
