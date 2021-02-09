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
        self._address = config_entry.data.get("address")
        self._height = random.randint(60, 130)
        self._unit_of_measurement = "cm"
        self._availability = "Off"
        
        if self._availability == "Off":
            self._state = self._availability
        else:
            self._state = self._height
        
    @property
    def unique_id(self) -> str:
        """Return the unique ID of the device."""
        return self._uuid

    @property
    def name(self):
        """Return the name of the device."""
        return self._name

    @property
    def address(self):
        """Return the address of the device."""
        return self._address

    @property
    def state(self):
        """Return the state of the device."""
        return self._state

    @property
    def availability(self):
        """Return the availability of the device."""
        return self._availability
        
    @property
    def device_state_attributes(self):
        """Return the state attributes of the device."""
        attr = {}
        attr["height"] = self._height
        attr["unit_of_measurement"] = self._unit_of_measurement
        attr["mac_address"] = self._address
        attr["availability"] = self._availability
        
        return attr