"""
Config Flow for Linak DPG Desk Panel Integration
"""

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.exceptions import ConfigEntryNotReady

import homeassistant.helpers.config_validation as cv

from .const import LOGGER, DOMAIN

DATA_SCHEMA = vol.Schema(
    {
        vol.Required("name", default="Linak Desk"): cv.string,
        vol.Required("address"): cv.string
    }
)


class LinakDPGConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a Linak DPG config flow."""
    
    def __init__(self):
        """Initialize flow."""
        self._address = None
        self._name = None
        self._id = None
        
    def _get_entry(self):
        data = {
            "address": self._address,
            "id": self._id,
            "name": self._name
        }

        return self.async_create_entry(
            title=self._title,
            data=data,
        )
        
    def _try_connect(self):
        """Try to connect."""
        return True
        
    async def async_step_import(self, user_input=None):
        """Handle configuration by yaml file."""
        return await self.async_step_user(user_input)

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        if user_input is not None:
            await self.async_set_unique_id(user_input["address"])
            self._abort_if_unique_id_configured()

            self._address = user_input.get("address")
            self._name = user_input.get("name")
            self._title = self._name

            result = await self.hass.async_add_executor_job(self._try_connect)

            if result != True:
                return self.async_abort(reason=result)
            return self._get_entry()

        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA)