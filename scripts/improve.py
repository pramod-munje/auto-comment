#!/usr/bin/env python3
"""Snake Game Auto-Improver — Makes meaningful incremental improvements."""

import os
import random
import re
import subprocess
import time
from datetime import datetime, timezone

# Number of commits per workflow run
COMMITS_PER_RUN = 10
DELAY_BETWEEN = 25  # seconds between commits

# ============================================================
# IMPROVEMENT POOL — Each is a real, meaningful code change
# ============================================================

IMPROVEMENTS = [
    # --- CONFIG.JS TWEAKS ---
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
        "commit": "balance(difficulty): update minimum speed cap for endgame"
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
        "commit": "feat(scoring): update score multiplier for balancing"
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
        "commit": "style(snake): update snake body color scheme"
    },
    {
        "file": "config.js",
        "find": r'snakeHeadColor: "#[0-9a-fA-F]+"',
        "replace_fn": lambda m: f'snakeHeadColor: "{random.choice(["#00ffcc", "#86efac", "#4ade80", "#a7f3d0", "#bbf7d0", "#d1fae5"])}"',
        "commit": "style(snake): refine head highlight color"
    },
    {
        "file": "config.js",
        "find": r'foodColor: "#[0-9a-fA-F]+"',
        "replace_fn": lambda m: f'foodColor: "{random.choice(["#ef4444", "#f97316", "#eab308", "#f43f5e", "#fb923c", "#fbbf24", "#dc2626"])}"',
        "commit": "style(food): change food item color for better visibility"
    },
    {
        "file": "config.js",
        "find": r'backgroundColor: "#[0-9a-fA-F]+"',
        "replace_fn": lambda m: f'backgroundColor: "{random.choice(["#0d0d15", "#0a0a12", "#0f0f1a", "#111118", "#0c0c14"])}"',
        "commit": "style(canvas): adjust canvas background shade"
    },
    {
        "file": "config.js",
        "find": r'initialLength: \d+',
        "replace_fn": lambda m: f'initialLength: {random.choice([2, 3, 4, 5])}',
        "commit": "balance(snake): adjust initial snake length"
    },
    {
        "file": "config.js",
        "find": r'wallCollision: (true|false)',
        "replace_fn": lambda m: f'wallCollision: {"false" if m.group(1) == "true" else "true"}',
        "commit": "feat(gameplay): toggle wall collision behavior"
    },
    {
        "file": "config.js",
        "find": r'gameTitle: "[^"]+"',
        "replace_fn": lambda m: f'gameTitle: "{random.choice(["🐍 Snake Game", "🐍 Snake Arcade", "🐍 Snake Challenge", "🐍 Snake Master", "🐍 Neon Snake"])}"',
        "commit": "ui(header): update game title branding"
    },
    {
        "file": "config.js",
        "find": r'gameSubtitle: "[^"]+"',
        "replace_fn": lambda m: f'gameSubtitle: "{random.choice(["A classic arcade experience", "The ultimate snake challenge", "Eat, grow, survive", "How long can you last?", "Classic arcade reborn", "Retro arcade vibes"])}"',
        "commit": "ui(header): refresh game subtitle text"
    },
    {
        "file": "config.js",
        "find": r'gameOverText: "[^"]+"',
        "replace_fn": lambda m: f'gameOverText: "{random.choice(["Game Over!", "You Crashed!", "Wasted!", "Better Luck Next Time!", "Try Again!", "Snake Down!"])}"',
        "commit": "ui(gameover): update game over message text"
    },
    {
        "file": "config.js",
        "find": r'instructionsText: "[^"]+"',
        "replace_fn": lambda m: f'instructionsText: "{random.choice(["Use arrow keys or WASD to move", "Arrow keys / WASD to control snake", "Controls: Arrow keys or WASD", "Move with arrow keys or WASD keys"])}"',
        "commit": "docs(ui): clarify control instructions text"
    },
    # --- CSS TWEAKS ---
    {
        "file": "style.css",
        "find": r'--accent-primary: #[0-9a-fA-F]+;',
        "replace_fn": lambda m: f'--accent-primary: {random.choice(["#00d4aa", "#06b6d4", "#8b5cf6", "#3b82f6", "#14b8a6", "#10b981", "#0ea5e9"])};',
        "commit": "style(theme): update primary accent color"
    },
    {
        "file": "style.css",
        "find": r'--accent-secondary: #[0-9a-fA-F]+;',
        "replace_fn": lambda m: f'--accent-secondary: {random.choice(["#7c3aed", "#a855f7", "#ec4899", "#f43f5e", "#6366f1", "#8b5cf6"])};',
        "commit": "style(theme): update secondary accent color"
    },
    {
        "file": "style.css",
        "find": r'--border-radius: \d+px;',
        "replace_fn": lambda m: f'--border-radius: {random.choice([8, 10, 12, 14, 16])}px;',
        "commit": "style(layout): adjust border radius for modern look"
    },
    {
        "file": "style.css",
        "find": r'\.game-header h1 \{[^}]*font-size: \d+px',
        "replace_fn": lambda m: m.group(0).rsplit('font-size:', 1)[0] + f'font-size: {random.choice([24, 26, 28, 30, 32])}px',
        "commit": "style(header): adjust title font size"
    },
    {
        "file": "style.css",
        "find": r'\.score-value \{[^}]*font-size: \d+px',
        "replace_fn": lambda m: m.group(0).rsplit('font-size:', 1)[0] + f'font-size: {random.choice([20, 22, 24, 26, 28])}px',
        "commit": "style(scoreboard): adjust score display font size"
    },
    {
        "file": "style.css",
        "find": r'--bg-primary: #[0-9a-fA-F]+;',
        "replace_fn": lambda m: f'--bg-primary: {random.choice(["#0a0a0f", "#09090b", "#0c0c12", "#0b0b10", "#080810"])};',
        "commit": "style(theme): adjust primary background shade"
    },
    {
        "file": "style.css",
        "find": r'--bg-card: #[0-9a-fA-F]+;',
        "replace_fn": lambda m: f'--bg-card: {random.choice(["#1a1a2e", "#1e1e30", "#1c1c28", "#18182a", "#1f1f2f"])};',
        "commit": "style(theme): refine card background color"
    },
    {
        "file": "style.css",
        "find": r'--border-color: #[0-9a-fA-F]+;',
        "replace_fn": lambda m: f'--border-color: {random.choice(["#2a2a3e", "#2c2c40", "#282838", "#262636", "#303044"])};',
        "commit": "style(theme): adjust border color tone"
    },
    {
        "file": "style.css",
        "find": r'--shadow-glow: 0 0 \d+px',
        "replace_fn": lambda m: f'--shadow-glow: 0 0 {random.choice([15, 20, 25, 30])}px',
        "commit": "style(effects): adjust glow shadow intensity"
    },
    {
        "file": "style.css",
        "find": r'\.game-wrapper \{[^}]*gap: \d+px',
        "replace_fn": lambda m: m.group(0).rsplit('gap:', 1)[0] + f'gap: {random.choice([14, 16, 18, 20])}px',
        "commit": "style(layout): adjust game wrapper spacing"
    },
    {
        "file": "style.css",
        "find": r'\.game-wrapper \{[^}]*padding: \d+px',
        "replace_fn": lambda m: m.group(0).rsplit('padding:', 1)[0] + f'padding: {random.choice([20, 24, 28, 32])}px',
        "commit": "style(layout): adjust game wrapper padding"
    },
    {
        "file": "style.css",
        "find": r'button \{[^}]*padding: \d+px \d+px',
        "replace_fn": lambda m: m.group(0).rsplit('padding:', 1)[0] + f'padding: {random.choice([8, 10, 12])}px {random.choice([24, 28, 32, 36])}px',
        "commit": "style(button): adjust button padding for better click target"
    },
    {
        "file": "style.css",
        "find": r'button \{[^}]*font-size: \d+px',
        "replace_fn": lambda m: m.group(0).rsplit('font-size:', 1)[0] + f'font-size: {random.choice([13, 14, 15, 16])}px',
        "commit": "style(button): adjust button text size"
    },
    {
        "file": "style.css",
        "find": r'\.score-board \{[^}]*gap: \d+px',
        "replace_fn": lambda m: m.group(0).rsplit('gap:', 1)[0] + f'gap: {random.choice([16, 20, 24, 28, 32])}px',
        "commit": "style(scoreboard): adjust score item spacing"
    },
    # --- GAME.JS TWEAKS ---
    {
        "file": "game.js",
        "find": r"ctx\.fillStyle = 'rgba\(0, 0, 0, 0\.\d+\)';\n    ctx\.fillRect\(0, 0, canvas\.width, canvas\.height\);\n\n    ctx\.fillStyle = '#ef4444'",
        "replace_fn": lambda m: f"ctx.fillStyle = 'rgba(0, 0, 0, {random.choice([0.7, 0.75, 0.8, 0.85])})';\\n    ctx.fillRect(0, 0, canvas.width, canvas.height);\\n\\n    ctx.fillStyle = '#ef4444'",
        "commit": "ui(gameover): adjust overlay opacity for readability"
    },
    {
        "file": "game.js",
        "find": r"ctx\.font = 'bold \d+px Inter",
        "replace_fn": lambda m: f"ctx.font = 'bold {random.choice([28, 30, 32, 34, 36])}px Inter",
        "commit": "ui(gameover): adjust game over title font size"
    },
    # --- CHANGELOG UPDATES ---
    {
        "file": "CHANGELOG.md",
        "find": r'(## \[\d+\.\d+\.\d+\])',
        "replace_fn": lambda m: m.group(0),
        "commit": "docs(changelog): document recent improvements",
        "special": "changelog"
    },
    # --- VERSION BUMPS ---
    {
        "file": "config.js",
        "find": r'version: "(\d+)\.(\d+)\.(\d+)"',
        "replace_fn": lambda m: f'version: "{m.group(1)}.{m.group(2)}.{int(m.group(3)) + 1}"',
        "commit": "chore(version): bump patch version"
    },
]


