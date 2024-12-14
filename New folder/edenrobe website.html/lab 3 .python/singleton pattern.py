class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        # Initialize default configurations
        self.config = {
            "setting1": "default_value1",
            "setting2": "default_value2",
        }

    def get(self, key):
        return self.config.get(key)

    def set(self, key, value):
        self.config[key] = value

    def load_config(self, config_dict):
        # Load a configuration dictionary
        self.config.update(config_dict)

# Example usage
if __name__ == "__main__":
    # Create first instance
    config1 = ConfigManager()
    print(config1.get("setting1"))  # Output: default_value1

    # Set a new value
    config1.set("setting1", "new_value1")

    # Create second instance
    config2 = ConfigManager()
    print(config2.get("setting1"))  # Output: new_value1

    # Load additional configurations
    config2.load_config({"setting2": "new_value2"})
    print(config1.get("setting2"))  # Output: new_value2
