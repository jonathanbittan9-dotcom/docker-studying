import os
import sys
from bot.log_handler import log



def python_version():
    log.info(f"[boot] python version: {sys.version.split(0)}")


def check_token():
        token = os.getenv("BOT_TOKEN")
        if token is None:
            log.exception("[boot] TOKEN IS MISSING")
            sys.exit(1)
        else:
            log.info("[boot] found the BOT_TOKEN")


if __name__ =="__main__":
    python_version()
    check_token()