from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelApp(App):
    """Dynamic Label App"""
    def __init__(self, **kwargs):
        """Initialise the app"""
        super().__init__(**kwargs)
        self.names_to_label = ["Bob", "James", "Ludwig"]

    def build(self):
        """Construct Kivy App"""
        self.title = "Creative Name"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.construct_labels()
        return self.root

    def construct_labels(self):
        """Construct Labels"""
        for name in self.names_to_label:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

DynamicLabelApp().run()



