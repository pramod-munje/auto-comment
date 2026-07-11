// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.27",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 130,
    speedIncrement: 8,
    minSpeed: 60,
    initialLength: 3,

    // Scoring
    pointsPerFood: 25,
    levelUpScore: 75,
    scoreMultiplier: 1.5,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: true,
    showParticles: false,

    // Visual settings
    snakeColor: "#22c55e",
    snakeHeadColor: "#a7f3d0",
    foodColor: "#f97316",
    backgroundColor: "#0a0a12",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Master",
    gameSubtitle: "The ultimate snake challenge",
    gameOverText: "You Crashed!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.27",

    // Food glow effect
    foodGlow: true,
    foodGlowIntensity: 15,

    // Rounded snake segments
    roundedSegments: true,
    segmentRadius: 4,

    // [CONFIG_MARKER]
};
