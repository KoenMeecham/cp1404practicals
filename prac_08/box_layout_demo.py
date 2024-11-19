"""
CP1404
Box Layout Demo
estimated: 5mins
actual: 6mins
"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy Box App"""
    def build(self):
        """Build Kivy App"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet the user"""
        print("Hello")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear user's name"""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
