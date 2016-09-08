from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
__author__ = "Sarah Domanti"

class MilesToKilometres(App):
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def handle_increment(self, value, increment):
        try:
            value = int(value)
        except ValueError:
            value = 0

        new_value = value + increment
        self.root.ids.input_number.text = str(new_value)

    def handle_convert(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        result = value*1.6
        self.root.ids.result_value.text = str(result)

MilesToKilometres().run()