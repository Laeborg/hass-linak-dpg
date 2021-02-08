"""
Config Flow for Linak DPG Desk Panel Integration
"""

import logging
import voluptuous as vol

from homeassistant import config_entries, core, exceptions

from .const import DOMAIN
from .hub import Hub

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema({
    ("name"): str,
    ("address"): str
})


async def validate_input(hass: core.HomeAssistant, data: dict):
    if len(data["name"]) < 3:
        raise InvalidName
        
    if len(data["address"]) < 3:
        raise InvalidAddress

    hub = Hub(hass, data["name"], data["address"])

    result = await hub.init_connection()
    if not result:
        raise CannotConnect

    return {
        "title": data["name"],
        "address": data["address"]
    }


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(self, user_input=None):
        errors = {}
        
        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)

                return self.async_create_entry(title=info["title"], data=user_input)
            except InvalidHost:
                errors["host"] = "cannot_connect"
            except Exception:
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )

class InvalidName(exceptions.HomeAssistantError):
    """Error to indicate there is an invalid name."""
    
class InvalidAddress(exceptions.HomeAssistantError):
    """Error to indicate there is an invalid address."""