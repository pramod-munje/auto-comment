#!/usr/bin/env python3
"""
Snake Game Auto-Improver v2 — Feature Scheduling System
========================================================
Every 5-minute run: 10 commits of small tweaks.
At scheduled milestones: real new features are added to the game.
Features are spread out over hours to look like natural development.
"""

import json
import os
import random
import re
import subprocess
import time
from datetime import datetime, timezone

COMMITS_PER_RUN = 10
DELAY_BETWEEN = 25  # seconds
STATE_FILE = "scripts/state.json"


# =============================================================
# STATE MANAGEMENT
# =============================================================

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"total_runs": 0, "features_applied": [], "tweaks_applied": 0}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def git_commit(msg):
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", msg], check=True)


# =============================================================
# MARKER INSERTION — inserts code BEFORE a marker so it persists
# =============================================================

def insert_before_marker(filepath, marker, code):
    content = read_file(filepath)
    if marker not in content:
        return False
    content = content.replace(marker, code + "\n    " + marker)
    write_file(filepath, content)
    return True


def insert_css_before_marker(filepath, marker, code):
    content = read_file(filepath)
    if marker not in content:
        return False
    content = content.replace(marker, code + "\n\n" + marker)
    write_file(filepath, content)
    return True


def insert_html_before_marker(filepath, marker, code):
    content = read_file(filepath)
    if marker not in content:
        return False
    content = content.replace(marker, code + "\n            " + marker)
    write_file(filepath, content)
    return True


# =============================================================
# FEATURE DEFINITIONS — Real game features added at milestones
# Each feature has: id, schedule_run, steps[]
# Each step has: commit message, list of operations
# =============================================================

