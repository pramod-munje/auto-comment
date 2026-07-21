// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.105",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 150,
    speedIncrement: 5,
    minSpeed: 40,
    initialLength: 2,

    // Scoring
    pointsPerFood: 10,
    levelUpScore: 100,
    scoreMultiplier: 1.2,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: false,
    showParticles: false,

    // Visual settings
    snakeColor: "#00d4aa",
    snakeHeadColor: "#a7f3d0",
    foodColor: "#f97316",
    backgroundColor: "#0c0c14",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Neon Snake",
    gameSubtitle: "Classic arcade reborn",
    gameOverText: "Try Again!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.105",

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

    // Snake gradient
    snakeGradient: true,
    snakeTailColor: "#065f46",

    // Screen shake on death
    screenShake: true,
    shakeIntensity: 5,
    shakeDuration: 300,

    // [CONFIG_MARKER]
};
