"""
Platform for Linak DPG Desk Panel Integration
"""

import random

from homeassistant.helpers.entity import Entity
from .const import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Linak DPG desk from a config entry."""

    async_add_entities([DeskSensor(config_entry)])

class DeskSensor(Entity):
    """Representation of Height Sensor for Linak DPG."""
    
    def __init__(self, config_entry):
        """Initialize the Linak DPG desk."""
        self._config_entry = config_entry
        self._name = config_entry.data.get("name")
        self._uuid = config_entry.data.get("id")
        self._state = random.randint(0, 100)
        
    @property
    def unique_id(self) -> str:
        """Return the unique ID of the device."""
        return self._uuid

    @property
    def name(self):
        """Return the name of the device."""
        return self._name

    @property
    def state(self):
        """Return the name of the device."""
        return self._state