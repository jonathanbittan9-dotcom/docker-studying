import sys
import os
from src.logs_setup import log

def main() -> None:
    log.info(f"[boot]: message from python] {sys.version.split()[0]} version")
    log.info("[boot] hello from my own dockerfile!")

def check_token() -> None:
    token = os.getenv("DISCORD_TOKEN")
    if token is None:
        log.exception("[boot]DISCORD TOKEN IS MISSING")
        sys.exit(1)
    else:
        log.info("[boot] found the DISCORD BOT TOKEN ")

def check_discord() -> None:
    try:
        import discord
    except ImportError:
        log.exception(f"[boot] ERROR: discord.py is not INSTALLED")
        log.exception(sys.exit(1))

if "__main__" == __name__:
    main()
    check_discord()