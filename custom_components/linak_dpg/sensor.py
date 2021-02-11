"""
Platform for Linak DPG Desk Panel Integration
"""

import random

from homeassistant.helpers.entity import Entity
from homeassistant.const import (
    STATE_OFF,
    STATE_ON,
)

from .const import DOMAIN, LOGGER
from .bluetoothctl import Bluetoothctl

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
        self._height = self.height
        self._unit_of_measurement = "cm"
        self._state = None
        
    def update(self):
        """Update state of the device."""
        try:
            connection = Bluetoothctl().connect(self._address)
            
            if not connection:
                raise Exception(f"Failed to establish connection")
                
        except Exception as e:
            LOGGER.error(e)
            self._state = STATE_OFF
            
        else:
            self._state = STATE_ON
        
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
        """Return the state of the device."""
        return self._state

    @property
    def address(self):
        """Return the address of the device."""
        return self._address
        
    @property
    def height(self):
        """Return the current height of the device."""
        return random.randint(60, 130)
        
    @property
    def device_state_attributes(self):
        """Return the state attributes of the device."""
        attr = {}
        attr["height"] = self._height
        attr["unit_of_measurement"] = self._unit_of_measurement
        attr["mac_address"] = self._address
        
        return attr