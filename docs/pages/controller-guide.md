# Controller PC Guide

To get optimal performance with a controller, follow these steps.

## 1. Drivers

- Install the latest Xbox / PlayStation drivers, or use [DS4Windows](https://github.com/Ryochan7/DS4Windows/releases) for DualShock / DualSense controllers.
- Make sure your controller shows up as **Xbox 360 Controller for Windows** in Device Manager. The software hooks the XInput API.

## 2. Steam Input

In Steam → **Settings → Controller**, **disable** Steam Input for the game you're playing. Steam Input intercepts inputs and can break aim-assist hooks.

## 3. In-game settings

- Set the game to **borderless windowed**.
- **Disable** Vsync, motion blur, and any frame-pacing options.
- Set aim-assist to **Standard** or **Default** (not "Precision" or "Black Ops").

## 4. Software settings

- Open the menu with ==**HOME**==.
- Set **Aim Mode** → `Controller`.
- Set **Trigger Key** → `LT` (left trigger) or your preferred bind.
- Tweak **Smoothing** between **5** and **15** for the most natural feel.

## 5. Common issues

| Symptom | Fix |
|---|---|
| Aim doesn't activate | Steam Input is enabled — disable it. |
| Aim is too snappy | Increase Smoothing, lower FOV. |
| Right-stick drifts off | Lower in-game deadzone, raise software deadzone. |
| Cheat doesn't read controller | Reconnect controller before launching the loader. |
