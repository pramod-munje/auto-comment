// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.16",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 140,
    speedIncrement: 3,
    minSpeed: 40,
    initialLength: 2,

    // Scoring
    pointsPerFood: 25,
    levelUpScore: 50,
    scoreMultiplier: 1.5,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: true,
    showParticles: false,

    // Visual settings
    snakeColor: "#00d4aa",
    snakeHeadColor: "#4ade80",
    foodColor: "#eab308",
    backgroundColor: "#0d0d15",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Game",
    gameSubtitle: "Classic arcade reborn",
    gameOverText: "Wasted!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.16",

    // Food glow effect
    foodGlow: true,
    foodGlowIntensity: 15,

    // [CONFIG_MARKER]
};
