"""
CP1404
convert m to km
estimate: 15mins
actual: 18mins
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

M_TO_KM = 1.60934

class MilesToKilometresApp(App):
    """Converter App"""
    output_km = StringProperty()
    def build(self):
        """Build App"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_calculation(self):
        """Calculate conversion"""
        value = self.get_miles_validated()
        result = value * M_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Increment up and down"""
        value = self.get_miles_validated() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculation()

    def get_miles_validated(self):
        """Return text as float or 0.0 for error"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0

MilesToKilometresApp().run()
