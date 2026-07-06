# 🐍 Snake Game

<p align="center">
  <img src="https://img.shields.io/badge/game-snake-brightgreen?style=for-the-badge" alt="Game">
  <img src="https://img.shields.io/badge/tech-HTML%20%2F%20CSS%20%2F%20JS-blue?style=for-the-badge" alt="Tech">
  <img src="https://img.shields.io/badge/status-actively%20developed-orange?style=for-the-badge" alt="Status">
</p>

---

A modern, polished **Snake game** built with vanilla HTML5 Canvas, CSS, and JavaScript. Features a dark neon theme, score tracking, level progression, and smooth gameplay.

## 🎮 Play

Open `index.html` in any modern browser to play!

### Controls

| Key | Action |
|-----|--------|
| `↑` `W` | Move Up |
| `↓` `S` | Move Down |
| `←` `A` | Move Left |
| `→` `D` | Move Right |
| `Space` | Pause / Resume |
| `Enter` | Start Game |

## ✨ Features

- 🎨 **Dark neon theme** with customizable color scheme
- 📊 **Score & high score** tracking (persisted in localStorage)
- 📈 **Level system** with progressive speed increase
- ⏸️ **Pause/Resume** functionality
- ⚙️ **Configurable** game parameters via `config.js`
- 🧱 **Wall collision** toggle (wrap-around mode available)
- 📱 **Responsive** design

## 📁 Project Structure

```
snake-game/
├── index.html          # Game HTML structure
├── style.css           # Dark theme styling
├── config.js           # Game configuration & tuning
├── game.js             # Core game engine
├── CHANGELOG.md        # Version history
└── README.md           # This file
```

## ⚙️ Configuration

All game parameters are tunable in `config.js`:

```javascript
CONFIG = {
    initialSpeed: 150,      // Starting speed (ms)
    pointsPerFood: 10,      // Points per food item
    levelUpScore: 50,       // Score to level up
    wallCollision: true,    // Walls kill or wrap?
    showGrid: false,        // Show grid overlay?
    // ... and more
};
```

## 📋 Changelog

See [CHANGELOG.md](./CHANGELOG.md) for version history and improvements.

## 🛠️ Development

This project is **actively maintained** with continuous improvements to gameplay balance, visual design, and user experience. Check the commit history for the latest tweaks!

### Areas of Active Development
- 🎨 Color scheme refinements
- ⚖️ Gameplay balance tuning
- 🖼️ UI/UX polish
- 📐 Layout & spacing adjustments
- 🏆 Scoring system optimization

---

<p align="center">
  <b>⭐ Star this repo if you enjoy the game!</b>
</p>
