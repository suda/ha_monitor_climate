"""Monitor Climate Platform"""
from homeassistant.components.climate import ClimateEntity
from homeassistant.const import UnitOfTemperature

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Monitor Climate platform."""
    async_add_entities([MonitorClimate(config.get("name", "Monitor Climate"),
                                       config.get("temperature_sensor"),
                                       config.get("humidity_sensor"))])

class MonitorClimate(ClimateEntity):
    """Representation of a Monitor Climate device."""

    def __init__(self, name, temperature_sensor, humidity_sensor):
        """Initialize the climate device."""
        self._name = name
        self._temperature_sensor = temperature_sensor
        self._humidity_sensor = humidity_sensor
        self._current_temperature = None
        self._current_humidity = None

    @property
    def name(self):
        """Return the name of the climate device."""
        return self._name

    @property
    def temperature_unit(self):
        """Return the unit of measurement."""
        return UnitOfTemperature.CELSIUS

    @property
    def current_temperature(self):
        """Return the current temperature."""
        return self._current_temperature

    @property
    def current_humidity(self):
        """Return the current humidity."""
        return self._current_humidity

    @property
    def hvac_modes(self):
        """Return the list of available hvac operation modes."""
        return ["off"]

    @property
    def hvac_mode(self):
        """Return hvac operation mode."""
        return "off"

    async def async_update(self):
        """Fetch new state data for this climate device."""
        temp_state = self.hass.states.get(self._temperature_sensor)
        if temp_state:
            self._current_temperature = float(temp_state.state)

        humid_state = self.hass.states.get(self._humidity_sensor)
        if humid_state:
            self._current_humidity = float(humid_state.state)