"""
Linak DPG Desk Panel Integration

For more details about this integration, please refer to the documentation at
https://github.com/Laeborg/hass-linak-dpg
"""

from .const import DOMAIN

async def async_setup(hass, config):
    """Set up the Linak DPG component."""
    if DOMAIN in config:
        hass.data[DOMAIN] = {}
        
        for entry_config in config[DOMAIN]:
            address = entry_config["address"]
            
            hass.data[DOMAIN][address] = {
                "name": entry_config.get("name")
            }
            
            hass.async_create_task(
                hass.config_entries.flow.async_init(
                    DOMAIN, context={"source": "import"}, data=entry_config
                )
            )
            
    return True
    
async def async_setup_entry(hass, entry):
    """Set up the Linak DPG platform."""
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )

    return True