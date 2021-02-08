"""
Hub for Linak DPG Desk Panel Integration
"""
import asyncio
import random


class Hub:
    def __init__(self, hass, name, address):
        self._hass = hass
        self._name = name
        self._address = address
        self._id = name.lower()
        self.online = True

    @property
    def hub_id(self):
        return self._id

    async def init_connection(self):
        await asyncio.sleep(1)
        return True