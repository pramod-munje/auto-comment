// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.2",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 130,
    speedIncrement: 7,
    minSpeed: 60,
    initialLength: 3,

    // Scoring
    pointsPerFood: 10,
    levelUpScore: 40,
    scoreMultiplier: 1.1,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: true,
    showParticles: false,

    // Visual settings
    snakeColor: "#10b981",
    snakeHeadColor: "#a7f3d0",
    foodColor: "#fbbf24",
    backgroundColor: "#0d0d15",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Neon Snake",
    gameSubtitle: "How long can you last?",
    gameOverText: "You Crashed!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.2",

    // [CONFIG_MARKER]
};
