// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.26",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 130,
    speedIncrement: 3,
    minSpeed: 60,
    initialLength: 5,

    // Scoring
    pointsPerFood: 15,
    levelUpScore: 75,
    scoreMultiplier: 1.5,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: true,
    showParticles: false,

    // Visual settings
    snakeColor: "#4ade80",
    snakeHeadColor: "#86efac",
    foodColor: "#f97316",
    backgroundColor: "#0c0c14",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Challenge",
    gameSubtitle: "The ultimate snake challenge",
    gameOverText: "Better Luck Next Time!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.26",

    // Food glow effect
    foodGlow: true,
    foodGlowIntensity: 15,

    // Rounded snake segments
    roundedSegments: true,
    segmentRadius: 4,

    // [CONFIG_MARKER]
};
