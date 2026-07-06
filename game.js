// Snake Game Engine — v1.0.0
// Core game logic and rendering

// Game state variables
let canvas, ctx;
let snake = [];
let food = {};
let direction = { x: 0, y: 0 };
let nextDirection = { x: 0, y: 0 };
let score = 0;
let highScore = 0;
let level = 1;
let gameSpeed;
let gameLoop = null;
let isPaused = false;
let isGameOver = false;
let isGameStarted = false;

// [VARS_MARKER]

// DOM elements
let scoreEl, highScoreEl, levelEl, startBtn, pauseBtn;

// Initialize the game
function init() {
    canvas = document.getElementById('gameCanvas');
    ctx = canvas.getContext('2d');
    canvas.width = CONFIG.canvasWidth;
    canvas.height = CONFIG.canvasHeight;

    scoreEl = document.getElementById('score');
    highScoreEl = document.getElementById('high-score');
    levelEl = document.getElementById('level');
    startBtn = document.getElementById('startBtn');
    pauseBtn = document.getElementById('pauseBtn');

    // Load high score from localStorage
    highScore = parseInt(localStorage.getItem('snakeHighScore')) || 0;
    highScoreEl.textContent = highScore;

    // Apply config to UI
    document.getElementById('game-title').textContent = CONFIG.gameTitle;
    document.getElementById('game-subtitle').textContent = CONFIG.gameSubtitle;
    document.getElementById('instructions').textContent = CONFIG.instructionsText;
    document.getElementById('footer-text').textContent = CONFIG.footerText;
    startBtn.textContent = CONFIG.startButtonText;

    // [INIT_MARKER]

    // Draw initial screen
    drawBackground();
    drawStartScreen();

    // Set up keyboard controls
    document.addEventListener('keydown', handleKeyPress);
}

// Start the game
function startGame() {
    // Reset game state
    const cols = Math.floor(CONFIG.canvasWidth / CONFIG.gridSize);
    const rows = Math.floor(CONFIG.canvasHeight / CONFIG.gridSize);
    const startX = Math.floor(cols / 2);
    const startY = Math.floor(rows / 2);

    snake = [];
    for (let i = 0; i < CONFIG.initialLength; i++) {
        snake.push({ x: startX - i, y: startY });
    }

    direction = { x: 1, y: 0 };
    nextDirection = { x: 1, y: 0 };
    score = 0;
    level = 1;
    gameSpeed = CONFIG.initialSpeed;
    isPaused = false;
    isGameOver = false;
    isGameStarted = true;

    updateScore();
    spawnFood();

    startBtn.style.display = 'none';
    pauseBtn.style.display = 'inline-block';
    pauseBtn.textContent = CONFIG.pauseButtonText;

    // [START_MARKER]

    // Start game loop
    if (gameLoop) clearInterval(gameLoop);
    gameLoop = setInterval(gameStep, gameSpeed);
}

// Main game step
function gameStep() {
    if (isPaused || isGameOver) return;

    // Update direction
    direction = { ...nextDirection };

    // Calculate new head position
    const head = {
        x: snake[0].x + direction.x,
        y: snake[0].y + direction.y
    };

    // Check wall collision
    const cols = Math.floor(CONFIG.canvasWidth / CONFIG.gridSize);
    const rows = Math.floor(CONFIG.canvasHeight / CONFIG.gridSize);

    if (CONFIG.wallCollision) {
        if (head.x < 0 || head.x >= cols || head.y < 0 || head.y >= rows) {
            gameOver();
            return;
        }
    } else {
        // Wrap around
        head.x = (head.x + cols) % cols;
        head.y = (head.y + rows) % rows;
    }

    // Check self collision
    if (CONFIG.selfCollision) {
        for (let segment of snake) {
            if (head.x === segment.x && head.y === segment.y) {
                gameOver();
                return;
            }
        }
    }

    // Add new head
    snake.unshift(head);

    // Check food collision
    if (head.x === food.x && head.y === food.y) {
        // Ate food
        const points = Math.floor(CONFIG.pointsPerFood * CONFIG.scoreMultiplier);
        score += points;

        // Level up check
        const newLevel = Math.floor(score / CONFIG.levelUpScore) + 1;
        if (newLevel > level) {
            level = newLevel;
            // Increase speed
            gameSpeed = Math.max(CONFIG.minSpeed, gameSpeed - CONFIG.speedIncrement);
            clearInterval(gameLoop);
            gameLoop = setInterval(gameStep, gameSpeed);
        }

        updateScore();
        spawnFood();
        // [FOOD_EATEN_MARKER]
    } else {
        // Remove tail
        snake.pop();
    }

    // Render
    render();
}

