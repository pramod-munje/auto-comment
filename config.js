// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.50",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 140,
    speedIncrement: 5,
    minSpeed: 45,
    initialLength: 4,

    // Scoring
    pointsPerFood: 25,
    levelUpScore: 50,
    scoreMultiplier: 1.0,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: false,
    showParticles: false,

    // Visual settings
    snakeColor: "#10b981",
    snakeHeadColor: "#bbf7d0",
    foodColor: "#fb923c",
    backgroundColor: "#0f0f1a",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Arcade",
    gameSubtitle: "The ultimate snake challenge",
    gameOverText: "Try Again!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.50",

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
