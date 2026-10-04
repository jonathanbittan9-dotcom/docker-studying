import sys
from src.logs_setup import log

def main() -> None:
    log.info(f"[boot]: message from python] {sys.version.split()[0]} version")
    log.info("[boot] hello from my own dockerfile!")

def check_discord() -> None:
    try:
        import discord
    except ImportError:
        log.exception(f"[boot] ERROR: discord.py is not INSTALLED")
        log.exception(sys.exit(1))

if "__main__" == __name__:
    main()
    check_discord()