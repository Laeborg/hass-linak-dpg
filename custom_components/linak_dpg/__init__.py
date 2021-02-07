"""
Linak DPG Desk Panel Integration

For more details about this integration, please refer to the documentation at
https://github.com/Laeborg/hass-linak-dpg
"""

from homeassistant.core import callback
from homeassistant.components import mqtt

import logging

# Domain configuration
DOMAIN = "linak_dpg"