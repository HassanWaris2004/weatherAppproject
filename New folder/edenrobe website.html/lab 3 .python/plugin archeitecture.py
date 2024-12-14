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

# Example Plugin: TextProcessorPlugin
class TextProcessorPlugin(Plugin):
    def initialize(self):
        print("TextProcessorPlugin initialized.")

    def execute(self):
        text = "Hello, World!"
        processed_text = text.lower()  # Simple text processing: convert to lowercase
        print(f"Processed Text: {processed_text}")

# Example Plugin: DataExporterPlugin
class DataExporterPlugin(Plugin):
    def initialize(self):
        print("DataExporterPlugin initialized.")

    def execute(self):
        data = {"name": "John", "age": 30, "city": "New York"}
        # Simulate exporting data to a CSV format
        csv_data = ','.join(data.keys()) + '\n' + ','.join(str(value) for value in data.values())
        print("Exported Data:\n", csv_data)

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

# Main class to test the Plugin architecture
class Main:
    @staticmethod
    def run():
        # Create the PluginManager instance
        plugin_manager = PluginManager()

        # Load and execute TextProcessorPlugin
        plugin_manager.load_plugin(__name__ + '.TextProcessorPlugin')  # Fully qualified name
        plugin_manager.execute_plugin('TextProcessorPlugin')

        # Load and execute DataExporterPlugin
        plugin_manager.load_plugin(__name__ + '.DataExporterPlugin')  # Fully qualified name
        plugin_manager.execute_plugin('DataExporterPlugin')

# Entry point for the application
if __name__ == "__main__":
    Main.run()

    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Home | Edenrobe Replica</title>
</head>
<body>
    <header>
        <h1>Edenrobe Replica</h1>
        <nav>
            <a href="index.html">Home</a>
            <a href="about.html">About Us</a>
            <a href="contact.html">Contact Us</a>
            <a href="privacy.html">Privacy Policy</a>
            <a href="terms.html">Terms and Conditions</a>
        </nav>
    </header>

    <div class="banner"></div>
    
    <div class="container">
        <h2>Welcome to Our Store</h2>
        <p>Your one-stop shop for the latest fashion trends.</p>
        <p>Discover our wide range of clothing and accessories.</p>
    </div>

    <footer>
        <p>&copy; 2024 Edenrobe Replica. All rights reserved.</p>
    </footer>
</body>
</html>

