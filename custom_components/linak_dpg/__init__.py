"""
Linak DPG Desk Panel Integration

For more details about this integration, please refer to the documentation at
https://github.com/Laeborg/hass-linak-dpg
"""

from homeassistant import core
from homeassistant.components import mqtt

import logging

VERSION = '0.0.1'

DOMAIN = 'linak_dpg'
PLATFORMS = ['sensor']

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Optional(CONF_NAME): cv.name,
        vol.Optional(CONF_MAC_ADDRESS): cv.mac_address
    }),
}, extra=vol.ALLOW_EXTRA)

def setup(hass, config):
    """Your controller/hub specific code."""
    
    hass.data[DOMAIN] = {
        'height': 0
    }

    hass.helpers.discovery.load_platform('sensor', DOMAIN, {}, config)

    return True