def get_features():
    return [
        # ── FEATURE 1: Food Glow Effect (~2 hours, run 24) ──
        {
            "id": "food_glow",
            "schedule_run": 24,
            "steps": [
                {
                    "commit": "feat(food): add glow effect configuration options",
                    "ops": [
                        ("config_marker", "config.js", "// [CONFIG_MARKER]",
                         "// Food glow effect\n    foodGlow: true,\n    foodGlowIntensity: 15,\n"),
                    ]
                },
                {
                    "commit": "feat(food): implement canvas shadow glow on food rendering",
                    "ops": [
                        ("init_marker", "game.js", "// [INIT_MARKER]",
                         "// Override drawFood to add glow effect\n    const _origDrawFood = drawFood;\n    drawFood = function() {\n        if (CONFIG.foodGlow) {\n            ctx.shadowColor = CONFIG.foodColor;\n            ctx.shadowBlur = CONFIG.foodGlowIntensity;\n        }\n        _origDrawFood();\n        ctx.shadowColor = 'transparent';\n        ctx.shadowBlur = 0;\n    };\n"),
                    ]
                },
                {
                    "commit": "docs(changelog): add food glow effect to changelog",
                    "ops": [("changelog", "", "", "Added food glow/shadow effect for better visual feedback")]
                },
            ]
        },

        # ── FEATURE 2: Rounded Snake Segments (~3.5 hours, run 42) ──
        {
            "id": "rounded_snake",
            "schedule_run": 42,
            "steps": [
                {
                    "commit": "feat(snake): add rounded segments config option",
                    "ops": [
                        ("config_marker", "config.js", "// [CONFIG_MARKER]",
                         "// Rounded snake segments\n    roundedSegments: true,\n    segmentRadius: 4,\n"),
                    ]
                },
                {
                    "commit": "feat(snake): implement rounded rectangle rendering for segments",
                    "ops": [
                        ("init_marker", "game.js", "// [INIT_MARKER]",
                         "// Override drawSnake for rounded segments\n    const _origDrawSnake = drawSnake;\n    drawSnake = function() {\n        if (CONFIG.roundedSegments && ctx.roundRect) {\n            const gs = CONFIG.gridSize;\n            snake.forEach((seg, i) => {\n                ctx.fillStyle = i === 0 ? CONFIG.snakeHeadColor : CONFIG.snakeColor;\n                ctx.beginPath();\n                ctx.roundRect(seg.x * gs + 1, seg.y * gs + 1, gs - 2, gs - 2, CONFIG.segmentRadius);\n                ctx.fill();\n            });\n        } else {\n            _origDrawSnake();\n        }\n    };\n"),
                    ]
                },
                {
                    "commit": "docs(changelog): document rounded snake segments feature",
                    "ops": [("changelog", "", "", "Added rounded rectangle rendering for snake segments")]
                },
            ]
        },

        # ── FEATURE 3: Score Popup Animation (~5 hours, run 60) ──
        {
            "id": "score_popup",
            "schedule_run": 60,
            "steps": [
                {
                    "commit": "feat(ui): add score popup state variables",
                    "ops": [
                        ("vars_marker", "game.js", "// [VARS_MARKER]",
                         "// Score popup animation\nlet scorePopups = [];\n"),
                    ]
                },
                {
                    "commit": "feat(ui): implement floating score popup on food eaten",
                    "ops": [
                        ("functions_marker", "game.js", "// [FUNCTIONS_MARKER]",
                         "// Create floating score popup\nfunction createScorePopup(x, y, points) {\n    scorePopups.push({\n        x: x * CONFIG.gridSize + CONFIG.gridSize / 2,\n        y: y * CONFIG.gridSize,\n        text: '+' + points,\n        alpha: 1.0,\n        velocity: -2\n    });\n}\n\n// Draw and update score popups\nfunction drawScorePopups() {\n    scorePopups = scorePopups.filter(p => p.alpha > 0);\n    scorePopups.forEach(p => {\n        ctx.save();\n        ctx.globalAlpha = p.alpha;\n        ctx.fillStyle = CONFIG.accent || '#00d4aa';\n        ctx.font = 'bold 16px Inter, sans-serif';\n        ctx.textAlign = 'center';\n        ctx.fillText(p.text, p.x, p.y);\n        ctx.restore();\n        p.y += p.velocity;\n        p.alpha -= 0.03;\n    });\n}\n"),
                    ]
                },
                {
                    "commit": "feat(ui): trigger popup on food collection and render in game loop",
                    "ops": [
                        ("food_marker", "game.js", "// [FOOD_EATEN_MARKER]",
                         "if (typeof createScorePopup === 'function') {\n            createScorePopup(head.x, head.y, points);\n        }\n"),
                        ("render_marker", "game.js", "// [RENDER_MARKER]",
                         "if (typeof drawScorePopups === 'function') drawScorePopups();\n"),
                    ]
                },
                {
                    "commit": "docs(changelog): document score popup animation feature",
                    "ops": [("changelog", "", "", "Added floating score popup animation when collecting food")]
                },
            ]
        },

        # ── FEATURE 4: Particle Effects (~7 hours, run 84) ──
        {
            "id": "particles",
            "schedule_run": 84,
            "steps": [
                {
                    "commit": "feat(effects): add particle system state and config",
                    "ops": [
                        ("vars_marker", "game.js", "// [VARS_MARKER]",
                         "// Particle system\nlet particles = [];\n"),
                        ("config_marker", "config.js", "// [CONFIG_MARKER]",
                         "// Particle effects\n    particlesEnabled: true,\n    particleCount: 8,\n    particleSpeed: 3,\n"),
                    ]
                },
                {
                    "commit": "feat(effects): implement particle burst and rendering functions",
                    "ops": [
                        ("functions_marker", "game.js", "// [FUNCTIONS_MARKER]",
                         "// Create particle burst at position\nfunction createParticles(x, y, color) {\n    if (!CONFIG.particlesEnabled) return;\n    const count = CONFIG.particleCount || 8;\n    for (let i = 0; i < count; i++) {\n        const angle = (Math.PI * 2 / count) * i;\n        const speed = CONFIG.particleSpeed || 3;\n        particles.push({\n            x: x * CONFIG.gridSize + CONFIG.gridSize / 2,\n            y: y * CONFIG.gridSize + CONFIG.gridSize / 2,\n            vx: Math.cos(angle) * speed * (0.5 + Math.random()),\n            vy: Math.sin(angle) * speed * (0.5 + Math.random()),\n            size: 3 + Math.random() * 3,\n            alpha: 1.0,\n            color: color || CONFIG.foodColor\n        });\n    }\n}\n\n// Update and draw particles\nfunction drawParticles() {\n    particles = particles.filter(p => p.alpha > 0);\n    particles.forEach(p => {\n        ctx.save();\n        ctx.globalAlpha = p.alpha;\n        ctx.fillStyle = p.color;\n        ctx.fillRect(p.x - p.size / 2, p.y - p.size / 2, p.size, p.size);\n        ctx.restore();\n        p.x += p.vx;\n        p.y += p.vy;\n        p.alpha -= 0.04;\n        p.size *= 0.97;\n    });\n}\n"),
                    ]
                },
                {
                    "commit": "feat(effects): trigger particles on food eat and render in loop",
                    "ops": [
                        ("food_marker", "game.js", "// [FOOD_EATEN_MARKER]",
                         "if (typeof createParticles === 'function') {\n            createParticles(head.x, head.y, CONFIG.foodColor);\n        }\n"),
                        ("render_marker", "game.js", "// [RENDER_MARKER]",
                         "if (typeof drawParticles === 'function') drawParticles();\n"),
                    ]
                },
                {
                    "commit": "docs(changelog): document particle effects system",
                    "ops": [("changelog", "", "", "Added particle burst effect when snake eats food")]
                },
            ]
        },

        # ── FEATURE 5: Touch Controls (~9 hours, run 108) ──
        {
            "id": "touch_controls",
            "schedule_run": 108,
            "steps": [
                {
                    "commit": "feat(mobile): add touch swipe detection for mobile controls",
                    "ops": [
                        ("functions_marker", "game.js", "// [FUNCTIONS_MARKER]",
                         "// Touch controls for mobile\nlet touchStartX = 0;\nlet touchStartY = 0;\n\nfunction handleTouchStart(e) {\n    const touch = e.touches[0];\n    touchStartX = touch.clientX;\n    touchStartY = touch.clientY;\n}\n\nfunction handleTouchEnd(e) {\n    if (!isGameStarted) return;\n    const touch = e.changedTouches[0];\n    const dx = touch.clientX - touchStartX;\n    const dy = touch.clientY - touchStartY;\n    const minSwipe = 30;\n    \n    if (Math.abs(dx) > Math.abs(dy)) {\n        if (dx > minSwipe && direction.x === 0) nextDirection = { x: 1, y: 0 };\n        else if (dx < -minSwipe && direction.x === 0) nextDirection = { x: -1, y: 0 };\n    } else {\n        if (dy > minSwipe && direction.y === 0) nextDirection = { x: 0, y: 1 };\n        else if (dy < -minSwipe && direction.y === 0) nextDirection = { x: 0, y: -1 };\n    }\n}\n"),
                    ]
                },
                {
                    "commit": "feat(mobile): register touch event listeners on canvas",
                    "ops": [
                        ("init_marker", "game.js", "// [INIT_MARKER]",
                         "// Set up touch controls\n    canvas.addEventListener('touchstart', handleTouchStart, { passive: true });\n    canvas.addEventListener('touchend', handleTouchEnd, { passive: true });\n"),
                    ]
                },
                {
                    "commit": "ui(mobile): add mobile controls hint text",
                    "ops": [
                        ("html_marker", "index.html", "<!-- [CONTROLS_MARKER] -->",
                         "<p id=\"touch-hint\" style=\"font-size:11px;color:#666;\">📱 Swipe on canvas to control on mobile</p>"),
                    ]
                },
                {
                    "commit": "docs(changelog): document touch/swipe controls for mobile",
                    "ops": [("changelog", "", "", "Added touch swipe controls for mobile gameplay")]
                },
            ]
        },

        # ── FEATURE 6: Speed Display (~12 hours, run 144) ──
        {
            "id": "speed_display",
            "schedule_run": 144,
            "steps": [
                {
                    "commit": "ui(scoreboard): add speed indicator HTML element",
                    "ops": [
                        ("html_marker", "index.html", "<!-- [SCOREBOARD_MARKER] -->",
                         """<div class="score-item">\n                <span class="score-label">Speed</span>\n                <span class="score-value" id="speed-display">1x</span>\n            </div>"""),
                    ]
                },
                {
                    "commit": "feat(ui): update speed display value during gameplay",
                    "ops": [
                        ("functions_marker", "game.js", "// [FUNCTIONS_MARKER]",
                         "// Update speed display\nfunction updateSpeedDisplay() {\n    const speedEl = document.getElementById('speed-display');\n    if (speedEl && gameSpeed) {\n        const ratio = CONFIG.initialSpeed / gameSpeed;\n        speedEl.textContent = ratio.toFixed(1) + 'x';\n    }\n}\n"),
                        ("init_marker", "game.js", "// [INIT_MARKER]",
                         "// Override updateScore to also update speed\n    const _origUpdateScore = updateScore;\n    updateScore = function() {\n        _origUpdateScore();\n        if (typeof updateSpeedDisplay === 'function') updateSpeedDisplay();\n    };\n"),
                    ]
                },
                {
                    "commit": "docs(changelog): document speed indicator in scoreboard",
                    "ops": [("changelog", "", "", "Added real-time speed indicator to the scoreboard")]
                },
            ]
        },

        # ── FEATURE 7: Snake Body Gradient (~15 hours, run 180) ──
        {
            "id": "snake_gradient",
            "schedule_run": 180,
            "steps": [
                {
                    "commit": "feat(snake): add gradient body color configuration",
                    "ops": [
                        ("config_marker", "config.js", "// [CONFIG_MARKER]",
                         "// Snake gradient\n    snakeGradient: true,\n    snakeTailColor: \"#065f46\",\n"),
                    ]
                },
                {
                    "commit": "feat(snake): implement gradient coloring along snake body",
                    "ops": [
                        ("functions_marker", "game.js", "// [FUNCTIONS_MARKER]",
                         "// Interpolate between two hex colors\nfunction lerpColor(a, b, t) {\n    const ah = parseInt(a.replace('#', ''), 16);\n    const bh = parseInt(b.replace('#', ''), 16);\n    const ar = (ah >> 16) & 0xff, ag = (ah >> 8) & 0xff, ab = ah & 0xff;\n    const br = (bh >> 16) & 0xff, bg = (bh >> 8) & 0xff, bb = bh & 0xff;\n    const rr = Math.round(ar + (br - ar) * t);\n    const rg = Math.round(ag + (bg - ag) * t);\n    const rb = Math.round(ab + (bb - ab) * t);\n    return '#' + ((1 << 24) + (rr << 16) + (rg << 8) + rb).toString(16).slice(1);\n}\n"),
                        ("init_marker", "game.js", "// [INIT_MARKER]",
                         "// Override drawSnake for gradient body\n    const _gradDrawSnake = drawSnake;\n    drawSnake = function() {\n        if (CONFIG.snakeGradient && snake.length > 1) {\n            const gs = CONFIG.gridSize;\n            const headColor = CONFIG.snakeHeadColor || '#00ffcc';\n            const tailColor = CONFIG.snakeTailColor || '#065f46';\n            snake.forEach((seg, i) => {\n                const t = i / (snake.length - 1);\n                ctx.fillStyle = i === 0 ? headColor : lerpColor(CONFIG.snakeColor, tailColor, t);\n                if (CONFIG.roundedSegments && ctx.roundRect) {\n                    ctx.beginPath();\n                    ctx.roundRect(seg.x * gs + 1, seg.y * gs + 1, gs - 2, gs - 2, CONFIG.segmentRadius || 4);\n                    ctx.fill();\n                } else {\n                    ctx.fillRect(seg.x * gs + 1, seg.y * gs + 1, gs - 2, gs - 2);\n                }\n            });\n        } else {\n            _gradDrawSnake();\n        }\n    };\n"),
                    ]
                },
                {
                    "commit": "docs(changelog): document snake body gradient feature",
                    "ops": [("changelog", "", "", "Added gradient color effect along the snake body")]
                },
            ]
        },

        # ── FEATURE 8: Screen Shake on Death (~18 hours, run 216) ──
        {
            "id": "screen_shake",
            "schedule_run": 216,
            "steps": [
                {
                    "commit": "feat(effects): add screen shake configuration",
                    "ops": [
                        ("config_marker", "config.js", "// [CONFIG_MARKER]",
                         "// Screen shake on death\n    screenShake: true,\n    shakeIntensity: 5,\n    shakeDuration: 300,\n"),
                    ]
                },
                {
                    "commit": "feat(effects): implement screen shake animation function",
                    "ops": [
                        ("functions_marker", "game.js", "// [FUNCTIONS_MARKER]",
                         "// Screen shake effect\nfunction triggerScreenShake() {\n    if (!CONFIG.screenShake) return;\n    const wrapper = document.querySelector('.game-wrapper');\n    if (!wrapper) return;\n    const intensity = CONFIG.shakeIntensity || 5;\n    const duration = CONFIG.shakeDuration || 300;\n    const start = Date.now();\n    function shakeFrame() {\n        const elapsed = Date.now() - start;\n        if (elapsed < duration) {\n            const decay = 1 - elapsed / duration;\n            const dx = (Math.random() - 0.5) * intensity * 2 * decay;\n            const dy = (Math.random() - 0.5) * intensity * 2 * decay;\n            wrapper.style.transform = 'translate(' + dx + 'px, ' + dy + 'px)';\n            requestAnimationFrame(shakeFrame);\n        } else {\n            wrapper.style.transform = '';\n        }\n    }\n    shakeFrame();\n}\n"),
                    ]
                },
                {
                    "commit": "feat(effects): trigger screen shake on game over",
                    "ops": [
                        ("gameover_marker", "game.js", "// [GAME_OVER_MARKER]",
                         "if (typeof triggerScreenShake === 'function') triggerScreenShake();\n"),
                    ]
                },
                {
                    "commit": "docs(changelog): document screen shake on death effect",
                    "ops": [("changelog", "", "", "Added screen shake effect when snake crashes")]
                },
            ]
        },
    ]


