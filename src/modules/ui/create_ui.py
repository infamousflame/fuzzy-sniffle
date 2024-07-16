"""Creates the app's UI."""

from kivy.app import App
from kivy.lang.builder import Builder


class MainUI(App):
    """Creates the main UI."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root = None
        self.title = 'Fuzzy Sniffle'

    def build(self):
        with open('./assets/ui/ui_layout.kv') as file:
            self.root = Builder.load_string(file.read())
        return self.root
