"""
Linak DPG Desk Panel Integration

For more details about this integration, please refer to the documentation at
https://github.com/Laeborg/hass-linak-dpg
"""

from homeassistant import core
from homeassistant.components import mqtt

import logging

def setup(hass, config):
    """Your controller/hub specific code."""
    
    hass.data[DOMAIN] = {
        'height': 0
    }

    hass.helpers.discovery.load_platform('sensor', DOMAIN, {}, config)

    return True