from abc import ABC, abstractmethod
import importlib

# Define the Plugin interface
class Plugin(ABC):
    @abstractmethod
    def initialize(self):
        """Initialize the plugin."""
        pass

    @abstractmethod
    def execute(self):
        """Execute the plugin's main functionality."""
        pass

# Example of a Concrete Plugin
class SamplePlugin(Plugin):
    def initialize(self):
        print("SamplePlugin initialized.")

    def execute(self):
        print("SamplePlugin executed.")

# PluginManager class
class PluginManager:
    def __init__(self):
        self.plugins = {}

    def load_plugin(self, plugin_name: str):
        """Load a plugin using its fully qualified class name."""
        try:
            module_name, class_name = plugin_name.rsplit('.', 1)
            module = importlib.import_module(module_name)
            plugin_class = getattr(module, class_name)
            plugin_instance = plugin_class()
            plugin_instance.initialize()  # Initialize the plugin
            self.plugins[class_name] = plugin_instance
            print(f"Loaded plugin: {class_name}")
        except (ImportError, AttributeError) as e:
            print(f"Failed to load plugin '{plugin_name}': {e}")

    def execute_plugin(self, class_name: str):
        """Execute a loaded plugin by its class name."""
        if class_name in self.plugins:
            self.plugins[class_name].execute()
        else:
            print(f"Plugin '{class_name}' not loaded.")

# Usage Example
if __name__ == "__main__":
    # Create the PluginManager instance
    plugin_manager = PluginManager()

    # Load the SamplePlugin using its fully qualified name
    plugin_manager.load_plugin(__name__ + '.SamplePlugin')  # Fully qualified name

    # Execute the loaded plugin
    plugin_manager.execute_plugin('SamplePlugin')