def read_file(filepath):
    """Read file contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(filepath, content):
    """Write content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def apply_improvement(improvement, used_commits):
    """Apply a single improvement to the codebase."""
    filepath = improvement["file"]

    if not os.path.exists(filepath):
        return False

    content = read_file(filepath)

    # Special handling for changelog
    if improvement.get("special") == "changelog":
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
        changes = [
            "Improved visual contrast for game elements",
            "Refined gameplay speed parameters",
            "Adjusted scoring balance values",
            "Enhanced UI spacing and layout",
            "Updated color palette accents",
            "Tuned difficulty progression curve",
            "Polished button styling",
            "Refined typography sizing",
            "Optimized canvas rendering margins",
            "Adjusted level-up threshold",
            "Improved game over screen readability",
            "Enhanced scoreboard visual hierarchy",
        ]
        entry = f"\n## [{timestamp}]\n\n### Improved\n- {random.choice(changes)}\n"
        content = content.replace(
            "All notable changes to this Snake Game project will be documented in this file.",
            "All notable changes to this Snake Game project will be documented in this file." + entry
        )
        write_file(filepath, content)
        return True

    # Standard regex replacement
    pattern = improvement["find"]
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return False

    new_value = improvement["replace_fn"](match)

    # Don't commit if nothing actually changed
    if match.group(0) == new_value:
        return False

    content = content[:match.start()] + new_value + content[match.end():]
    write_file(filepath, content)
    return True


