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
    initialSpeed: 140,
    speedIncrement: 5,
    minSpeed: 55,
    initialLength: 2,

    // Scoring
    pointsPerFood: 15,
    levelUpScore: 40,
    scoreMultiplier: 1.5,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: false,
    showParticles: false,

    // Visual settings
    snakeColor: "#10b981",
    snakeHeadColor: "#86efac",
    foodColor: "#fb923c",
    backgroundColor: "#111118",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Challenge",
    gameSubtitle: "Classic arcade reborn",
    gameOverText: "Better Luck Next Time!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.6",

    // [CONFIG_MARKER]
};
