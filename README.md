# 📷 ASCII Camera

> **Transform your real-time webcam feed into stunning, retro ASCII art directly in your browser.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-lightgrey.svg?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-yellow.svg?style=flat-square&logo=javascript&logoColor=black)](https://javascript.info)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

---

## 🔍 Overview

**ASCII Camera** is a sleek, real-time webcam-to-ASCII converter built with Python and Vanilla JavaScript. It leverages the browser's `navigator.mediaDevices.getUserMedia` API to stream video frames, processes pixel luminance in real-time, and renders it inside a retro, cyber-themed terminal interface. 

Designed for both creativity and performance, ASCII Camera runs entirely client-side for ultra-low latency rendering, using Python Flask purely as a lightweight server to host the application.

---

## ✨ Features

- ⚡ **Real-Time Rendering:** Instant webcam-to-ASCII processing with adjustable FPS throttling.
- 🎨 **Aesthetic Themes:**
  - *Neon Green* (default cyber-terminal look)
  - *Ghost White* (clean, modern bright display)
  - *Inverted* (classic black-on-white print style)
  - *True Color* (renders characters mapped to the actual camera-pixel RGB colors!)
- 🎛️ **Granular Controls:**
  - Adjustable output resolution/width (40 to 180 characters wide).
  - Fine-grained image contrast slider (0.5x to 3x).
  - Real-time frame freezing ("Freeze Frame") and lens mirroring.
- 🔤 **Dynamic Character Sets:** Switch between *Detailed*, *Simple*, *Blocks (Solid)*, *Minimalist*, and *Matrix (Binary)* configurations.
- 📋 **One-Click Export:** Copy the generated text art directly to your clipboard.
- 🌐 **Sleek Glassmorphic UI:** Modern control dashboard built with Outfit typography and cyberglow accents.

---

## 🛠️ Tech Stack

- **Backend:** [Python](https://www.python.org/) & [Flask](https://flask.palletsprojects.com/) (to serve the application locally)
- **Frontend:** [HTML5 Canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API), [CSS3 Custom Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties), and [ES6+ JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- **Typography:** [Outfit](https://fonts.google.com/specimen/Outfit) (UI elements) and [Fira Code](https://fonts.google.com/specimen/Fira+Code) (monospace terminal font)

---

## ⚙️ How It Works

ASCII Camera runs high-performance rendering logic directly in the browser:

1. **Capture:** The browser requests webcam permissions and pipes the input stream into a hidden `<video>` element.
2. **Draw:** An active `requestAnimationFrame` render loop draws the video frames onto an offscreen `<canvas>` at a throttled frame-rate.
3. **Analyze:** JavaScript extracts raw pixel data. For each pixel, the luminance is calculated using standard color weightings:
   $$\text{Luminance} = 0.299R + 0.587G + 0.114B$$
4. **Map:** The computed luminance determines which ASCII character (from light to dark) maps to that coordinate.
5. **Render:** The mapping output is written inside the custom cyber terminal panel.

---

## 🚀 Installation & Setup

Get ASCII Camera running locally in less than 2 minutes.

### Prerequisites

- Python 3.8 or higher installed on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/joeflaming777/ASCII-art.git
cd ASCII-art
```

### 2. Set Up a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install Flask
```

### 4. Run the Server

```bash
python app.py
```

Open your browser and navigate to **`http://127.0.0.1:5000`** to experience it!

---

## 🎮 Usage Example

1. Launch the application and click **Initialize Camera**.
2. Allow webcam permission in the browser popup (HTTPS or localhost is required by browsers for media device access).
3. Play with the controls:
   - Adjust the **Width** slider to change the character density.
   - Choose the **Matrix (Binary)** charset for a retro coding feel.
   - Switch the **Theme** to **True Color** to see standard color video converted to text.
4. Click **Freeze Frame** to pause, then **Copy Art** to copy the raw text to your clipboard.

---

---

## 📁 Project Structure

```text
ASCII-art/
├── .vscode/             # Editor settings
├── app.py               # Flask server entrypoint
├── index.html           # Core single-page web app (HTML/CSS/JS)
└── README.md            # Project documentation (this file)
```

---

## 🔮 Future Improvements

- 🧪 **Offline Image Upload:** Support drag-and-drop of `.jpg`/`.png` files to process static images.
- 💾 **ASCII Video Recording:** Export short `.mp4` or `.gif` video clips of your live ASCII streams.
- 🌈 **Custom CSS Color Gradients:** Allow users to define custom color gradients for characters.
- 📱 **Mobile Camera Selector:** Ability to switch between front-facing (selfie) and rear cameras on mobile devices.

---

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more details.
