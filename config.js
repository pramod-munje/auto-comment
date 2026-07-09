// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.19",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 130,
    speedIncrement: 3,
    minSpeed: 45,
    initialLength: 2,

    // Scoring
    pointsPerFood: 25,
    levelUpScore: 75,
    scoreMultiplier: 1.0,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: false,
    showParticles: false,

    // Visual settings
    snakeColor: "#6ee7b7",
    snakeHeadColor: "#4ade80",
    foodColor: "#fbbf24",
    backgroundColor: "#111118",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Arcade",
    gameSubtitle: "A classic arcade experience",
    gameOverText: "Try Again!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.19",

    // Food glow effect
    foodGlow: true,
    foodGlowIntensity: 15,

    // [CONFIG_MARKER]
};
