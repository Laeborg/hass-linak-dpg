"""
Config Flow for the Linak DPG integration
"""

from homeassistant.core import callback

import logging

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Optional(CONF_NAME): cv.name,
        vol.Optional(CONF_MAC_ADDRESS): cv.mac_address
    }),
}, extra=vol.ALLOW_EXTRA)