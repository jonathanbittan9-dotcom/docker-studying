import sys

def main() -> None:
    print(f"[boot: message from python]{sys.version.split()[0]} version")
    print("[boot] hello from my own dockerfile")

if "__main__" == __name__:
    main()






import discord