"""Entry point. Async, typed, ready to grow into cogs later."""
import sys
import asyncio
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RuntimeReport:
    python: str
    async_ok: bool


async def probe_asyncio() -> RuntimeReport:
    await asyncio.sleep(0)  # prove the event loop actually runs
    return RuntimeReport(python=sys.version.split()[0], async_ok=True)


async def main() -> None:
    report = await probe_asyncio()
    print(f"[boot] Python {report.python} | asyncio: {report.async_ok}")
    print("[boot] Docker milestone 1 OK")


if __name__ == "__main__":
    asyncio.run(main())
