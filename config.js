// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.18",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 130,
    speedIncrement: 7,
    minSpeed: 60,
    initialLength: 4,

    // Scoring
    pointsPerFood: 10,
    levelUpScore: 40,
    scoreMultiplier: 1.0,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: true,
    showParticles: false,

    // Visual settings
    snakeColor: "#6ee7b7",
    snakeHeadColor: "#4ade80",
    foodColor: "#fbbf24",
    backgroundColor: "#0f0f1a",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Arcade",
    gameSubtitle: "How long can you last?",
    gameOverText: "Game Over!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.18",

    // Food glow effect
    foodGlow: true,
    foodGlowIntensity: 15,

    // [CONFIG_MARKER]
};
