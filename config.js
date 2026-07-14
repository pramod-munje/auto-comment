// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.51",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 130,
    speedIncrement: 8,
    minSpeed: 55,
    initialLength: 4,

    // Scoring
    pointsPerFood: 15,
    levelUpScore: 50,
    scoreMultiplier: 1.5,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: true,
    showParticles: false,

    // Visual settings
    snakeColor: "#6ee7b7",
    snakeHeadColor: "#4ade80",
    foodColor: "#fb923c",
    backgroundColor: "#0d0d15",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Arcade",
    gameSubtitle: "Classic arcade reborn",
    gameOverText: "Wasted!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.51",

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
