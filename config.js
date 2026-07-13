// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.43",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 150,
    speedIncrement: 3,
    minSpeed: 60,
    initialLength: 2,

    // Scoring
    pointsPerFood: 10,
    levelUpScore: 60,
    scoreMultiplier: 1.2,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: true,
    showParticles: false,

    // Visual settings
    snakeColor: "#059669",
    snakeHeadColor: "#bbf7d0",
    foodColor: "#fb923c",
    backgroundColor: "#0a0a12",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Master",
    gameSubtitle: "A classic arcade experience",
    gameOverText: "Wasted!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.43",

    // Food glow effect
    foodGlow: true,
    foodGlowIntensity: 15,

    // Rounded snake segments
    roundedSegments: true,
    segmentRadius: 4,

    // Particle effects
    particlesEnabled: true,
    particleCount: 8,
    particleSpeed: 3,

    // [CONFIG_MARKER]
};
