import pytest
import aiohttp


@pytest.fixture(autouse=True)
async def disable_network_calls(monkeypatch: pytest.MonkeyPatch):
    async with aiohttp.ClientSession() as session:

        def stunted_get():
            raise RuntimeError("Network access not allowed during testing!")

        await monkeypatch.setattr(session, "get", lambda *args, **kwargs: stunted_get())


# FIXME: Resolve the warning --> RuntimeWarning: coroutine 'disable_network_calls' was never awaited
