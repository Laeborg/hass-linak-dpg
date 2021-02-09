# Linak DPG Desk Panel Integration
Home Assistant integration to control Linak DPG Desk Panels with adjustable heights.

🛠️ **This project is work-in-progress and not ready for use** 🛠️

## Configuration
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