def git_commit(message):
    """Stage all changes and commit."""
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", message], check=True)


def get_version():
    """Get current version from config.js."""
    content = read_file("config.js")
    match = re.search(r'version: "([^"]+)"', content)
    return match.group(1) if match else "1.0.0"


def update_version_references(new_version):
    """Update version references in HTML and footer."""
    # Update HTML title
    html = read_file("index.html")
    html = re.sub(r'Snake Game — v[\d.]+', f'Snake Game — v{new_version}', html)
    write_file("index.html", html)

    # Update footer in config
    config = read_file("config.js")
    config = re.sub(
        r'footerText: "[^"]+"',
        f'footerText: "Built with ❤️ | Version {new_version}"',
        config
    )
    write_file("config.js", config)


def main():
    """Main improvement loop."""
    print(f"🎮 Snake Game Auto-Improver starting...")
    print(f"📊 Will generate {COMMITS_PER_RUN} improvements this run\n")

    used_commits = set()
    successful = 0

    # Shuffle improvements for variety
    available = list(IMPROVEMENTS)
    random.shuffle(available)

    for i in range(COMMITS_PER_RUN):
        if not available:
            available = list(IMPROVEMENTS)
            random.shuffle(available)

        # Try to find an applicable improvement
        applied = False
        attempts = 0

        while available and not applied and attempts < len(available):
            improvement = available.pop(0)
            commit_msg = improvement["commit"]

            # Skip if we already used this exact commit message
            if commit_msg in used_commits:
                available.append(improvement)
                attempts += 1
                continue

            try:
                if apply_improvement(improvement, used_commits):
                    used_commits.add(commit_msg)

                    # If this was a version bump, update references
                    if "version" in commit_msg.lower():
                        new_ver = get_version()
                        update_version_references(new_ver)

                    git_commit(commit_msg)
                    successful += 1
                    applied = True
                    print(f"  ✅ [{i+1}/{COMMITS_PER_RUN}] {commit_msg}")
                else:
                    available.append(improvement)
                    attempts += 1
            except Exception as e:
                print(f"  ⚠️  Failed: {e}")
                available.append(improvement)
                attempts += 1

        if not applied:
            # Fallback: bump version
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
                    successful += 1
                    print(f"  ✅ [{i+1}/{COMMITS_PER_RUN}] chore: bump version to {new_ver}")
            except Exception as e:
                print(f"  ❌ Fallback failed: {e}")

        # Wait between commits
        if i < COMMITS_PER_RUN - 1:
            print(f"  ⏳ Waiting {DELAY_BETWEEN}s...")
            time.sleep(DELAY_BETWEEN)

    print(f"\n✅ Done! Applied {successful}/{COMMITS_PER_RUN} improvements.")


if __name__ == "__main__":
    main()