// Render the game
function render() {
    drawBackground();

    if (CONFIG.showGrid) {
        drawGrid();
    }

    drawFood();
    drawSnake();
    // [RENDER_MARKER]
}

// Draw background
function drawBackground() {
    ctx.fillStyle = CONFIG.backgroundColor;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
}

// Draw grid lines
function drawGrid() {
    ctx.strokeStyle = CONFIG.gridColor;
    ctx.lineWidth = 0.5;
    const gs = CONFIG.gridSize;

    for (let x = 0; x <= canvas.width; x += gs) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, canvas.height);
        ctx.stroke();
    }
    for (let y = 0; y <= canvas.height; y += gs) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(canvas.width, y);
        ctx.stroke();
    }
}

// Draw the snake
function drawSnake() {
    const gs = CONFIG.gridSize;
    snake.forEach((segment, index) => {
        if (index === 0) {
            ctx.fillStyle = CONFIG.snakeHeadColor;
        } else {
            ctx.fillStyle = CONFIG.snakeColor;
        }
        ctx.fillRect(
            segment.x * gs + 1,
            segment.y * gs + 1,
            gs - 2,
            gs - 2
        );
    });
}

// Draw the food
function drawFood() {
    const gs = CONFIG.gridSize;
    ctx.fillStyle = CONFIG.foodColor;
    ctx.fillRect(
        food.x * gs + 1,
        food.y * gs + 1,
        gs - 2,
        gs - 2
    );
}

// Spawn food at random position
function spawnFood() {
    const cols = Math.floor(CONFIG.canvasWidth / CONFIG.gridSize);
    const rows = Math.floor(CONFIG.canvasHeight / CONFIG.gridSize);
    let newFood;

    do {
        newFood = {
            x: Math.floor(Math.random() * cols),
            y: Math.floor(Math.random() * rows)
        };
    } while (snake.some(seg => seg.x === newFood.x && seg.y === newFood.y));

    food = newFood;
}

// Draw start screen
function drawStartScreen() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = '#ffffff';
    ctx.font = '24px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Press Start to Play', canvas.width / 2, canvas.height / 2);
}

// Game over
function gameOver() {
    isGameOver = true;
    isGameStarted = false;
    clearInterval(gameLoop);
    // [GAME_OVER_MARKER]

    // Update high score
    if (score > highScore) {
        highScore = score;
        localStorage.setItem('snakeHighScore', highScore);
        highScoreEl.textContent = highScore;
    }

    // Draw game over screen
    ctx.fillStyle = 'rgba(0, 0, 0, 0.75)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = '#ef4444';
    ctx.font = 'bold 32px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(CONFIG.gameOverText, canvas.width / 2, canvas.height / 2 - 20);

    ctx.fillStyle = '#ffffff';
    ctx.font = '18px Inter, sans-serif';
    ctx.fillText('Score: ' + score, canvas.width / 2, canvas.height / 2 + 20);

    // Show start button again
    startBtn.style.display = 'inline-block';
    startBtn.textContent = 'Play Again';
    pauseBtn.style.display = 'none';
}

// Toggle pause
function togglePause() {
    isPaused = !isPaused;
    pauseBtn.textContent = isPaused ? CONFIG.resumeButtonText : CONFIG.pauseButtonText;

    if (isPaused) {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#ffffff';
        ctx.font = '28px Inter, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('PAUSED', canvas.width / 2, canvas.height / 2);
    }
}

// Handle keyboard input
function handleKeyPress(e) {
    switch (e.key) {
        case 'ArrowUp':
        case 'w':
        case 'W':
            if (direction.y === 0) nextDirection = { x: 0, y: -1 };
            break;
        case 'ArrowDown':
        case 's':
        case 'S':
            if (direction.y === 0) nextDirection = { x: 0, y: 1 };
            break;
        case 'ArrowLeft':
        case 'a':
        case 'A':
            if (direction.x === 0) nextDirection = { x: -1, y: 0 };
            break;
        case 'ArrowRight':
        case 'd':
        case 'D':
            if (direction.x === 0) nextDirection = { x: 1, y: 0 };
            break;
        case ' ':
            if (isGameStarted) togglePause();
            break;
        case 'Enter':
            if (!isGameStarted) startGame();
            break;
    }
}

// Update score display
function updateScore() {
    scoreEl.textContent = score;
    levelEl.textContent = level;
}

// [FUNCTIONS_MARKER]

// Initialize on page load
window.addEventListener('load', init);
