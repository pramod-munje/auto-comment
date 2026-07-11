// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.31",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 130,
    speedIncrement: 5,
    minSpeed: 45,
    initialLength: 2,

    // Scoring
    pointsPerFood: 25,
    levelUpScore: 50,
    scoreMultiplier: 1.5,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: false,
    showParticles: false,

    // Visual settings
    snakeColor: "#6ee7b7",
    snakeHeadColor: "#86efac",
    foodColor: "#fb923c",
    backgroundColor: "#0a0a12",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Game",
    gameSubtitle: "Eat, grow, survive",
    gameOverText: "Game Over!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.31",

    // Food glow effect
    foodGlow: true,
    foodGlowIntensity: 15,

    // Rounded snake segments
    roundedSegments: true,
    segmentRadius: 4,

    // [CONFIG_MARKER]
};
