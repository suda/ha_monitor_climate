# Monitor Climate

[![hacs](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

_Expose temperature and humidity sensors as a climate entity_

## Usage

```yaml
climate:
    - platform: monitor_climate
        name: "Office Climate"
        temperature_sensor: sensor.office_climate_temperature
        humidity_sensor: sensor.office_climate_humidity
```

## Installation

### HACS (Recommended)

1. Ensure that [HACS](https://hacs.xyz/) is installed.
2. In the Home Assistant UI, navigate to HACS.
3. Click on "Integrations".
4. Click the "+" button in the bottom right corner.
5. Search for "Monitor Climate" and select it.
6. Click "Install" and wait for the installation to complete.
7. Restart Home Assistant.
8. In the HA UI, go to "Configuration" -> "Integrations", click "+" and search for "Monitor Climate".

### Manual Installation

If you prefer to install manually, follow these steps:

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `monitor_climate`.
4. Download _all_ the files from the `custom_components/monitor_climate/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Monitor Climate"