# =============================================================
# SMALL TWEAKS — Config/CSS/text changes between features
# =============================================================

def get_small_tweaks():
    return [
        {
            "file": "config.js",
            "find": r'pointsPerFood: \d+',
            "replace_fn": lambda m: f'pointsPerFood: {random.choice([10, 15, 20, 25])}',
            "commit": "feat(scoring): adjust base points per food pickup"
        },
        {
            "file": "config.js",
            "find": r'initialSpeed: \d+',
            "replace_fn": lambda m: f'initialSpeed: {random.choice([120, 130, 140, 150, 160])}',
            "commit": "perf(gameplay): tune initial snake speed for better feel"
        },
        {
            "file": "config.js",
            "find": r'speedIncrement: \d+',
            "replace_fn": lambda m: f'speedIncrement: {random.choice([3, 4, 5, 7, 8])}',
            "commit": "balance(difficulty): adjust speed increment per level"
        },
        {
            "file": "config.js",
            "find": r'minSpeed: \d+',
            "replace_fn": lambda m: f'minSpeed: {random.choice([40, 45, 50, 55, 60])}',
            "commit": "balance(difficulty): update minimum speed cap"
        },
        {
            "file": "config.js",
            "find": r'levelUpScore: \d+',
            "replace_fn": lambda m: f'levelUpScore: {random.choice([40, 50, 60, 75, 100])}',
            "commit": "balance(progression): modify level-up score threshold"
        },
        {
            "file": "config.js",
            "find": r'scoreMultiplier: [\d.]+',
            "replace_fn": lambda m: f'scoreMultiplier: {random.choice(["1.0", "1.1", "1.2", "1.25", "1.5"])}',
            "commit": "feat(scoring): update score multiplier"
        },
        {
            "file": "config.js",
            "find": r'showGrid: (true|false)',
            "replace_fn": lambda m: f'showGrid: {"false" if m.group(1) == "true" else "true"}',
            "commit": "ui(canvas): toggle grid overlay visibility"
        },
        {
            "file": "config.js",
            "find": r'snakeColor: "#[0-9a-fA-F]+"',
            "replace_fn": lambda m: f'snakeColor: "{random.choice(["#00d4aa", "#4ade80", "#22c55e", "#10b981", "#34d399", "#6ee7b7", "#059669"])}"',
            "commit": "style(snake): update snake body color"
        },
        {
            "file": "config.js",
            "find": r'snakeHeadColor: "#[0-9a-fA-F]+"',
            "replace_fn": lambda m: f'snakeHeadColor: "{random.choice(["#00ffcc", "#86efac", "#4ade80", "#a7f3d0", "#bbf7d0"])}"',
            "commit": "style(snake): refine head color"
        },
        {
            "file": "config.js",
            "find": r'foodColor: "#[0-9a-fA-F]+"',
            "replace_fn": lambda m: f'foodColor: "{random.choice(["#ef4444", "#f97316", "#eab308", "#f43f5e", "#fb923c", "#fbbf24"])}"',
            "commit": "style(food): update food color for visibility"
        },
        {
            "file": "config.js",
            "find": r'backgroundColor: "#[0-9a-fA-F]+"',
            "replace_fn": lambda m: f'backgroundColor: "{random.choice(["#0d0d15", "#0a0a12", "#0f0f1a", "#111118", "#0c0c14"])}"',
            "commit": "style(canvas): adjust background shade"
        },
        {
            "file": "config.js",
            "find": r'initialLength: \d+',
            "replace_fn": lambda m: f'initialLength: {random.choice([2, 3, 4, 5])}',
            "commit": "balance(snake): adjust initial snake length"
        },
        {
            "file": "config.js",
            "find": r'gameTitle: "[^"]+"',
            "replace_fn": lambda m: f'gameTitle: "{random.choice(["🐍 Snake Game", "🐍 Snake Arcade", "🐍 Snake Challenge", "🐍 Snake Master", "🐍 Neon Snake"])}"',
            "commit": "ui(header): update game title"
        },
        {
            "file": "config.js",
            "find": r'gameSubtitle: "[^"]+"',
            "replace_fn": lambda m: f'gameSubtitle: "{random.choice(["A classic arcade experience", "The ultimate snake challenge", "Eat, grow, survive", "How long can you last?", "Classic arcade reborn"])}"',
            "commit": "ui(header): refresh subtitle text"
        },
        {
            "file": "config.js",
            "find": r'gameOverText: "[^"]+"',
            "replace_fn": lambda m: f'gameOverText: "{random.choice(["Game Over!", "You Crashed!", "Wasted!", "Better Luck Next Time!", "Try Again!"])}"',
            "commit": "ui(gameover): update game over text"
        },
        {
            "file": "style.css",
            "find": r'--accent-primary: #[0-9a-fA-F]+;',
            "replace_fn": lambda m: f'--accent-primary: {random.choice(["#00d4aa", "#06b6d4", "#8b5cf6", "#3b82f6", "#14b8a6", "#10b981"])};',
            "commit": "style(theme): update primary accent color"
        },
        {
            "file": "style.css",
            "find": r'--accent-secondary: #[0-9a-fA-F]+;',
            "replace_fn": lambda m: f'--accent-secondary: {random.choice(["#7c3aed", "#a855f7", "#ec4899", "#f43f5e", "#6366f1"])};',
            "commit": "style(theme): update secondary accent color"
        },
        {
            "file": "style.css",
            "find": r'--border-radius: \d+px;',
            "replace_fn": lambda m: f'--border-radius: {random.choice([8, 10, 12, 14, 16])}px;',
            "commit": "style(layout): adjust border radius"
        },
        {
            "file": "style.css",
            "find": r'--bg-primary: #[0-9a-fA-F]+;',
            "replace_fn": lambda m: f'--bg-primary: {random.choice(["#0a0a0f", "#09090b", "#0c0c12", "#0b0b10", "#080810"])};',
            "commit": "style(theme): adjust background shade"
        },
        {
            "file": "style.css",
            "find": r'--bg-card: #[0-9a-fA-F]+;',
            "replace_fn": lambda m: f'--bg-card: {random.choice(["#1a1a2e", "#1e1e30", "#1c1c28", "#18182a", "#1f1f2f"])};',
            "commit": "style(theme): refine card background"
        },
        {
            "file": "style.css",
            "find": r'--border-color: #[0-9a-fA-F]+;',
            "replace_fn": lambda m: f'--border-color: {random.choice(["#2a2a3e", "#2c2c40", "#282838", "#262636", "#303044"])};',
            "commit": "style(theme): adjust border color"
        },
        {
            "file": "style.css",
            "find": r'--shadow-glow: 0 0 \d+px',
            "replace_fn": lambda m: f'--shadow-glow: 0 0 {random.choice([15, 20, 25, 30])}px',
            "commit": "style(effects): adjust glow intensity"
        },
        {
            "file": "config.js",
            "find": r'version: "(\d+)\.(\d+)\.(\d+)"',
            "replace_fn": lambda m: f'version: "{m.group(1)}.{m.group(2)}.{int(m.group(3)) + 1}"',
            "commit": "chore(version): bump patch version"
        },
    ]


