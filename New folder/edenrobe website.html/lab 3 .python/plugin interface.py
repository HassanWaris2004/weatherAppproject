from abc import ABC, abstractmethod

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

# Example usage
if __name__ == "__main__":
    plugin = SamplePlugin()
    plugin.initialize()
    plugin.execute()
