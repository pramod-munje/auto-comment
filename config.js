// Game Configuration — v1.0.0
// This file contains all tunable game parameters

const CONFIG = {
    // Version
    version: "1.0.107",

    // Canvas settings
    canvasWidth: 400,
    canvasHeight: 400,
    gridSize: 20,

    // Snake settings
    initialSpeed: 160,
    speedIncrement: 4,
    minSpeed: 60,
    initialLength: 4,

    // Scoring
    pointsPerFood: 10,
    levelUpScore: 40,
    scoreMultiplier: 1.5,

    // Game behavior
    wallCollision: true,
    selfCollision: true,
    showGrid: true,
    showParticles: false,

    // Visual settings
    snakeColor: "#059669",
    snakeHeadColor: "#86efac",
    foodColor: "#fb923c",
    backgroundColor: "#0a0a12",
    gridColor: "#15151f",

    // UI text
    gameTitle: "🐍 Snake Challenge",
    gameSubtitle: "Eat, grow, survive",
    gameOverText: "You Crashed!",
    startButtonText: "Start Game",
    pauseButtonText: "Pause",
    resumeButtonText: "Resume",
    instructionsText: "Use arrow keys or WASD to move",
    footerText: "Built with ❤️ | Version 1.0.107",

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
