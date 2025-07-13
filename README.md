# 🐍 Snake Game

A classic Snake game implementation in Python using the Turtle graphics library. This version includes improved gameplay mechanics, better code structure, and enhanced features.

## 🎮 Features

- **Classic Snake Gameplay**: Move the snake to eat food and grow longer
- **Improved Controls**: Support for both arrow keys and WASD
- **High Score Tracking**: Persistent high score storage
- **Grid-Aligned Food**: Food spawns on a grid for better gameplay
- **Collision Prevention**: Food won't spawn on the snake
- **180-Degree Turn Prevention**: Snake can't reverse direction instantly
- **Clean Code Structure**: Well-organized, documented, and type-hinted code

## 🚀 How to Play

1. **Run the game**:
   ```bash
   python main.py
   ```

2. **Controls**:
   - **Arrow Keys** or **WASD**: Control snake direction
   - **Space**: Pause/Resume (future feature)
   - **Close window**: Exit game

3. **Objective**:
   - Eat the red food to grow and increase your score
   - Avoid hitting the walls or your own tail
   - Try to beat your high score!

## 📁 Project Structure

```
Snake+Project+Code+from+Day+21/
├── main.py           # Main game logic and entry point
├── snake.py          # Snake class with movement and growth
├── food.py           # Food class with positioning logic
├── scoreboard.py     # Score tracking and display
├── requirements.txt  # Project dependencies
└── README.md         # This file
```

## 🔧 Code Improvements Made

### 1. **main.py** - Game Logic
- ✅ Organized into a `SnakeGame` class
- ✅ Added constants for better maintainability
- ✅ Improved collision detection methods
- ✅ Added WASD controls alongside arrow keys
- ✅ Better game state management
- ✅ Proper main function with `if __name__ == "__main__"`

### 2. **snake.py** - Snake Class
- ✅ Added type hints for better code clarity
- ✅ Improved direction change logic (prevents 180-degree turns)
- ✅ Added helper methods for position and length
- ✅ Added reset functionality
- ✅ Better constants organization
- ✅ Comprehensive docstrings

### 3. **food.py** - Food Class
- ✅ Grid-aligned positioning for better gameplay
- ✅ Collision avoidance with snake segments
- ✅ Improved positioning algorithms
- ✅ Added color and size customization methods
- ✅ Better constants and type hints

### 4. **scoreboard.py** - Scoreboard Class
- ✅ High score persistence to file
- ✅ Enhanced display with high score
- ✅ New high score celebration
- ✅ Pause message support
- ✅ Better font and positioning constants

## 🛠️ Technical Improvements

### Code Quality
- **Type Hints**: Added throughout for better IDE support and code clarity
- **Constants**: Moved magic numbers to named constants
- **Docstrings**: Comprehensive documentation for all methods
- **Error Handling**: Graceful handling of file operations
- **Code Organization**: Logical separation of concerns

### Gameplay Enhancements
- **Grid Alignment**: Food spawns on a 20x20 grid for predictable movement
- **Collision Avoidance**: Food won't spawn on snake segments
- **Direction Prevention**: Snake can't reverse direction instantly
- **High Score Persistence**: Scores are saved between game sessions
- **Better Controls**: Multiple control schemes supported

### Performance
- **Efficient Collision Detection**: Optimized tail collision checking
- **Reduced Redundant Operations**: Better state management
- **Memory Management**: Proper cleanup of turtle objects

## 🎯 Future Enhancements

- [ ] Pause/Resume functionality
- [ ] Different difficulty levels
- [ ] Sound effects
- [ ] Power-ups and special food
- [ ] Multiplayer support
- [ ] Game settings menu
- [ ] Different snake and food skins

## 📋 Requirements

- **Python**: 3.7 or higher (for type hints support)
- **Dependencies**: None (uses built-in turtle module)

## 🏃‍♂️ Running the Game

```bash
# Clone or download the project
cd Snake+Project+Code+from+Day+21

# Run the game
python main.py
```

## 🤝 Contributing

Feel free to contribute improvements:
1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request


🖼️ Screenshots

<img width="2560" height="1600" alt="Screenshot 2025-07-13 at 10 26 56 PM" src="https://github.com/user-attachments/assets/116053a8-1cdd-487d-9fa6-79139cb32f5d" />



