# 👁️ OpticPointer – Eye-Controlled Mouse with Blink Click

Control your mouse cursor using your eyes with real-time facial landmark detection!

[![GitHub Repo](https://img.shields.io/badge/GitHub-abdullahakintobi%2Foptic--pointer-blue?logo=github)](https://github.com/abdullahakintobi/optic-pointer)
[![License](https://img.shields.io/badge/License-Apache%202.0-brightgreen.svg)](https://github.com/abdullahakintobi/optic-pointer/blob/main/LICENSE)

---

## 📽️ Demo

> *\[This will be added soon]*

---

## 🧠 How It Works

**Optic Pointer** uses your webcam to track your iris movements and facial landmarks using **MediaPipe’s FaceMesh**, then translates those movements into cursor positions. It also detects **blinks of the left eye** to perform mouse clicks using **PyAutoGUI**.

---

## ⚙️ Features

* 👁️ Eye-based cursor movement
* 👀 Blink (left eye) for mouse click
* 🔄 Real-time webcam tracking
* 🎛️ Adjustable sensitivity
* 🖥️ Works on most systems with a webcam
* 🐍 Built with Python, OpenCV, MediaPipe & PyAutoGUI

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/abdullahakintobi/optic-pointer.git
cd optic-pointer
```

### 2. Create and activate a virtual environment (optional)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python main.py
```

---

## 🖱️ How to Use

* Look around to move the mouse cursor.
* Blink your **left eye** to perform a mouse click.
* Press `Ctrl + C` or close the window to exit.

---

## 🎛️ Sensitivity Adjustment

If the cursor is moving too fast or too slow, you can adjust the sensitivity in `main.py`:

```python
SENSITIVITY_X = 4.5
SENSITIVITY_Y = 4.0
```

---

## 🤝 Contributing

Contributions are welcome!
Feel free to **fork** the repository, improve the code, fix bugs, or add new features and open a pull request.

---

## 📜 License

This project is licensed under the **Apache License 2.0**.
See the [LICENSE](https://github.com/abdullahakintobi/optic-pointer/blob/main/LICENSE) file for more details.
