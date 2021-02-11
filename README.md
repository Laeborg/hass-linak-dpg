# Linak DPG Desk Panel Integration
Home Assistant integration to control Linak DPG Desk Panels with adjustable heights.

🛠️ **This project is work-in-progress and not ready for use** 🛠️

## Installation
Upload the custom component to Home Assistant's custom_components directory and restart the service.

### Recommended configuration
Add the integration though interface of HomeAssistant

### Manuel configuration
Add the sensor to your configuration.yaml:
```
sensor:
  - platform: linak_dpg
    name: Linak Desk
    address: 00:11:22:33:44:55
```

## Notable projects
nconrad's [idasen-desk-controller](https://github.com/nconrad/idasen-desk-controller)
kosme's [bluetoothctl_lib](https://github.com/kosme/bluetoothctl_lib)
castis' [bluetoothctl](https://gist.github.com/castis/0b7a162995d0b465ba9c84728e60ec01)