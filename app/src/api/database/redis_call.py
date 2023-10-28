import json
from json import JSONDecodeError
from typing import Union, Any

import redis.asyncio as redis
from fastapi.encoders import jsonable_encoder

from src.settings import CacheSettings


class ClientCacheRedis:
    def __init__(
        self,
        host: str = CacheSettings.CACHE_HOST,
        port: int = CacheSettings.CACHE_PORT,
        password=CacheSettings.CACHE_PASSWORD,
    ):
        is_ssl = password is not None
        self.client = redis.Redis(host=host, port=port, password=password, ssl=is_ssl)

    async def get(self, key: str) -> Union[None, dict, str, bytes]:
        value = await self.client.get(name=key)
        if value:
            try:
                return json.loads(value)
            except JSONDecodeError:
                return value.decode()

    async def set(
        self,
        key: str,
        value: Any,
        ttl_seconds: int = None,
        ttl_milliseconds: int = None,
    ) -> None:
        if ttl_seconds:
            ttl_milliseconds = None
        if isinstance(value, (dict, list)):
            value = json.dumps(jsonable_encoder(value))
        await self.client.set(
            name=key, value=value, ex=ttl_seconds, px=ttl_milliseconds
        )

    async def delete(self, key: str) -> None:
        await self.client.delete(key)

    async def delete_all(self, key: str) -> None:
        async for key in self.client.scan_iter(key):
            await self.delete(key=key)