# =============================================================
# APPLY LOGIC
# =============================================================

def apply_feature_step(step):
    """Apply all operations in a feature step."""
    for op in step["ops"]:
        op_type = op[0]

        if op_type == "changelog":
            add_changelog_entry(op[3])
        elif op_type in ("config_marker", "vars_marker", "init_marker",
                         "food_marker", "render_marker", "gameover_marker",
                         "functions_marker", "start_marker"):
            marker_map = {
                "config_marker": "// [CONFIG_MARKER]",
                "vars_marker": "// [VARS_MARKER]",
                "init_marker": "// [INIT_MARKER]",
                "food_marker": "// [FOOD_EATEN_MARKER]",
                "render_marker": "// [RENDER_MARKER]",
                "gameover_marker": "// [GAME_OVER_MARKER]",
                "functions_marker": "// [FUNCTIONS_MARKER]",
                "start_marker": "// [START_MARKER]",
            }
            filepath = op[1]
            marker = marker_map.get(op_type, op[2])
            code = op[3]
            content = read_file(filepath)
            if marker in content:
                content = content.replace(marker, code + "\n    " + marker)
                write_file(filepath, content)
        elif op_type == "html_marker":
            filepath = op[1]
            marker = op[2]
            code = op[3]
            insert_html_before_marker(filepath, marker, code)
        elif op_type == "css_marker":
            filepath = op[1]
            marker = op[2]
            code = op[3]
            insert_css_before_marker(filepath, marker, code)


