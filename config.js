// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.6",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 120,
    speedIncrement: 5,
    minSpeed: 45,
    initialLength: 4,

    // Scoring
    pointsPerFood: 20,
    levelUpScore: 60,
    scoreMultiplier: 1.1,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: true,
    showParticles: false,

    // Visual settings
    snakeColor: "#34d399",
    snakeHeadColor: "#86efac",
    foodColor: "#fb923c",
    backgroundColor: "#0c0c14",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Master",
    gameSubtitle: "The ultimate snake challenge",
    gameOverText: "Try Again!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.6",

    // [CONFIG_MARKER]
};
