// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.55",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 130,
    speedIncrement: 7,
    minSpeed: 50,
    initialLength: 3,

    // Scoring
    pointsPerFood: 15,
    levelUpScore: 100,
    scoreMultiplier: 1.5,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: false,
    showParticles: false,

    // Visual settings
    snakeColor: "#059669",
    snakeHeadColor: "#a7f3d0",
    foodColor: "#ef4444",
    backgroundColor: "#0d0d15",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Challenge",
    gameSubtitle: "A classic arcade experience",
    gameOverText: "Wasted!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.55",

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
