// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.13",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 130,
    speedIncrement: 4,
    minSpeed: 50,
    initialLength: 5,

    // Scoring
    pointsPerFood: 20,
    levelUpScore: 75,
    scoreMultiplier: 1.25,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: false,
    showParticles: false,

    // Visual settings
    snakeColor: "#6ee7b7",
    snakeHeadColor: "#4ade80",
    foodColor: "#ef4444",
    backgroundColor: "#0c0c14",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Arcade",
    gameSubtitle: "A classic arcade experience",
    gameOverText: "Wasted!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.13",

    // Food glow effect
    foodGlow: true,
    foodGlowIntensity: 15,

    // [CONFIG_MARKER]
};
