# 🔴 CRIMSON Selfbot

<div align="center">

```
 ██████╗██████╗ ██╗███╗   ███╗███████╗ ██████╗ ███╗   ██╗
██╔════╝██╔══██╗██║████╗ ████║██╔════╝██╔═══██╗████╗  ██║
██║     ██████╔╝██║██╔████╔██║███████╗██║   ██║██╔██╗ ██║
██║     ██╔══██╗██║██║╚██╔╝██║╚════██║██║   ██║██║╚██╗██║
╚██████╗██║  ██║██║██║ ╚═╝ ██║███████║╚██████╔╝██║ ╚████║
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
```

![Python](https://img.shields.io/badge/Python-3.8+-red?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-black?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-crimson?style=for-the-badge)

**A powerful Discord selfbot with an interactive terminal panel.**

</div>

---

## ✨ Features

| # | Module | Status |
|---|--------|--------|
| 1 | 🟢 AFK System | **Active** |
| 2 | Auto Responder | Coming Soon |
| 3 | Anti-Spam | Coming Soon |
| 4 | Nuke Guard | Coming Soon |
| 5 | Auto React | Coming Soon |
| 6 | Status Rotator | Coming Soon |
| 7 | DM Logger | Coming Soon |
| 8 | Ghost Ping | Coming Soon |
| 9 | Dev Tools | Coming Soon |

---

## 📱 AFK System

- Set a custom AFK message via the terminal
- Auto-replies **every time** someone pings or DMs you
- Works across all servers and DMs simultaneously
- Stop anytime with `Ctrl+C` — returns to main menu

---

## ⚙️ Installation

### Termux (Android)

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/crimsonpardon/crimson_selfbot.py.git
cd crimson_selfbot.py
pip install discord.py-self colorama pyfiglet
python crimson_selfbot.py
```

### Linux / VPS

```bash
sudo apt update
sudo apt install python3 python3-pip git -y
git clone https://github.com/crimsonpardon/crimson_selfbot.py.git
cd crimson_selfbot.py
pip3 install discord.py-self colorama pyfiglet
python3 crimson_selfbot.py
```

---

## 🚀 Usage

```
1. Run the script
2. CRIMSON panel will open
3. Press [1] for AFK System
4. Paste your Discord account token
5. Enter your AFK message
6. Done — bot is now live
```

> To get your token: Discord → DevTools (`Ctrl+Shift+I`) → Console → paste:
> ```js
> (webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
> ```

---

## 📦 Dependencies

```
discord.py-self
colorama
pyfiglet
```

---

## ⚠️ Disclaimer

> This project is for **educational purposes only.**
> Using selfbots violates [Discord's Terms of Service](https://discord.com/terms).
> Use at your own risk. The developer is not responsible for any account bans.

---

## 👤 Developer

**crimsonpardon** — built with 🔴 by CRIMSON

---

<div align="center">
⭐ Star this repo if you found it useful
</div>
