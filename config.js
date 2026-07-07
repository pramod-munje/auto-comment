// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.11",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 120,
    speedIncrement: 8,
    minSpeed: 40,
    initialLength: 5,

    // Scoring
    pointsPerFood: 20,
    levelUpScore: 60,
    scoreMultiplier: 1.1,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: false,
    showParticles: false,

    // Visual settings
    snakeColor: "#6ee7b7",
    snakeHeadColor: "#a7f3d0",
    foodColor: "#fb923c",
    backgroundColor: "#0f0f1a",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Game",
    gameSubtitle: "The ultimate snake challenge",
    gameOverText: "You Crashed!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.11",

    // [CONFIG_MARKER]
};
