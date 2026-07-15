// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.58",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 140,
    speedIncrement: 8,
    minSpeed: 40,
    initialLength: 4,

    // Scoring
    pointsPerFood: 15,
    levelUpScore: 100,
    scoreMultiplier: 1.2,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: true,
    showParticles: false,

    // Visual settings
    snakeColor: "#4ade80",
    snakeHeadColor: "#bbf7d0",
    foodColor: "#fbbf24",
    backgroundColor: "#0c0c14",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Neon Snake",
    gameSubtitle: "A classic arcade experience",
    gameOverText: "You Crashed!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.58",

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
