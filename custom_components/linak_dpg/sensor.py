"""
Sensor Platform for the Linak DPG Integration
"""

from homeassistant.helpers.entity import Entity

from . import DOMAIN

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
        
    add_entities([LinakSensor()])
    
class LinakSensor(Entity):
    """Representation of a sensor."""
    
    def __init__(self):
        """Initialize the sensor."""
        self._state = "unavailable"