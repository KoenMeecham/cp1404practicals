"""
CP1404
convert m to km
estimate: 15mins
actual:
"""

from kivy.app import App
from kivy.lang import Builder

class MilesToKilometersApp(App):
    """Converter App"""
    def build(self):
        """Build App"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root
