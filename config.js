// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.37",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 150,
    speedIncrement: 4,
    minSpeed: 45,
    initialLength: 2,

    // Scoring
    pointsPerFood: 15,
    levelUpScore: 50,
    scoreMultiplier: 1.2,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: true,
    showParticles: false,

    // Visual settings
    snakeColor: "#00d4aa",
    snakeHeadColor: "#bbf7d0",
    foodColor: "#fb923c",
    backgroundColor: "#0f0f1a",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Challenge",
    gameSubtitle: "How long can you last?",
    gameOverText: "Wasted!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.37",

    // Food glow effect
    foodGlow: true,
    foodGlowIntensity: 15,

    // Rounded snake segments
    roundedSegments: true,
    segmentRadius: 4,

    // [CONFIG_MARKER]
};