def add_changelog_entry(description):
    """Add a changelog entry."""
    filepath = "CHANGELOG.md"
    content = read_file(filepath)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    entry = f"\n## [{timestamp}]\n\n### Added\n- {description}\n"
    anchor = "All notable changes to this Snake Game project will be documented in this file."
    content = content.replace(anchor, anchor + entry)
    write_file(filepath, content)


def apply_small_tweak(tweak):
    """Apply a single small tweak."""
    filepath = tweak["file"]
    if not os.path.exists(filepath):
        return False

    content = read_file(filepath)
    match = re.search(tweak["find"], content, re.DOTALL)

    if not match:
        return False

    new_value = tweak["replace_fn"](match)
    if match.group(0) == new_value:
        return False

    content = content[:match.start()] + new_value + content[match.end():]
    write_file(filepath, content)
    return True


def get_version():
    content = read_file("config.js")
    match = re.search(r'version: "([^"]+)"', content)
    return match.group(1) if match else "1.0.0"


def update_version_references(new_version):
    html = read_file("index.html")
    html = re.sub(r'Snake Game — v[\d.]+', f'Snake Game — v{new_version}', html)
    write_file("index.html", html)

    config = read_file("config.js")
    config = re.sub(r'footerText: "[^"]+"',
                    f'footerText: "Built with ❤️ | Version {new_version}"', config)
    write_file("config.js", config)


