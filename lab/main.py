import sys
import os
from lab.logs_setup import log
import time
import signal
import psycopg


def main() -> None:
    log.info(f"[boot]: message from python] {sys.version.split()[0]} version")
    log.info("[boot] hello from my own dockerfile!")

def check_token() -> None:
    token = os.getenv("DISCORD_TOKEN")
    if token is None:
        log.exception("[boot] DISCORD TOKEN IS MISSING")
        sys.exit(1)
    else:
        log.info("[boot] found the DISCORD BOT TOKEN ")

def check_discord() -> None:
    try:
        import discord
    except ImportError:
        log.exception(f"[boot] ERROR: discord.py is not INSTALLED")
        log.exception(sys.exit(1))

running = True

def run_forever() -> None:
    beat = 0
    while running:
        beat+=1
        log.info(f"heartbeat {beat}")
        time.sleep(5)
    log.info("saved everything")

def handle_stop(signum, frame) -> None:
    global running
    log.info("[bot] got SIGTERM , fishing current work..")
    running = False

signal.signal(signal.SIGTERM , handle_stop)

def check_db():
    url = os.getenv("DATABASE_URL")
    try:
        with psycopg.connect(url) as conn:
            version  = conn.execute("SELECT version()").fetchone()[0]
            log.info(f"[boot] connected to DB: {version.split(',')[0]}")
    except Exception:
        log.exception("[boot] FAILED TO CONNECT TO THE DB")
        sys.exit(1)

def test():
    """idk"""
    """sup"""
if "__main__" == __name__:
    main()
    check_discord()
    check_token()
    check_db()
    run_forever()

