"""Entry point. Async, typed, ready to grow into cogs later."""
import sys
import asyncio


class RuntimeReport:
    """Immutable holder for what we discovered about the runtime."""

    def __init__(self, python: str, async_ok: bool) -> None:
        self.python = python
        self.async_ok = async_ok

    def __repr__(self) -> str:
        return f"RuntimeReport(python={self.python!r}, async_ok={self.async_ok!r})"


async def probe_asyncio() -> RuntimeReport:
    await asyncio.sleep(0)  # prove the event loop actually runs
    return RuntimeReport(python=sys.version.split()[0], async_ok=True)
    

async def main() -> None:
    report = await probe_asyncio()
    print(f"[boot] Python {report.python} | asyncio: {report.async_ok}")
    print("[boot] Docker milestone 1 OK")


if __name__ == "__main__":
    asyncio.run(main())