# =============================================================
# MAIN
# =============================================================

def main():
    state = load_state()
    state["total_runs"] += 1
    run = state["total_runs"]

    print(f"🎮 Snake Game Auto-Improver v2 — Run #{run}")
    print(f"📊 Will generate {COMMITS_PER_RUN} commits this run\n")

    commits_made = 0
    features = get_features()

    # Check if a feature is due this run
    pending_feature = None
    for feat in features:
        if feat["id"] not in state["features_applied"] and run >= feat["schedule_run"]:
            pending_feature = feat
            break

    # If feature is due, apply its steps first
    if pending_feature:
        print(f"🚀 NEW FEATURE: {pending_feature['id']} (scheduled at run {pending_feature['schedule_run']})")
        for step in pending_feature["steps"]:
            if commits_made >= COMMITS_PER_RUN:
                break
            try:
                apply_feature_step(step)
                git_commit(step["commit"])
                commits_made += 1
                print(f"  ✅ [{commits_made}/{COMMITS_PER_RUN}] {step['commit']}")
                if commits_made < COMMITS_PER_RUN:
                    time.sleep(DELAY_BETWEEN)
            except Exception as e:
                print(f"  ⚠️ Step failed: {e}")

        state["features_applied"].append(pending_feature["id"])
        print(f"  🎉 Feature '{pending_feature['id']}' fully applied!\n")

    # Fill remaining commits with small tweaks
    tweaks = get_small_tweaks()
    random.shuffle(tweaks)
    used = set()

    while commits_made < COMMITS_PER_RUN:
        applied = False
        for tweak in tweaks:
            if tweak["commit"] in used:
                continue
            try:
                if apply_small_tweak(tweak):
                    used.add(tweak["commit"])

                    if "version" in tweak["commit"].lower():
                        new_ver = get_version()
                        update_version_references(new_ver)

                    git_commit(tweak["commit"])
                    commits_made += 1
                    applied = True
                    print(f"  ✅ [{commits_made}/{COMMITS_PER_RUN}] {tweak['commit']}")
                    if commits_made < COMMITS_PER_RUN:
                        time.sleep(DELAY_BETWEEN)
                    break
            except Exception as e:
                print(f"  ⚠️ Tweak failed: {e}")

        if not applied:
            # Fallback version bump
            try:
                config = read_file("config.js")
                match = re.search(r'version: "(\d+)\.(\d+)\.(\d+)"', config)
                if match:
                    new_patch = int(match.group(3)) + 1
                    new_ver = f"{match.group(1)}.{match.group(2)}.{new_patch}"
                    config = config.replace(match.group(0), f'version: "{new_ver}"')
                    write_file("config.js", config)
                    update_version_references(new_ver)
                    git_commit(f"chore: bump version to {new_ver}")
                    commits_made += 1
                    print(f"  ✅ [{commits_made}/{COMMITS_PER_RUN}] chore: bump to {new_ver}")
                    if commits_made < COMMITS_PER_RUN:
                        time.sleep(DELAY_BETWEEN)
            except Exception as e:
                print(f"  ❌ Fallback failed: {e}")
                break

    save_state(state)

    # Summary
    applied_features = state["features_applied"]
    next_feat = None
    for feat in features:
        if feat["id"] not in applied_features:
            next_feat = feat
            break

    print(f"\n{'='*50}")
    print(f"✅ Run #{run} complete — {commits_made} commits made")
    print(f"📦 Features applied so far: {len(applied_features)}/{len(features)}")
    if next_feat:
        runs_left = next_feat["schedule_run"] - run
        mins_left = max(0, runs_left * 5)
        print(f"⏳ Next feature '{next_feat['id']}' in ~{mins_left} min (run {next_feat['schedule_run']})")
    else:
        print("🏁 All features have been applied!")


if __name__ == "__main__":
    main()
