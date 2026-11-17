import os
import sys
import time
import asyncio
import threading

# ── dependency check ──────────────────────────────────────────────────────────
def install(pkg):
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"])

try:
    import discord
except ImportError:
    print("installing discord.py-self …")
    install("discord.py-self")
    import discord

try:
    from colorama import init, Fore, Back, Style
except ImportError:
    print("installing colorama …")
    install("colorama")
    from colorama import init, Fore, Back, Style

try:
    import pyfiglet
except ImportError:
    print("installing pyfiglet …")
    install("pyfiglet")
    import pyfiglet

init(autoreset=True)

# ── colours ───────────────────────────────────────────────────────────────────
R  = Fore.RED
W  = Fore.WHITE
DG = Fore.LIGHTBLACK_EX
C  = Fore.CYAN
Y  = Fore.YELLOW
G  = Fore.GREEN
RS = Style.RESET_ALL
BD = Style.BRIGHT

# ── banner ────────────────────────────────────────────────────────────────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear()
    fig = pyfiglet.figlet_format("CRIMSON", font="banner3-D")
    lines = fig.splitlines()
    print()
    for line in lines:
        print(R + BD + "  " + line)
    print()
    print(R + "  " + "━" * 54)
    print(W + BD + "    Self-Bot Panel  " + DG + "│" + R + " by CRIMSON")
    print(R + "  " + "━" * 54)
    print()

# ── menu ──────────────────────────────────────────────────────────────────────
MENU_ITEMS = {
    "1": ("AFK System",     True),
    "2": ("Auto Responder", False),
    "3": ("Anti-Spam",      False),
    "4": ("Nuke Guard",     False),
    "5": ("Auto React",     False),
    "6": ("Status Rotator", False),
    "7": ("DM Logger",      False),
    "8": ("Ghost Ping",     False),
    "9": ("Dev Tools",      False),
}

def show_menu():
    banner()
    print(W + BD + "   ┌─────────────────────────────────────────────┐")
    print(W + BD + "   │              SELECT A MODULE                │")
    print(W + BD + "   └─────────────────────────────────────────────┘")
    print()
    for key, (name, available) in MENU_ITEMS.items():
        if available:
            tag   = G  + BD + " ✦ ACTIVE "
            label = W  + BD + f"  [{key}]  " + G + BD + name
        else:
            tag   = DG + " coming soon "
            label = DG + f"  [{key}]  " + DG + name
        print(f"   {label:<42}{DG}│{tag}")
    print()
    print(R + "   " + "─" * 48)
    print(DG + "   [0]  Exit")
    print(R + "   " + "─" * 48)
    print()

# ── AFK flow ──────────────────────────────────────────────────────────────────
def ask(prompt_text):
    return input(C + BD + "  ❯ " + W + prompt_text + C + " : " + RS).strip()

def afk_setup():
    banner()
    print(G + BD + "  ╔══════════════════════════════════════╗")
    print(G + BD + "  ║          AFK SYSTEM SETUP            ║")
    print(G + BD + "  ╚══════════════════════════════════════╝")
    print()

    token = ask("Paste your account token")
    if not token:
        print(R + "\n  ✖ Token cannot be empty.\n")
        time.sleep(1.5)
        return

    print()
    afk_msg = ask("AFK message (shown on every ping/DM)")
    if not afk_msg:
        print(R + "\n  ✖ Message cannot be empty.\n")
        time.sleep(1.5)
        return

    print()
    print(Y + "  ⌛  Connecting …")
    run_selfbot(token, afk_msg)

# ── selfbot logic ─────────────────────────────────────────────────────────────
def run_selfbot(token: str, afk_message: str):
    client = discord.Client()

    @client.event
    async def on_ready():
        clear()
        banner()
        print(G + BD + f"  ✔  Logged in as  →  {client.user}")
        print(G + BD + f"  ✔  AFK message   →  {afk_message}")
        print()
        print(Y + BD + "  AFK mode is LIVE. Press Ctrl+C to stop.\n")
        print(R + "  " + "─" * 48)

    @client.event
    async def on_message(message: discord.Message):
        # ignore own messages
        if message.author.id == client.user.id:
            return

        me = client.user
        mentioned = me in message.mentions

        # direct message
        is_dm = isinstance(message.channel, discord.DMChannel)

        if mentioned or is_dm:
            try:
                await message.channel.send(afk_message)
                who = message.author
                where = "DM" if is_dm else message.guild.name
                print(C + f"  ↩  Replied to {who} in {where}")
            except Exception as e:
                print(R + f"  ✖ Could not send: {e}")

    try:
        try:
            client.run(token, bot=False)   # newer discord.py-self
        except TypeError:
            client.run(token)              # older discord.py-self
    except discord.LoginFailure:
        print(R + BD + "\n  ✖ Invalid token! Please try again.\n")
        time.sleep(2)
    except KeyboardInterrupt:
        print(Y + "\n\n  AFK stopped. Returning to menu …\n")
        time.sleep(1)
    except Exception as e:
        print(R + f"\n  ✖ Error: {e}\n")
        time.sleep(2)

# ── main loop ─────────────────────────────────────────────────────────────────
def main():
    while True:
        show_menu()
        choice = input(W + BD + "   Select option (0-9) : " + RS).strip()

        if choice == "0":
            clear()
            print(R + BD + "\n  Goodbye. — CRIMSON\n")
            sys.exit(0)

        elif choice == "1":
            afk_setup()

        elif choice in MENU_ITEMS:
            banner()
            print(Y + BD + f"\n  ⏳  [{MENU_ITEMS[choice][0]}] is coming soon!\n")
            time.sleep(1.8)

        else:
            print(R + "\n  ✖ Invalid option.\n")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print(R + BD + "\n  Exited. — CRIMSON\n")
